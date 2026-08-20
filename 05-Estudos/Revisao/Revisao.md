---
type: moc
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Revisao

#area/estudos #estudos/revisao

Sistema de **revisão espaçada** para os conceitos do vault. O objetivo é revisar cada nota em intervalos crescentes (1-3-7-14-30 dias) até dominar o conteúdo.

## Como funciona

1. Toda nota de conceito tem um campo `progresso` no frontmatter: `estudando`, `revisar` ou `dominado`.
2. Após estudar um conceito, marque `progresso: estudando`.
3. Revisões em intervalos espaçados (ver [[Metodo-de-Revisao]]).
4. Ao acertar a revisão, avance o campo; ao errar, volte para `estudando`.

## Fila de revisão

```dataview
TABLE progresso AS "Progresso", file.updated AS "Última atualização"
FROM "05-Estudos"
WHERE type = "concept" AND progresso = "revisar"
SORT file.updated ASC
```

## Em estudo

```dataview
TABLE file.updated AS "Última atualização"
FROM "05-Estudos"
WHERE type = "concept" AND progresso = "estudando"
SORT file.updated ASC
```

## Dominados

```dataview
TABLE file.updated AS "Última atualização"
FROM "05-Estudos"
WHERE type = "concept" AND progresso = "dominado"
SORT file.updated ASC
```

## Relacionadas
- [[Metodo-de-Revisao]]

