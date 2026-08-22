---
type: snippet
area: referencias
status: active
created: "2026-08-22"
updated: "2026-08-22"
---

# cURL-testar-APIs

#area/referencias #referencias/snippets

Comandos cURL para testar endpoints sem interface. Quando usar: reproduzir bug de API, validar contrato antes de automatizar, inspecionar headers e autenticação.

## GET básico com detalhes

```bash
curl -i https://api.exemplo.com/usuarios/42        # inclui status + headers na resposta
curl -v https://api.exemplo.com/ping               # modo verboso (handshake TLS, timing)
```

## POST com JSON

```bash
curl -X POST https://api.exemplo.com/usuarios \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"nome": "Teste QA", "email": "qa@teste.com"}'
```

## PUT/PATCH e DELETE

```bash
curl -X PATCH https://api.exemplo.com/usuarios/42 \
  -H "Content-Type: application/json" \
  -d '{"ativo": false}'

curl -X DELETE -H "Authorization: Bearer $TOKEN" https://api.exemplo.com/usuarios/42
```

## Truques úteis

```bash
curl -o resposta.json -w "%{http_code}" URL        # salvar corpo e imprimir só o status
curl -L URL                                        # seguir redirects
curl --data-urlencode "q=café com leite" URL       # encodar query string corretamente
```

> `-d` já implica POST; sem `Content-Type: application/json` muitos frameworks tratam o corpo como form-data.
