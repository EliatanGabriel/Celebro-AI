---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Svelte

#area/estudos #estudos/frontend #conceito

**Resumo:** Compilador de componentes que transforma código Svelte em JavaScript puro otimizado, sem virtual DOM, com reatividade embutida e bundles pequenos.

## Conceitos-chave
- **Modelo mental:** Svelte é um compilador, não um runtime — o componente é escrito em `.svelte` (script + style + markup) e vira código imperativo que manipula o DOM diretamente.
- **Sem virtual DOM:** as atualizações são compiladas para manipulações diretas de DOM, eliminando a camada de diff.
- **Reatividade:** mudanças em variáveis declaradas com `let` re-renderizam automaticamente; declarações reativas `$:` recalculam dependências.
- **Stores:** objetos reativos compartilháveis para estado entre componentes (`writable`, `derived`), com prefixo `$` no template.
- **Ciclo de vida:** `onMount`, `beforeUpdate`, `onDestroy` gerenciam efeitos; no Svelte 5, `$effect` e runes substituem parte disso.
- **Particularidades:** transições/animações embutidas, acessibilidade checada em tempo de compilação, SvelteKit como framework oficial (SSR/rotas).
- **Quando usar:** aplicações e componentes de médio porte que priorizam performance, simplicidade e bundle reduzido.

## Exemplos

```svelte
<script>
  let count = 0;
</script>

<button type="button" on:click={() => (count += 1)}>
  Cliques: {count}
</button>

<style>
  button {
    font-size: 1.2rem;
  }
</style>
```

```svelte
<!-- store reativo para estado compartilhado -->
<script>
  import { writable } from 'svelte/store';
  export const contador = writable(0);
</script>

<!-- em outro componente -->
<script>
  import { contador } from './store.js';
</script>
<p>Valor: {$contador}</p>
```

## Boas práticas
- Preferir Svelte para apps pequenos/médios e componentes de alto desempenho; para apps grandes, avalie o SvelteKit.
- Usar stores para estado compartilhado e `$:` para valores derivados.
- Aproveitar transições e animações nativas em vez de libs de animação.
- Seguir os avisos de acessibilidade do compilador, que apontam problemas reais.
- Em Svelte 5, adotar runes (`$state`, `$props`, `$effect`) no código novo.

## Armadilhas comuns
- Achar que a reatividade acompanha mutações — em Svelte clássico, é preciso atribuição (`arr.push()` não dispara; `arr = [...arr, x]` dispara).
- Declarar `$:` com dependências implícitas, recalculando quando não deveria.
- Confundir Svelte (biblioteca/compilador) com SvelteKit (framework com SSR e rotas).
- Usar APIs de browser fora de `onMount`, quebrando em ambiente SSR.
- Misturar lifecycle antigo (`onMount`) com runes do Svelte 5 sem entender o novo modelo de reatividade.

## Relacionadas
- [[React]]
- [[Vue]]
- [[Frontend]]
- [[Componentes]]
- [[Props]]
- [[Vite]]