---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# FastAPI

#area/estudos #estudos/backend #conceito

**Resumo:** Framework Python moderno para APIs, construído sobre type hints, Pydantic e asyncio, com geração automática de OpenAPI e alta performance.

## Conceitos-chave
- **O que é:** framework que usa type hints do Python para validação, serialização e documentação automáticas.
- **Quando usar:** APIs REST/JSON, microserviços, integração com Machine Learning e cenários que exigem alto throughput.
- **Async:** suporte nativo a `async/await`, com performance comparável a Node.js/Go em I/O.
- **Pydantic:** models que validam dados automaticamente e geram esquemas JSON.
- **OpenAPI automático:** `/docs` (Swagger UI) e `/redoc` gerados a partir do código.
- **Estrutura básica:** `FastAPI()` + decorators de rota + funções com parâmetros tipados.
- **Diferenças-chave:** mais leve que Django e mais "moderno" que Flask (tipagem, async, docs automáticas).

## Exemplos
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    nome: str
    email: str
    ativo: bool = True

@app.get("/")
def raiz():
    return {"mensagem": "Olá"}

@app.get("/usuarios/{usuario_id}")
async def get_usuario(usuario_id: int):
    if usuario_id <= 0:
        raise HTTPException(status_code=404, detail="Não encontrado")
    return {"id": usuario_id}

@app.post("/usuarios", status_code=201)
def criar(usuario: Usuario):
    return usuario
```

```python
# Dependência de autenticação
from fastapi import Depends

def verificar_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401)
    return authorization

@app.get("/perfil", dependencies=[Depends(verificar_token)])
def perfil():
    return {"dados": "protegidos"}
```

## Boas práticas
- Definir models Pydantic para entradas e saídas, nunca usar dicts soltos.
- Usar `Depends` para reutilizar lógica de auth, banco e validação.
- Aproveitar `async` apenas para operações de I/O; código CPU-bound deve ir para workers.
- Tratar erros com `HTTPException` e códigos de status adequados.
- Usar a documentação automática como contrato vivo da API.

## Armadilhas comuns
- Declarar parâmetro sem tipo, perdendo validação e documentação automática.
- Bloquear o event loop com código síncrono pesado dentro de `async def`.
- Confundir `Body`/`Query`/`Path` ao extrair parâmetros de requisição.
- Comparar com Flask sem considerar que FastAPI exige familiarity com type hints.
- Não definir `response_model`, expondo campos indesejados na resposta.

## Relacionadas
- [[Python]]
- [[APIs]]
- [[REST]]
- [[Backend]]
- [[Flask]]
- [[Django]]
- [[Middleware]]