---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Transactions

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Grupo de operações de banco que executam de forma atômica, consistente, isolada e durável (ACID), com `COMMIT` para efetivar e `ROLLBACK` para desfazer.

## Conceitos-chave
- **ACID:** Atomicidade (tudo ou nada), Consistência (invariantes mantidas), Isolamento (transações concorrentes não se interferem) e Durabilidade (mudanças persistem após commit).
- **COMMIT/ROLLBACK:** commit efetiva as alterações; rollback reverte todas as operações da transação.
- **Níveis de isolamento:** READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ e SERIALIZABLE.
- **Problemas de concorrência:** dirty read, non-repeatable read e phantom read.
- **MVCC:** versões de linha para leituras consistentes sem bloqueio de escritas.
- **Deadlock:** transações concorrentes esperando recursos umas das outras; o banco detecta e aborta uma delas.

## Exemplos

```sql
BEGIN;
UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;
-- ROLLBACK; em caso de erro em alguma operação
```

```sql
-- Definindo o nível de isolamento (PostgreSQL)
BEGIN ISOLATION LEVEL SERIALIZABLE;
```

## Boas práticas
- Manter transações curtas, sem trabalho pesado dentro delas.
- Acessar recursos em ordem consistente para reduzir deadlocks.
- Escolher o isolamento conforme a necessidade (READ COMMITTED é o padrão no PostgreSQL).
- Tratar conflitos de serialização com retry na aplicação.

## Armadilhas comuns
- Esquecer `COMMIT`/`ROLLBACK` e segurar locks por muito tempo.
- Usar autocommit e achar que operações multi-etapa são atômicas.
- Não conhecer o isolamento padrão do banco (MySQL REPEATABLE READ vs PostgreSQL READ COMMITTED).
- Executar parte da lógica fora da transação e perder atomicidade.

## Relacionadas
- [[Bancos-de-Dados]]
- [[PostgreSQL]]
- [[SQLite]]
- [[MySQL]]