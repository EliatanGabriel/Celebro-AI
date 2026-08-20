---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Hooks

#area/estudos #estudos/frontend #conceito

**Resumo:** Funções do React (`useState`, `useEffect`, `useContext`) que habilitam estado, efeitos e contexto em componentes funcionais, substituindo as classes.

## Conceitos-chave
- **useState:** declara estado local com valor e função de atualização; retorna `[valor, setValor]`.
- **useEffect:** executa efeitos colaterais (busca de dados, listeners, timers) após a renderização, com array de dependências.
- **useContext:** acessa valores de contexto sem prop drilling.
- **useRef:** guarda referências estáveis (DOM ou valores) que não disparam re-render.
- **useMemo/useCallback:** memorizam cálculos e funções para evitar trabalho e re-render desnecessários.
- **Custom hooks:** funções que encapsulam lógica reutilizável com estado/efeitos, seguindo a convenção `use*`.
- **Regras dos Hooks:** chamar apenas no nível superior e apenas dentro de componentes React ou custom hooks.

## Exemplos

```tsx
import { useEffect, useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Contagem: ${count}`;
  }, [count]);

  return (
    <button type="button" onClick={() => setCount((c) => c + 1)}>
      Cliques: {count}
    </button>
  );
}
```

```tsx
// custom hook reutilizável
import { useEffect, useState } from 'react';

export function useWindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);

  useEffect(() => {
    const onResize = () => setWidth(window.innerWidth);
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []);

  return width;
}
```

## Boas práticas
- Chamar hooks sempre no topo do componente, nunca em condicionais ou loops.
- Declarar as dependências corretas no `useEffect` (todas as variáveis usadas).
- Usar `setState` funcional (`setCount((c) => c + 1)`) quando o novo valor depende do anterior.
- Retornar cleanup nos efeitos que registram listeners, timers ou subscriptions.
- Extrair lógica repetida para custom hooks e separar efeitos por responsabilidade.

## Armadilhas comuns
- Violar as regras de hooks (chamar dentro de `if`/loops) — React quebra silenciosamente a ordem.
- Omitir dependências no `useEffect`, usando valores desatualizados (stale closures).
- Criar loops infinitos com `setState` dentro de `useEffect` sem dependência adequada.
- Abusar de `useMemo`/`useCallback` para "otimizar" sem medir — mais overhead que ganho.
- Guardar estado derivado duplicado que deveria ser calculado durante a renderização.

## Relacionadas
- [[React]]
- [[Componentes]]
- [[Props]]
- [[Frontend]]
- [[Eventos]]
- [[Redux]]