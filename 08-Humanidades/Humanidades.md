---
type: hub
area: humanidades
status: active
created: "2026-08-22"
updated: "2026-08-22"
---

# Humanidades

#area/humanidades

As grandes perguntas humanas: o que é real, como sabemos, como devemos viver — e Deus no centro de tudo.

## Subáreas
- [[Filosofia]]
- [[Teologia]]
- [[Historia]]
- [[Literatura]]
- [[Sociologia-e-Economia]]
- [[Revisao]]

## Dashboard

```dataview
TABLE length(rows) AS "Conceitos"
FROM "08-Humanidades"
WHERE type = "concept" AND !contains(file.path, "Revisao")
FLATTEN file.etags AS tag
WHERE contains(tag, "#humanidades/")
FLATTEN substring(tag, 13) AS subarea
GROUP BY subarea
SORT length(rows) DESC
```

### Fila de revisão de hoje

```dataview
LIST
FROM "08-Humanidades"
WHERE type = "concept" AND progresso = "revisar"
SORT file.updated ASC
LIMIT 5
```
