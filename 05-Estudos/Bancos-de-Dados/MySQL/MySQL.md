---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# MySQL

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Sistema gerenciador de banco de dados relacional open-source, um dos mais usados na web, historicamente combinado com PHP e Node.js em stacks como LAMP.

## Conceitos-chave
- **Relacional/SQL:** tabelas, chaves, constraints, JOINs e transações ACID com o storage engine InnoDB.
- **Storage engines:** InnoDB (padrão, transacional, com foreign keys) versus MyISAM (antigo, sem transações nem FK).
- **Índices:** B-tree para igualdade e range; HASH disponível em tabelas MEMORY.
- **Replicação:** master-slave assíncrona e Group Replication para disponibilidade e leitura.
- **Stacks populares:** LAMP (Linux, Apache, MySQL, PHP) e combinações com Node.
- **Variantes:** MariaDB (fork) e Percona Server.

## Exemplos

```sql
CREATE TABLE usuarios (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(120) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

SELECT u.nome, COUNT(p.id) AS total
FROM usuarios u
LEFT JOIN pedidos p ON p.usuario_id = u.id
GROUP BY u.id
HAVING total > 3;
```

## Boas práticas
- Usar InnoDB para dados transacionais com foreign keys.
- Definir tipos de coluna corretos e índices para as consultas reais.
- Diagnosticar queries lentas com `EXPLAIN`.
- Fazer backup com `mysqldump` e testar o restore.

## Armadilhas comuns
- Usar `SELECT *` em produção sem necessidade.
- Achar que MySQL e PostgreSQL são idênticos — sintaxe e recursos diferem.
- Usar MyISAM para dados críticos (sem transações nem FK).
- Usar charset `utf8` antigo (utf8mb3), que não suporta emojis; preferir `utf8mb4`.

## Relacionadas
- [[Bancos-de-Dados]]
- [[PHP]]
- [[Transactions]]
- [[Indexes]]
- [[Estudos-SQL]]