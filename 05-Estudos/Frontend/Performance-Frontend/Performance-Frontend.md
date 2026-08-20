---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Performance-Frontend

#area/estudos #estudos/frontend #conceito

**Resumo:** Conjunto de otimizações para reduzir o tempo de carregamento e melhorar a responsividade da interface, medido por métricas como Core Web Vitals.

## Conceitos-chave
- **Core Web Vitals:** LCP (carregamento do conteúdo principal), INP (responsividade às interações) e CLS (estabilidade visual).
- **Code splitting / lazy loading:** dividir o bundle e carregar partes sob demanda (import dinâmico, rotas) reduz o JavaScript inicial.
- **Otimização de imagens:** formatos modernos (WebP/AVIF), dimensões corretas, `loading="lazy"` e `sizes` evitam downloads desnecessários.
- **Caching:** headers HTTP e cache do navegador evitam re-baixar assets; CDN aproxima o conteúdo do usuário.
- **Tree shaking e minificação:** remover código não usado e compactar o bundle final.
- **Recursos bloqueantes:** CSS/JS no caminho crítico atrasam a primeira renderização (render-blocking).
- **Ferramentas:** Lighthouse, PageSpeed Insights e DevTools de performance para medir e diagnosticar.

## Exemplos

```js
// code splitting: import dinâmico de um módulo pesado
import('./editor-pesado.js').then(({ montarEditor }) => {
  montarEditor();
});
```

```html
<!-- imagem otimizada e carregada sob demanda -->
<img
  src="banner.webp"
  alt="Banner"
  width="1200"
  height="630"
  loading="lazy"
/>
```

```js
// preload do recurso mais importante para o LCP
<link rel="preload" as="image" href="/banner.webp" />
```

## Boas práticas
- Medir com Lighthouse/Core Web Vitals antes de otimizar — otimização sem métrica é adivinhação.
- Carregar primeiro o conteúdo crítico e só então o resto (lazy loading, prioritários).
- Otimizar e dimensionar imagens corretamente (o maior ganho fácil de LCP).
- Definir tamanhos estáveis para elementos (reserve espaço) para evitar CLS.
- Configurar cache agressivo para assets com hash imutável e usar CDN.

## Armadilhas comuns
- Aplicar lazy loading em tudo, inclusive no conteúdo inicial — piora LCP e experiência.
- Ignorar o peso de fontes e libs JS grandes, mesmo com o HTML "leve".
- Imagens de hero sem `width`/`height` ou preload, causando CLS e LCP lento.
- Otimizar apenas o HTML e deixar bundle JS com centenas de KB não splitado.
- Esquecer `sizes` em imagens responsivas, baixando versões maiores que o necessário.

## Relacionadas
- [[Vite]]
- [[Next-js]]
- [[Caching]]
- [[Frontend]]
- [[Webpack]]
- [[PWA]]