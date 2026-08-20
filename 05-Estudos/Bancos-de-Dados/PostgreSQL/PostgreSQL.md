---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# PostgreSQL

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** SGBD relacional open-source e avançado, referência em conformidade com o padrão SQL, extensibilidade e recursos como JSONB, full-text search e transações ACID com MVCC.

## Conceitos-chave
- **ACID com MVCC:** controle de concorrência multiversão permite leituras consistentes sem bloquear escritas.
- **JSONB:** tipo binário JSON com operadores e índices GIN, unindo flexibilidade NoSQL ao SQL.
- **Extensões:** PostGIS (geo), pgvector (vetores), pg_stat_statements, entre outras.
- **Full-text search:** busca textual nativa com `to_tsvector`/`to_tsquery`.
- **Tipos avançados:** arrays, enums, ranges, tipos de rede, UUID nativo.
- **VACUUM/autovacuum:** limpeza das versões mortas de linhas geradas pelo MVCC.
- **Conformidade SQL:** implementação ampla e madura do padrão ANSI.

## Exemplos

```sql
CREATE TABLE usuarios (
  id   BIGSERIAL PRIMARY KEY,
  nome VARCHAR(120) NOT NULL,
  meta JSONB
);

CREATE INDEX idx_usuarios_meta ON usuarios USING GIN (meta);

-- Full-text search em português
SELECT * FROM artigos
WHERE to_tsvector('portuguese', titulo || ' ' || corpo)
  @@ to_tsquery('portuguese', 'banco & dados');
```

## Boas práticas
- Monitorar o autovacuum para evitar bloat e queda de performance.
- Usar `EXPLAIN ANALYZE` para entender e otimizar consultas.
- Aproveitar recursos nativos (JSONB, FTS, extensões) antes de ferramentas externas.
- Backup com `pg_dump`/`pg_basebackup` e restore testado.

## Armadilhas comuns
- Ignorar o MVCC: consultas longas seguram versões e geram bloat.
- Usar `SELECT *` e criar índices desnecessários.
- Tratar JSONB como "NoSQL": sem índices, os scans ficam caros.
- Confundir sintaxe com MySQL (ex.: `SERIAL`/`BIGSERIAL`, concatenação com `||`).

## Relacionadas
- [[Bancos-de-Dados]]
- [[Transactions]]
- [[Indexes]]
- [[Supabase]]