---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# APIs

#area/estudos #estudos/backend #conceito

**Resumo:** Interface de programação de aplicações que define um contrato de comunicação entre sistemas, permitindo que eles troquem dados e funcionalidades de forma padronizada.

## Conceitos-chave
- **Contrato de comunicação:** define como o cliente deve fazer a requisição (formato, endpoints, verbos) e o que o servidor responde (formato e status).
- **Estilos:** REST (recursos + verbos HTTP), GraphQL (query única tipada), gRPC (RPC com Protocol Buffers) e SOAP (XML, legado).
- **Serialização:** JSON (leve e legível) e XML (verboso, usado em SOAP) transportam dados entre cliente e servidor.
- **Versionamento:** manter `/v1/`, `/v2/` permite evoluir a API sem quebrar consumidores existentes.
- **Documentação:** OpenAPI/Swagger, Postman e ferramentas de mocking padronizam contrato e testes.
- **Segurança:** toda API exposta precisa de autenticação, rate limiting, validação de entrada e HTTPS.

## Exemplos
```http
GET /v1/users/42 HTTP/1.1
Host: api.exemplo.com
Authorization: Bearer <token>

HTTP/1.1 200 OK
Content-Type: application/json

{ "id": 42, "nome": "Ana", "email": "ana@exemplo.com" }
```

```javascript
// Chamada de API no cliente
const resposta = await fetch("https://api.exemplo.com/v1/users/42", {
  headers: { Authorization: `Bearer ${token}` }
});
const usuario = await resposta.json();
```

## Boas práticas
- Versionar a API desde o início e documentar mudanças (changelog).
- Usar nomes de recursos no plural, consistentes e no singular apenas para identificadores.
- Responder sempre com status codes apropriados e corpo de erro padronizado.
- Aplicar rate limiting e validação de entrada para proteção contra abuso.
- Publicar documentação OpenAPI e manter exemplos de uso atualizados.

## Armadilhas comuns
- Confundir API com REST: uma API pode ser REST, GraphQL, gRPC etc.
- Esquecer de versionar e quebrar clientes ao alterar o contrato.
- Expor dados sensíveis no payload de resposta sem necessidade.
- Retornar `200 OK` para erros de negócio em vez de status adequado (4xx/5xx).
- Não definir limites de paginação, gerando respostas gigantes e lentas.

## Relacionadas
- [[REST]]
- [[HTTP]]
- [[GraphQL]]
- [[gRPC]]
- [[Middleware]]
- [[WebSocket]]