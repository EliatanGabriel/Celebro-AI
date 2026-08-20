---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# ORM

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Object-Relational Mapping: técnica que mapeia tabelas do banco para objetos/classes no código, abstraindo SQL e gerenciando relacionamentos, ciclo de vida e migrações.

## Conceitos-chave
- **Mapeamento:** entidades ↔ tabelas, propriedades ↔ colunas, tipos e constraints.
- **Relacionamentos:** 1:1, 1:N e N:N representados entre modelos, com carregamento lazy ou eager.
- **Query builder:** consultas via API da linguagem em vez de SQL manual.
- **Migrations versionadas:** o ORM gerencia evolução de schema.
- **Portabilidade:** o mesmo código pode trocar de banco com pouco esforço.
- **Problema N+1:** executar uma consulta por entidade dentro de um loop.

## Exemplos

```prisma
model Usuario {
  id      Int      @id @default(autoincrement())
  nome    String
  email   String   @unique
  pedidos Pedido[]
}

model Pedido {
  id        Int     @id @default(autoincrement())
  valor     Float
  usuario   Usuario @relation(fields: [usuarioId], references: [id])
  usuarioId Int
}
```

```ts
// Carregamento com include para evitar N+1
const pedidos = await prisma.usuario.findUnique({
  where: { id: 1 },
  include: { pedidos: true },
});
```

## Boas práticas
- Usar `include`/`select` explícitos para evitar o problema N+1.
- Versionar schema com migrations, e não sincronização automática.
- Conhecer o SQL gerado (logs de query) e otimizar quando preciso.
- Recorrer a SQL bruto em consultas e agregações complexas quando necessário.

## Armadilhas comuns
- Sofrer N+1 por carregamento lazy dentro de loops.
- Acreditar que ORM elimina a necessidade de entender SQL.
- Traduzir JOINs e agregações complexas de forma ineficiente.
- Confiar em sync automático de schema em produção.

## Relacionadas
- [[Prisma]]
- [[Django]]
- [[Backend]]
- [[Migrations]]
- [[Estudos-SQL]]