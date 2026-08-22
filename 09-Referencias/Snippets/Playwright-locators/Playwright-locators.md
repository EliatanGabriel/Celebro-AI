---
type: snippet
area: referencias
status: active
created: "2026-08-22"
updated: "2026-08-22"
---

# Playwright-locators

#area/referencias #referencias/snippets

Locators e esperas do Playwright para automação E2E estável. Quando usar: escrever seletores que não quebram a cada deploy — prioridade **role > label > test-id**, CSS/`xpath` só como último recurso.

## Locators por acessibilidade (preferidos)

```javascript
page.getByRole('button', { name: 'Entrar' });
page.getByLabel('E-mail');
page.getByPlaceholder('Buscar produtos');
page.getByText('Pedido confirmado');
page.getByTestId('btn-checkout');           // se o time usa data-testid
```

## Encadear e filtrar

```javascript
// linha da tabela com texto específico → botão dentro dela
page.getByRole('row', { name: /pedido 123/ }).getByRole('button', { name: 'Detalhes' });

// pegar item exato de uma lista
page.getByRole('listitem').filter({ hasText: 'Ativo' });
```

## Esperas (quase nunca precisa de sleep)

```javascript
await expect(page.getByText('Sucesso')).toBeVisible({ timeout: 5000 });

// esperar rede acalmar após clique que dispara requisições
await Promise.all([
  page.waitForResponse(r => r.url().includes('/api/pedidos') && r.status() === 200),
  page.getByRole('button', { name: 'Finalizar' }).click(),
]);
```

> `waitForTimeout(3000)` é code smell: testa lento E frágil. Espere por condição, não por tempo.

## Debug rápido

```bash
npx playwright test --headed --debug     # pausa passo a passo com inspector
npx playwright codegen site.com          # grava cliques e gera código
```
