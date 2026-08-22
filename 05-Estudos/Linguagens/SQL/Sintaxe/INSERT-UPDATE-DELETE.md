---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# INSERT, UPDATE e DELETE

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Comandos DML para inserir, modificar e remover linhas, com atenção redobrada ao WHERE do UPDATE/DELETE.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `INSERT INTO t (cols) VALUES (...)` | Insere uma linha | ver exemplo |
| `VALUES (...), (...), ...` | Insere múltiplas linhas de uma vez | ver exemplo |
| `UPDATE t SET col = val` | Altera valores existentes | sempre com WHERE! |
| `DELETE FROM t` | Remove linhas | sempre com WHERE! |
| `RETURNING *` (Postgres) | Retorna as linhas afetadas | `INSERT ... RETURNING id;` |

## Exemplos

```sql
-- Inserção simples
INSERT INTO clientes (nome, email, cidade)
VALUES ('Ana Souza', 'ana@email.com', 'São Paulo');

-- Inserção em lote: mais rápido que vários INSERTs
INSERT INTO produtos (nome, preco) VALUES
    ('Teclado', 149.90),
    ('Mouse',   79.90),
    ('Monitor', 899.00);

-- Postgres: já devolve o id gerado
INSERT INTO clientes (nome) VALUES ('Bia') RETURNING id;
```

```sql
-- UPDATE sempre acompanhado de WHERE
UPDATE produtos
SET preco = preco * 1.10,      -- aumento de 10%
    atualizado_em = CURRENT_TIMESTAMP
WHERE categoria = 'periféricos';

-- DELETE pontual
DELETE FROM clientes
WHERE ativo = FALSE AND criado_em < '2024-01-01';

-- Sem WHERE afeta TODAS as linhas!
UPDATE produtos SET preco = 0;        -- zera a tabela inteira
```

## Boas práticas

- Escreva o WHERE antes do SET/da condição mentalmente antes de rodar.
- Teste o filtro com um SELECT antes de transformar em UPDATE/DELETE.
- Prefira inserções em lote a laços de INSERTs individuais.
- Use transações para poder reverter operações perigosas.
- Em Postgres, aproveite RETURNING para pegar ids sem nova consulta.

## Armadilhas comuns

- UPDATE ou DELETE sem WHERE altera/apaga todas as linhas da tabela.
- Omitir colunas no INSERT gera NULL ou erro nas obrigatórias.
- Ordem dos valores deve casar exatamente com a lista de colunas.
- DELETE em tabela pai falha se houver FK sem CASCADE.
- Rodar DML direto em produção sem transação nem backup prévio.

## Relacionadas

- [[Estudos-SQL]]
- [[Views-e-Transacoes]]
- [[Constraints-e-Chaves]]
