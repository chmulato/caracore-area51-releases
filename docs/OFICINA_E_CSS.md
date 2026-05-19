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

- **Pasta canônica:** `docs/assets/img/` — **todas** as imagens da loja (panoramas 16:9, favicon, novos raster/vetoriais). Nas páginas em `docs/*.html`, use **`assets/img/…`** (URL relativo à raiz `docs/` no deploy).
- **Wiki:** a partir de `docs/wiki/*.html`, referencie com `../assets/img/…` (por exemplo `favicon.ico`).

Consulte também o texto em `docs/assets/img/README.md`.

Cara Core Informática — Área 51.
