# caracore-area51-releases — Loja oficial Área 51

Site estático publicado em `docs/` (GitHub Pages) do Suporte Área 51, em torno de OpenID Connect e OAuth 2.1, com PKCE nos exemplos públicos. Publicação habitual: https://area51.caracore.com.br/. Código baseline e operações residem no repositório caracore-area51.

Este ficheiro é o único Markdown do repositório caracore-area51-releases.

Referências na oficina:

- Orientação geral: [caracore-area51/OFICINA.md](https://github.com/chmulato/caracore-area51/blob/main/OFICINA.md)
- Alinhamento visual e navegação: [caracore-area51/docs/ALINHAMENTO_LOJA_PRESENTACAO.md](https://github.com/chmulato/caracore-area51/blob/main/docs/ALINHAMENTO_LOJA_PRESENTACAO.md)
- Índice de documentação técnica: [caracore-area51/docs/README.md](https://github.com/chmulato/caracore-area51/blob/main/docs/README.md)

## Produto Área 51

O Produto Área 51 é de titularidade do Governo Federal. A Cara Core Informática actua como implementadora técnica e mantenedora dos artefatos de implantação associados ao serviço Suporte Área 51.

A loja comunica uma linha de apoio à implantação de ambientes OpenID Connect e OAuth 2.1, com baseline publicada, exemplo de automatização para Keycloak em Docker e roteiros de validação. O material destina-se a órgãos públicos, empresas, integradores e equipas técnicas que necessitem de referência institucional antes de contratar implementação supervisada.

Entrega técnica referenciada na documentação pública:

- Scripts baseline de configuração OIDC (Python), no repositório caracore-area51
- Exemplo operacional de deploy com Keycloak em Docker e aplicação protegida, em operational/
- Testes de validação de fluxo OAuth 2.1 e PKCE conforme versão publicada
- Páginas HTML desta loja e guias Markdown na oficina

O Suporte Área 51 designa o serviço contratado de implementação e configuração executado pela Cara Core no ambiente do cliente. Não se confunde com um pacote genérico de download isolado; o canal formal de orçamento e esclarecimentos é [canal-feedback.html](docs/canal-feedback.html).

Referência de tempo em laboratório, apenas ilustrativa: ordem frequentemente relatada de vários minutos após pré-requisitos atendidos. Em produção, o calendário segue o ciclo e a infraestrutura de cada cliente.

## Loja e oficina

| Papel | Repositório | Conteúdo |
|-------|-------------|----------|
| Loja | caracore-area51-releases, pasta docs/ | HTML e CSS público, GitHub Pages |
| Oficina | caracore-area51 | Baseline Python, operational/, testes, Markdown técnico |

| Repositório | Propósito | Público |
|-------------|-----------|---------|
| caracore-area51 | Desenvolvimento e operação | Desenvolvedores, DevOps |
| caracore-area51-releases | Vitrine oficial (este repositório) | Clientes, interessados |

## Convenções técnicas da vitrine

### CSS

| Ficheiro | Função |
|----------|--------|
| docs/assets/css/store-public.css | Páginas principais (classe store no body) |
| docs/wiki/assets/css/wiki-loja-align.css | Wiki Bootstrap (data-loja-shell="1" no html) |
| docs/assets/caracore-core-typography.css | Tipografia institucional opcional |
| docs/assets/caracore-institutional-components.css | Componentes institucionais opcionais |

Margens responsivas partilhadas pela variável --sf-gutter em store-public.css (header, main, secções, rodapé).

Artefactos legados em docs/assets/legacy/ (loja.css, area51.css, loja.js) foram substituídos por store-public.css e area51.js. Nenhuma página activa os importa.

### Imagens

| Item | Convenção |
|------|-----------|
| Pasta canónica | docs/assets/img/ |
| Páginas docs/*.html | assets/img/… |
| Wiki docs/wiki/*.html | ../assets/img/… |
| Prompts na oficina | caracore-area51/marketing/prompts/ (01 a 10, formato 16:9) |

Conteúdo típico: panoramas numerados e favicon.ico.

### Fluxo oficina para loja

1. Desenvolver baseline e testes em caracore-area51 (src/, tests/).
2. Alterar HTML da vitrine em docs/*.html ou via delivery opcional (scripts/delivery_vitrine_area51_to_releases.py na oficina).
3. Antes de publicar CSS ou navegação, cruzar com ALINHAMENTO_LOJA_PRESENTACAO.md na oficina.
4. Copiar imagens finais para docs/assets/img/.

## Páginas publicadas

Domínio: https://area51.caracore.com.br/

| Página | Descrição | Tipo |
|--------|-----------|------|
| [index.html](docs/index.html) | Início institucional | Landing |
| [produto.html](docs/produto.html) | Visão de produto e cenários | Produto |
| [servicos.html](docs/servicos.html) | Modelos de contratação | Serviços |
| [galeria.html](docs/galeria.html) | Dez imagens panorama 16:9 | Material |
| [imprensa.html](docs/imprensa.html) | Kit institucional de imprensa | Imprensa |
| [wiki](docs/wiki/index.html) | Wiki no mesmo domínio | Wiki |
| [download.html](docs/download.html) | O que o serviço contratado pode entregar | Serviço |
| [licenca-uso.html](docs/licenca-uso.html) | Licença e titularidade | Jurídico |
| [canal-feedback.html](docs/canal-feedback.html) | Suporte e orçamento | Canal |

## Início rápido (repositório caracore-area51)

```bash
git clone https://github.com/chmulato/caracore-area51.git
cd caracore-area51
pip install -r operational/requirements.txt
python operational/setup_oidc_environment.py \
  --server 192.168.1.100 \
  --docker-user admin \
  --docker-pass password
python operational/tests/validate_oidc_flow.py \
  --keycloak-url http://192.168.1.100:8080
```

Resultado esperado, ilustrativo: Keycloak, aplicação protegida e validação segundo guias públicos; o tempo depende da infraestrutura do cliente.

Implementação guiada, integração com aplicações do cliente, validação de segurança e suporte durante o projecto: [canal-feedback.html](docs/canal-feedback.html).

## Comparativo ilustrativo

| Aspecto | Montagem manual dispersa | Com baseline e rotinas publicadas |
|---------|--------------------------|-----------------------------------|
| Lead time em laboratório | Semanas típicas só com montagem manual | Minutos frequentemente relatados após pré-requisitos |
| PKCE no exemplo público | Inconsistente sem padrão comum | Fluxos descritos na baseline e nos testes |
| Testes de fluxo | Frequentemente adiados | Scripts em operational/tests/ |
| Documentação | Dispersa | Páginas desta loja e guias operational/ |
| Repetibilidade | Dependente de anotações locais | Rotinas e containers documentados |

## Segurança referida na documentação

OAuth 2.1, OIDC, PKCE, fluxo de código de autorização, validação de JWT quando aplicável, parâmetro state contra CSRF, introspecção de token conforme desenho, cookies HTTP-only nos exemplos apresentados.

## Componentes comunicados

Scripts baseline (repositório de código): configuração OIDC padronizada, testes de validação, versionamento Git, entrega via GitHub.

Operação exemplo (operational/): Keycloak em Docker, aplicação Flask protegida, validação de fluxo OIDC, documentação passo a passo.

Suporte Cara Core (contrato): consultoria OIDC, customizações, integração Gov.br ou Entra ID, auditoria de segurança.

## Ligações úteis

- Loja: https://area51.caracore.com.br/
- Código: https://github.com/chmulato/caracore-area51
- Produto: [produto.html](docs/produto.html)
- Serviços: [servicos.html](docs/servicos.html)
- Download: [download.html](docs/download.html)
- Wiki: [wiki](docs/wiki/index.html)
- Licença: [licenca-uso.html](docs/licenca-uso.html)
- Contato: [canal-feedback.html](docs/canal-feedback.html)
- Proposta de serviço: [PROPOSTA_SERVICO_AREA51.md](https://github.com/chmulato/caracore-area51/blob/main/PROPOSTA_SERVICO_AREA51.md)

## Licença e titularidade

Produto Área 51 de titularidade do Governo Federal. A Cara Core Informática actua como implementadora técnica. Texto integral: [licenca-uso.html](docs/licenca-uso.html) e [LICENSE](LICENSE).

## Contato

E-mail: suporte@caracore.com.br  
Canal institucional: [canal-feedback.html](docs/canal-feedback.html)

Cara Core Informática — Área 51 — implementação técnica de serviço.
