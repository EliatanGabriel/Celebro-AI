---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# NoSQL

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Família de bancos não relacionais que priorizam escala horizontal, esquema flexível e performance, sacrificando características como JOINs e ACID forte em favor do caso de uso específico.

## Conceitos-chave
- **Tipos principais:** chave-valor (Redis), documentos (MongoDB), grafos (Neo4j) e colunares (Cassandra).
- **Esquema flexível:** sem schema fixo; o modelo é desenhado pelos padrões de acesso.
- **Escala horizontal:** sharding e distribuição natural entre servidores.
- **Consistência eventual:** em sistemas distribuídos, réplicas podem divergir temporariamente.
- **Teorema CAP:** trade-off entre consistência, disponibilidade e tolerância a partição.
- **Quando usar:** leituras massivas, tempo real, alto volume; quando evitar: transações e relacionamentos complexos.

## Exemplos

```js
// Documento (MongoDB)
db.produtos.insertOne({ sku: "P1", nome: "Cadeira", preco: 350 });

// Chave-valor (Redis)
SET produto:P1 '{"nome":"Cadeira","preco":350}'

// Grafo (Neo4j)
CREATE (:Produto {sku: "P1", nome: "Cadeira"})
```

## Boas práticas
- Escolher o modelo de banco pelo padrão de acesso, não por tendência.
- Definir chaves e partições evitando hot spots.
- Planejar índices e consultas desde a modelagem.
- Documentar os trade-offs de consistência para a equipe.

## Armadilhas comuns
- Tratar NoSQL como "sem modelagem" ou "sempre mais rápido".
- Aplicar NoSQL onde JOINs e transações são essenciais.
- Ignorar o teorema CAP e assumir consistência forte em sistemas eventuais.
- Comparar bancos pela sintaxe e esquecer os trade-offs reais.

## Relacionadas
- [[MongoDB]]
- [[Redis]]
- [[Neo4j]]
- [[Bancos-de-Dados]]
- [[Elasticsearch]]
- [[Sharding]]