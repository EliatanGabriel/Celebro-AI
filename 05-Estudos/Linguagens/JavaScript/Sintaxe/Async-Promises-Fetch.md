---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Async, Promises e Fetch em JavaScript

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** JavaScript lida com operações assíncronas via callbacks, Promises (`then/catch/finally`) e a sintaxe moderna `async/await`, além de `fetch` para requisições HTTP.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `new Promise((res, rej) => {})` | Cria uma Promise pendente que resolve ou rejeita | `new Promise(r => setTimeout(r, 1000))` |
| `.then(fn)` / `.catch(fn)` | Trata sucesso / erro da Promise | `api.get().then(d).catch(e)` |
| `.finally(fn)` | Roda independente do resultado | `.finally(() => carregando = false)` |
| `Promise.all([...])` | Espera todas; rejeita na primeira falha | `await Promise.all([a(), b()])` |
| `async function` | Função que sempre retorna uma Promise | `async function buscar() {}` |
| `await` | Pausa até a Promise resolver (só em async) | `const dados = await resposta.json();` |
| `fetch(url)` | Requisição HTTP (GET por padrão) | `fetch("/api/users")` |
| `response.ok` / `response.status` | Indica se o status é 2xx / código HTTP | `if (!response.ok) throw ...` |
| `setTimeout` / `setInterval` | Executa após delay / repetidamente | `setTimeout(fn, 2000); clearInterval(id);` |

## Exemplos

```js
// async/await com fetch GET e tratamento de erro
async function buscarUsuario(id) {
  try {
    const resposta = await fetch(`https://api.exemplo.com/users/${id}`);
    if (!resposta.ok) throw new Error(`Erro ${resposta.status}`);
    const usuario = await resposta.json();
    return usuario;
  } catch (erro) {
    console.error("Falha ao buscar:", erro.message);
    return null;
  } finally {
    ocultarSpinner();
  }
}
```

```js
// POST com JSON e requisições paralelas
async function criarPost(post) {
  const resp = await fetch("/api/posts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(post)
  });
  return resp.json();
}

Promise.all([buscarUsuario(1), buscarUsuario(2)])
  .then(([u1, u2]) => console.log(u1, u2));
```

## Boas práticas

- Prefira `async/await`: fica linear e legível como código síncrono.
- Sempre verifique `response.ok`; o `fetch` não rejeita em 404/500.
- Use `try/catch/finally` para tratar erros e estados de carregamento.
- Paralelize chamadas independentes com `Promise.all`.
- Guarde o id do `setInterval` para poder limpar com `clearInterval`.

## Armadilhas comuns

- Callback hell: aninhar callbacks cria o famoso código em pirâmide.
- Esquecer o `await` retorna uma Promise, não o valor.
- Usar `await` fora de função `async` (ou topo de script sem suporte) dá erro.
- `response.json()` também é assíncrono: precisa de outro `await`.
- `setTimeout(fn, 0)` não roda imediatamente: entra na fila de eventos.

## Relacionadas

- [[Funcoes]]
- [[DOM-e-Eventos]]
- [[JavaScript]]
