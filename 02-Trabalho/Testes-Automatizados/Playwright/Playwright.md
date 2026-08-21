---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Playwright

#area/trabalho #trabalho/testes-automatizados #conceito

**Resumo:** Framework de automação web moderno da Microsoft, multi-navegador.

## Conceitos-chave
- Automação web moderna da Microsoft, multi-navegador: Chromium, Firefox e WebKit.
- Auto-wait embutido: ações aguardam o elemento ficar pronto automaticamente.
- Codegen para gerar testes a partir de interações gravadas.
- Trace viewer para depurar execuções passo a passo.
- Suporte a mobile (dispositivos), testes de API e execução paralela com workers.

## Exemplos
```
import { test, expect } from '@playwright/test';

test('busca um produto', async ({ page }) => {
  await page.goto('https://exemplo.com');
  await page.getByRole('searchbox', { name: 'Buscar' }).fill('QA');
  await page.getByRole('button', { name: 'Buscar' }).click();
  await expect(page.getByText('Resultados')).toBeVisible();
});
```

## Boas práticas
- Preferir locators por papel/texto (getByRole, getByLabel) em vez de seletores frágeis.
- Configurar baseURL e dispositivos no playwright.config.
- Habilitar traces em caso de falha para debug rápido.
- Usar fixtures para estado inicial (login, dados seed) e isolar testes.
- Rodar em CI com workers paralelos e reuso de servidor web.

## Armadilhas comuns
- Seletores CSS acoplados a classes que mudam com frequência.
- Testes paralelos compartilhando estado (banco, cookies, arquivos).
- waitForTimeout arbitrário para "esperar carregar" — preferir esperas automáticas.
- Diferenças de comportamento entre navegadores não cobertas.
- Ignorar a gravação de traces quando o teste falha.

## Relacionadas
- [[Cypress]]
- [[E2E]]
- [[Test-frameworks]]
- [[Testes-Automatizados]]