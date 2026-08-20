---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Caching

#area/estudos #estudos/backend #conceito

**Resumo:** Técnica de armazenar resultados de computações ou consultas em um armazenamento de acesso rápido, reduzindo latência, carga no servidor e custos de infraestrutura.

## Conceitos-chave
- **Cache em memória:** dados guardados em RAM (ex.: Redis, Memcached) com latência de micro/milissegundos.
- **TTL (Time-To-Live):** prazo de validade de cada entrada; expira automaticamente quando vence.
- **Cache invalidação:** estratégias para remover/atualizar dados obsoletos (write-through, write-back, cache-aside).
- **Níveis:** navegador, CDN, banco de dados, aplicação — cada camada tem seu escopo e custo.
- **Cache-aside:** aplicação consulta o cache; em miss, busca na origem e popula o cache.
- **Miss vs hit:** hit é quando o dado está no cache; miss força ida à origem e acarreta custo maior.

## Exemplos
```python
# Cache-aside com Redis em Python
import redis, json

r = redis.Redis(host="localhost", decode_responses=True)

def get_usuario(usuario_id):
    chave = f"usuario:{usuario_id}"
    dados = r.get(chave)
    if dados is not None:
        return json.loads(dados)  # cache hit

    usuario = buscar_no_banco(usuario_id)  # cache miss
    r.set(chave, json.dumps(usuario), ex=3600)  # TTL de 1h
    return usuario
```

```javascript
// Header de cache no servidor HTTP
res.setHeader("Cache-Control", "public, max-age=60");
```

## Boas práticas
- Definir TTLs realistas e usar `Cache-Control`/`ETag` em respostas HTTP.
- Priorizar cache para dados caros de gerar e pouco mutáveis.
- Escolher a estratégia de invalidação conforme o caso de uso (leitura pesada, escrita frequente).
- Monitorar hit ratio (taxa de acertos) para avaliar a eficácia.
- Cachear com prefixos/chaves versionadas para facilitar invalidação em deploy.

## Armadilhas comuns
- Cachear dados sensíveis ou específicos de usuário sem isolamento por chave.
- Confiar em TTL para correção: TTL protege consistência, mas não garante atualização imediata.
- Cache stampede: picos simultâneos de miss derrubam a origem (usar lock ou cache de renovação).
- Esquecer de invalidar o cache ao atualizar o dado de origem.
- Tratar cache como fonte de verdade: ele é sempre um espelho temporário.

## Relacionadas
- [[Redis]]
- [[Performance-Frontend]]
- [[Load-Balancer]]
- [[CDN]]
- [[Proxy]]