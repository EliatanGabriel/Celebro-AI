---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Webpack

#area/estudos #estudos/frontend #conceito

**Resumo:** Empacotador (bundler) de módulos JavaScript que constrói um grafo de dependências, aplica loaders e plugins, e gera bundles otimizados para produção.

## Conceitos-chave
- **Module bundling:** o Webpack parte de um `entry`, segue os imports e monta um grafo de dependências de todos os módulos do projeto.
- **Entry e Output:** `entry` define o ponto de partida; `output` onde o bundle final é gravado (com `[name].[contenthash].js` para cache).
- **Loaders:** transformam arquivos não-JS antes do bundling (`babel-loader` para JS/JSX, `css-loader` + `style-loader`, `sass-loader`, `ts-loader`).
- **Plugins:** estendem o ciclo de build (`HtmlWebpackPlugin` gera o HTML, `MiniCssExtractPlugin` extrai CSS, `DefinePlugin` injeta variáveis).
- **Code splitting:** `import()` dinâmico e `optimization.splitChunks` dividem o bundle em partes carregadas sob demanda.
- **Mode:** `development` (mapas de fonte, sem minificar) vs `production` (minificação, tree shaking via `sideEffects`).
- **Dev server / HMR:** recarregamento e hot module replacement no desenvolvimento.
- **Quando usar:** projetos legados com config específica; para projetos novos, Vite costuma ser mais simples.

## Exemplos

```js
// webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].[contenthash].js',
    clean: true,
  },
  module: {
    rules: [
      { test: /\.jsx?$/, exclude: /node_modules/, use: 'babel-loader' },
      { test: /\.css$/, use: ['style-loader', 'css-loader'] },
    ],
  },
  plugins: [new HtmlWebpackPlugin({ template: './index.html' })],
  optimization: {
    splitChunks: { chunks: 'all' },
  },
  mode: process.env.NODE_ENV === 'production' ? 'production' : 'development',
};
```

## Boas práticas
- Configurar `cache: { type: 'filesystem' }` para acelerar builds repetidos.
- Separar configs de dev e produção (ou usar presets/merge).
- Habilitar `optimization.splitChunks` para separar dependências de vendor do código da app.
- Definir `publicPath` corretamente para assets em CDN ou subpastas.
- Manter alertas de performance (`performance.hints`) para detectar bundles inchados.

## Armadilhas comuns
- Configuração verbosa e frágil — cada novo loader/plugin adiciona complexidade.
- Ordem errada de loaders (executados da direita para a esquerda): `sass-loader` antes de `css-loader`.
- Bundle único gigante sem code splitting, deixando o primeiro carregamento lento.
- Cache desatualizado por nomes de arquivo sem `[contenthash]` ou config de cache antiga.
- Escolher Webpack em projetos novos quando Vite entrega o mesmo resultado com muito menos config.

## Relacionadas
- [[Vite]]
- [[Babel]]
- [[Frontend]]
- [[JavaScript]]
- [[Sass]]
- [[Performance-Frontend]]
- [[TypeScript-Frontend]]