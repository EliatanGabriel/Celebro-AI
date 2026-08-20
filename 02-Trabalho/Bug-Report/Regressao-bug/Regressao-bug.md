---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Regressao-bug

#area/trabalho #trabalho/bug-report #conceito

**Resumo:** Bug que reaparece após correção ou nova funcionalidade.

## Conceitos-chave
- Regressão de bug é o retorno de um defeito já corrigido, ou a quebra de funcionalidade por mudança posterior.
- Geralmente causada por correção parcial, falta de cobertura de teste ou conflito entre mudanças.
- Detecta-se por re-teste de cenários já validados e por suítes de regressão.

## Estrutura de um bom bug report
- Registrar se o bug **já havia sido corrigido** e em qual versão/commit.
- Indicar a mudança provável que reintroduziu o problema (PR, branch, feature).
- Comparar comportamento entre a versão que funcionava e a versão atual.
- Vínculo com o bug report original para rastreabilidade do histórico.

## Boas práticas
- Ao corrigir um bug, adicionar um teste automatizado que cubra o cenário.
- Rodar suíte de regressão antes de liberar releases.
- Investigar regressões com histórico de deploys e `git log` das mudanças.
- Tratar bug reaparecido como prioridade, pois indica falha no processo.

## Armadilhas comuns
- Corrigir o sintoma sem cobrir a causa raiz com teste.
- Não verificar funcionalidades vizinhas após uma correção.
- Confundir regressão com bug novo e não rastrear o original.
- Liberar correção sem passar pela suíte de regressão.

## Relacionadas
- [[Deploy]]
- [[Regressao]]
- [[Rastreabilidade]]