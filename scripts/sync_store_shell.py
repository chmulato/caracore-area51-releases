"""Sincroniza cabeçalho e rodapé institucional em todas as páginas da loja e wiki."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "docs"

# Catálogo numerado da vitrine (01–10) + apresentação técnica (11)
FOOTER_PAGES = [
    (1, "index.html", "Início"),
    (2, "produto.html", "Produto"),
    (3, "servicos.html", "Serviços"),
    (4, "galeria.html", "Galeria"),
    (5, "wiki/index.html", "Wiki"),
    (6, "download.html", "Download"),
    (7, "imprensa.html", "Imprensa"),
    (8, "faq.html", "FAQ"),
    (9, "licenca-uso.html", "Licença"),
    (10, "canal-feedback.html", "Contato"),
    (11, "apresentacao-tecnica.html", "Apresentação"),
]

STORE_ITEMS = [
    ("index.html", "Início"),
    ("produto.html", "Produto"),
    ("servicos.html", "Serviços"),
    ("galeria.html", "Galeria"),
    ("wiki/index.html", "Wiki"),
    ("download.html", "Download"),
    ("imprensa.html", "Imprensa"),
    ("canal-feedback.html", "Contato"),
]
MOBILE_EXTRA = [
    ("faq.html", "FAQ"),
    ("licenca-uso.html", "Licença"),
]

STORE_CURRENT = {
    "index.html": "index.html",
    "produto.html": "produto.html",
    "apresentacao-tecnica.html": "apresentacao-tecnica.html",
    "servicos.html": "servicos.html",
    "galeria.html": "galeria.html",
    "download.html": "download.html",
    "imprensa.html": "imprensa.html",
    "faq.html": "faq.html",
    "licenca-uso.html": "licenca-uso.html",
    "canal-feedback.html": "canal-feedback.html",
}

WIKI_CURRENT = {
    "index.html": "index.html",
    "projeto-area51.html": "index.html",
}

HEADER_PATTERN = re.compile(
    r"    <a class=\"sf-skip\" href=\"#main\">.*?</header>",
    re.DOTALL,
)
FOOTER_PATTERN = re.compile(
    r"    <footer class=\"sf-footer\">.*?</footer>",
    re.DOTALL,
)


def mobile_items():
    core = [item for item in STORE_ITEMS if item[0] != "canal-feedback.html"]
    contato = next(item for item in STORE_ITEMS if item[0] == "canal-feedback.html")
    return core + MOBILE_EXTRA + [contato]


def link(href: str, label: str, current_href: str, indent: str, wrap_li: bool = False) -> str:
    cur = ' aria-current="page"' if href == current_href else ""
    inner = f'<a href="{href}"{cur}>{label}</a>'
    if wrap_li:
        return f"{indent}<li>{inner}</li>"
    return f"{indent}{inner}"


def footer_link(num: int, href: str, label: str, current_href: str, indent: str) -> str:
    cur = ' aria-current="page"' if href == current_href else ""
    num_str = f"{num:02d}"
    return (
        f'{indent}<a href="{href}"{cur}>'
        f'<span class="sf-footer-num" aria-hidden="true">{num_str}</span> {label}</a>'
    )


def wiki_mobile_items():
    prefix = "../"
    core = []
    for h, l in STORE_ITEMS:
        if h == "canal-feedback.html":
            continue
        if h == "wiki/index.html":
            core.append(("index.html", "Wiki"))
        else:
            core.append((prefix + h, l))
    contato = (prefix + "canal-feedback.html", "Contato")
    extra = [(prefix + h, l) for h, l in MOBILE_EXTRA]
    return core + extra + [contato]


def wiki_footer_hrefs():
    prefix = "../"
    items = []
    for num, href, label in FOOTER_PAGES:
        if href == "wiki/index.html":
            items.append((num, "index.html", label))
        else:
            items.append((num, prefix + href, label))
    return items


def store_header(current_href: str, brand_href: str = "index.html") -> str:
    nav_lines = [
        link(h, l, current_href, "                    ", wrap_li=True)
        for h, l in STORE_ITEMS
    ]
    mobile = [link(h, l, current_href, "                    ") for h, l in mobile_items()]
    return (
        '    <a class="sf-skip" href="#main">Ir para o conteúdo</a>\n'
        '    <header class="sf-header">\n'
        '        <div class="sf-header-inner">\n'
        f'            <a class="sf-brand" href="{brand_href}">Área 51 — Loja</a>\n'
        '            <nav class="sf-nav" aria-label="Principal">\n'
        '                <ul>\n'
        + "\n".join(nav_lines)
        + "\n                </ul>\n"
        '            </nav>\n'
        '            <details class="sf-menu">\n'
        '                <summary>Menu</summary>\n'
        '                <div class="sf-menu-body">\n'
        + "\n".join(mobile)
        + "\n                </div>\n"
        "            </details>\n"
        "        </div>\n"
        "    </header>"
    )


def wiki_header(current_href: str) -> str:
    prefix = "../"
    fixed = []
    for h, l in STORE_ITEMS:
        if h == "wiki/index.html":
            fixed.append(("index.html", "Wiki"))
        else:
            fixed.append((prefix + h, l))
    nav_lines = [link(h, l, current_href, "                    ", wrap_li=True) for h, l in fixed]
    mobile = [link(h, l, current_href, "                    ") for h, l in wiki_mobile_items()]
    return (
        '    <a class="sf-skip" href="#main">Ir para o conteúdo</a>\n'
        '    <header class="sf-header">\n'
        '        <div class="sf-header-inner">\n'
        '            <a class="sf-brand" href="../index.html">Área 51 — Loja</a>\n'
        '            <nav class="sf-nav" aria-label="Principal">\n'
        '                <ul>\n'
        + "\n".join(nav_lines)
        + "\n                </ul>\n"
        '            </nav>\n'
        '            <details class="sf-menu">\n'
        '                <summary>Menu</summary>\n'
        '                <div class="sf-menu-body">\n'
        + "\n".join(mobile)
        + "\n                </div>\n"
        "            </details>\n"
        "        </div>\n"
        "    </header>"
    )


def store_footer(current_href: str) -> str:
    links = [
        footer_link(num, href, label, current_href, "                ")
        for num, href, label in FOOTER_PAGES
    ]
    return (
        '    <footer class="sf-footer">\n'
        '        <div class="sf-footer-inner">\n'
        '            <h2 class="sf-visually-hidden">Rodapé institucional</h2>\n'
        '            <p class="sf-footer-brand">Área 51</p>\n'
        '            <p class="sf-footer-implementer">Cara Core Informática — implementadora técnica do Suporte Área 51</p>\n'
        '            <p class="sf-footer-tagline">Pacote técnico OpenID Connect com Keycloak em Docker, baseline versionada e documentação para equipes técnicas.</p>\n'
        '            <nav class="sf-footer-links" aria-label="Mapa do site">\n'
        + "\n".join(links)
        + "\n            </nav>\n"
        '            <div class="sf-footer-leg">\n'
        '                <p>&copy; 2026 Cara Core Informática · Área 51 — implementação técnica de serviço</p>\n'
        '                <p>Produto de titularidade do Governo Federal</p>\n'
        '                <p class="sf-footer-contact">Contato institucional: '
        '<a href="mailto:suporte@caracore.com.br">suporte@caracore.com.br</a> · '
        '<a href="canal-feedback.html">Canal de feedback</a></p>\n'
        "            </div>\n"
        "        </div>\n"
        "    </footer>"
    )


def wiki_footer(current_href: str) -> str:
    links = [
        footer_link(num, href, label, current_href, "                ")
        for num, href, label in wiki_footer_hrefs()
    ]
    return (
        '    <footer class="sf-footer">\n'
        '        <div class="sf-footer-inner">\n'
        '            <h2 class="sf-visually-hidden">Rodapé institucional</h2>\n'
        '            <p class="sf-footer-brand">Área 51</p>\n'
        '            <p class="sf-footer-implementer">Cara Core Informática — implementadora técnica do Suporte Área 51</p>\n'
        '            <p class="sf-footer-tagline">Pacote técnico OpenID Connect com Keycloak em Docker, baseline versionada e documentação para equipes técnicas.</p>\n'
        '            <nav class="sf-footer-links" aria-label="Mapa do site">\n'
        + "\n".join(links)
        + "\n            </nav>\n"
        '            <div class="sf-footer-leg">\n'
        '                <p>&copy; 2026 Cara Core Informática · Área 51 — implementação técnica de serviço</p>\n'
        '                <p>Produto de titularidade do Governo Federal</p>\n'
        '                <p class="sf-footer-contact">Contato institucional: '
        '<a href="mailto:suporte@caracore.com.br">suporte@caracore.com.br</a> · '
        '<a href="../canal-feedback.html">Canal de feedback</a></p>\n'
        "            </div>\n"
        "        </div>\n"
        "    </footer>"
    )


def sync_headers() -> None:
    for path in ROOT.glob("*.html"):
        if path.name not in STORE_CURRENT:
            continue
        text = path.read_text(encoding="utf-8")
        new_header = store_header(STORE_CURRENT[path.name])
        new_text, n = HEADER_PATTERN.subn(new_header, text, count=1)
        if n:
            path.write_text(new_text, encoding="utf-8")
            print("header", path.name)

    for path in (ROOT / "wiki").glob("*.html"):
        if path.name not in WIKI_CURRENT:
            continue
        text = path.read_text(encoding="utf-8")
        new_header = wiki_header(WIKI_CURRENT[path.name])
        new_text, n = HEADER_PATTERN.subn(new_header, text, count=1)
        if n:
            path.write_text(new_text, encoding="utf-8")
            print("header wiki", path.name)


def sync_footers() -> None:
    for path in ROOT.glob("*.html"):
        if path.name not in STORE_CURRENT:
            continue
        text = path.read_text(encoding="utf-8")
        new_footer = store_footer(STORE_CURRENT[path.name])
        new_text, n = FOOTER_PATTERN.subn(new_footer, text, count=1)
        if n:
            path.write_text(new_text, encoding="utf-8")
            print("footer", path.name)

    for path in (ROOT / "wiki").glob("*.html"):
        if path.name not in WIKI_CURRENT:
            continue
        text = path.read_text(encoding="utf-8")
        new_footer = wiki_footer(WIKI_CURRENT[path.name])
        new_text, n = FOOTER_PATTERN.subn(new_footer, text, count=1)
        if n:
            path.write_text(new_text, encoding="utf-8")
            print("footer wiki", path.name)


def main() -> None:
    sync_headers()
    sync_footers()


if __name__ == "__main__":
    main()
