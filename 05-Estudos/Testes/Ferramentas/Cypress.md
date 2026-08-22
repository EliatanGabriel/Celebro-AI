---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# Cypress

#area/estudos #estudos/testes #ferramenta

**Resumo:** Framework E2E que roda dentro do navegador, oferecendo viagem no tempo, auto-waiting nativo e comandos encadeados para testar fluxos completos de aplicações web.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `cy.visit(url)` | Abre uma página | `cy.visit("/login")` |
| `cy.get(sel)` | Seleciona elemento (auto-wait) | `cy.get("[data-testid=enviar]")` |
| `cy.contains(txt)` | Acha elemento pelo texto | `cy.contains("Entrar")` |
| `.type()` | Digita em input | `cy.get("#email").type("a@b.c")` |
| `.click()` | Clica no elemento | `.click()` |
| `.should()` | Assertiva encadeada | `.should("have.text", "Olá")` |
| `cy.intercept()` | Intercepta/stubba requisições | `cy.intercept("POST", "/api/login")` |
| `cy.fixture()` | Carrega dados de teste | `cy.fixture("usuario.json")` |
| `.as()` | Nomeia alias para reuso | `.as("usuario")` → `cy.get("@usuario")` |
| `cy.wait("@alias")` | Espera request interceptada | Sincronizar com a API |

## Exemplos

```js
describe("fluxo de login", () => {
  it("faz login com credenciais validas", () => {
    cy.intercept("POST", "/api/login").as("loginReq");

    cy.visit("/login");
    cy.get("[data-testid=email]").type("ana@teste.com");
    cy.get("[data-testid=senha]").type("secreta123");
    cy.get("[data-testid=enviar]").click();

    cy.wait("@loginReq").its("response.statusCode").should("eq", 200);
    cy.url().should("include", "/dashboard");
    cy.contains("Bem-vinda, Ana").should("be.visible");
  });
});
```

## Comandos úteis

```bash
npx cypress open      # abre o runner interativo
npx cypress run       # roda headless (CI)
npx cypress run --spec cypress/e2e/login.cy.js  # arquivo específico
```

## Boas práticas

- Use seletores estáveis como `data-testid`, não classes de CSS.
- Confiar no auto-waiting: nunca escreva `cy.wait(3000)` fixo.
- Interceptar chamadas externas lentas (`intercept`) mantém o teste determinístico.
- Um cenário de negócio por `it`; use `beforeEach` para o estado inicial.

## Armadilhas comuns

- Comandos Cypress são assíncronos e NÃO retornam promises comuns — não use `async/await` neles.
- Guardar valor em variável (`const x = cy.get(...)`) não funciona; use `.then()` ou aliases.
- Estado entre testes vaza: resete cookies/DB em `beforeEach`.
- Paralelismo completo depende do Dashboard pago; local é sequencial.

## Relacionadas

- [[Testes]]
- [[Playwright]]
- [[Tipos-de-Teste]]
- [[Piramide-de-Testes]]
