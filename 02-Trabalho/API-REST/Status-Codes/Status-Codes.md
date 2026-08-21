---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Status-Codes

#area/trabalho #trabalho/api-rest #conceito

**Resumo:** Códigos padronizados que indicam o resultado de uma requisição.

## Conceitos-chave
- Padrão HTTP que indica o resultado de uma requisição.
- 2xx sucesso: 200 OK, 201 Created, 204 No Content.
- 3xx redirecionamento: 301, 302, 304 Not Modified.
- 4xx erro do cliente: 400, 401, 403, 404, 409, 422, 429.
- 5xx erro do servidor: 500, 502 Bad Gateway, 503 Unavailable.

## Exemplos
```
# Verificação de códigos comuns
curl -i https://api.exemplo.com/usuarios
# 200 OK (listagem)

curl -i -X POST https://api.exemplo.com/usuarios -d '{}'
# 201 Created ou 400 Bad Request (validação)

curl -i https://api.exemplo.com/usuarios/9999
# 404 Not Found
```

## Boas práticas
- Usar o código semanticamente correto para cada caso.
- 400 para requisição malformada; 401 para não autenticado; 403 para sem permissão.
- 422 para falha de validação de regra de negócio.
- Padronizar o formato das respostas de erro da API.
- Documentar os códigos possíveis por endpoint.

## Armadilhas comuns
- Retornar 200 para erros, escondendo falhas do cliente.
- Usar 500 para erros de entrada do cliente.
- 403 quando deveria ser 401 (e vice-versa).
- Códigos inconsistentes entre endpoints semelhantes.
- Ignorar 429 e não informar limites de requisição.

## Relacionadas
- [[Metodos-HTTP]]
- [[Endpoints]]
- [[Rate-Limiting]]