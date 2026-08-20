---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Next-js

#area/estudos #estudos/frontend #conceito

**Resumo:** Framework React para produção com renderização no servidor (SSR), geração estática (SSG), rotas baseadas em arquivos e API routes, otimizado para SEO e performance.

## Conceitos-chave
- **Modelo mental:** React resolve a interface no cliente; o Next adiciona a camada de servidor — cada rota pode ser renderizada de formas diferentes (SSG, SSR, ISR, CSR) escolhidas por convenção ou configuração.
- **File-based routing:** pastas em `app/` (App Router) ou `pages/` (Pages Router) viram rotas; `app/layout.tsx` define layouts compartilhados.
- **Server Components:** componentes React executados no servidor por padrão, reduzindo JavaScript enviado ao cliente; `"use client"` marca interatividade.
- **SSG/SSR/ISR:** geração estática no build, renderização por requisição, e revalidação incremental (`revalidate`) que atualiza páginas estáticas em segundo plano.
- **API routes / Route handlers:** funções em `app/api/*/route.ts` expõem endpoints sem backend separado.
- **Otimizações:** `next/image` otimiza e faz lazy load de imagens; fontes otimizadas; streaming com `Suspense`.
- **Quando usar:** aplicações React que exigem SEO, carregamento inicial rápido e estrutura opinativa, em geral hospedadas na Vercel.

## Exemplos

```tsx
// app/page.tsx — Server Component com fetch e revalidação
export const revalidate = 3600;

export default async function Home() {
  const res = await fetch('https://api.exemplo.com/posts');
  const posts = await res.json();

  return (
    <main>
      <h1>Posts</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </main>
  );
}
```

```tsx
// app/api/posts/route.ts — Route Handler
export async function GET() {
  return Response.json({ hello: 'world' });
}
```

## Boas práticas
- Preferir SSG/ISR sempre que a página não depender do usuário — cacheia melhor e é mais rápida.
- Usar `next/image` para otimizar tamanho, formato e lazy load de imagens.
- Delegar carregamento de componentes pesados com `dynamic`/`Suspense` para não bloquear a primeira renderização.
- Manter Server Components no padrão e reservar `"use client"` apenas onde há interatividade.
- Medir Core Web Vitals e ajustar `revalidate` de acordo com a frequência de atualização dos dados.

## Armadilhas comuns
- Confundir SSR (renderizado no servidor a cada request) com SSG (uma vez no build) — escolha errada degrada performance ou desatualiza dados.
- Acessar `window`/`navigator` em Server Components, causando erros de build ou hydration mismatch.
- Abusar de `"use client"` e voltar a ter uma SPA pesada, perdendo o benefício do servidor.
- Esquecer `key` estável em listas ou gerar HTML diferente entre servidor e cliente (hydration failure).
- Usar fetch dentro de componentes client sem cache explícito, repetindo requisições.

## Relacionadas
- [[React]]
- [[SEO]]
- [[Frontend]]
- [[Performance-Frontend]]
- [[TypeScript-Frontend]]
- [[PWA]]