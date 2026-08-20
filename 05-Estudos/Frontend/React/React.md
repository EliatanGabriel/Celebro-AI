---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# React

#area/estudos #estudos/frontend #conceito

**Resumo:** Biblioteca JavaScript para interfaces de usuário baseada em componentes declarativos, estado local e virtual DOM, com um dos maiores ecossistemas do frontend.

## Conceitos-chave
- **Modelo mental:** a UI é uma função do estado — `f(estado) -> UI`. O dev declara o que renderizar; o React cuida de aplicar mudanças ao DOM de forma eficiente.
- **Componentes:** funções (ou classes) que retornam JSX; combinados por composição, recebem props e mantêm estado.
- **Virtual DOM / reconciliação:** React mantém uma árvore em memória, compara com a anterior (diff) e aplica só as diferenças no DOM real.
- **Estado declarativo:** `useState` re-renderiza o componente quando o estado muda; o fluxo de dados é unidirecional (props descem, callbacks sobem).
- **Hooks:** `useState`, `useEffect`, `useContext`, `useMemo` e custom hooks habilitam estado e efeitos sem classes.
- **JSX:** sintaxe de marcação dentro de JavaScript, compilada para chamadas de `createElement`.
- **Ecossistema:** roteamento (React Router), estado (Redux/Zustand), SSR (Next.js), UI (Tailwind, MUI) e build (Vite).
- **Quando usar:** SPAs interativas de qualquer porte; é uma biblioteca, não framework — decisões de estrutura ficam com o time.

## Exemplos

```tsx
import { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Você clicou {count} vezes</p>
      <button type="button" onClick={() => setCount((c) => c + 1)}>
        Incrementar
      </button>
    </div>
  );
}
```

## Boas práticas
- Manter componentes puros: dados de entrada via props, saída via JSX, sem efeitos escondidos.
- Usar Hooks corretamente (regras de hooks) e extrair lógica repetida para custom hooks.
- Fornecer `key` estável e única em listas (nunca o índice quando a ordem muda).
- Separar estado que pertence a vários componentes (elevá-lo ou usar contexto/store).
- Otimizar re-renders com `memo`/`useCallback` apenas quando medido e necessário.

## Armadilhas comuns
- Mutar estado diretamente (`count++`) em vez de `setState` — o React não detecta a mudança.
- Usar o índice como `key` em listas ordenáveis/filtradas, causando bugs de reconciliação.
- Achar que React é framework e aplicar tudo ao mesmo tempo — é uma biblioteca, o resto é escolha.
- Colocar efeitos colaterais na renderização em vez de `useEffect`.
- Duplicar estado em múltiplos componentes quando ele deveria estar elevado ou centralizado.

## Relacionadas
- [[JavaScript]]
- [[Hooks]]
- [[Componentes]]
- [[Frontend]]
- [[Redux]]
- [[Next-js]]
- [[Props]]
- [[TypeScript-Frontend]]
- [[Vite]]