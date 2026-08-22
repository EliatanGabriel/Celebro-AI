---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Funções de Agregação

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Funções que condensam várias linhas em um único valor (COUNT, SUM, AVG...) combinadas com GROUP BY e HAVING.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `COUNT(*)` | Conta TODAS as linhas, inclusive nulas | `SELECT COUNT(*) FROM pedidos;` |
| `COUNT(coluna)` | Conta apenas valores não nulos | `COUNT(telefone)` |
| `SUM(col)` | Soma os valores | `SUM(total)` |
| `AVG(col)` | Média aritmética | `AVG(preco)` |
| `MIN(col)` / `MAX(col)` | Menor / maior valor | `MIN(criado_em)` |
| `GROUP BY col` | Agrupa linhas por coluna(s) | `GROUP BY cidade` |
| `HAVING cond` | Filtra grupos após a agregação | `HAVING COUNT(*) > 5` |

## Exemplos

```sql
-- Total de vendas por cidade, só cidades com mais de 10 clientes
SELECT
    cidade,
    COUNT(*)        AS clientes,
    AVG(saldo)      AS saldo_medio,
    MAX(criado_em)  AS ultimo_cadastro
FROM clientes
WHERE ativo = TRUE            -- filtra LINHAS antes do agrupamento
GROUP BY cidade
HAVING COUNT(*) > 10          -- filtra GRUPOS depois da agregação
ORDER BY clientes DESC;
```

```sql
-- COUNT(*) vs COUNT(coluna): nulos mudam o resultado
SELECT
    COUNT(*)          AS total_linhas,
    COUNT(telefone)   AS com_telefone,
    COUNT(*) - COUNT(telefone) AS sem_telefone
FROM clientes;

-- Agregação sobre expressão calculada
SELECT SUM(preco * quantidade) AS faturamento
FROM itens_pedido;
```

## Boas práticas

- Toda coluna no SELECT fora de agregação deve estar no GROUP BY.
- Use aliases descritivos para resultados agregados.
- Filtre linhas no WHERE e grupos no HAVING: cada um no seu lugar.
- Prefira COUNT(*) para contar linhas; COUNT(col) quando nulls importam.
- Combine com ORDER BY para deixar relatórios legíveis.

## Armadilhas comuns

- Colocar condição de grupo no WHERE (ou de linha no HAVING) dá erro.
- Esquecer uma coluna não agregada do GROUP BY quebra a consulta.
- AVG ignora NULL: a média pode não ser a esperada.
- COUNT(DISTINCT col) é caro em tabelas muito grandes.
- SUM de coluna toda nula retorna NULL, não zero: use COALESCE.

## Relacionadas

- [[Estudos-SQL]]
- [[JOINs]]
- [[WHERE-e-Filtros]]
