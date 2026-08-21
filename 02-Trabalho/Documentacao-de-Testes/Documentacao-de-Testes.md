---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Documentacao de Testes

#area/trabalho #trabalho/documentacao-de-testes #conceito

**Resumo:** Registros que descrevem planos, casos e resultados de testes.

## Conceitos-chave
- Documentação de testes cobre plano de testes, casos, execução, resultados e evidências.
- Garante rastreabilidade entre requisito, caso de teste e resultado.
- Serve de base para auditoria, regressão e onboarding de novos QAs.

## Exemplos
```
Plano de testes (v1.4.0):
- Escopo: fluxo de compra, login, cupom
- Fora de escopo: API legacy
- Ambientes: staging
- Critério de saída: 100% casos críticos passando

Resultado de execução:
| CT | Status | Observação | Evidência |
| CT-014 | Passou | ... | print_014.png |
| CT-021 | Falhou | erro 422 | print_021.png |
```

## Boas práticas
- Manter a documentação versionada e próxima do código (docs/ ou wiki).
- Vincular cada caso ao requisito e ao resultado da execução.
- Registrar evidências e a versão do sistema testado.
- Revisar e atualizar a documentação a cada mudança relevante.

## Armadilhas comuns
- Documentação desatualizada que descreve comportamento antigo.
- Registrar só o "passou" sem evidência ou observação.
- Plano sem critérios de saída, impossível saber se o ciclo fechou.
- Guardar documentação em lugar não acessível ao time.

## Relacionadas
- [[Caso-de-Teste]]
- [[Report]]
- [[Testes-Automatizados]]