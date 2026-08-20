---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# E2E

#area/trabalho #trabalho/testes-automatizados #conceito

**Resumo:** Testes ponta a ponta que validam fluxos completos do usuário.

## Conceitos-chave
- Testes ponta a ponta que percorrem o fluxo completo do usuário no navegador.
- Validam a integração entre frontend, backend, banco de dados e serviços externos.
- Cobrem cenários críticos: login, busca, checkout, pagamento, cadastro.
- Baseados em ferramentas como Cypress, Playwright e Selenium.
- Também usados como smoke tests pós-deploy.

## Exemplos
```
// Fluxo típico coberto por testes E2E
1. Usuário acessa a home
2. Faz login com credenciais válidas
3. Adiciona um item ao carrinho
4. Fecha o pedido e informa pagamento
5. Confere a confirmação do pedido
```

## Boas práticas
- Priorizar fluxos de maior valor e risco de negócio.
- Executar em ambiente controlado (staging) com dados seed previsíveis.
- Manter a suíte enxuta: poucos testes, mas robustos.
- Usar seletores estáveis e esperas automáticas.
- Integrar ao pipeline de CI para rodar a cada deploy.

## Armadilhas comuns
- Suítes lentas e flaky por dependência de dados reais.
- Alto custo de manutenção quando a UI muda.
- Tentar substituir testes unitários e de integração por E2E.
- Dependência da ordem de execução entre testes.
- Rodar contra produção sem dados isolados.

## Relacionadas
- [[Cypress]]
- [[Playwright]]
- [[Integration-testing]]