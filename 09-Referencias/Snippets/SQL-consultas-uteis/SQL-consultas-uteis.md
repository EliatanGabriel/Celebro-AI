---
type: snippet
area: referencias
status: active
created: "2026-08-22"
updated: "2026-08-22"
---

# SQL-consultas-uteis

#area/referencias
#referencias/snippets

Padrões SQL para validação de dados e consultas do dia a dia de QA. Quando usar: conferir integridade de dados, montar massa de teste, investigar bug no banco.

## Duplicados

```sql
-- emails duplicados na base
SELECT email, COUNT(*) AS qtd
FROM usuarios
GROUP BY email
HAVING COUNT(*) > 1;
```

## Último registro por grupo (window function)

```sql
-- último pedido de cada cliente
SELECT *
FROM (
  SELECT *,
         ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY criado_em DESC) AS rn
  FROM pedidos
) t
WHERE rn = 1;
```

## Registros sem correspondência (anti-join)

```sql
-- usuários que nunca fizeram pedido
SELECT u.*
FROM usuarios u
LEFT JOIN pedidos p ON p.usuario_id = u.id
WHERE p.id IS NULL;
```

## Upsert (inserir ou atualizar)

```sql
INSERT INTO config (chave, valor)
VALUES ('timeout', '30')
ON CONFLICT (chave) DO UPDATE SET valor = EXCLUDED.valor;  -- Postgres
```

## Datas rápidas

```sql
SELECT NOW() - INTERVAL '7 days';                       -- 7 dias atrás (Postgres)
SELECT * FROM logs WHERE criado_em::date = CURRENT_DATE; -- só hoje
```

> Sintaxe de intervalo varia: MySQL usa `NOW() - INTERVAL 7 DAY`.
