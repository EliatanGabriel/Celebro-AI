---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Denormalizacao

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Introduzir redundância controlada no modelo de dados para melhorar a performance de leitura, aceitando custo maior de escrita e responsabilidade de manter a consistência.

## Conceitos-chave
- **Redundância controlada:** duplicar dados de forma deliberada para evitar JOINs e agregações caras em leituras.
- **Read-heavy:** em cenários com muito mais leitura do que escrita, menos JOINs significam latência menor e consultas mais simples.
- **Colunas derivadas:** armazenar valores calculados (ex.: `total_pedidos`) em vez de calcular com `COUNT` a cada consulta.
- **Tabelas de resumo:** manter agregados pré-computados (por dia, por categoria, etc.).
- **Contraponto à normalização:** é o oposto da `Normalizacao`, que busca eliminar redundância.
- **Comportamento cache-like:** aproxima o banco de um cache materializado, trocando integridade por velocidade.

## Exemplos

```sql
-- Normalizado: consulta com JOIN e agregação
SELECT u.nome, COUNT(p.id) AS total
FROM usuarios u
LEFT JOIN pedidos p ON p.usuario_id = u.id
GROUP BY u.id;

-- Denormalizado: campo total_pedidos mantido na tabela usuarios
SELECT nome, total_pedidos FROM usuarios;
```

## Boas práticas
- Denormalizar somente depois de esgotar indexação e ajustes de queries.
- Atualizar os campos redundantes nos pontos de escrita (aplicação, triggers, eventos).
- Documentar as regras de consistência da redundância para a equipe.
- Combinar com índices e views materializadas quando possível.

## Armadilhas comuns
- Confundir denormalização com falta de modelagem — é uma decisão consciente e documentada.
- Esquecer de atualizar campos redundantes, gerando dados inconsistentes.
- Denormalizar cedo demais em cenários write-heavy.
- Multiplicar manutenção sem medir o ganho real de performance.

## Relacionadas
- [[Indexes]]
- [[Bancos-de-Dados]]
- [[Caching]]
- [[Estudos-Normalizacao]]