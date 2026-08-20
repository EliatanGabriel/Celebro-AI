---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Indexes

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Estruturas de dados (tipicamente B-tree) que aceleram consultas e buscas no banco, ao custo de espaço em disco e lentidão nas operações de escrita.

## Conceitos-chave
- **B-tree:** estrutura balanceada e ordenada que permite busca, inserção e range queries em O(log n).
- **Índice único:** garante unicidade dos valores e é usado por constraints `UNIQUE` e `PRIMARY KEY`.
- **Índice composto:** cobre múltiplas colunas; a ordem importa (prefixedamento à esquerda).
- **Índice cobridor (covering index):** inclui as colunas retornadas, evitando acesso à tabela.
- **Índice parcial (PostgreSQL):** indexa apenas um subconjunto de linhas (`WHERE` no índice).
- **Índice de expressão:** indexa o resultado de uma função sobre a coluna.
- **Planejador de consultas:** o banco escolhe entre index scan e sequential scan com base em custo.

## Exemplos

```sql
-- Índice simples (PostgreSQL/MySQL)
CREATE INDEX idx_usuarios_email ON usuarios(email);

-- Índice composto — a ordem das colunas importa
CREATE INDEX idx_pedidos_user_status ON pedidos(usuario_id, status);

-- Índice único
CREATE UNIQUE INDEX idx_usuarios_cpf ON usuarios(cpf);

-- PostgreSQL: índice parcial
CREATE INDEX idx_pedidos_ativos ON pedidos(status) WHERE status = 'ATIVO';
```

## Boas práticas
- Indexar colunas usadas em `WHERE`, `JOIN`, `ORDER BY` e `GROUP BY`.
- Validar com `EXPLAIN ANALYZE` antes de criar índices.
- Remover índices sem uso — cada um pesa nas escritas.
- Em índices compostos, considerar a seletividade e os padrões reais de consulta.

## Armadilhas comuns
- Indexar colunas de baixa cardinalidade (ex.: booleano) que raramente ajudam.
- Acreditar que índice "corrige" qualquer query ruim (ex.: `LIKE '%x%'` não usa B-tree tradicional).
- Criar índices em excesso, desacelerando `INSERT`, `UPDATE` e `DELETE`.
- Aplicar função sobre a coluna indexada (`WHERE DATE(col) = ...`) e impedir o uso do índice.

## Relacionadas
- [[Bancos-de-Dados]]
- [[PostgreSQL]]
- [[Denormalizacao]]