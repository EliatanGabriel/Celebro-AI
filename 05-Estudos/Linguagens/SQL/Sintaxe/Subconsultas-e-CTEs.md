---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Subconsultas e CTEs

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Consultas dentro de consultas (no WHERE, no FROM) e CTEs com WITH para decompor problemas complexos.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `(SELECT ...)` no WHERE | Valor ou lista para comparar | `WHERE id IN (SELECT ...)` |
| `EXISTS (SELECT 1 ...)` | Testa se a subconsulta retorna linhas | mais rápido que IN às vezes |
| subquery correlacionada | Referencia coluna da query externa | roda linha a linha |
| `FROM (SELECT ...) AS t` | Tabela derivada: consulta como fonte | precisa de alias |
| `WITH nome AS (...)` | CTE: consulta nomeada reutilizável | `SELECT * FROM nome` |
| `WITH RECURSIVE` | CTE que referencia a si mesma | hierarquias, árvores |

## Exemplos

```sql
-- Subconsulta no WHERE: produtos acima da média
SELECT nome, preco
FROM produtos
WHERE preco > (SELECT AVG(preco) FROM produtos);

-- EXISTS correlacionado: clientes com pedidos
SELECT c.nome
FROM clientes c
WHERE EXISTS (
    SELECT 1 FROM pedidos p
    WHERE p.cliente_id = c.id      -- usa a tabela externa
);
```

```sql
-- Tabela derivada no FROM + CTE nomeada
WITH vendas_por_cliente AS (
    SELECT cliente_id, SUM(total) AS total_gasto
    FROM pedidos
    GROUP BY cliente_id
)
SELECT c.nome, v.total_gasto
FROM clientes c
JOIN vendas_por_cliente v ON v.cliente_id = c.id
WHERE v.total_gasto > 1000;

-- CTE recursiva: árvore de categorias
WITH RECURSIVE arvore AS (
    SELECT id, nome FROM categorias WHERE pai_id IS NULL
    UNION ALL
    SELECT f.id, f.nome
    FROM categorias f JOIN arvore a ON f.pai_id = a.id
)
SELECT * FROM arvore;
```

## Boas práticas

- Prefira CTEs a subconsultas aninhadas profundas: ficam legíveis.
- Use EXISTS para testar existência; IN para listas pequenas de valores.
- Nomeie CTEs pelo que retornam, não pela origem.
- Quebre consultas gigantes em várias CTEs em etapas.
- Compare o plano com EXPLAIN: otimizadores modernos expandem CTEs.

## Armadilhas comuns

- NOT IN com NULL na subconsulta devolve zero linhas.
- Subquery no FROM sem alias é erro de sintaxe.
- Correlacionada mal escrita roda por linha e derruba a performance.
- WITH RECURSIVE sem condição de parada gera loop infinito.
- Alguns bancos antigos limitam níveis de aninhamento de subconsultas.

## Relacionadas

- [[Estudos-SQL]]
- [[JOINs]]
- [[Funcoes-de-Agregacao]]
