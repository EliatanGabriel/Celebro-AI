---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# GraphQL

#area/estudos #estudos/backend #conceito

**Resumo:** Linguagem de consulta para APIs que permite ao cliente pedir exatamente os dados que precisa em uma única requisição, com um schema fortemente tipado.

## Conceitos-chave
- **O que é:** query language + runtime; o cliente descreve a forma do dado desejado e o servidor devolve apenas isso.
- **Quando usar:** frontends com dados de múltiplas fontes, aplicações mobile (menos payload) e equipes que querem evolução sem versões.
- **Query única:** elimina N requisições REST, reduzindo over-fetching e under-fetching.
- **Schema tipado:** tipos, campos e relações definidos explicitamente; serve como contrato e documentação.
- **Resolvers:** funções que resolvem cada campo; podem consultar banco, outra API etc.
- **Introspection:** permite descobrir o schema em tempo de execução (base de ferramentas como GraphiQL).
- **Diferenças-chave:** REST usa verbos+recursos; GraphQL usa um único endpoint POST com queries/mutations e assinaturas (subscriptions).

## Exemplos
```graphql
# Schema
type Usuario {
  id: ID!
  nome: String!
  posts: [Post!]!
}

type Query {
  usuario(id: ID!): Usuario
}
```

```graphql
# Query do cliente
query {
  usuario(id: 42) {
    nome
    posts {
      titulo
    }
  }
}
```

```javascript
// Resolver em Node (Apollo Server)
const resolvers = {
  Query: {
    usuario: (_, { id }, ctx) => ctx.db.usuarios.find(id)
  }
};
```

## Boas práticas
- Modelar o schema pensando no domínio, não nas telas do frontend.
- Limitar profundidade e quantidade de campos para evitar queries abusivas (DoS).
- Usar `DataLoader` para evitar N+1 nos resolvers.
- Expor paginação consistente (connection pattern) em listas.
- Versionar por evolução de campos/depreciação (`@deprecated`) em vez de versões de endpoint.

## Armadilhas comuns
- Não mitigar queries profundas/amplas, abrindo porta para DoS.
- Resolver sem batching: N queries ao banco em vez de uma (N+1).
- Confundir mutações com queries e abusar de GET para alterações.
- Tratar cache como no REST: caching em GraphQL é mais complexo (persisted queries, apollo cache).
- Sobrecarregar resolvers com lógica de negócio.

## Relacionadas
- [[APIs]]
- [[REST]]
- [[Backend]]
- [[HTTP]]
- [[gRPC]]