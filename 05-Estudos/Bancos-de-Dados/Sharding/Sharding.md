---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Sharding

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Divisão dos dados em partições (shards) distribuídas entre múltiplos servidores para escalar horizontalmente, a custo de maior complexidade operacional.

## Conceitos-chave
- **Chave de shard (shard key):** campo que determina em qual servidor cada dado reside.
- **Escala horizontal:** adicionar servidores aumenta capacidade de armazenamento e processamento.
- **Re-sharding:** redistribuição dos dados quando os shards crescem ou ficam desbalanceados.
- **Hot spot:** concentração de acessos em um único shard por chave mal escolhida.
- **Relação com replicação:** estratégias são complementares — cada shard pode ter suas réplicas.
- **Transações e JOINs cross-shard:** suportados com custo e complexidade altos.

## Exemplos

```js
// MongoDB: habilitar sharding e definir chave
sh.enableSharding("loja");
sh.shardCollection("loja.pedidos", { usuario_id: 1 });
```

```sql
-- PostgreSQL: particionamento declarativo (partições no mesmo servidor)
CREATE TABLE pedidos (
  id BIGINT, criado_em DATE, ...
) PARTITION BY RANGE (criado_em);

CREATE TABLE pedidos_2026 PARTITION OF pedidos
  FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');
```

## Boas práticas
- Escolher shard key com alta cardinalidade e distribuição uniforme.
- Planejar crescimento e rebalanceamento desde o início.
- Combinar com replicação para alta disponibilidade.
- Manter consultas dentro de um único shard sempre que possível.

## Armadilhas comuns
- Shard key de baixa cardinalidade que gera hot spots.
- Transações e JOINs cross-shard caros e limitados.
- Sharding sem rebalanceamento planejado, criando desbalanceamento.
- Confundir sharding (múltiplos servidores) com particionamento de tabela (mesmo servidor).

## Relacionadas
- [[Replication]]
- [[Bancos-de-Dados]]
- [[NoSQL]]
- [[MongoDB]]