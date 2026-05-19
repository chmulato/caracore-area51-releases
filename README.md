# caracore-area51-releases — Loja oficial Área 51

Site estático publicado em `docs/` (GitHub Pages) do Suporte Área 51, em torno de OpenID Connect e OAuth 2.1, com PKCE nos exemplos documentados. Publicação habitual: https://area51.caracore.com.br/. A baseline e a oficina são produto privado licenciado — não open source.

Este ficheiro é o único Markdown do repositório caracore-area51-releases.

Referências na oficina:

- Orientação geral: [caracore-area51/OFICINA.md](https://github.com/chmulato/caracore-area51/blob/main/OFICINA.md)
- Alinhamento visual e navegação: [caracore-area51/docs/ALINHAMENTO_LOJA_PRESENTACAO.md](https://github.com/chmulato/caracore-area51/blob/main/docs/ALINHAMENTO_LOJA_PRESENTACAO.md)
- Índice de documentação técnica: [caracore-area51/docs/README.md](https://github.com/chmulato/caracore-area51/blob/main/docs/README.md)

## Produto Área 51

O Área 51 é um pacote técnico para implantar autenticação federada com OpenID Connect e Keycloak em Docker. Inclui baseline versionada, scripts automatizados, testes de fluxo OAuth/OIDC e documentação para equipes técnicas. Oferece autenticação compatível com OAuth 2.1 e PKCE, deploy repetível entre ambientes e suporte opcional para implantação, integração e capacitação.

Titularidade do produto institucional: Governo Federal. Scripts da oficina: software proprietário, entrega mediante licença. A Cara Core Informática actua como implementadora técnica do Suporte Área 51.

## Estrutura da loja (index.html)

1. O que é — hero com definição do pacote técnico
2. Principais funcionalidades — autenticação, deploy, ambientes distribuídos, implantação repetível
3. O que acompanha o pacote — documentação, galeria, apresentação técnica
4. Casos de uso — órgãos públicos, empresas, desenvolvimento, capacitação
5. Serviços disponíveis — baseline licenciada, implementação guiada, acompanhamento SLA
6. Como começar — apresentação técnica, entrega, canal de feedback

Páginas complementares: produto.html, apresentacao-tecnica.html, servicos.html, galeria.html, download.html, faq.html, wiki, imprensa, licença, contato.

## Loja e oficina

| Papel | Repositório | Conteúdo |
|-------|-------------|----------|
| Loja | caracore-area51-releases, pasta docs/ | HTML e CSS público, GitHub Pages |
| Oficina | caracore-area51 (privado) | Baseline Python, operational/, testes — produto licenciado |

| Repositório | Propósito | Público |
|-------------|-----------|---------|
| caracore-area51 | Desenvolvimento e operação | Desenvolvedores, DevOps |
| caracore-area51-releases | Vitrine oficial (este repositório) | Clientes, interessados |

## Convenções técnicas da vitrine

### CSS

| Ficheiro | Função |
|----------|--------|
| docs/assets/css/store-public.css | Páginas principais (classe store no body) |
| docs/wiki/assets/css/wiki-loja-align.css | Wiki: tema escuro alinhado à loja (html data-loja-shell="1", body.store.wiki-loja) |
| docs/assets/caracore-core-typography.css | Tipografia institucional opcional |
| docs/assets/caracore-institutional-components.css | Componentes institucionais opcionais |

Margens responsivas partilhadas pela variável --sf-gutter em store-public.css (header, main, secções, rodapé).

Menu principal (todas as páginas em docs/ e docs/wiki/): mesma ordem linear — Início, Produto, Serviços, Galeria, Wiki, Download, Imprensa, Contato (desktop); mobile acrescenta FAQ e Licença antes de Contato. Fragmentos em docs/assets/inc/store-nav.html e docs/wiki/assets/inc/wiki-nav.html.

Rodapé institucional (todas as páginas): mapa do site numerado 01–11 (item 11 = apresentação técnica), implementadora técnica, titularidade federal e contacto suporte@caracore.com.br. Fragmentos em docs/assets/inc/store-footer.html e docs/wiki/assets/inc/wiki-footer.html. Sincronização de cabeçalho e rodapé: scripts/sync_store_shell.py (ou scripts/sync_store_nav.py).

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

| # | Página | Descrição | Tipo |
|---|--------|-----------|------|
| 01 | [index.html](docs/index.html) | Início institucional | Landing |
| 02 | [produto.html](docs/produto.html) | Visão de produto e cenários | Produto |
| 03 | [servicos.html](docs/servicos.html) | Modelos de contratação | Serviços |
| 04 | [galeria.html](docs/galeria.html) | Dez imagens panorama 16:9 | Material |
| 05 | [wiki](docs/wiki/index.html) | Wiki no mesmo domínio | Wiki |
| 06 | [download.html](docs/download.html) | Entrega licenciada da baseline e serviço contratado | Download |
| 07 | [imprensa.html](docs/imprensa.html) | Kit institucional de imprensa | Imprensa |
| 08 | [faq.html](docs/faq.html) | Perguntas frequentes (produto, oficina, serviços) | FAQ |
| 09 | [licenca-uso.html](docs/licenca-uso.html) | Licença e titularidade | Jurídico |
| 10 | [canal-feedback.html](docs/canal-feedback.html) | Suporte e orçamento | Canal |
| 11 | [apresentacao-tecnica.html](docs/apresentacao-tecnica.html) | Apresentação técnica institucional do produto | Documentação |

Subpáginas wiki (herdam cabeçalho e rodapé da vitrine; mapa 05 marca Wiki como secção activa):

| Página | Descrição |
|--------|-----------|
| [wiki/index.html](docs/wiki/index.html) | Entrada da wiki |
| [wiki/projeto-area51.html](docs/wiki/projeto-area51.html) | Documentação do projecto Área 51 |

## Início rápido (clientes licenciados)

1. Ler a [apresentação técnica](docs/apresentacao-tecnica.html) e a [licença de uso](docs/licenca-uso.html).
2. Solicitar entrega da baseline pelo [canal de feedback](docs/canal-feedback.html) ou conforme acordo institucional activo.
3. Seguir os guias incluídos no pacote entregue (setup Docker, Keycloak, testes de fluxo OIDC).

Resultado esperado, ilustrativo: Keycloak activo, aplicação protegida e validação automatizada concluída; o tempo depende da infraestrutura do cliente.

Implementação guiada, integração com aplicações do cliente, validação de segurança e suporte durante o projecto: [canal-feedback.html](docs/canal-feedback.html).

## Comparativo ilustrativo

| Aspecto | Montagem manual dispersa | Com baseline Área 51 licenciada |
|---------|--------------------------|-----------------------------------|
| Lead time em laboratório | Semanas típicas só com montagem manual | Minutos frequentemente relatados após pré-requisitos |
| PKCE no exemplo público | Inconsistente sem padrão comum | Fluxos descritos na baseline e nos testes |
| Testes de fluxo | Frequentemente adiados | Scripts em operational/tests/ |
| Documentação | Dispersa | Páginas desta loja e guias operational/ |
| Repetibilidade | Dependente de anotações locais | Rotinas e containers documentados |

## Segurança referida na documentação

OAuth 2.1, OIDC, PKCE, fluxo de código de autorização, validação de JWT quando aplicável, parâmetro state contra CSRF, introspecção de token conforme desenho, cookies HTTP-only nos exemplos apresentados.

## Componentes comunicados

Scripts baseline (oficina privada): configuração OIDC padronizada, testes de validação, versionamento interno, entrega licenciada.

Operação exemplo (operational/): Keycloak em Docker, aplicação Flask protegida, validação de fluxo OIDC, documentação passo a passo.

Suporte Cara Core (contrato): consultoria OIDC, customizações, integração Gov.br ou Entra ID, auditoria de segurança.

## Ligações úteis

- Loja: https://area51.caracore.com.br/
- Apresentação técnica: [apresentacao-tecnica.html](docs/apresentacao-tecnica.html)
- Produto: [produto.html](docs/produto.html)
- Serviços: [servicos.html](docs/servicos.html)
- Download: [download.html](docs/download.html)
- FAQ: [faq.html](docs/faq.html)
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
