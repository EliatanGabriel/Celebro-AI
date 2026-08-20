---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Prisma

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** ORM moderno para TypeScript/Node.js focado em type-safety, migrações versionadas e uma API declarativa de consulta (Prisma Client).

## Conceitos-chave
- **Prisma Schema:** arquivo DSL (`schema.prisma`) que define datasource, generator e modelos com relações.
- **Prisma Client:** cliente gerado a partir do schema com tipos inferidos — erros de tipagem são capturados em compilação.
- **Prisma Migrate:** migrations versionadas aplicadas com `migrate dev` (local) e `migrate deploy` (produção).
- **Prisma Studio:** interface web para visualizar e editar dados.
- **Query API:** `findUnique`, `findMany`, `create`, `update`, `delete` com `where`, `include`, `select` e `orderBy`.
- **Bancos suportados:** PostgreSQL, MySQL, SQLite, SQL Server e MongoDB.

## Exemplos

```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model Post {
  id      Int    @id @default(autoincrement())
  titulo  String
  autor   User   @relation(fields: [autorId], references: [id])
  autorId Int
}

model User {
  id    Int    @id @default(autoincrement())
  nome  String
  posts Post[]
}
```

```ts
const posts = await prisma.post.findMany({
  where: { autorId: 1 },
  orderBy: { id: "desc" },
  include: { autor: true },
});
```

## Boas práticas
- Sempre usar o cliente tipado; evitar `any` e `$queryRaw` desnecessários.
- Versionar migrations e rodar `prisma migrate deploy` em produção.
- Usar transações para operações multi-etapas.
- Regenerar o client após cada mudança no schema.

## Armadilhas comuns
- Rodar `prisma db push` em produção em vez de migrations versionadas.
- Causar N+1 ao carregar relações em loops sem `include`.
- Expor credenciais no `.env`.
- Esquecer de regenerar o client após alterar o schema — erros de tipo aparecem.

## Relacionadas
- [[ORM]]
- [[Node-js]]
- [[TypeScript]]
- [[Migrations]]