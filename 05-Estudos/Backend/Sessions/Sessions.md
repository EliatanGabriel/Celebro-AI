---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Sessions

#area/estudos #estudos/backend #conceito

**Resumo:** Mecanismo server-side que mantém o estado do usuário entre requisições HTTP, identificado por um session ID entregue ao cliente, normalmente via cookie.

## Conceitos-chave
- **Por quê:** HTTP é stateless; sessions permitem lembrar o login e preferências entre requisições.
- **Fluxo:** no login, o servidor cria uma sessão, guarda os dados e devolve um `session_id`; o cliente o envia em cada requisição.
- **Transporte do ID:** cookie `HttpOnly` é o padrão; também pode via URL/header (menos seguro).
- **Armazenamento:** em memória (só para dev), banco de dados, ou Redis para escalar entre instâncias.
- **Expiração:** TTL da sessão no servidor + expiração do cookie no cliente.
- **Diferenças-chave:** sessions são revogáveis instantaneamente e mantêm estado no servidor; JWTs são stateless e difíceis de revogar antes da expiração.

## Exemplos
```javascript
// Sessão com express-session
import session from "express-session";

app.use(session({
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  cookie: { httpOnly: true, secure: true, maxAge: 1000 * 60 * 60 },
  store: redisStore, // persistência compartilhada via Redis
}));

app.post("/login", (req, res) => {
  req.session.usuarioId = 42; // cria/atualiza a sessão
  res.send("Logado");
});

app.get("/perfil", (req, res) => {
  if (!req.session.usuarioId) return res.status(401).json({ erro: "Não autenticado" });
  res.json({ usuarioId: req.session.usuarioId });
});

app.post("/logout", (req, res) => req.session.destroy(() => res.send("Ok")));
```

## Boas práticas
- Usar cookie `HttpOnly` + `Secure` + `SameSite` para o session ID.
- Armazenar sessões em Redis/banco para escalar horizontalmente (não em memória).
- Definir TTL realista e encerrar sessão no logout e no reset de senha.
- Guardar na sessão apenas identificadores, não dados sensíveis em texto.
- Rotacionar o session ID após o login (session fixation).

## Armadilhas comuns
- Guardar sessão só em memória: instâncias atrás de load balancer perdem a sessão do usuário.
- Não expirar sessões, acumulando memória/estado no servidor.
- Confiar em dados editáveis do cliente sem validar contra o estado do servidor.
- Misturar conceitos: sessions (server-side) vs tokens (stateless) — são abordagens distintas.
- Ignorar session fixation e manter o mesmo ID antes/depois do login.

## Relacionadas
- [[Auth]]
- [[Backend]]
- [[HTTP]]
- [[Cookies]]
- [[Redis]]
- [[JWT]]