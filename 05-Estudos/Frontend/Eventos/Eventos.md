---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Eventos

#area/estudos #estudos/frontend #conceito

**Resumo:** Mecanismo pelo qual o navegador notifica o JavaScript sobre interações do usuário e mudanças de estado, permitindo que a aplicação responda.

## Conceitos-chave
- **Tipos de evento:** `click`, `keydown`, `input`, `submit`, `scroll`, `resize`, `load`, entre outros.
- **Event listeners:** `addEventListener` registra uma função executada quando o evento dispara no elemento.
- **Propagação:** o evento viaja do alvo até a raiz (bubbling) e pode ser capturado na fase de captura; `event.target` é o alvo real, `event.currentTarget` o elemento do listener.
- **Delegação:** um único listener no pai trata eventos de todos os filhos, útil para listas dinâmicas.
- **Controle:** `preventDefault()` cancela o comportamento padrão (ex.: envio de formulário); `stopPropagation()` impede que o evento continue subindo.
- **Performance:** `debounce` e `throttle` limitam a frequência de handlers em eventos de alta frequência (scroll, resize).

## Exemplos

```js
// listener simples
const btn = document.querySelector('#salvar');
btn.addEventListener('click', () => {
  console.log('Salvo!');
});
```

```js
// delegação de eventos: um listener para itens dinâmicos
const list = document.querySelector('#items');
list.addEventListener('click', (event) => {
  if (event.target.matches('li')) {
    console.log('Clicou em:', event.target.textContent);
  }
});
```

```js
// debounce simples para busca
let timer;
input.addEventListener('input', () => {
  clearTimeout(timer);
  timer = setTimeout(() => buscar(input.value), 300);
});
```

## Boas práticas
- Usar delegação para coleções que crescem (listas, tabelas) em vez de listener por item.
- Remover listeners no cleanup (ex.: retorno de `useEffect`) para evitar vazamentos de memória.
- Usar `{ passive: true }` em `scroll`/`touchmove` quando o handler não chama `preventDefault`.
- Em formulários, capturar `submit` e chamar `preventDefault()` em vez de usar `onclick` no botão.
- Tratar eventos específicos de teclado com `event.key` (ex.: `'Enter'`, `'Escape'`), não `keyCode` antigo.

## Armadilhas comuns
- Chamar `stopPropagation()` indiscriminadamente, quebrando handlers de outros componentes.
- Não remover listeners ao destruir elementos — o elemento fica retido em memória.
- Anexar listeners a elementos recém-criados sem delegação, perdendo o primeiro evento.
- Esquecer `preventDefault()` no `submit`, recarregando a página e perdendo estado.
- Registrar `scroll`/`resize` sem debounce, travando a interface.

## Relacionadas
- [[DOM]]
- [[JavaScript]]
- [[Frontend]]
- [[Componentes]]
- [[Hooks]]
- [[React]]