---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# WHERE e Filtros

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** O WHERE filtra linhas com comparações, operadores lógicos, intervalos, listas, padrões e testes de nulo.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `= <> !=` | Igual / diferente | `WHERE status = 'ativo'` |
| `< > <= >=` | Comparações numéricas/datas | `WHERE preco >= 100` |
| `AND` / `OR` / `NOT` | Combina condições | `AND (a OR b)` |
| `BETWEEN x AND y` | Intervalo inclusivo | `BETWEEN 10 AND 20` |
| `IN (...)` | Lista de valores possíveis | `IN ('SP', 'RJ')` |
| `LIKE '%x_'` | Padrão: `%` vários, `_` um caractere | `LIKE 'Ana%'` |
| `IS NULL` / `IS NOT NULL` | Testa ausência de valor | `WHERE tel IS NULL` |

## Exemplos

```sql
-- Combinação de filtros com parênteses controlando precedência
SELECT nome, cidade, saldo
FROM clientes
WHERE ativo = TRUE
  AND (cidade = 'São Paulo' OR cidade = 'Rio')
  AND saldo BETWEEN 100 AND 5000;

-- Busca por padrão e valores em lista
SELECT * FROM produtos
WHERE nome LIKE '%notebook%'
  AND marca IN ('Acer', 'Lenovo', 'Dell');
```

```sql
-- Nulo exige IS NULL; = NULL não funciona
SELECT id, telefone
FROM clientes
WHERE telefone IS NULL;

-- Datas: use BETWEEN com cuidado na hora final do dia
SELECT * FROM pedidos
WHERE criado_em >= '2026-01-01'
  AND criado_em <  '2026-02-01';
```

## Boas práticas

- Use parênteses sempre que misturar AND com OR.
- Prefira IN a uma longa cadeia de ORs.
- Para busca textual complexa, considere full-text search em vez de LIKE %...%.
- Compare datas com meio-aberto (`>= início AND < fim`) para incluir tudo.
- Colunas filtradas com frequência são candidatas a índice.

## Armadilhas comuns

- `= NULL` nunca é verdadeiro: só IS NULL encontra nulos.
- NOT IN com NULL na subconsulta retorna zero linhas surpreendentemente.
- LIKE no início com `%texto%` não aproveita índices.
- BETWEEN em TIMESTAMP inclui o limite final exato, perdendo registros.
- Precedência: AND é avaliado antes de OR, mudando o resultado esperado.

## Relacionadas

- [[Estudos-SQL]]
- [[SELECT-Basico]]
- [[Subconsultas-e-CTEs]]
