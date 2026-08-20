---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# DOM

#area/estudos #estudos/frontend #conceito

**Resumo:** Document Object Model: representação em árvore da página HTML que o JavaScript consulta e modifica para construir interfaces dinâmicas.

## Conceitos-chave
- **Árvore de nós:** o documento é uma hierarquia de nós (elementos, textos, atributos), navegada por `parentNode`, `children`, `nextElementSibling`.
- **Seleção:** `document.querySelector`, `querySelectorAll` e `getElementById` localizam elementos para manipular.
- **Manipulação:** `createElement`, `appendChild`, `textContent` e `setAttribute` alteram a árvore em tempo real.
- **Rendering:** mudanças no DOM disparam etapas do navegador — layout/reflow, paint e composição.
- **Eventos:** o DOM é a origem dos eventos (`click`, `input`) que o JS captura.
- **Virtual DOM:** React mantém uma cópia em memória da árvore e aplica só as diferenças ao DOM real, reduzindo operações caras.
- **Shadow DOM:** encapsulamento de subárvores usado por web components.

## Exemplos

```js
// selecionar e modificar elementos
const list = document.querySelector('#items');

const item = document.createElement('li');
item.textContent = 'Novo item';
list.appendChild(item);
```

```js
// melhor performance: atualizar fora do fluxo com DocumentFragment
const fragment = document.createDocumentFragment();
for (let i = 0; i < 100; i++) {
  const li = document.createElement('li');
  li.textContent = `Item ${i}`;
  fragment.appendChild(li);
}
list.appendChild(fragment);
```

## Boas práticas
- Guardar referências de elementos usados repetidamente (evita consultas ao DOM a cada interação).
- Agrupar alterações e usar `DocumentFragment` para reduzir reflows.
- Validar e escapar dados de usuário antes de inserir (nunca concatenar em `innerHTML`).
- Registrar listeners via `addEventListener` e removê-los quando o elemento sai da página.
- Delegar eventos para elementos dinâmicos em vez de anexar um listener por item.

## Armadilhas comuns
- Manipular o DOM em loops dentro de `innerHTML`/`appendChild`, causando reflow a cada iteração.
- Usar `innerHTML` com dados não sanitizados — vetor clássico de XSS.
- Confundir `NodeList` (resultado de `querySelectorAll`) com `Array` — `map` e `filter` não existem por padrão.
- Tentar acessar o DOM antes do `DOMContentLoaded`, quando a árvore ainda não existe.
- Esperar que `textContent` e `innerHTML` se comportem igual — o primeiro é seguro, o segundo interpreta marcação.

## Relacionadas
- [[JavaScript]]
- [[Eventos]]
- [[Frontend]]
- [[Performance-Frontend]]
- [[Componentes]]
- [[React]]