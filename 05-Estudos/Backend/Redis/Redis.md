---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Redis

#area/estudos #estudos/backend #conceito

**Resumo:** Banco de dados em memória, open source, do tipo chave-valor, usado como cache, broker de filas, pub/sub e store de sessões por sua latência extremamente baixa.

## Conceitos-chave
- **In-memory:** dados em RAM, leituras/escritas em micro/milissegundos; por isso não é substituto de banco persistente.
- **Estruturas:** strings, hashes, lists, sets, sorted sets, bitmaps e streams — além de chave-valor simples.
- **Cache:** uso clássico com TTL (`EXPIRE`/`SET ... EX`), aliviando o banco.
- **Persistência:** RDB (snapshots) e AOF (append-only log); escolha conforme o trade-off de durabilidade.
- **Pub/Sub e streams:** mensageria leve e filas (ver [[Queue]]) para comunicação entre serviços.
- **Sessões:** armazenamento de sessão compartilhado e escalável entre instâncias.
- **Diferenças-chave:** comparado a um banco SQL/NoSQL, é ultra rápido porém volátil; compara a memcached, tem mais estruturas e persistência.

## Exemplos
```bash
# CLI do Redis
SET usuario:42 '{"nome":"Ana"}' EX 3600
GET usuario:42
INCR contador:acessos
LPUSH fila:tarefas job-1
BRPOP fila:tarefas 0
PUBLISH canal:noticias "nova mensagem"
```

```javascript
// Node.js com node-redis
import { createClient } from "redis";

const redis = createClient({ url: "redis://localhost:6379" });
await redis.connect();

await redis.set("usuario:42", JSON.stringify({ nome: "Ana" }), { EX: 3600 });
const dados = await redis.get("usuario:42");
```

## Boas práticas
- Definir TTLs para chaves de cache e monitorar a taxa de acertos.
- Usar estruturas adequadas (hashes para objetos, sorted sets para rankings/filas).
- Configurar `maxmemory` e política de evicção (ex.: `allkeys-lru`).
- Considerar persistência apenas quando a perda de dados não for aceitável.
- Usar Redis em camadas claras: cache, sessão, fila, pub/sub — não misturar responsabilidades na mesma chave.

## Armadilhas comuns
- Usar Redis como banco de dados principal sem estratégia de persistência/backup.
- Chaves gigantes ou sem padrão de nomenclatura, dificultando manutenção.
- Ignorar a política de evicção e estourar memória.
- Fazer N comandos em rede sem pipeline (latência acumulada).
- Assumir que dados estão sempre presentes: tratar miss com fallback ao banco.

## Relacionadas
- [[Caching]]
- [[Queue]]
- [[Bancos-de-Dados]]
- [[NoSQL]]
- [[Sessions]]