---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Jira

#area/trabalho #trabalho/ferramentas #conceito

**Resumo:** Ferramenta de gestão de projetos ágeis com issues e boards.

## Conceitos-chave
- Ferramenta de gestão ágil com issues, boards e sprints.
- Tipos de issue: epic, story, task, bug.
- Workflows com transições de status (A Fazer, Em Progresso, Review, Pronto).
- JQL para consultas e dashboards.
- Estimativas, campos customizados e integrações com CI/DevOps.

## Exemplos
```
# JQL típica do time de QA
project = QA AND issuetype = Bug AND status = "Em Progresso" ORDER BY priority DESC

# Buscar bugs da sprint atual
sprint = openSprints() AND issuetype = Bug
```

## Boas práticas
- Manter campos e descrições preenchidos com contexto.
- Atualizar o status conforme o fluxo real do trabalho.
- Definir e seguir o Definition of Done da equipe.
- Usar JQL em dashboards para acompanhar qualidade.
- Vincular tarefas a épicos e sprints corretos.

## Armadilhas comuns
- Cards sem descrição ou critérios de aceite.
- Status inconsistentes com o trabalho real.
- Estimativas irreais e nunca revisadas.
- Board desorganizado com itens sem dono.
- Criar issues duplicadas em vez de pesquisar antes.

## Relacionadas
- [[Trello]]
- [[Prioridade-de-Bugs]]