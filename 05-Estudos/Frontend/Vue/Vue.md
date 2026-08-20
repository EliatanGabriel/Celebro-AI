---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Vue

#area/estudos #estudos/frontend #conceito

**Resumo:** Framework progressivo e leve para interfaces, com reatividade reativa, single-file components e adoção incremental — do script tag à aplicação completa.

## Conceitos-chave
- **Modelo mental:** o componente Vue combina template declarativo, `script` (dados/lógica) e `style` em um Single-File Component (`.vue`); o estado reativo atualiza o template automaticamente.
- **Reatividade:** em Vue 3, `ref`/`reactive` (baseados em Proxy) tornam dados reativos; o template re-renderiza ao mudar.
- **Diretivas:** `v-if`, `v-for`, `v-bind` (`:`), `v-on` (`@`) e `v-model` (two-way binding em inputs) controlam o DOM declarativamente.
- **Composição:** `<script setup>` + composables (funções que encapsulam estado reativo) são a API moderna de reuso.
- **Virtual DOM:** Vue usa virtual DOM com renderização eficiente, sem exigir conhecimento interno do framework.
- **Progressivo:** pode ser usado como CDN num HTML simples ou com build completo (Vite, Nuxt).
- **Quando usar:** ótima curva de aprendizado, ideal para equipes menores e apps que crescem de forma incremental; competidor direto do React.

## Exemplos

```vue
<!-- Counter.vue — Single-File Component -->
<script setup lang="ts">
import { ref } from 'vue';

const count = ref(0);
</script>

<template>
  <div>
    <p>Cliques: {{ count }}</p>
    <button type="button" @click="count++">Incrementar</button>
  </div>
</template>

<style scoped>
p {
  font-size: 1.2rem;
}
</style>
```

```vue
<!-- v-model: two-way binding em formulários -->
<script setup>
import { ref } from 'vue';

const nome = ref('');
</script>

<template>
  <input v-model="nome" placeholder="Seu nome" />
  <p>Olá, {{ nome }}</p>
</template>
```

## Boas práticas
- Preferir a Composition API com `<script setup>` em vez da Options API no Vue 3.
- Usar `v-for` sempre com `:key` estável e não combinar `v-if` com `v-for` no mesmo elemento.
- Extrair lógica reativa em composables para reuso entre componentes.
- Reservar `v-model` para formulários; para dados de negócio, usar props e eventos explícitos.
- Gerenciar estado global com Pinia (sucessor do Vuex) apenas quando necessário.

## Armadilhas comuns
- Mutar props no filho — props são de mão única; mudanças sobem via eventos/`emit`.
- Esperar reatividade em adição de propriedades — com `ref`/`reactive` (Proxy) funciona, mas com objects criados antes, use `reactive` corretamente.
- Confundir Options API e Composition API ao ler código de origens diferentes.
- Mudar arrays/objetos por mutação direta em padrões antigos (Vue 2), sem disparar atualização.
- Usar `this` dentro do `<script setup>`, onde ele não existe.

## Relacionadas
- [[JavaScript]]
- [[Frontend]]
- [[Componentes]]
- [[React]]
- [[Nuxt]]
- [[TypeScript-Frontend]]
- [[Props]]