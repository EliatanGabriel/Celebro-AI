---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# HTTP

#area/estudos #estudos/backend #conceito

**Resumo:** Protocolo de aplicação da web que define a troca de mensagens entre cliente e servidor, organizada em requisições e respostas com métodos, headers e status codes.

## Conceitos-chave
- **Requisição e resposta:** cliente envia request (método, URI, headers, corpo); servidor responde com status, headers e corpo.
- **Métodos:** GET (leitura), POST (criação), PUT/PATCH (atualização), DELETE (remoção), OPTIONS e HEAD.
- **Status codes:** 2xx (sucesso), 3xx (redirecionamento), 4xx (erro do cliente), 5xx (erro do servidor).
- **Headers:** metadados como `Content-Type`, `Authorization`, `Cache-Control`, `Cookie`, `Accept`.
- **Stateless:** cada requisição é independente; estado é mantido com cookies, tokens ou sessões.
- **Segurança:** HTTPS (TLS) criptografa o conteúdo; versões HTTP/1.1, HTTP/2 e HTTP/3 diferem em multiplexação e transporte.

## Exemplos
```http
GET /usuarios/42 HTTP/1.1
Host: api.exemplo.com
Authorization: Bearer eyJhbGciOi...
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json

{"id": 42, "nome": "Ana"}
```

```http
POST /usuarios HTTP/1.1
Content-Type: application/json

{"nome": "Ana", "email": "ana@exemplo.com"}

HTTP/1.1 201 Created
Location: /usuarios/43
```

## Boas práticas
- Usar os métodos e status codes com significado semântico correto.
- Configurar `Cache-Control` e `ETag` para respostas cacheáveis.
- Validar e sanitizar toda entrada vinda do cliente.
- Enviar e respeitar headers de segurança (`Content-Security-Policy`, `Strict-Transport-Security`).
- Usar HTTPS em qualquer ambiente de produção.

## Armadilhas comuns
- Retornar `200 OK` para erros de negócio em vez de status apropriado (ex.: 400/404/409).
- Enviar dados sensíveis no corpo de URL (GET) — vazam em logs e histórico.
- Confundir `PUT` (substituição completa) com `PATCH` (atualização parcial).
- Ignorar `Content-Type` correto, causando parsing incorreto no cliente.
- Não tratar `413 Payload Too Large` e limites de corpo ao receber uploads.

## Relacionadas
- [[REST]]
- [[APIs]]
- [[WebSocket]]
- [[Cookies]]
- [[Sessions]]
- [[HTTPS]]
- [[TLS]]