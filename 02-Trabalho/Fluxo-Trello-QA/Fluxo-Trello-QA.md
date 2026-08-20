---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Fluxo Trello QA

#area/trabalho #trabalho/fluxo-trello-qa #conceito

**Resumo:** Fluxo de trabalho do time de QA usando o Trello.

## Conceitos-chave
- O Trello organiza o trabalho de QA em quadros com listas (colunas) e cards.
- Cada card representa uma tarefa: bug, caso de teste, feature a validar.
- Transições de coluna espelham o estado: A fazer -> Em teste -> Bloqueado -> Concluído.
- Labels e checklists padronizam tipo, severidade e critérios.

## Exemplos
```
Quadro "QA":
| Backlog   | Em teste     | Bloqueado    | Concluído |
| --------- | ------------ | ------------ | --------- |
| Bug #123  | Feature #45  | Bug aguard.  | Bug #100  |
| Melhoria  | Bug #118     | fix do dev   | Suíte R2  |

Labels: bug | feature | alta | média | baixa | bloqueado
Checklist de bug: título, ambiente, passos, expected/actual, evidência.
```

## Boas práticas
- Definir um fluxo único e comunicado para todo o time (QA e devs).
- Usar labels padronizados para prioridade e tipo.
- Manter o card atualizado no estado real para o quadro ser fonte da verdade.
- Criar automações simples: mover card ao mudar label, notificar por tag.

## Armadilhas comuns
- Quadro sem definição de fluxo, cada pessoa movendo de forma diferente.
- Cards sem contexto suficiente, obrigando abrir o bug report fora.
- Acumular cards em "Em teste" sem fechamento ou devolução.
- Confundir o quadro do Trello com o registro definitivo do bug report.

## Relacionadas
- [[Trello]]
- [[Prioridade-de-Bugs]]
- [[Bug-Report]]