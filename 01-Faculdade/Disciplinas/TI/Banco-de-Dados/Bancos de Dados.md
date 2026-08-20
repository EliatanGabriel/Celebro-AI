---
type: concept
area: faculdade
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Bancos de Dados

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Bancos de dados: o que são, modelos relacional e NoSQL, SQL básico, modelagem e boas práticas de consulta.

## 1. O que é um banco de dados

Um banco de dados (BD) é uma coleção organizada de dados, armazenada e acessada eletronicamente. Um **SGBD** (*Sistema Gerenciador de Banco de Dados*) é o software que gerencia o BD (MySQL, PostgreSQL, SQL Server, Oracle).

## 2. Banco relacional

Organiza os dados em **tabelas** com linhas (registros) e colunas (atributos).

**Exemplo — tabela Alunos:**

| id | nome | idade |
| --- | --- | --- |
| 1 | Ana | 20 |
| 2 | João | 22 |

**Conceitos:**

- **Chave primária (PK)** — identifica cada registro de forma única.
- **Chave estrangeira (FK)** — referencia uma chave primária de outra tabela.
- **Normalização** — elimina redundâncias e inconsistências.

## 3. Modelo entidade-relacionamento (MER)

Representa entidades (coisas) e seus relacionamentos.

```
ALUNO ──< CURSA >── DISCIPLINA
```

- **1:N** — um para muitos (um curso, muitos alunos).
- **N:N** — muitos para muitos (alunos e disciplinas, via tabela de ligação).

## 4. SQL — consultas básicas

```sql
-- Selecionar
SELECT nome, idade FROM Alunos WHERE idade >= 18;

-- Inserir
INSERT INTO Alunos (nome, idade) VALUES ('Maria', 21);

-- Atualizar
UPDATE Alunos SET idade = 23 WHERE nome = 'João';

-- Deletar
DELETE FROM Alunos WHERE id = 3;

-- Ordenar
SELECT * FROM Alunos ORDER BY nome ASC;

-- Agrupar
SELECT COUNT(*) FROM Alunos;
```

## 5. JOIN

Junta dados de duas ou mais tabelas.

```sql
SELECT a.nome, c.nome_curso
FROM Alunos a
JOIN Matriculas m ON a.id = m.aluno_id
JOIN Cursos c ON m.curso_id = c.id;
```

- **INNER JOIN** — só registros com correspondência.
- **LEFT JOIN** — todos da tabela esquerda + correspondências.
- **RIGHT JOIN** — todos da direita + correspondências.

## 6. Índices

Índices aceleram as consultas, como o índice de um livro.

- Consultas em colunas com índice ficam muito mais rápidas.
- Índices demais tornam as escritas (INSERT/UPDATE) mais lentas.

## 7. NoSQL

Para dados não estruturados ou alta escalabilidade:

- **Documento** — JSON (MongoDB, CouchDB).
- **Chave-valor** — Redis, DynamoDB.
- **Colunas** — Cassandra, HBase.
- **Grafos** — Neo4j.

| Relacional | NoSQL |
| --- | --- |
| Tabelas e SQL | Diversos modelos |
| Esquema rígido | Esquema flexível |
| Transações ACID | Escala horizontal |
| Pagamentos, sistemas financeiros | Big data, catálogos, sessões |

## 8. ACID

Garantias das transações relacionais:

- **Atomicidade** — tudo ou nada.
- **Consistência** — estado válido antes e depois.
- **Isolamento** — transações concorrentes não interferem.
- **Durabilidade** — dados sobrevivem a falhas.

## 9. Boas práticas

- Sempre filtrar com `WHERE` (evite `SELECT *`).
- Usar índices nas colunas de busca e JOIN.
- Normalizar até um nível adequado (ex.: 3FN).
- Fazer backups regulares.
- Sanitizar parâmetros para evitar SQL Injection (use prepared statements).

## Tópicos
- 

## Relacionadas

- [[TI]]
- [[Fundamentos de TI]]
- [[Faculdade]]