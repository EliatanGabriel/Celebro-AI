---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# SEO

#area/estudos #estudos/frontend #conceito

**Resumo:** Search Engine Optimization: práticas para melhorar a visibilidade e o ranqueamento de páginas nos mecanismos de busca, com foco em conteúdo indexável e boa experiência.

## Conceitos-chave
- **Meta tags:** `title` e `description` únicos por página influenciam o clique nos resultados; Open Graph controla a prévia em redes sociais.
- **HTML semântico:** hierarquia de `h1`/`h2`, `main`, `article` e `nav` ajudam os crawlers a entender a estrutura.
- **SSR/SSG:** páginas renderizadas no servidor (ou estáticas) são indexáveis; SPA client-only depende de JavaScript e indexa pior.
- **Sitemap e robots.txt:** `sitemap.xml` lista URLs para os crawlers; `robots.txt` controla o que deve ser rastreado.
- **Canonical e dados estruturados:** `rel="canonical"` evita conteúdo duplicado; JSON-LD (Schema.org) enriquece os resultados.
- **Core Web Vitals:** velocidade e estabilidade (LCP, INP, CLS) são fatores de ranqueamento e de experiência.
- **Ferramentas:** Google Search Console monitora indexação, erros e consultas.

## Exemplos

```html
<!-- meta tags e Open Graph -->
<title>Como otimizar SEO — Guia Prático</title>
<meta name="description" content="Aprenda as práticas essenciais de SEO em 10 minutos." />
<meta property="og:title" content="Como otimizar SEO" />
<meta property="og:type" content="article" />
<meta property="og:image" content="/og-image.png" />
<link rel="canonical" href="https://exemplo.com/guia-seo" />
```

```html
<!-- dados estruturados JSON-LD -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Como otimizar SEO",
  "author": { "@type": "Person", "name": "Maria" }
}
</script>
```

## Boas práticas
- Escrever um `title` e `description` únicos e descritivos para cada página.
- Usar SSR/SSG (Next.js, Nuxt) ou pré-renderização para garantir conteúdo indexável.
- Definir URLs limpas e hierárquicas, com uma URL canônica por conteúdo.
- Adicionar `alt` em imagens e dados estruturados para conteúdo relevante.
- Enviar o sitemap ao Search Console e monitorar erros de indexação regularmente.

## Armadilhas comuns
- Depender de client-side rendering (SPA) para conteúdo importante — muitos bots não executam JS.
- Títulos e descrições duplicados em várias páginas, diluindo relevância.
- Esconder conteúdo (textos em abas, `display: none`) para "enganar" crawlers — é penalizado.
- Ignorar performance mobile, prejudicando o ranqueamento independente do conteúdo.
- Excesso de palavras-chave (keyword stuffing) ou textos sem estrutura de headings.

## Relacionadas
- [[Next-js]]
- [[Frontend]]
- [[Performance-Frontend]]
- [[Nuxt]]
- [[Estudos-Acessibilidade]]