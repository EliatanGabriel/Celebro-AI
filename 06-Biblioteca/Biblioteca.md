---
type: hub
area: biblioteca
status: active
created: "2026-08-15"
updated: "2026-08-19"
---

# Biblioteca

#area/biblioteca

Livros lidos, em leitura, por ler e abandonados.

## Coleções
- [[Quero-Ler]]
- [[Lendo]]
- [[Lidos]]
- [[Abandonei]]

## Dashboard

```dataview
TABLE rows.file.name AS "Livro"
FROM "06-Biblioteca"
WHERE type = "book"
GROUP BY status
```

### Por status

```dataview
LIST FROM "06-Biblioteca"
WHERE type = "book" AND status = "lendo" SORT file.name ASC
```

```dataview
LIST FROM "06-Biblioteca"
WHERE type = "book" AND status = "lido" SORT file.name ASC
```

```dataview
LIST FROM "06-Biblioteca"
WHERE type = "book" AND status = "quero-ler" SORT file.name ASC
```

```dataview
LIST FROM "06-Biblioteca"
WHERE type = "book" AND status = "abandonei" SORT file.name ASC
```
