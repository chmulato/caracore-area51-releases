# caracore-area51-releases — Loja oficial Área 51

Vitrine estática em `docs/` (GitHub Pages): https://area51.caracore.com.br/

Pacote técnico OpenID Connect e Keycloak em Docker. **Produto privado licenciado** — oficina não open source. Titularidade: Governo Federal. Implementação: Cara Core Informática (Suporte Área 51).

Único Markdown deste repositório. Memória de manutenção: [docs/assets/inc/loja-memoria.txt](docs/assets/inc/loja-memoria.txt).

Referências na oficina: [OFICINA.md](https://github.com/chmulato/caracore-area51/blob/main/OFICINA.md) · [ALINHAMENTO_LOJA_PRESENTACAO.md](https://github.com/chmulato/caracore-area51/blob/main/docs/ALINHAMENTO_LOJA_PRESENTACAO.md)

## Loja e oficina

| Papel | Repositório | Conteúdo |
|-------|-------------|----------|
| Loja | caracore-area51-releases / docs/ | HTML, CSS, wiki conceptual |
| Oficina | caracore-area51 (privado) | Baseline, operational/, testes |

## Páginas (# = rodapé)

| # | Página | Função |
|---|--------|--------|
| 01 | [index.html](docs/index.html) | Landing |
| 02 | [produto.html](docs/produto.html) | Visão geral |
| 03 | [servicos.html](docs/servicos.html) | Contratação |
| 04 | [galeria.html](docs/galeria.html) | Material visual (prompts 01–10) |
| 05 | [wiki](docs/wiki/index.html) | Conceitos OIDC |
| 06 | [download.html](docs/download.html) | Entrega licenciada |
| 07 | [imprensa.html](docs/imprensa.html) | Kit imprensa |
| 08 | [faq.html](docs/faq.html) | FAQ |
| 09 | [licenca-uso.html](docs/licenca-uso.html) | Licença |
| 10 | [canal-feedback.html](docs/canal-feedback.html) | Contato |
| 11 | [apresentacao-tecnica.html](docs/apresentacao-tecnica.html) | Documentação técnica |

Wiki: [projeto-area51.html](docs/wiki/projeto-area51.html).

## Convenções

- **CSS:** [store-public.css](docs/assets/css/store-public.css); wiki: [wiki-loja-align.css](docs/wiki/assets/css/wiki-loja-align.css).
- **Imagens:** [docs/assets/img/](docs/assets/img/); prompts na oficina: `marketing/prompts/01–10`.
- **Menu:** ordem linear partilhada; mobile inclui FAQ e Licença. Fragmentos em `docs/assets/inc/` e `docs/wiki/assets/inc/`.
- **Sincronização:** `python scripts/sync_store_shell.py` (cabeçalho + rodapé).

## Início (cliente licenciado)

1. [Apresentação técnica](docs/apresentacao-tecnica.html) e [licença](docs/licenca-uso.html).
2. Entrega da baseline via [canal de feedback](docs/canal-feedback.html) ou acordo activo.
3. Guias do pacote entregue (Docker, Keycloak, testes OIDC).

Implementação supervisada: [canal-feedback.html](docs/canal-feedback.html).

## Contato

suporte@caracore.com.br · [canal-feedback.html](docs/canal-feedback.html)
