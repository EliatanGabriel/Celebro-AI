---
type: hub
area: referencias
status: active
created: "2026-08-22"
updated: "2026-08-22"
---

# Referencias

#area/referencias

A **busca rápida** do vault: definições curtas, comandos prontos e investigações com método. Não é para estudar a fundo — é para consultar como quem digita no Google.

> **Como usar:** aperte `Ctrl+O` (quick switcher) e digite o termo. Ou `Ctrl+Shift+F` para busca global em tudo.

## Subáreas
- [[Glossario]] — verbetes curtos: o que é X em 2 linhas
- [[Snippets]] — código e comandos prontos para copiar

## Inventário automático

```dataview
TABLE length(rows) AS "Notas"
FROM "09-Referencias"
FLATTEN file.etags AS tag
WHERE contains(tag, "#referencias/") AND !contains(tag, "#referencias/pesquisas")
FLATTEN substring(tag, 15) AS subarea
GROUP BY subarea
SORT length(rows) DESC
```

## Pesquisas em aberto

```dataview
LIST status
FROM ""
WHERE type = "pesquisa" AND status != "done"
SORT file.updated DESC
LIMIT 10
```
