---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Elasticsearch

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Motor de busca e análise distribuído baseado em Apache Lucene, usado para full-text search, observabilidade de logs e dados de séries temporais.

## Conceitos-chave
- **Índice:** coleção lógica de documentos JSON que compartilham configuração e mapeamento.
- **Documento:** unidade de dados, um JSON com campos pesquisáveis e agregáveis.
- **Inverted index:** estrutura que mapeia termos para documentos, permitindo busca full-text muito rápida.
- **Shards e réplicas:** o índice é dividido em shards primários e replicados entre nós, dando escala horizontal e disponibilidade.
- **Query DSL:** API REST/JSON para buscar, filtrar (bool/filter) e agregar (aggregations).
- **Aggregations:** cálculo de métricas, buckets e estatísticas sobre os documentos.
- **Stack ELK/Elastic:** Kibana para visualização e Logstash/Beats para ingestão de logs.

## Exemplos

```json
// Criar um documento
PUT /produtos/_doc/1
{
  "nome": "Notebook Gamer",
  "preco": 4999.90,
  "tags": ["eletronico", "laptop"]
}

// Busca full-text
GET /produtos/_search
{
  "query": {
    "match": { "nome": "notebook" }
  }
}
```

## Boas práticas
- Definir mapeamentos (mappings) e analisadores antes de indexar dados.
- Evitar indexar campos que nunca serão buscados ou filtrados.
- Planejar o número de shards primários antecipadamente (não muda depois).
- Usar aliases de índice para reindexação sem downtime.

## Armadilhas comuns
- Tratar o Elasticsearch como fonte de verdade transacional — não é relacional/ACID.
- Deep pagination com `from/size` muito grande; usar `search_after`.
- Ignorar os disk watermarks e deixar o cluster ficar amarelo/vermelho.
- Descobrir mapeamento errado tarde demais e precisar reindexar.

## Relacionadas
- [[Bancos-de-Dados]]
- [[NoSQL]]
- [[Sharding]]