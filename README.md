# caracore-area51-releases — Loja oficial Área 51

Site estático em **`docs/`** (GitHub Pages) do **Suporte Área 51**, em torno de **OpenID Connect** e **OAuth 2.1** (PKCE nos exemplos públicos). Publicação habitual: **https://area51.caracore.com.br/**. Código baseline e operações: repositório **caracore-area51**.

- **CSS da vitrine e vínculo com a oficina:** [docs/OFICINA_E_CSS.md](docs/OFICINA_E_CSS.md)
- **Imagens da vitrine:** pasta canônica **`docs/assets/img/`** (inclui favicon e panoramas). Convenções em [OFICINA_E_CSS.md](docs/OFICINA_E_CSS.md).
- **Ao gerar HTML institucional a partir da oficina:** `caracore-area51/docs/ALINHAMENTO_LOJA_PRESENTACAO.md`

## O que comunicamos ao público

**Implementação exemplo de ambientes OIDC seguros**, referenciados ao projeto técnico publicado.

- **Scripts baseline** — Configuração OIDC padronizada (Python); detalhes no repositório de código.
- **Deploy automatizado (exemplo)** — Keycloak e aplicação protegida em Docker, segundo guias de `operational/`.
- **Testes exemplo** — Validação de fluxo OAuth 2.1 e PKCE conforme projeto atual.
- **Documentação combinada** — Páginas desta loja e guias técnicos no repositório de oficina.

**Referência de tempo em laboratório:** ordem frequentemente relatada até **vários minutos** após pré‑requisitos atendidos (ilustrativo; produção segue ciclo do cliente).

---

## Repositórios

| Repositório | Propósito | Público |
|------------|----------|---------|
| **caracore-area51** | Código (desenvolvimento + operação) | Desenvolvedores, DevOps |
| **caracore-area51-releases** | Loja oficial (este repositório) | Clientes, interessados |

---

## Páginas em `docs/`

Domínio publicado: **https://area51.caracore.com.br/**

| Página | Descrição | Tipo |
|--------|-----------|------|
| [index.html](docs/index.html) | Início institucional | Landing |
| [produto.html](docs/produto.html) | Visão de produto, cenários | Produto |
| [servicos.html](docs/servicos.html) | Modelos baseline, implementação guiada e contratos | Serviços |
| [galeria.html](docs/galeria.html) | Dez imagens panorama 16:9 | Material |
| [imprensa.html](docs/imprensa.html) | Kit institucional de imprensa | Imprensa |
| [wiki](docs/wiki/index.html) | Wiki no mesmo domínio (Bootstrap + `wiki-loja-align.css`) | Wiki |
| [download.html](docs/download.html) | O que o serviço contratado pode entregar | Serviço |
| [licenca-uso.html](docs/licenca-uso.html) | Licença e titularidade | Jurídico |
| [canal-feedback.html](docs/canal-feedback.html) | Solicitar suporte ou orçamento | Canal |

---

## Quick Start

### 1. Baseline público (repositório `caracore-area51`)

```bash
# Clonar repositório de código
git clone https://github.com/chmulato/caracore-area51.git
cd caracore-area51

# Instalar dependências
pip install -r operational/requirements.txt

# Deploy automático
python operational/setup_oidc_environment.py \
  --server 192.168.1.100 \
  --docker-user admin \
  --docker-pass password

# Validar
python operational/tests/validate_oidc_flow.py \
  --keycloak-url http://192.168.1.100:8080
```

**Resultado esperado (ilustrativo):** Keycloak, aplicação protegida e validação segundo guias públicos atualizados; tempo depende da infraestrutura do cliente.

---

### 2. Implementação guiada

**[Pedir orçamento ou suporte formal](docs/canal-feedback.html)**

- Setup no seu ambiente
- Integração com sua aplicação
- Validação de segurança
- Suporte durante implementação

---

### 3. Contrato com SLA (“Platinum” apenas como rótulo comercial habitual)

Para órgãos com requisitos críticos:
- Implementação completa
- Integração Gov.br / Entra ID
- Auditoria de segurança
- Suporte 24x5 com SLA

**[Falar com especialista](docs/canal-feedback.html)**

---

## Comparativo apenas ilustrativo

| Aspecto | Cenário tipicamente manual disperso | Com baseline e rotinas públicas do projeto |
|---------|--------------------------------------|--------------------------------------------|
| Lead time laboratório | Ordens típicas de semanas apenas com montagem manual | Minutos habitualmente relatados após pré‑requisitos e rotina de guias |
| PKCE em exemplo público | Inconsistente sem padrão comum | Fluxos descritos na baseline e nos testes de fluxo do repositório |
| Testes de fluxo | Frequentemente adiados quando não há automatização exemplo | Scripts em `operational/tests/` segundo versão atual do GitHub |
| Documentação | Dispersão típica só com montagens manuais | Páginas desta loja e guias `operational/` no repositório |
| Repetibilidade | Depende fortemente de quem instalou e de anotações locais | Rotinas e containers documentados no repositório `caracore-area51` |

---

## Segurança referida na documentação

O material público costuma destacar OAuth 2.1, OIDC, PKCE, fluxo código de autorização, validação exemplo de JWT quando aplicável, parâmetro de estado contra CSRF, introspecção de token conforme desenho, cookies HTTP‑only segundo exemplos apresentados.

---

## Componentes comunicados institucionalmente

### Scripts baseline (repositório de código)
- Configuração OIDC padronizada
- Testes de validação
- Versionamento Git
- Entrega via GitHub

### Operação exemplo (`operational/`)
- Keycloak em Docker (automatizado)
- Exemplo de app protegida (Flask)
- Validação de fluxo OIDC
- Documentação passo-a-passo

### Suporte Cara Core (contrato)
- Consultoria OIDC
- Customizações
- Integração Gov.br/Entra ID
- Auditoria de segurança

---

## Documentação

- **Produto:** [produto.html](docs/produto.html)
- **Serviços:** [servicos.html](docs/servicos.html)
- **Download:** [download.html](docs/download.html)
- **Wiki:** [wiki](docs/wiki/index.html)
- **Termos:** [licenca-uso.html](docs/licenca-uso.html)
- **Contato:** [canal-feedback.html](docs/canal-feedback.html)

---

## Links

- **Loja online:** https://area51.caracore.com.br/
- **Código (GitHub):** https://github.com/chmulato/caracore-area51
- **Proposta de serviço:** [PROPOSTA_SERVICO_AREA51.md](https://github.com/chmulato/caracore-area51/blob/main/PROPOSTA_SERVICO_AREA51.md)

---

## Licença

> **Titularidade:** Produto Área 51 é de titularidade do **Governo Federal**. A Cara Core Informática atua como implementadora técnica. Ver [licenca-uso.html](docs/licenca-uso.html).

O produto não é MIT e não é “open source” no sentido de licença única ampla. Consulte [LICENSE](LICENSE).

---

## Contato

**Suporte & Orçamentos:**
- Email: suporte@caracore.com.br
- [Canal de feedback](docs/canal-feedback.html)

---

© 2026 Cara Core Informática · Área 51 — Implementação técnica de serviço

