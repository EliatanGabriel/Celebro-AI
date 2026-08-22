---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Constraints e Chaves

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Restrições que garantem a integridade dos dados: chaves primárias e estrangeiras, unicidade, valores padrão e regras de verificação.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `PRIMARY KEY` | Identificador único da linha | `id SERIAL PRIMARY KEY` |
| `FOREIGN KEY ... REFERENCES` | Liga à chave de outra tabela | ver exemplo |
| `UNIQUE` | Valor sem repetição na coluna | `email VARCHAR UNIQUE` |
| `NOT NULL` | Impede valor ausente | `nome VARCHAR NOT NULL` |
| `DEFAULT valor` | Valor quando não informado | `DEFAULT 0` |
| `CHECK (cond)` | Regra que a linha deve satisfazer | `CHECK (preco >= 0)` |
| `ON DELETE CASCADE` | Apaga filhos ao apagar o pai | alternativas: SET NULL, RESTRICT |

## Exemplos

```sql
CREATE TABLE clientes (
    id    SERIAL PRIMARY KEY,          -- Postgres
    email VARCHAR(150) NOT NULL UNIQUE,
    nome  VARCHAR(100) NOT NULL,
    ativo BOOLEAN DEFAULT TRUE
);

CREATE TABLE pedidos (
    id          SERIAL PRIMARY KEY,
    cliente_id  INT NOT NULL REFERENCES clientes(id) ON DELETE CASCADE,
    total       DECIMAL(10,2) CHECK (total >= 0),
    status      VARCHAR(20) DEFAULT 'novo'
);
```

```sql
-- Auto incremento em outros bancos
-- MySQL:
CREATE TABLE t (id INT AUTO_INCREMENT PRIMARY KEY);
-- Padrão SQL / SQL Server / Postgres moderno:
CREATE TABLE t (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
);
-- Constraint nomeada com múltiplas colunas
ALTER TABLE pedidos
    ADD CONSTRAINT uq_pedido UNIQUE (cliente_id, criado_em);
```

## Boas práticas

- Toda tabela merece uma PRIMARY KEY simples e imutável.
- Modele o ON DELETE/ON UPDATE da FK conscientemente (CASCADE vs RESTRICT).
- Use CHECK para regras de negócio básicas que cabem no banco.
- Dê nomes às constraints para facilitar migrações e mensagens de erro.
- UNIQUE composto resolve casos como "um voto por usuário por enquete".

## Armadilhas comuns

- FK sem índice na coluna filtra/joina lentamente.
- CASCADE apaga dados em silêncio em cadeia: avalie o impacto.
- CHECK só valida linhas novas/mudadas; dados antigos podem violar.
- GENERATED ALWAYS rejeita INSERT com id explícito (use BY DEFAULT).
- Trocar PRIMARY KEY depois que o sistema está em produção dói muito.

## Relacionadas

- [[Estudos-SQL]]
- [[DDL-Criando-Estruturas]]
- [[Indexes-e-Performance]]
