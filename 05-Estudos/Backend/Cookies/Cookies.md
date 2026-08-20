---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Cookies

#area/estudos #estudos/backend #conceito

**Resumo:** Pequenos dados armazenados no navegador e enviados automaticamente ao servidor a cada requisição, usados para manter estado, identificar sessões e rastrear preferências.

## Conceitos-chave
- **Papel:** HTTP é stateless; cookies permitem ao servidor reconhecer o cliente entre requisições.
- **Atributos de segurança:** `Secure` (só HTTPS), `HttpOnly` (inacessível ao JavaScript) e `SameSite` (proteção contra CSRF).
- **Escopo:** `Domain` e `Path` definem para quais domínios/caminhos o cookie é enviado.
- **Tipo:** cookies de sessão (somem ao fechar o navegador) e persistentes (com `Expires`/`Max-Age`).
- **Third-party cookies:** criados por outro domínio (ex.: rastreadores) e cada vez mais bloqueados pelos navegadores.
- **Relação com auth:** sessions e tokens frequentemente transitam em cookies (`Set-Cookie` no login).

## Exemplos
```http
HTTP/1.1 200 OK
Set-Cookie: session_id=abc123; HttpOnly; SameSite=Lax; Path=/; Max-Age=86400
Set-Cookie: preferencia_tema=escuro; Max-Age=2592000
```

```javascript
// Lendo e definindo cookie no servidor Express
import cookieParser from "cookie-parser";

app.use(cookieParser());

app.post("/login", (req, res) => {
  res.cookie("session_id", token, { httpOnly: true, sameSite: "lax", maxAge: 86400000 });
  res.send("Logado");
});

app.get("/perfil", (req, res) => {
  const session = req.cookies.session_id;
  res.json({ session });
});
```

## Boas práticas
- Sempre usar `HttpOnly` em cookies de sessão e `Secure` em produção.
- Definir `SameSite=Lax` ou `Strict` para mitigar CSRF.
- Não armazenar dados sensíveis no cookie; guardar apenas identificadores.
- Limitar o tamanho (~4KB) e o número de cookies por domínio.
- Usar assinatura/criptografia se o cookie precisar ser confiável.

## Armadilhas comuns
- Confiar no valor de um cookie editável sem assinatura ou validação.
- Esquecer `HttpOnly` e expor o cookie de sessão via XSS.
- Tentar armazenar tokens grandes (JWT) em cookies excedendo o limite do navegador.
- Misturar conceitos de cookies de sessão com cookies de rastreamento/persistência.
- Ignorar `SameSite`, deixando a aplicação vulnerável a [[CSRF]].

## Relacionadas
- [[Sessions]]
- [[Auth]]
- [[JWT]]
- [[HTTP]]
- [[CSRF]]