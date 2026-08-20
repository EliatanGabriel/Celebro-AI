---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Vite

#area/estudos #estudos/frontend #conceito

**Resumo:** Build tool moderna para frontend baseada em ES modules nativos, com hot module replacement instantâneo no desenvolvimento e bundle otimizado via Rollup para produção.

## Conceitos-chave
- **Dev server com ESM:** o navegador importa módulos nativos; sem bundle completo, o servidor entrega módulos sob demanda, tornando o start quase instantâneo.
- **HMR (Hot Module Replacement):** atualiza módulos alterados sem recarregar a página, preservando o estado da aplicação.
- **Build de produção:** Rollup empacota, minifica e faz code splitting; esbuild transpila TS/JSX rapidamente no dev.
- **Templates oficiais:** `npm create vite@latest` gera projetos React, Vue, Svelte, Vanilla e mais.
- **Plugins:** ecossistema de plugins (`@vitejs/plugin-react`, `@vitejs/plugin-vue`) e plugins de comunidade.
- **Variáveis de ambiente:** `import.meta.env.*` expõe `MODE`, `DEV`, `PROD` e variáveis `VITE_*`.
- **Proxy de dev:** redireciona `/api` para o backend local, evitando CORS no desenvolvimento.
- **Quando usar:** hoje o padrão de facto para iniciar projetos frontend, substituindo setups complexos de Webpack.

## Exemplos

```ts
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { fileURLToPath, URL } from 'node:url';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    proxy: {
      '/api': 'http://localhost:3000',
    },
  },
});
```

```bash
# criar e iniciar um projeto
npm create vite@latest minha-app -- --template react-ts
cd minha-app
npm install
npm run dev
```

## Boas práticas
- Usar os templates oficiais para começar com configuração correta.
- Configurar alias de imports (`@/`) no `resolve.alias` e no `tsconfig`.
- Aproveitar code splitting automático para rotas/lazy imports.
- Colocar assets estáticos em `public/` e assets processados em `src/assets`.
- Usar `vite preview` para testar o build de produção localmente.

## Armadilhas comuns
- Esperar `process.env` disponível no cliente — Vite usa `import.meta.env`, não `process.env`.
- Importar de `public/` como módulo — arquivos lá são servidos na raiz, não bundlados.
- Achar que Vite é específico do React — é agnóstico de framework (Vue, Svelte, vanilla).
- Confundir HMR com hot reload completo: HMR preserva estado e atualiza só o módulo alterado.
- Ignorar compatibilidade com navegadores legados — sem o plugin `@vitejs/plugin-legacy`, o build assume ESM moderno.

## Relacionadas
- [[Frontend]]
- [[Webpack]]
- [[React]]
- [[Vue]]
- [[Svelte]]
- [[TypeScript-Frontend]]
- [[Performance-Frontend]]