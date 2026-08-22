---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# SELECT Básico

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** O comando SELECT consulta dados: escolha de colunas, apelidos, remoção de duplicatas e ordenação/paginação.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `SELECT col1, col2` | Retorna colunas específicas | `SELECT nome, email FROM clientes;` |
| `SELECT *` | Retorna todas as colunas | `SELECT * FROM produtos;` |
| `FROM tabela` | Define a fonte dos dados | `FROM pedidos` |
| `AS` / alias | Renomeia coluna ou tabela na saída | `SELECT nome AS cliente` |
| `DISTINCT` | Remove linhas repetidas | `SELECT DISTINCT cidade FROM ...` |
| `ORDER BY a ASC, b DESC` | Ordena por uma ou mais colunas | ver exemplo |
| `LIMIT n OFFSET m` | Pagina resultados | `LIMIT 10 OFFSET 20` |
| `FETCH FIRST n ROWS ONLY` | Alternativa padrão SQL ao LIMIT | `FETCH FIRST 5 ROWS ONLY` |

## Exemplos

```sql
-- Lista com apelidos e ordenação por duas colunas
SELECT
    nome AS cliente,
    cidade,
    criado_em AS cadastro
FROM clientes
ORDER BY cidade ASC, cadastro DESC;

-- Cidades únicas cadastradas
SELECT DISTINCT cidade
FROM clientes;
```

```sql
-- Paginação: página 3 com 10 registros por página
SELECT id, nome
FROM produtos
ORDER BY preco DESC
LIMIT 10 OFFSET 20;

-- Sintaxe padrão (SQL standard), usada no SQL Server/Oracle
SELECT id, nome
FROM produtos
ORDER BY preco DESC
OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY;
```

## Boas práticas

- Liste apenas as colunas necessárias em vez de `SELECT *`.
- Use aliases claros quando juntar tabelas ou calcular valores.
- Sempre combine ORDER BY com LIMIT para paginação estável.
- Ordene por coluna indexada quando o volume for grande.
- Comente consultas complexas explicando a intenção.

## Armadilhas comuns

- `SELECT *` em tabelas largas degrada performance e quebra código.
- ORDER BY sem desempate retorna ordens diferentes entre execuções.
- OFFSET alto (página 1000) fica lento: considere keyset pagination.
- Em alguns bancos (Oracle antigo) não há LIMIT: usa-se ROWNUM/FETCH.
- Alias definido no SELECT não pode ser usado dentro do WHERE.

## Relacionadas

- [[Estudos-SQL]]
- [[WHERE-e-Filtros]]
- [[Funcoes-de-Agregacao]]
