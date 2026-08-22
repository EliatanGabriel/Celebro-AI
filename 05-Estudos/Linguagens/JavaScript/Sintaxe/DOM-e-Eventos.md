---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# DOM e Eventos em JavaScript

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** O DOM permite ler e manipular a página com seletores, criação/remoção de elementos e escuta de eventos via `addEventListener`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `querySelector(sel)` | Retorna o primeiro elemento que casa o seletor | `document.querySelector("#app");` |
| `querySelectorAll(sel)` | Retorna NodeList com todos os matches | `document.querySelectorAll(".item");` |
| `createElement(tag)` | Cria um novo elemento | `document.createElement("li");` |
| `appendChild(el)` / `el.remove()` | Anexa filho / remove o elemento | `lista.appendChild(li);` |
| `textContent` | Define/lê apenas texto (seguro) | `titulo.textContent = "Olá";` |
| `innerHTML` | Define HTML interno (cuidado com XSS) | `card.innerHTML = "<b>x</b>";` |
| `classList.add/remove/toggle` | Manipula classes CSS do elemento | `modal.classList.toggle("aberto");` |
| `addEventListener("click", fn)` | Registra função para um evento | `btn.addEventListener("click", salvar);` |
| `event.target` | Elemento que disparou o evento | `e.target.dataset.id;` |
| `e.preventDefault()` | Cancela comportamento padrão (ex.: submit) | `form.addEventListener("submit", e => ...)` |

## Exemplos

```js
// Criar, preencher e anexar elementos
const lista = document.querySelector("#tarefas");
const item = document.createElement("li");
item.textContent = "Estudar DOM";        // seguro contra injeção
item.classList.add("pendente");
lista.appendChild(item);
```

```js
// Evento de clique com delegação e formulário com preventDefault
const form = document.querySelector("#novo-form");

form.addEventListener("submit", evento => {
  evento.preventDefault();               // evita recarregar a página
  const input = form.querySelector("input");
  if (!input.value.trim()) return;
  console.log("salvando:", input.value.trim());
});

document.querySelector("#tarefas").addEventListener("click", e => {
  if (e.target.matches("li")) {
    e.target.classList.toggle("concluida");   // marca/desmarca
  }
});
```

## Boas práticas

- Prefira `textContent` a `innerHTML` quando não houver HTML real.
- Use delegação de eventos no elemento pai para listas dinâmicas.
- Remova listeners (`removeEventListener`) quando não forem mais úteis.
- Consulte elementos uma vez e guarde em variáveis/constantes.
- Use `classList` em vez de mexer direto em `className`.
- Rode o script com `defer` ou ao final do `body` para garantir o DOM pronto.

## Armadilhas comuns

- Script no `<head>` sem `defer` roda antes do DOM existir.
- `innerHTML` com dados do usuário abre brecha de XSS.
- `querySelectorAll` retorna estático: itens criados depois não aparecem nele.
- Esquecer `preventDefault` no submit recarrega a página.
- `addEventListener` duplicado registra a mesma função duas vezes.

## Relacionadas

- [[Funcoes]]
- [[Async-Promises-Fetch]]
- [[JavaScript]]
