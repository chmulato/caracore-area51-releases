# Loja Área 51 e repositório de oficina

- **Este repositório** (`caracore-area51-releases`) é a vitrine HTML/CSS publicada (pasta `docs/`).
- **Oficina / código-fonte** (`caracore-area51`) mantém baseline Python, operações Linux e documentação técnica em Markdown.

O guia mestre sobre **cores, navegação e convenções CSS** faz parte da oficina em:

[`caracore-area51/docs/ALINHAMENTO_LOJA_PRESENTACAO.md`](https://github.com/chmulato/caracore-area51/blob/main/docs/ALINHAMENTO_LOJA_PRESENTACAO.md)

(ajuste o URL do GitHub conforme organização ou remoto em uso.)

Arquivos canónicos de estilo **neste** repositório:

| Arquivo | Função |
|---------|--------|
| `docs/assets/css/store-public.css` | Páginas principais (`index`, produto, serviços, galeria, imprensa, download, licença, canal) |
| `docs/wiki/assets/css/wiki-loja-align.css` | Ajustes da wiki Bootstrap para o mesmo cromático e tipografia da loja |

### Imagens da vitrine (convenção de pastas)

- **Pasta padrão (canônica):** `docs/assets/img/` — usar para novo conteúdo visual ligado ao site da loja. Nas páginas em `docs/*.html`, o caminho de referência típico é **`assets/img/…`** (URL relativo à raiz `docs/` no deploy).
- **Legado atual:** várias páginas ainda carregam os panoramas 16:9 a partir de `docs/images/` com `src="images/…"`. Mantém URLs estáveis até uma migração coordenada; **não** é obrigatório renomear arquivos ou `src` só por este guia.
- **Wiki:** favicon e estáticos similares costumam apontar para `../assets/images/…` a partir das HTML em `docs/wiki/`; isso refere-se sobretudo a **ícone e metadados**, não ao conjunto principal de ilustrações de conteúdo (que deve seguir `assets/img` quando forem criados novos materiais ali).

Consulte também o texto em `docs/assets/img/README.md`.

Cara Core Informática — Área 51.
