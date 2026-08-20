---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Redis-DB

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Uso do Redis como banco de dados além de cache: estrutura de dados in-memory com persistência, expiração (TTL), Pub/Sub e tipos ricos.

## Conceitos-chave
- **In-memory:** operações em RAM com latência de microssegundos.
- **Estruturas de dados:** strings, lists, sets, sorted sets, hashes e streams.
- **Persistência:** RDB (snapshots periódicos) e AOF (append-only file com cada escrita).
- **TTL:** chaves com tempo de expiração para cache e sessões.
- **Pub/Sub e Streams:** mensageria leve; Streams adicionam persistência e grupos de consumidores.
- **Casos de uso:** cache, filas, sessões, rate limiting, contadores, rankings.
- **Alta disponibilidade:** Sentinel para failover e Cluster para sharding.

## Exemplos

```bash
SET usuario:1 '{"nome":"Ana"}'
EXPIRE usuario:1 300

LPUSH fila:tarefas 'job-1'
RPOP fila:tarefas

SADD online:usuarios "u1" "u2"

INCR contador:visitas

PUBLISH canal:alertas "novo evento"
SUBSCRIBE canal:alertas
```

## Boas práticas
- Definir TTL para dados que não precisam persistir indefinidamente.
- Escolher persistência conforme o RPO: AOF é mais durável; RDB é mais rápido.
- Usar a estrutura correta (ex.: sorted set para rankings, hash para objetos).
- Tratar o Redis como cache/banco auxiliar, não como fonte única de dados críticos.

## Armadilhas comuns
- Assumir durabilidade total: sem persistência configurada, restart perde dados.
- Usar `KEYS *` em produção (bloqueia o servidor); preferir `SCAN`.
- Nomes de chaves sem padrão, dificultando manutenção e prevenção de colisões.
- Confundir Pub/Sub (sem durabilidade/ack) com filas de mensageria robustas.

## Relacionadas
- [[Redis]]
- [[NoSQL]]
- [[Caching]]
- [[Bancos-de-Dados]]