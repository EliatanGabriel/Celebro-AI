---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# REST

#area/estudos #estudos/backend #conceito

**Resumo:** Estilo arquitetural para APIs baseado em recursos nomeados e verbos HTTP, com comunicação stateless e respostas padronizadas por status codes.

## Conceitos-chave
- **Recursos:** entidades do domínio expostas como URIs (ex.: `/usuarios`, `/usuarios/42`).
- **Verbos HTTP:** GET (ler), POST (criar), PUT (substituir), PATCH (parcial), DELETE (remover) mapeiam operações sobre recursos.
- **Stateless:** cada requisição carrega tudo que precisa; o servidor não guarda contexto entre chamadas.
- **Status codes:** expressam o resultado (200/201, 204, 400/401/404, 500).
- **Representações:** JSON/XML; o cliente pode negociar via `Accept`/`Content-Type`.
- **Nível de maturidade:** Richardson Maturity Model vai de plain XML até HATEOAS (links navegáveis).
- **Diferenças-chave:** REST usa recursos e verbos; GraphQL usa uma query única; gRPC usa RPC binário.

## Exemplos
```http
GET /usuarios            -> lista usuários (200)
POST /usuarios           -> cria usuário (201)
GET /usuarios/42         -> detalha usuário (200)
PUT /usuarios/42         -> substitui usuário (200)
PATCH /usuarios/42       -> atualiza parcial (200)
DELETE /usuarios/42      -> remove (204)
```

```javascript
// Exemplo de API REST com Express
app.get("/usuarios/:id", async (req, res) => {
  const usuario = await db.buscar(req.params.id);
  if (!usuario) return res.status(404).json({ erro: "Não encontrado" });
  res.json(usuario);
});
```

## Boas práticas
- Usar substantivos no plural para recursos e ações como verbos HTTP ou sub-recursos.
- Manter URIs previsíveis e versionar (ex.: `/v1/`).
- Retornar status codes e formatos de erro consistentes.
- Aplicar paginação, filtros e ordenação via query params em listas.
- Documentar com OpenAPI e seguir convenções de nomes de campos.

## Armadilhas comuns
- Criar endpoints verbosos tipo `/getUser` ou `/deleteUser` em vez de usar verbos HTTP.
- Colocar ações (ex.: enviar email) como verbos na URL em vez de POST no recurso.
- Retornar 200 para tudo, sem diferenciar erro de cliente/servidor.
- Ignorar paginação e devolver listas gigantes.
- Acreditar que toda API HTTP é "REST": muitas são apenas APIs com verbos HTTP.

## Relacionadas
- [[APIs]]
- [[HTTP]]
- [[GraphQL]]
- [[gRPC]]
- [[Express]]