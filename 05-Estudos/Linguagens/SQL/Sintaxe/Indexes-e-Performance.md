---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Indexes e Performance

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Índices aceleram buscas e joins ao custo de espaço e escritas; EXPLAIN revela se a consulta está aproveitando bem.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `CREATE INDEX` | Índice comum em uma coluna | `CREATE INDEX idx_email ON clientes(email);` |
| `CREATE UNIQUE INDEX` | Índice que impede duplicatas | `UNIQUE INDEX ON t(cpf)` |
| índice composto | Várias colunas na ordem de uso | `(cidade, criado_em)` |
| `DROP INDEX` | Remove o índice | `DROP INDEX idx_email;` |
| `EXPLAIN consulta` | Mostra o plano de execução | custo estimado |
| `EXPLAIN ANALYZE` | Executa de verdade e mostra tempos reais (Postgres) | ver exemplo |

## Exemplos

```sql
-- Colunas muito filtradas merecem índice
CREATE INDEX idx_pedidos_cliente ON pedidos(cliente_id);

-- Composto: funciona para filtros por cidade,
-- e também cidade + data (ordem importa!)
CREATE INDEX idx_cli_cidade_data ON clientes(cidade, criado_em);

-- Índice único
CREATE UNIQUE INDEX idx_prod_slug ON produtos(slug);
```

```sql
-- Diagnóstico no Postgres
EXPLAIN ANALYZE
SELECT id, nome
FROM clientes
WHERE cidade = 'Recife'
ORDER BY criado_em DESC
LIMIT 10;

-- Antes: Seq Scan + Sort (lento)
-- Depois do índice: Index Scan usando idx_cli_cidade_data
```

## Boas práticas

- Crie índices para colunas usadas em WHERE, JOIN e ORDER BY frequentes.
- Em índices compostos, coloque primeiro a coluna mais seletiva/usada.
- Monitore consultas lentas antes de sair criando índices.
- Remova índices não utilizados que só custam em INSERT/UPDATE.
- Liste colunas específicas em vez de SELECT * para permitir index-only scan.

## Armadilhas comuns

- Cada índice extra deixa INSERT/UPDATE/DELETE mais lentos.
- Funções na coluna (`WHERE YEAR(data) = 2026`) anulam o índice.
- LIKE '%texto' no início da busca não usa índice comum.
- Ordem errada nas colunas do índice composto o torna inútil.
- EXPLAIN sem ANALYZE mostra estimativas, não a realidade.

## Relacionadas

- [[Estudos-SQL]]
- [[SELECT-Basico]]
- [[Constraints-e-Chaves]]
