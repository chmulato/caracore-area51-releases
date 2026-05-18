# caracore-area51-releases — Loja Oficial Área 51

**Loja e releases** do **Suporte Área 51** — Plataforma completa de OIDC (OpenID Connect / OAuth 2.1).

## 🎯 O Que É Área 51

**Plataforma de configuração e operação de ambientes OpenID Connect seguro** para órgãos públicos e empresas.

- ✅ **Scripts baseline** — Configuração OIDC padronizada (Python)
- ✅ **Deploy automatizado** — Keycloak + Protected App em um comando
- ✅ **Testes integrados** — Validação OAuth 2.1 + PKCE
- ✅ **Documentação completa** — Setup, conceitos, troubleshooting

**Tempo:** &lt;5 minutos de setup (vs. 2-3 semanas manual)

---

## 📍 Repositórios

| Repositório | Propósito | Público |
|------------|----------|---------|
| **caracore-area51** | Código (desenvolvimento + operação) | Desenvolvedores, DevOps |
| **caracore-area51-releases** | Loja oficial (este repositório) | Clientes, interessados |

---

## 🛍️ Acesso Rápido (GitHub Pages)

A pasta `docs/` é publicada em: **https://area51.caracore.com.br/**

| Página | Descrição |
|--------|-----------|
| [**produto.html**](docs/produto.html) | 🎯 Visão geral do produto, features, casos de uso |
| [**servicos.html**](docs/servicos.html) | 💼 Três opções de engajamento (Básico, Implementação, Platinum) |
| [**index.html**](docs/index.html) | 🏠 Página inicial da loja |
| [**download.html**](docs/download.html) | 📥 Como baixar e começar |
| [**licenca-uso.html**](docs/licenca-uso.html) | ⚖️ Termos e licença |
| [**canal-feedback.html**](docs/canal-feedback.html) | 💬 Contato e suporte |

---

## 🚀 Quick Start

### 1. Produto Básico (Gratuito)

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

**Resultado:** Keycloak + Protected App + Testes ✅ em &lt;5 minutos

---

### 2. Implementação Guiada

Precisa de ajuda? **[Solicite orçamento](docs/canal-feedback.html)**

- Setup no seu ambiente
- Integração com sua aplicação
- Validação de segurança
- Suporte durante implementação

---

### 3. Suporte Platinum

Para órgãos críticos:
- Implementação completa
- Integração Gov.br / Entra ID
- Auditoria de segurança
- Suporte 24x5 com SLA

**[Falar com especialista](docs/canal-feedback.html)**

---

## 📊 Comparação: Antes vs. Depois

| Aspecto | Antes (Manual) | Com Área 51 |
|--------|---------------|-----------|
| Tempo de setup | 2-3 semanas | &lt;5 min ⚡ |
| Segurança (PKCE) | Manual | Automático ✅ |
| Testes OIDC | Inexistentes | Inclusos ✅ |
| Documentação | Dispersa | Centralizada ✅ |
| Reprodutibilidade | Inconsistente | 100% ✅ |

---

## 🔐 Segurança

Implementamos **padrões OAuth 2.1 + OpenID Connect**:

- ✅ PKCE (Proof Key Code Exchange)
- ✅ Authorization Code Flow
- ✅ JWT Token Validation
- ✅ State Parameter (CSRF)
- ✅ Token Introspection
- ✅ HTTP-only Cookies

---

## 📋 Componentes

### Componente 1: Scripts Baseline
- Configuração OIDC padronizada
- Testes de validação
- Versionamento Git
- Entrega via GitHub

### Componente 2: Deploy Operacional
- Keycloak em Docker (automatizado)
- Exemplo de app protegida (Flask)
- Validação de fluxo OIDC
- Documentação passo-a-passo

### Componente 3: Suporte Técnico
- Consultoria OIDC
- Customizações
- Integração Gov.br/Entra ID
- Auditoria de segurança

---

## 📚 Documentação

- **Produto:** [produto.html](docs/produto.html)
- **Serviços:** [servicos.html](docs/servicos.html)
- **Download:** [download.html](docs/download.html)
- **Termos:** [licenca-uso.html](docs/licenca-uso.html)
- **Contato:** [canal-feedback.html](docs/canal-feedback.html)

---

## 🔗 Links

- **Loja online:** https://area51.caracore.com.br/
- **Código (GitHub):** https://github.com/chmulato/caracore-area51
- **Propose serviço:** Ver [PROPOSTA_SERVICO_AREA51.md](https://github.com/chmulato/caracore-area51/blob/main/PROPOSTA_SERVICO_AREA51.md)

---

## ⚖️ Licença

> ⚠️ **Titularidade:** Produto Área 51 é de titularidade do **Governo Federal**.
> Cara Core Informática atua como implementadora técnica.

O produto não é MIT e não é open source. Consulte [LICENSE](LICENSE) para detalhes.

---

## 📞 Contato

**Suporte & Orçamentos:**
- Email: suporte@caracore.com.br
- [Canal de feedback](docs/canal-feedback.html)

---

© 2026 Cara Core Informática · Área 51 — Implementação técnica de serviço

