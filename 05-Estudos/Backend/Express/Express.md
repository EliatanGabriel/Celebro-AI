---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Express

#area/estudos #estudos/backend #conceito

**Resumo:** Framework web minimalista para Node.js, padrão de facto para APIs REST e aplicações HTTP, organizado em rotas e middleware.

## Conceitos-chave
- **O que é:** camada fina sobre o módulo `http` do Node que simplifica rotas, middleware e parsing de requisições.
- **Quando usar:** APIs REST, protótipos, microserviços e projetos que precisam de liberdade total de estrutura.
- **Estrutura básica:** instância do app + definição de rotas (GET/POST/PUT/DELETE) + lista de middlewares em pipeline.
- **Middleware:** funções executadas em sequência entre a requisição e a resposta; base para auth, logging, CORS e validação.
- **Diferenças-chave:** mais simples e flexível que NestJS (que traz estrutura, DI e TypeScript); menos opinativo que Django.
- **Ecossistema:** `express.json()` (body parsing), routers modulares, template engines e integração com WebSocket.

## Exemplos
```javascript
import express from "express";

const app = express();
app.use(express.json());

app.get("/", (req, res) => res.send("Olá!"));
app.get("/usuarios/:id", (req, res) => {
  res.json({ id: req.params.id });
});
app.post("/usuarios", (req, res) => {
  const { nome } = req.body;
  res.status(201).json({ nome });
});

app.listen(3000);
```

```javascript
// Middleware de autenticação
function auth(req, res, next) {
  const token = req.headers.authorization;
  if (!token) return res.status(401).json({ erro: "Sem token" });
  req.usuario = validarToken(token);
  next();
}

app.get("/perfil", auth, (req, res) => res.json(req.usuario));
```

## Boas práticas
- Separar rotas em routers e controladores, mantendo o app enxuto.
- Tratar erros com middleware centralizado de erro.
- Validar entradas com bibliotecas (ex.: zod, joi) antes de usar `req.body`.
- Usar `next()` corretamente e retornar em respostas para evitar respostas duplicadas.
- Configurar CORS, rate limiting e `helmet` em produção.

## Armadilhas comuns
- Chamadas assíncronas sem `try/catch` dentro de handlers (erros não capturados).
- Ordenar middlewares de forma incorreta (ex.: auth depois da rota que deveria proteger).
- Colocar toda a aplicação em um único arquivo sem modularização.
- Confundir `req.query` (parâmetros de URL) com `req.params` (segmentos de rota).
- Enviar duas respostas na mesma requisição (causa erro "headers already sent").

## Relacionadas
- [[Node-js]]
- [[REST]]
- [[APIs]]
- [[Backend]]
- [[Middleware]]
- [[NestJS]]