---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Migrations

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Controle de versão do esquema do banco de dados: cada alteração estrutural vira uma migration versionada, aplicada de forma incremental, reproduzível e auditável.

## Conceitos-chave
- **Up/Down:** métodos ou arquivos para aplicar e reverter uma mudança de esquema.
- **Histórico de migrations:** tabela de controle registra quais migrations já foram aplicadas em cada banco.
- **Imutabilidade:** migrations já aplicadas não devem ser editadas; novas mudanças exigem nova migration.
- **Ferramentas:** Prisma Migrate, Alembic (Python), Knex (Node), Flyway/Liquibase (Java).
- **Deploy seguro:** migrations são aplicadas antes da nova versão da aplicação para evitar incompatibilidade.
- **Baseline:** criação de uma migration inicial a partir de um esquema existente sem histórico.
- **DDL transacional:** alguns bancos (PostgreSQL) permitem DDL dentro de transação; MySQL muitas vezes não.

## Exemplos

```sql
-- 002_add_email_usuarios.up.sql
ALTER TABLE usuarios ADD COLUMN email VARCHAR(255) UNIQUE;

-- 002_add_email_usuarios.down.sql
ALTER TABLE usuarios DROP COLUMN email;
```

```bash
# Prisma
npx prisma migrate dev --name add_email_usuarios
npx prisma migrate deploy   # produção
```

## Boas práticas
- Versionar migrations junto com o código no repositório.
- Nunca editar uma migration já aplicada em produção; criar outra.
- Testar o `down` antes de rodar em produção.
- Rodar migrations de forma idempotente e segura no pipeline de deploy.

## Armadilhas comuns
- Publicar migration e código na mesma release de forma que quebre o deploy (rollout/backout).
- Editar migrations antigas em vez de criar novas.
- DDL que trava a tabela em produção (ex.: `ADD COLUMN` com `DEFAULT` em versões antigas do MySQL).
- Aplicar migrations só localmente e esquecer os demais ambientes.

## Relacionadas
- [[ORM]]
- [[Bancos-de-Dados]]
- [[Prisma]]