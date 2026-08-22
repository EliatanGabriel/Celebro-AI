---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# JOINs

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** JOINs combinam linhas de tabelas relacionadas: INNER para interseção, LEFT/RIGHT/FULL para preservar lados, CROSS para produto cartesiano.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `INNER JOIN ... ON` | Só linhas com correspondência nos dois lados | ver exemplo |
| `LEFT JOIN` | Tudo da esquerda + casamentos (NULL se não houver) | `FROM a LEFT JOIN b ON ...` |
| `RIGHT JOIN` | Tudo da direita + casamentos | menos comum, troque a ordem |
| `FULL OUTER JOIN` | Tudo dos dois lados | união de LEFT e RIGHT |
| `CROSS JOIN` | Todas as combinações possíveis | `CROSS JOIN b` |
| `ON a.x = b.x` | Condição de ligação entre tabelas | sempre explícita |
| aliases `a`, `b` | Encurtam nomes; essenciais no self join | `FROM t p JOIN t f` |

## Exemplos

```sql
-- Pedidos com dados do cliente (só os que têm cliente)
SELECT p.id, c.nome, p.total
FROM pedidos p
INNER JOIN clientes c ON c.id = p.cliente_id
ORDER BY p.total DESC;

-- Clientes SEM pedidos: LEFT JOIN + IS NULL
SELECT c.nome
FROM clientes c
LEFT JOIN pedidos p ON p.cliente_id = c.id
WHERE p.id IS NULL;
```

```sql
-- Self join: funcionário e seu gestor na MESMA tabela
SELECT f.nome AS funcionario, g.nome AS gestor
FROM funcionarios f
LEFT JOIN funcionarios g ON g.id = f.gestor_id;

-- Múltiplos joins encadeados
SELECT c.nome, p.id, pr.nome AS produto
FROM pedidos p
JOIN clientes   c  ON c.id = p.cliente_id
JOIN itens_pedido ip ON ip.pedido_id = p.id
JOIN produtos   pr ON pr.id = ip.produto_id;
```

## Boas práticas

- Declare o join sempre com ON explícito, nunca na cláusula WHERE.
- Use aliases curtos e consistentes ao juntar várias tabelas.
- Prefira LEFT JOIN quando quiser preservar registros do lado principal.
- Filtros em colunas do lado NULL devem ficar no ON ou tratar IS NULL.
- Confira o plano (EXPLAIN) em joins sobre tabelas grandes.

## Armadilhas comuns

- Esquecer o ON cria um cross join acidental com milhões de linhas.
- WHERE em coluna da tabela direita mata o efeito do LEFT JOIN.
- Duplicar linhas quando a relação é 1:N e depois somar valores errados.
- FULL OUTER JOIN não existe em MySQL antigo: simule com UNION.
- Ambiguidade de coluna (id) sem prefixo de alias gera erro.

## Relacionadas

- [[Estudos-SQL]]
- [[Funcoes-de-Agregacao]]
- [[Subconsultas-e-CTEs]]
