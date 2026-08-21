---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Autenticacao-API

#area/trabalho #trabalho/api-rest #conceito

**Resumo:** Processo de validar a identidade de quem acessa uma API.

## Conceitos-chave
- Valida a identidade de quem consome a API.
- Mecanismos: API keys, tokens JWT, sessões/cookies, OAuth 2.0.
- JWT: token assinado com claims e expiração.
- Refresh tokens para renovar acesso sem nova autenticação.
- Autorização define o que o usuário pode fazer (escopos, RBAC).

## Exemplos
```
# Enviar token de acesso em requisições autenticadas
curl -H "Authorization: Bearer <token>" https://api.exemplo.com/perfil

# Fluxo OAuth 2.0 (Authorization Code)
1. GET /oauth/authorize?response_type=code&client_id=x
2. POST /oauth/token  -> access_token + refresh_token
3. Usar access_token nas requisições
```

## Boas práticas
- Usar HTTPS obrigatoriamente para trafegar tokens.
- Definir expiração curta para access tokens e revogação de refresh.
- Conceder escopos e permissões mínimas.
- Nunca logar tokens ou chaves em logs e repositórios.
- Retornar 401 sem credenciais/inválidas e 403 sem permissão.

## Armadilhas comuns
- Enviar token via query string (vaza em logs/referrers).
- Segredos hardcoded em código ou coleções.
- Expiração muito longa ou ausente.
- Não validar escopo na autorização.
- Armazenar tokens sem proteção no cliente.

## Relacionadas
- [[Endpoints]]
- [[Status-Codes]]
- [[Metodos-HTTP]]