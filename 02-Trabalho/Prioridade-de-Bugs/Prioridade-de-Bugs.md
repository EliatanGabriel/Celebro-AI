---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Prioridade de Bugs

#area/trabalho #trabalho/prioridade-de-bugs #conceito

**Resumo:** Critérios para priorizar correções de bugs.

## Conceitos-chave
- Priorização decide a ordem de correção usando impacto, urgência, severidade e esforço.
- Combina fatores técnicos (severidade, abrangência) com de negócio (cliente, receita, deadline).
- A prioridade é um acordo de triagem, revisável conforme o contexto muda.

## Exemplos
```
Matriz simples (impacto x frequência):
|          | Alta frequência | Baixa frequência |
| Alto     | Crítica (agora) | Alta (planejada) |
| Impacto  | Alta (próx. ciclo) | Média (backlog)  |

Fatores: severidade, nº de usuários, data limite, workaround, esforço de correção.
```

## Boas práticas
- Triar bugs em reunião periódica com PO e devs, registrando o motivo.
- Definir critérios claros e compartilhados para cada nível de prioridade.
- Considerar workaround: se existe, o bug pode ser rebaixado.
- Revisar prioridades conforme a release se aproxima.

## Armadilhas comuns
- Priorizar só pela ordem de chegada ou pela pessoa que reportou.
- Ignorar o impacto em negócio e priorizar pelo gosto do reporter.
- Critérios subjetivos que geram disputa a cada bug.
- Bugs de baixa prioridade nunca revisados e acumulando dívida.

## Relacionadas
- [[Prioridade]]
- [[Severidade]]
- [[Bug-Report]]
- [[Jira]]