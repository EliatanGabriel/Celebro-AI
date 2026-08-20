---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Neo4j

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Banco de dados de grafos orientado a nós, relacionamentos e propriedades, otimizado para consultar dados altamente conectados.

## Conceitos-chave
- **Nós (nodes):** entidades com labels e propriedades (ex.: `:Usuario`, `:Produto`).
- **Relacionamentos (edges):** conectam nós com tipo, direção e propriedades (ex.: `:SEGUE`, `:COMPROU`).
- **Cypher:** linguagem declarativa de consulta com padrões (`MATCH`, `CREATE`, `WHERE`, `RETURN`).
- **Índices:** aceleram buscas por label/propriedade em lookups pontuais.
- **Modelagem graph-first:** a estrutura das relações é central para o modelo.
- **Casos de uso:** recomendação, redes sociais, detecção de fraude e grafos de conhecimento.

## Exemplos

```cypher
CREATE (a:Usuario {nome: "Ana"})-[:SEGUE]->(b:Usuario {nome: "Bia"});

-- Sugestão de quem seguir (amigos de amigos)
MATCH (u:Usuario {nome: "Ana"})-[:SEGUE]->(amigo)-[:SEGUE]->(sugerido)
WHERE NOT (u)-[:SEGUE]->(sugerido) AND u <> sugerido
RETURN DISTINCT sugerido.nome AS sugestao;
```

## Boas práticas
- Usar Neo4j quando o valor dos dados está nas relações, não em tabelas.
- Indexar os campos usados em lookups pontuais de `MATCH`.
- Modelar relacionamentos com tipos semânticos claros e direção explícita.
- Evitar forçar um modelo "tabelar" dentro do grafo.

## Armadilhas comuns
- Usar grafo para dados naturalmente tabulares, pagando custo sem benefício.
- Percursos sem índices que varrem o grafo inteiro.
- Pensar em termos de JOINs — Cypher é baseado em padrões de grafo.
- Ignorar direção e cardinalidade dos relacionamentos no modelo.

## Relacionadas
- [[Bancos-de-Dados]]
- [[NoSQL]]