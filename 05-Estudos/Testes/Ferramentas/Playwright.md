---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# Playwright

#area/estudos #estudos/testes #ferramenta

**Resumo:** Framework E2E multi-browser (Chromium, Firefox, WebKit) da Microsoft, com auto-waiting, locators web-first, paralelismo gratuito e ferramentas de depuração como trace e codegen.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `page.goto(url)` | Navega até uma URL | `await page.goto("/login")` |
| `page.getByRole` | Locator por acessibilidade | `page.getByRole("button", { name: "Enviar" })` |
| `page.getByText` | Locator por texto | `page.getByText("Bem-vindo")` |
| `page.getByLabel` | Input via label associado | `page.getByLabel("Email")` |
| `page.getByTestId` | Locator por data-testid | `page.getByTestId("enviar")` |
| `.fill()` | Limpa e digita num campo | `.fill("ana@teste.com")` |
| `.click()` | Clica no elemento | `.click()` |
| `expect(loc).toHaveText` | Asserção web-first (auto-wait) | `await expect(msg).toBeVisible()` |
| `route.fulfill` | Mock de rede | Stub de resposta de API |
| `test.describe.configure` | Paralelismo/sharding | Rodar workers simultâneos |

## Exemplos

```js
import { test, expect } from "@playwright/test";

test("login redireciona para dashboard", async ({ page }) => {
  await page.route("**/api/session", (rota) =>
    rota.fulfill({ status: 200, body: JSON.stringify({ token: "abc" }) })
  );

  await page.goto("/login");
  await page.getByLabel("Email").fill("ana@teste.com");
  await page.getByLabel("Senha").fill("secreta123");
  await page.getByRole("button", { name: "Entrar" }).click();

  await expect(page).toHaveURL(/dashboard/);
  await expect(page.getByText("Bem-vinda, Ana")).toBeVisible();
});
```

## Comandos úteis

```bash
npx playwright test            # roda toda a suite
npx playwright test --ui       # modo UI interativo com time travel
npx playwright codegen         # grava ações e gera código do teste
npx playwright show-report     # relatório HTML com traces
npx playwright test --project=firefox  # só um browser
```

## Boas práticas

- Prefira locators de papel/rótulo (`getByRole`) — melhoram a acessibilidade de graça.
- Confie no auto-waiting: asserções web-first retryam sozinhas.
- Habilite traces em retries (`trace: "on-first-retry"`) para depurar CI.
- Use fixtures de contexto (`{ page }`) e usuários de teste por papel (admin, cliente).

## Armadilhas comuns

- Misturar locator API antiga (`page.$`, `page.waitForSelector`) com a nova gera testes frágeis.
- `page.waitForTimeout(3000)` fixo: substitua por `expect(...).toBeVisible()`.
- Esquecer `await`: todas as APIs Playwright são promessas.
- Testes dependentes de ordem quebram com paralelismo ativado.

## Relacionadas

- [[Testes]]
- [[Cypress]]
- [[Testing-Library]]
- [[Tipos-de-Teste]]
- [[Piramide-de-Testes]]
