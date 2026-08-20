---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Middleware

#area/estudos #estudos/backend #conceito

**Resumo:** Funções que interceptam requisições e respostas em um pipeline, permitindo processar, validar, modificar ou bloquear o tráfego antes de chegar à lógica da rota.

## Conceitos-chave
- **Pipeline:** cada requisição passa por uma cadeia de middlewares em ordem, até a rota final e a resposta.
- **Funções típicas:** autenticação, autorização, logging, CORS, compressão, rate limiting, parsing de body e tratamento de erros.
- **Controle de fluxo:** o middleware chama `next()` para seguir o pipeline ou encerra com resposta própria (ex.: 401).
- **Escopo:** pode ser global (`app.use`), por rota ou por grupo de rotas.
- **Estrutura comum:** `(req, res, next)` em Express/Node; decorators `@app.middleware` em FastAPI; `before`/`after` em outros frameworks.
- **Importância:** permite separar preocupações transversais (auth, logging) do código de negócio.

## Exemplos
```javascript
// Express: middleware de logging e de erro
app.use((req, res, next) => {
  console.log(`${req.method} ${req.path} - ${Date.now()}`);
  next();
});

app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({ erro: "Erro interno" });
});
```

```python
# FastAPI: middleware via decorator
from fastapi import Request

@app.middleware("http")
async def medir_tempo(request: Request, call_next):
    inicio = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Tempo-ms"] = str((time.perf_counter() - inicio) * 1000)
    return response
```

## Boas práticas
- Manter cada middleware com uma única responsabilidade e testável.
- Registrar middlewares na ordem correta (auth antes de rotas protegidas; parse antes de usar o body).
- Tratar erros em middleware centralizado para evitar respostas inconsistentes.
- Evitar lógica pesada síncrona em middlewares que bloqueiam o pipeline.
- Documentar a ordem do pipeline, que afeta o comportamento de todos os endpoints.

## Armadilhas comuns
- Chamar `next()` e também enviar resposta, gerando respostas duplicadas.
- Esquecer de chamar `next()`, deixando a requisição pendurada.
- Ordenar middlewares incorretamente (ex.: validação de auth depois da rota).
- Colocar lógica de negócio em middleware, tornando-a invisível para quem lê as rotas.
- Não capturar erros assíncronos em middlewares de Node (require wrappers ou try/catch).

## Relacionadas
- [[Express]]
- [[Node-js]]
- [[Backend]]
- [[Auth]]
- [[NestJS]]
- [[FastAPI]]