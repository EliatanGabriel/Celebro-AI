---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Views e Transações

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Views encapsulam consultas como tabelas virtuais; transações garantem que operações aconteçam por completo ou de jeito nenhum.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `CREATE VIEW v AS ...` | Consulta salva com nome | ver exemplo |
| view materializada | Armazena o resultado fisicamente | `CREATE MATERIALIZED VIEW` |
| `BEGIN TRANSACTION` | Inicia a transação | também `START TRANSACTION` |
| `COMMIT` | Confirma as mudanças | torna-as permanentes |
| `ROLLBACK` | Desfaz tudo desde o BEGIN | em erro ou teste |
| `SAVEPOINT nome` | Ponto intermediário de retorno | `ROLLBACK TO nome` |
| ACID | Atomicidade, Consistência, Isolamento, Durabilidade | garantias das transações |

## Exemplos

```sql
-- View: relatório reutilizável
CREATE VIEW resumo_clientes AS
SELECT c.id, c.nome, COUNT(p.id) AS pedidos,
       COALESCE(SUM(p.total), 0) AS total_gasto
FROM clientes c
LEFT JOIN pedidos p ON p.cliente_id = c.id
GROUP BY c.id, c.nome;

SELECT * FROM resumo_clientes WHERE total_gasto > 1000;
```

```sql
-- Transação: transferência precisa ser tudo ou nada
BEGIN;

UPDATE contas SET saldo = saldo - 200 WHERE id = 1;
UPDATE contas SET saldo = saldo + 200 WHERE id = 2;

-- se algo der errado no meio:
ROLLBACK;
-- se estiver tudo certo:
COMMIT;

-- Savepoints para desfazer só parte
SAVEPOINT antes_do_bonus;
UPDATE contas SET saldo = saldo + 50 WHERE id = 3;
ROLLBACK TO antes_do_bonus;  -- descarta só o bônus
COMMIT;
```

## Boas práticas

- Use views para padronizar consultas complexas compartilhadas.
- Prefira transações explícitas em qualquer DML múltiplo ou crítico.
- Mantenha transações curtas para não segurar locks demais.
- Atualize views materializadas (REFRESH) em janelas planejadas.
- Em código de aplicação, sempre trate erros com rollback no catch.

## Armadilhas comuns

- View não melhora performance sozinha: roda a consulta por baixo.
- Esquecer o COMMIT deixa a conexão travando dados alheios.
- ROLLBACK TO savepoint não encerra a transação: ainda precisa COMMIT.
- Views materializadas ficam desatualizadas até novo REFRESH.
- Transação longa + muitos usuários gera deadlocks.

## Relacionadas

- [[Estudos-SQL]]
- [[INSERT-UPDATE-DELETE]]
- [[DDL-Criando-Estruturas]]
