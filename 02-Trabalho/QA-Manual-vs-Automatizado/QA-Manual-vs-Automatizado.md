---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# QA Manual vs Automatizado

#area/trabalho #trabalho/qa-manual-vs-automatizado #conceito

**Resumo:** Comparação entre testes manuais e automatizados.

## Conceitos-chave
- Teste manual é executado por uma pessoa; explora UI, UX e cenários não previstos.
- Teste automatizado roda via script/ferramenta; ideal para repetição e regressão.
- A escolha depende de frequência, estabilidade, custo e valor do cenário.

## Exemplos
```
Manual:          Automação:
- Exploração     - Regressão a cada release
- Cenários novos - Smoke pós-deploy
- UX/visual      - Testes críticos repetitivos
- 1º uso de UI   - Volumetria/API (cenários estáveis)
```
```bash
# Exemplo de teste automatizado (Playwright)
test('login com sucesso', async ({ page }) => {
  await page.goto('/login');
  await page.fill('#email', 'qa@exemplo.com');
  await page.click('text=Entrar');
  await expect(page).toHaveURL('/dashboard');
});
```

## Boas práticas
- Automatizar o que é repetitivo, crítico e estável; manter o manual no exploratório.
- Não automatizar tudo de primeira; priorizar por risco e retorno.
- Escolher a ferramenta pelo time e pelo stack (Playwright, Selenium, Cypress).
- Manter a suíte automatizada veloz e confiável para não perder valor.

## Armadilhas comuns
- Automatizar cenário instável, gerando manutenção e desconfiança.
- Automatizar o fluxo e abandonar o manual até para exploração.
- Suíte lenta que roda raramente e desatualiza com o produto.
- Comparar os dois como concorrentes em vez de complementares.

## Relacionadas
- [[Testes-Automatizados]]
- [[Caso-de-Teste]]
- [[Selenium]]