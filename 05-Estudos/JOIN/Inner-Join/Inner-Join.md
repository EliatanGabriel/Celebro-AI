---
type: concept
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# INNER JOIN

#area/estudos #join #conceito #sql #join #consultas

**Resumo:** Retorna apenas as linhas com correspondência nas duas tabelas, eliminando registros sem par na outra tabela.

## Conceitos-chave
- **Chave de junção:** coluna (ou conjunto de colunas) usada para correlacionar as tabelas, normalmente uma chave primária e sua chave estrangeira.
- **Sintaxe:** `SELECT ... FROM a JOIN b ON a.id = b.fk` (a palavra `INNER` é opcional).
- **Resultado:** interseção lógica das duas tabelas; linhas sem correspondência são descartadas.
- **Tabelas intermediárias:** JOINs encadeados montam resultados que cruzam várias tabelas.
- **Equivalência:** `INNER JOIN` equivale a um produto cartesiano filtrado (`FROM a, b WHERE a.id = b.fk`).

## Exemplos
```sql
SELECT pedidos.id, clientes.nome
FROM pedidos
INNER JOIN clientes ON pedidos.cliente_id = clientes.id;

-- Com alias e múltiplas junções
SELECT o.id, c.nome, p.descricao
FROM pedidos AS o
INNER JOIN clientes AS c ON o.cliente_id = c.id
INNER JOIN pedido_itens AS i ON i.pedido_id = o.id
INNER JOIN produtos AS p ON p.id = i.produto_id;
```

## Boas práticas
- Sempre qualificar as colunas com o nome ou alias da tabela.
- Referenciar índices na chave de junção para evitar full scans.
- Preferir `INNER JOIN` explícito ao `WHERE` com vírgulas para legibilidade.
- Conferir as contagens antes e depois do JOIN para validar a cardinalidade.

## Armadilhas comuns
- Esquecer a condição de junção (ON), gerando produto cartesiano não intencional.
- Duplicar linhas quando a tabela da direita tem mais de um registro correspondente.
- Confundir `INNER JOIN` com `LEFT JOIN` e perder linhas esperadas.
- Comparar colunas com tipos diferentes, forçando conversões implícitas lentas.

## Relacionadas
- [[Left-Join]]
- [[Cross-Join]]
- [[Estudos-SQL]]
- [[Indexes]]