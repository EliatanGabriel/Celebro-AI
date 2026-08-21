---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Regressao

#area/trabalho #trabalho/regressao #conceito

**Resumo:** Verificação de que mudanças não quebraram funcionalidades existentes.

## Conceitos-chave
- Teste de regressão revalida funcionalidades já entregues após novas mudanças.
- Foco em proteger contra bugs reintroduzidos (regressão de bug) por novas features/correções.
- Pode ser manual (re-teste) ou automatizado (suíte de regressão).

## Exemplos
```bash
# Rodar suíte de regressão automatizada antes de release
npx playwright test --grep "@regressao"

# Smoke rápido pós-deploy
npm run test:smoke
```
```yaml
# Pipeline: suíte de regressão como gate antes de produção
  regression:
    runs-on: ubuntu-latest
    steps:
      - run: npx playwright test --grep "@regressao"
```

## Boas práticas
- Priorizar automação dos cenários críticos e de maior risco de regressão.
- Rodar regressão a cada release e quando houver mudança de dependências.
- Manter a suíte estável e rápida para rodar com frequência.
- Cobrir com teste a correção de cada bug para evitar reincidência.

## Armadilhas comuns
- Suíte de regressão enorme, lenta e flaky que ninguém executa.
- Testar só funcionalidades novas e ignorar as existentes.
- Regressão manual incompleta ou sem registro de resultado.
- Não correlacionar bug reaparecido com a suíte que deveria ter pegado.

## Relacionadas
- [[Regressao-bug]]
- [[Testes-Automatizados]]
- [[Ciclo-de-Release]]