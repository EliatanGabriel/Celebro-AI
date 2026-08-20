---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Paginacao

#area/trabalho #trabalho/api-rest #conceito

**Resumo:** Divisão de grandes conjuntos de resultados em páginas menores.

## Conceitos-chave
- Divide grandes conjuntos em páginas menores.
- Abordagens: page/limit, offset/limit e cursor (keyset).
- Meta com total, página atual e tamanho.
- Links de navegação: next, prev, first, last.
- Ordenação estável para páginas consistentes.

## Exemplos
```
GET /api/produtos?page=2&limit=20

{
  "data": [ ... ],
  "meta": { "page": 2, "limit": 20, "total": 154, "pages": 8 },
  "links": { "next": "/api/produtos?page=3&limit=20" }
}
```

## Boas práticas
- Definir limit padrão e máximo para a API.
- Incluir meta e links de navegação na resposta.
- Manter ordenação estável para evitar duplicatas entre páginas.
- Usar cursor/keyset para datasets grandes e de alta escrita.
- Documentar os parâmetros de paginação.

## Armadilhas comuns
- Offset lento e inconsistente em datasets grandes.
- Paginação instável quando a ordenação não é determinística.
- Omitir total/pages, dificultando o cliente.
- Cursor mal implementado (sem chave composta correta).
- Não validar limites extremos (0, negativo, acima do máximo).

## Relacionadas
- [[Endpoints]]
- [[Rate-Limiting]]
- [[Serializacao]]