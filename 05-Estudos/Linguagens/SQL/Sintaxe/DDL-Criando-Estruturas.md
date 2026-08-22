---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# DDL - Criando Estruturas

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Comandos de definição de dados (DDL) que criam e alteram a estrutura de bancos e tabelas.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `CREATE DATABASE` | Cria um novo banco | `CREATE DATABASE loja;` |
| `CREATE TABLE` | Cria tabela com colunas/tipos | ver exemplo |
| `INT` / `BIGINT` | Inteiros comuns/grandes | `id INT` |
| `VARCHAR(n)` / `TEXT` | Texto limitado / longo | `nome VARCHAR(100)` |
| `DECIMAL(p,s)` | Valores exatos (dinheiro) | `DECIMAL(10,2)` |
| `DATE` / `TIMESTAMP` | Data / data com hora | `criado_em TIMESTAMP` |
| `BOOLEAN` | Verdadeiro/falso | `ativo BOOLEAN` |
| `SERIAL` / `IDENTITY` | Auto incremento | `id SERIAL` ou `BIGINT IDENTITY` |
| `ALTER TABLE ADD/DROP COLUMN` | Adiciona/remove coluna | ver exemplo |
| `DROP TABLE` vs `TRUNCATE` | Apaga estrutura vs esvazia linhas | ver boas práticas |

## Exemplos

```sql
CREATE DATABASE loja;

CREATE TABLE clientes (
    id        SERIAL PRIMARY KEY,      -- Postgres
    nome      VARCHAR(100) NOT NULL,
    email     VARCHAR(150) UNIQUE,
    saldo     DECIMAL(10, 2) DEFAULT 0,
    ativo     BOOLEAN DEFAULT TRUE,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```sql
-- MySQL usa AUTO_INCREMENT em vez de SERIAL
CREATE TABLE pedidos (
    id          BIGINT AUTO_INCREMENT PRIMARY KEY,
    cliente_id  INT NOT NULL,
    total       DECIMAL(10,2)
);

ALTER TABLE pedidos ADD COLUMN observacao TEXT;
ALTER TABLE pedidos DROP COLUMN observacao;

TRUNCATE TABLE pedidos;   -- esvazia rápido, sem WHERE
DROP TABLE pedidos;       -- apaga tabela inteira
```

## Boas práticas

- Sempre declare chaves primárias desde a criação da tabela.
- Use VARCHAR com tamanho realista; TEXT só para conteúdo longo.
- Prefira DECIMAL para dinheiro: FLOAT tem erro de arredondamento.
- Nomeie tabelas no singular ou plural, mas mantenha o padrão no projeto.
- Em produção, teste ALTER em staging: algumas operações travam a tabela.

## Armadilhas comuns

- TRUNCATE não pode ser revertido facilmente nem filtrado com WHERE.
- DROP TABLE destrói estrutura e dados: cuidado ao rodar em produção.
- VARCHAR sem limite definido varia entre bancos e dificulta migração.
- Esquecer NOT NULL em colunas obrigatórias gera liço de dados nulos.
- Diferenças de tipos entre bancos (SERIAL vs AUTO_INCREMENT vs IDENTITY).

## Relacionadas

- [[Estudos-SQL]]
- [[Constraints-e-Chaves]]
- [[Indexes-e-Performance]]
