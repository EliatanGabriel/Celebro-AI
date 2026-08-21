---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# SQL

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem declarativa padrão para criar, consultar e manipular dados em bancos de dados relacionais, com operações set-based e transações.

## Conceitos-chave
- Paradigma declarativo: você descreve o *que* quer (não *como* obter), e o otimizador do banco decide a estratégia.
- Sem tipagem tradicional de programação; os tipos vêm das colunas (INT, VARCHAR, DATE, etc.).
- Interpretada/executada pelo SGBD (PostgreSQL, MySQL, SQLite), que processa a consulta.
- Principais sublinguagens: DDL (CREATE/ALTER/DROP), DML (SELECT/INSERT/UPDATE/DELETE), DCL (GRANT/REVOKE).
- Operações set-based: JOIN, GROUP BY, ORDER BY, agregados (COUNT, SUM, AVG).
- Chaves primárias, estrangeiras, índices e constraints garantem integridade.
- Transações (ACID) e normalização são fundamentos para consistência dos dados.

## Exemplos
```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT CHECK (idade >= 0),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO usuarios (nome, idade) VALUES ('Ana', 30), ('Bruno', 16);

SELECT nome
FROM usuarios
WHERE idade >= 18
ORDER BY nome;

SELECT COUNT(*) AS total_maiores
FROM usuarios
WHERE idade >= 18;

UPDATE usuarios SET idade = idade + 1 WHERE nome = 'Bruno';
```

## Boas práticas
- Use `JOIN` explícito em vez de join implícito na cláusula WHERE.
- Crie índices para colunas filtradas e com JOIN frequente, mas evite excesso.
- Prefira `NOT NULL` e constraints sempre que fizer sentido no domínio.
- Consulte apenas as colunas necessárias (`SELECT *` apenas quando indispensável).
- Execute alterações de dados dentro de transações e revise com `EXPLAIN`.

## Armadilhas comuns
- Comparar com `= NULL` em vez de `IS NULL` — NULL não é igual a nada.
- `SELECT *` e falta de `LIMIT` em consultas pesadas, degradando a performance.
- Uso de `WHERE` com função em coluna indexada (`WHERE UPPER(nome) = ...`), anulando o índice.
- Confundir `HAVING` (filtra agregados) com `WHERE` (filtra linhas).
- Esquecer o `ON` no JOIN, gerando produto cartesiano e resultados explosivos.

## Relacionadas
- [[Bancos-de-Dados]]
- [[Transactions]]