---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# JWT

#area/estudos #estudos/backend #conceito

**Resumo:** JSON Web Token: token compacto e autossuficiente, assinado digitalmente, usado para autenticação stateless entre cliente e servidor.

## Conceitos-chave
- **Estrutura:** três partes codificadas em Base64URL separadas por `.`: header, payload e assinatura.
- **Assinatura:** garante integridade; pode ser HMAC (segredo compartilhado) ou RSA/ECDSA (par de chaves).
- **Stateless:** o servidor não precisa guardar o token; verifica a assinatura e confia no payload.
- **Payload (claims):** dados como `sub` (usuário), `exp` (expiração), `iat` (emissão), `iss` e `aud`.
- **Uso típico:** enviado no header `Authorization: Bearer <token>`; também comum em cookies `HttpOnly`.
- **Diferenças-chave:** sessions guardam estado no servidor (revogação imediata); JWTs são revogáveis apenas antes da expiração, a menos que haja blocklist.

## Exemplos
```javascript
// Gerando e verificando JWT em Node.js
import jwt from "jsonwebtoken";

const segredo = process.env.JWT_SECRET;

function gerarToken(usuarioId) {
  return jwt.sign({ sub: usuarioId }, segredo, { expiresIn: "1h" });
}

function verificarToken(token) {
  try {
    return jwt.verify(token, segredo);
  } catch (e) {
    return null; // expirado ou inválido
  }
}
```

```python
# Verificando payload (claims típicos)
# header.payload.signature
import jwt
from datetime import datetime, timezone

payload = jwt.decode(token, segredo, algorithms=["HS256"])
assert payload["exp"] > datetime.now(timezone.utc).timestamp()
```

## Boas práticas
- Definir `exp` sempre e manter TTLs curtos com refresh tokens.
- Usar segredo forte, único e fora do código (variável de ambiente).
- Não incluir dados sensíveis no payload (o conteúdo é apenas codificado, não criptografado).
- Validar `iss`/`aud` em aplicações com múltiplos emissores.
- Considerar blocklist/allowlist ou sessions para casos que exigem revogação imediata.

## Armadilhas comuns
- Achar que JWT é criptografado: a assinatura só garante integridade, não confidencialidade.
- Guardar o segredo no código-fonte ou no frontend.
- Aceitar `alg: none` ou não fixar o algoritmo (`algorithms` explícito).
- Colocar claims sensíveis (CPF, senha) no payload.
- Usar JWT de longa duração sem rotação, aumentando a janela de risco após vazamento.

## Relacionadas
- [[Auth]]
- [[OAuth]]
- [[Backend]]
- [[Sessions]]
- [[Cookies]]
- [[Criptografia]]