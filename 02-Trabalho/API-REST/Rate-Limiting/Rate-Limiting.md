---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Rate-Limiting

#area/trabalho #trabalho/api-rest #conceito

**Resumo:** Controle do número de requisições permitidas por janela de tempo.

## Conceitos-chave
- Limita requisições por janela de tempo por chave/IP/usuário.
- Estratégias: fixed window, sliding window, token bucket.
- Headers: X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, Retry-After.
- Status 429 Too Many Requests quando o limite é excedido.
- Protege a API contra abuso e sobrecarga.

## Exemplos
```
curl -i https://api.exemplo.com/busca?q=qa

# Resposta com headers de limite
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1724169600

# Limite excedido
HTTP/1.1 429 Too Many Requests
Retry-After: 30
```

## Boas práticas
- Informar os limites em headers e na documentação.
- Retornar 429 com Retry-After para orientar o cliente.
- Aplicar limites por chave/cliente, não só por IP.
- Escalar a infraestrutura para não derrubar clientes legítimos.
- Implementar backoff/retry no cliente conforme os headers.

## Armadilhas comuns
- Limites apertados demais derrubando clientes legítimos.
- Não informar o cliente sobre os limites.
- Limites globais que penalizam todos os usuários.
- Cliente sem tratamento de 429, gerando erros em cascata.
- Documentação sem as cotas por plano.

## Relacionadas
- [[Status-Codes]]
- [[Endpoints]]
- [[Paginacao]]