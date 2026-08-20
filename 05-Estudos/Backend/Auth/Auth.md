---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Auth

#area/estudos #estudos/backend #conceito

**Resumo:** Autenticação verifica a identidade de quem acessa um sistema; autorização determina o que essa identidade pode fazer. São conceitos distintos e complementares.

## Conceitos-chave
- **Autenticação vs autorização:** autenticação responde "quem é você?"; autorização responde "o que você pode fazer?".
- **Métodos:** login/senha, tokens (JWT), sessions server-side, chaves de API, certificados e MFA.
- **Sessions:** estado mantido no servidor, referenciado por um ID (geralmente via cookie).
- **Tokens:** credenciais autossuficientes (JWT) verificadas por assinatura, sem estado no servidor.
- **MFA:** segunda camada de verificação (TOTP, SMS, biometria) para reduzir impacto de senha vazada.
- **Protocolos delegados:** OAuth 2.0 (autorização) e OpenID Connect (identidade), usados em "entrar com Google/GitHub".

## Exemplos
```javascript
// Verificação simples de credenciais em Node.js
import bcrypt from "bcrypt";

const senhaHash = await bcrypt.hash("senha-forte", 10);

async function login(usuario, senhaDigitada) {
  const ok = await bcrypt.compare(senhaDigitada, usuario.senhaHash);
  if (!ok) throw new Error("Credenciais inválidas");
  return gerarToken(usuario.id);
}
```

```python
# Decorator de autenticação em FastAPI
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer

bearer = HTTPBearer()

def usuario_atual(token = Security(bearer)):
    payload = verificar_token(token.credentials)
    if not payload:
        raise HTTPException(status_code=401)
    return payload["sub"]
```

## Boas práticas
- Nunca armazenar senha em texto puro; usar hash com salt (bcrypt, argon2).
- Aplicar MFA em contas administrativas e operações sensíveis.
- Limitar tentativas de login e implementar bloqueio temporário.
- Expirar tokens/sessões e permitir revogação.
- Registrar eventos de autenticação (login, falha, logout) para auditoria.

## Armadilhas comuns
- Confundir autenticação com autorização e liberar ações sem checar permissões.
- Guardar segredos no código ou no frontend.
- Ignorar CSRF ao usar cookies de sessão (ver [[CSRF]]).
- Aceitar token de longa duração sem rotação ou revogação.
- Logar senhas ou tokens em arquivos de log.

## Relacionadas
- [[JWT]]
- [[OAuth]]
- [[Sessions]]
- [[Backend]]
- [[Cookies]]
- [[MFA]]
- [[Tokens]]