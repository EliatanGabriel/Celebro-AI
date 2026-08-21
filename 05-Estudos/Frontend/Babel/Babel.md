---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Babel

#area/estudos #estudos/frontend #conceito

**Resumo:** Transpilador que converte JavaScript moderno (ES2020+, JSX, TypeScript) para versões compatíveis com navegadores antigos e ambientes restritos.

## Conceitos-chave
- **Transpilação:** processo de três etapas — parse para AST, transformação com plugins, e geração do código de saída.
- **Presets:** conjuntos de plugins prontos, como `@babel/preset-env` (JS moderno), `@babel/preset-react` (JSX) e `@babel/preset-typescript`.
- **Plugins:** transformações individuais (ex.: transformar arrow functions, destructuring) que os presets agregam.
- **Polyfills:** código que adiciona APIs ausentes (ex.: `Array.prototype.includes`) — Babel transpila sintaxe, mas não polyfill automaticamente.
- **Targets:** via `browserslist`, `preset-env` só transpila o que o público-alvo não suporta.
- **Babel não é bundler:** não resolve imports entre módulos; essa tarefa fica com Webpack, Vite ou Rollup.

## Exemplos

```json
// .babelrc.json
{
  "presets": [
    [
      "@babel/preset-env",
      {
        "targets": "> 0.5%, last 2 versions, not dead",
        "useBuiltIns": "usage",
        "corejs": 3
      }
    ],
    "@babel/preset-react"
  ]
}
```

```bash
# uso via CLI
npx babel src --out-dir dist
```

```js
// entrada: JS moderno e JSX
const greet = (name) => `Olá, ${name}`;
const el = <h1>{greet('Mundo')}</h1>;

// saída (com preset-env + preset-react): sintaxe ES5
var greet = function (name) {
  return 'Olá, ' + name;
};
var el = /*#__PURE__*/ React.createElement('h1', null, greet('Mundo'));
```

## Boas práticas
- Definir `targets`/`browserslist` reais para não transpilar/polyfill em excesso.
- Usar `useBuiltIns: "usage"` com `core-js` para incluir apenas os polyfills necessários.
- Separar sintaxe (transpilação) de runtime (polyfills) ao planejar o bundle.
- Integrar via loader (ex.: `babel-loader` no Webpack) em vez de rodar como etapa isolada.
- Manter Babel, presets e `@babel/core` na mesma versão major.

## Armadilhas comuns
- Achar que Babel instala polyfills sozinho — sem `useBuiltIns`/core-js, APIs novas falham em navegadores antigos.
- Confundir transpilação com polyfill: arrow functions são transpiladas, `fetch` e `Promise` precisam de polyfill.
- Usar `@babel/preset-env` sem targets, transpilando tudo desnecessariamente.
- Depender de `@babel/cli` no build em produção em vez de integrar ao bundler.
- Incluir `@babel/preset-react` sem configurar runtime automático (`runtime: "automatic"`), obrigando a importar React.

## Relacionadas
- [[Webpack]]
- [[JavaScript]]
- [[TypeScript]]
- [[Frontend]]
- [[Vite]]
- [[TypeScript-Frontend]]