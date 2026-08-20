---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# OAuth

#area/estudos #estudos/backend #conceito

**Resumo:** Protocolo aberto de autorização delegada que permite a um aplicativo acessar recursos de um usuário em outro serviço sem receber sua senha, base dos "entrar com Google/GitHub".

## Conceitos-chave
- **Delegação:** o usuário autoriza o app a agir em seu nome com escopos limitados, sem compartilhar credenciais.
- **Papéis:** resource owner (usuário), client (app), authorization server (ex.: Google) e resource server (API protegida).
- **Authorization Code:** fluxo principal com redirect e troca de code por tokens, seguro para web/mobile.
- **Access token:** credencial que o client usa para chamar a API; tem escopo e expiração.
- **Scopes:** limitam o que o client pode fazer (ex.: `email`, `profile`, `repo`).
- **Refresh token:** permite obter novos access tokens sem reautorizar o usuário.
- **OpenID Connect (OIDC):** camada de identidade sobre OAuth 2.0 que fornece o `id_token` (JWT) com dados do usuário.

## Exemplos
```text
1. Client redireciona o usuário:
   GET /authorize?response_type=code
     &client_id=app&redirect_uri=https://app/callback
     &scope=email&state=xyz

2. Usuário autoriza; servidor redireciona com o code:
   GET https://app/callback?code=abc123&state=xyz

3. Client troca o code por tokens (backchannel):
   POST /token  (client_id, client_secret, code, grant_type=authorization_code)

4. Client usa o access token:
   GET /userinfo   Authorization: Bearer <access_token>
```

```javascript
// Verificando id_token OIDC
import { jwtVerify } from "jose";

const { payload } = await jwtVerify(idToken, chavePublica, {
  issuer: "https://accounts.google.com",
  audience: clientId,
});
console.log(payload.email);
```

## Boas práticas
- Usar o fluxo Authorization Code com PKCE para apps públicos (SPA/mobile).
- Restringir scopes ao mínimo necessário e revogá-los quando não usados.
- Validar `state` para prevenir CSRF no redirect.
- Nunca guardar `client_secret` em código do frontend.
- Preferir OIDC quando também precisa da identidade do usuário, não só de acesso.

## Armadilhas comuns
- Confundir OAuth (autorização) com autenticação; sozinho não valida identidade — daí o OIDC.
- Armazenar access tokens em localStorage (XSS) em vez de memória/cookies `HttpOnly`.
- Não validar `state`, permitindo ataques de login CSRF.
- Usar implicit flow legado em vez de authorization code + PKCE.
- Pedir mais escopos que o necessário, assustando o usuário e aumentando a superfície.

## Relacionadas
- [[Auth]]
- [[JWT]]
- [[Backend]]
- [[Sessions]]
- [[Tokens]]
- [[RBAC]]