---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Tokens

#area/estudos #estudos/seguranca #conceito

**Resumo:** Estruturas de dados que representam autenticação ou autorização sem manter estado no servidor, como JWT e OAuth access tokens.

## Conceitos-chave
- **Stateless:** o token carrega as informações e o servidor valida a assinatura sem consultar sessão.
- **JWT:** composto de header, payload e assinatura (HS256/RS256); o payload não é cifrado, só assinado.
- **Ciclo de vida:** emissão, expiração (exp), emissor (iss), público (aud) e revogação.
- **Refresh vs. access token:** access de curta duração; refresh de longa duração renovado offline.
- **Armazenamento:** tokens devem ficar em memória/cookies seguros, não em localStorage vulnerável a XSS.
- **Segredos e assinatura:** a chave de assinatura é um segredo (ver [[Segredos]]); RS256 usa par de chaves.

## Exemplos
```javascript
// Decodificação (não valida) de um JWT
const jwt = require("jsonwebtoken");
const token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIiwicm9sIjoiYWRtaW4ifQ.assinatura";

// Payload visível em base64url (não é segredo)
// { "sub": "1", "rol": "admin" }

// Validação com assinatura no servidor
jwt.verify(token, process.env.JWT_SECRET);
```

## Boas práticas
- Usar algoritmos fortes (RS256/ES256) e nunca `alg: none` no servidor.
- Definir `exp`, `iss`, `aud` e validar todos na verificação.
- Emitir access tokens de curta duração e revogar refresh tokens quando necessário.
- Armazenar tokens fora do alcance do JavaScript (cookies `HttpOnly` + `Secure`) quando possível.
- Nunca colocar dados sensíveis no payload — ele é legível sem a chave.

## Armadilhas comuns
- Acreditar que JWT é criptografado — o payload é apenas codificado em base64.
- Aceitar tokens sem verificar expiração ou assinatura (ataques de downgrade `alg: none`/HS256).
- Guardar tokens em localStorage: XSS pode ler e exfiltrar.
- Fazer logout só no cliente, sem revogar/expirar o token no servidor.
- Colocar informações sensíveis no payload de tokens compartilhados.

## Relacionadas
- [[Autenticacao]]
- [[JWT]]
- [[Segredos]]
- [[CSRF]]