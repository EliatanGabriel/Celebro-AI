---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Redux

#area/estudos #estudos/frontend #conceito

**Resumo:** Biblioteca de gerenciamento de estado global com fluxo previsível e unidirecional, baseada em ações, reducers puros e um store único imutável.

## Conceitos-chave
- **Store único:** todo o estado da aplicação vive em um único objeto imutável, acessível de qualquer componente.
- **Ações:** objetos simples `{ type, payload }` que descrevem intenções (ex.: `'INCREMENTAR'`).
- **Reducers:** funções puras `(estado, ação) -> novo estado` que calculam o próximo estado sem mutar o anterior.
- **Dispatch:** componentes disparam ações via `store.dispatch(action)`; nunca alteram o estado diretamente.
- **Selectors:** funções que extraem partes derivadas do estado, podendo ser memoizadas (Reselect).
- **Middlewares:** camada entre dispatch e reducer para efeitos colaterais (Redux Thunk, Redux Saga, logging).
- **DevTools:** inspeção de ações, state e time-travel debugging.
- **Redux Toolkit:** a forma moderna e recomendada — `createSlice`, `configureStore`, reducers com Immer.
- **Quando usar:** estado global real compartilhado por muitas partes da app (auth, carrinho, cache), especialmente em apps grandes.

## Exemplos

```ts
import { configureStore, createSlice } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      state.value += 1; // Immer permite "mutações" seguras
    },
    add: (state, action) => {
      state.value += action.payload;
    },
  },
});

export const { increment, add } = counterSlice.actions;

export const store = configureStore({
  reducer: { counter: counterSlice.reducer },
});
```

```tsx
// consumindo no React
import { useDispatch, useSelector } from 'react-redux';
import { increment } from './store';

export function Counter() {
  const value = useSelector((state) => state.counter.value);
  const dispatch = useDispatch();

  return (
    <button type="button" onClick={() => dispatch(increment())}>
      {value}
    </button>
  );
}
```

## Boas práticas
- Sempre usar Redux Toolkit em vez de Redux puro — menos boilerplate e Immer embutido.
- Manter reducers puros e sem efeitos colaterais (fetch, timers vão em thunks/middlewares).
- Normalizar o estado (entidades por id) em vez de aninhar listas.
- Usar selectors memoizados para derivar dados e evitar re-renders.
- Mover para o Redux apenas estado realmente global; estado local fica em componentes.

## Armadilhas comuns
- Colocar tudo no Redux, inclusive estado efêmero de um input — incha e complica o store.
- Mutar o estado dentro do reducer em Redux clássico (sem Immer), quebrando a imutabilidade e o DevTools.
- Executar side effects (fetch, timers) dentro de reducers.
- Escrever boilerplate manual (constants, actions, reducers) em vez de usar Toolkit.
- Adotar Redux onde `useContext`/estado local resolveriam, adicionando complexidade sem necessidade.

## Relacionadas
- [[React]]
- [[JavaScript]]
- [[Componentes]]
- [[Hooks]]
- [[TypeScript-Frontend]]