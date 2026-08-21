---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Nuxt

#area/estudos #estudos/frontend #conceito

**Resumo:** Framework Vue para aplicações universais com SSR e SSG, roteamento baseado em arquivos, auto-imports e arquitetura full-stack via Nitro.

## Conceitos-chave
- **Modelo mental:** Nuxt é o "Next.js do Vue" — o componente Vue continua com template/script/style reativos, e o Nuxt adiciona servidor, rotas por arquivo e convenções de projeto.
- **File-based routing:** a pasta `pages/` define rotas; `app.vue` e `layouts/` controlam a estrutura compartilhada.
- **Auto-imports:** componentes, composables e utilitários em `components/` e `composables/` são importados automaticamente, sem declaração manual.
- **SSR/SSG/ISR:** Nitro (servidor embutido) renderiza no servidor ou gera estático; páginas podem ser híbridas por rota com `routeRules`.
- **Data fetching:** `useFetch` e `useAsyncData` são a forma recomendada de buscar dados com SSR, deduplicação e cache.
- **Módulos:** ecossistema de extensões (`@nuxtjs/tailwindcss`, `@nuxt/image`, i18n, auth).
- **Full-stack:** `server/api/*` cria endpoints servidos pelo próprio Nuxt.
- **Quando usar:** aplicações Vue que precisam de SEO, carregamento inicial rápido e estrutura full-stack em um único projeto.

## Exemplos

```vue
<!-- pages/index.vue -->
<script setup lang="ts">
const { data: posts } = await useFetch('/api/posts');
</script>

<template>
  <main>
    <h1>Posts</h1>
    <ul>
      <li v-for="post in posts" :key="post.id">{{ post.title }}</li>
    </ul>
  </main>
</template>
```

```ts
// server/api/posts.ts — endpoint full-stack
export default defineEventHandler(() => {
  return [{ id: 1, title: 'Olá Nuxt' }];
});
```

## Boas práticas
- Usar `useFetch`/`useAsyncData` em vez de `fetch` bruto para aproveitar SSR e deduplicação.
- Definir `routeRules` para misturar SSG e SSR por rota conforme a necessidade.
- Configurar SEO com `useHead`/`useSeoMeta` (title, description, Open Graph).
- Explorar auto-imports de composables e componentes para reduzir imports repetitivos.
- Manter dependências de módulos versionadas e configuradas via `nuxt.config.ts`.

## Armadilhas comuns
- Tratar o projeto como uma SPA Vue simples, perdendo SSR/SEO sem perceber.
- Usar `window`/`document` fora de guardas (ex.: `onMounted`), quebrando o build no servidor.
- Hidratação divergente quando o servidor e o cliente geram marcação diferente (ex.: `Date.now()` no template).
- Buscar dados com `fetch` bruto no setup, duplicando requisições ou pulando o cache do Nuxt.
- Confundir lifecycle do Vue (`onMounted`) com ciclo do servidor (`onServerPrefetch`/`useAsyncData`).

## Relacionadas
- [[Vue]]
- [[Next-js]]
- [[Frontend]]
- [[SEO]]
- [[Performance-Frontend]]
- [[TypeScript-Frontend]]