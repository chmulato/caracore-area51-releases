# caracore-area51-releases — Loja Área 51

**Objetivo:** vitrine pública e documentação do produto licenciado de identidade e acesso institucional.

Publicação: [area51.caracore.com.br](https://area51.caracore.com.br/) · conteúdo estático em `docs/` (GitHub Pages).

Titularidade: Governo Federal. Implementação: Cara Core Informática (Suporte Área 51).

## O que é este repositório

| Aqui (loja) | Na oficina (`caracore-area51`) |
|-------------|--------------------------------|
| HTML, CSS, wiki | Código, baseline, testes, `operational/` |
| Comercial e conceitos | Entrega técnica licenciada |

A loja **não** distribui o pacote por download público — explica o produto e canaliza pedidos via [licença](docs/licenca-uso.html) e [contato](docs/canal-feedback.html).

## Onde ir

| Público | Página |
|---------|--------|
| Visitante / comprador | [Início](docs/index.html) · [Produto](docs/produto.html) · [Serviços](docs/servicos.html) |
| Técnico licenciado | [Wiki](docs/wiki/index.html) · [Apresentação técnica](docs/apresentacao-tecnica.html) |
| Manutenção deste site | [loja-memoria.txt](docs/assets/inc/loja-memoria.txt) |

Wiki (baseline **0.1.0-dev**): o que é → [entrega](docs/wiki/o-que-recebe-entrega.html) → componentes → fronteiras → [fluxo OIDC](docs/wiki/fluxo-oidc-referencia.html).

## Manutenção

```bash
python scripts/sync_store_shell.py   # cabeçalho e rodapé em docs/*.html e docs/wiki/*.html
```

Alinhamento com a oficina: [OFICINA.md](https://github.com/chmulato/caracore-area51/blob/main/OFICINA.md) · [ALINHAMENTO_LOJA_PRESENTACAO.md](https://github.com/chmulato/caracore-area51/blob/main/docs/ALINHAMENTO_LOJA_PRESENTACAO.md)

**Contato:** suporte@caracore.com.br
