---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# MongoDB

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Banco NoSQL orientado a documentos que armazena dados em BSON, com esquema flexível e escala horizontal por sharding e replica sets.

## Conceitos-chave
- **Documento:** unidade de dados em BSON (JSON binário), com estrutura aninhada.
- **Coleção:** conjunto de documentos sem esquema obrigatório.
- **_id:** chave primária obrigatória e automaticamente indexada.
- **Aggregation pipeline:** processamento em estágios (`$match`, `$group`, `$sort`, `$lookup`).
- **Replica set:** grupo de instâncias com alta disponibilidade e failover automático.
- **Sharding:** distribuição horizontal dos dados por uma chave de shard.
- **Transactions:** suporte multi-documento com propriedades ACID a partir da versão 4.0.

## Exemplos

```js
db.usuarios.insertOne({
  nome: "Ana",
  email: "ana@ex.com",
  endereco: { cidade: "São Paulo", uf: "SP" },
  tags: ["vip", "dev"]
});

db.pedidos.aggregate([
  { $match: { status: "PAGO" } },
  { $group: { _id: "$usuario_id", total: { $sum: "$valor" } } },
  { $sort: { total: -1 } }
]);
```

## Boas práticas
- Modelar conforme os padrões de acesso, agrupando dados lidos juntos.
- Indexar campos usados em filtros, ordenações e agregações.
- Usar replica sets e sharding para disponibilidade e escala.
- Evitar documentos gigantes e arrays sem limite de crescimento.

## Armadilhas comuns
- Confundir esquema flexível com ausência de modelagem.
- Abusar de `$lookup`, que é caro comparado a JOINs de bancos relacionais.
- Fazer consultas sem índice, caindo em collection scan.
- Comparar diretamente com SQL e esperar joins nativos poderosos.

## Relacionadas
- [[NoSQL]]
- [[Bancos-de-Dados]]
- [[APIs]]
- [[Backend]]
- [[Sharding]]
- [[Replication]]