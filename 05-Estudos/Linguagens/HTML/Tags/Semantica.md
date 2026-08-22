---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# HTML Semântico

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Tags semânticas dão significado à estrutura da página, facilitando navegação por leitores de tela, indexação por buscadores e manutenção do código.

## Referência rápida

| Tag/Sintaxe | O que faz | Exemplo |
|---|---|---|
| `<header>` | Cabeçalho de página ou seção | `<header><h1>Blog</h1></header>` |
| `<nav>` | Bloco de navegação principal | `<nav><a href="/">Início</a></nav>` |
| `<main>` | Conteúdo principal (um por página) | `<main>...</main>` |
| `<section>` | Agrupamento temático com título | `<section><h2>Sobre</h2></section>` |
| `<article>` | Conteúdo independente e completo | post, notícia, comentário |
| `<aside>` | Conteúdo relacionado/periférico | barra lateral, propaganda |
| `<footer>` | Rodapé com créditos/links | `<footer>&copy; 2026</footer>` |
| `<address>` | Contato do autor/seção | `<address>email@x.com</address>` |
| `<time datetime>` | Data legível por máquinas | `<time datetime="2026-08-21">hoje</time>` |
| `<details>/<summary>` | Bloco retrátil nativo (sem JS) | ver exemplo abaixo |
| `<div>` | Contêiner genérico em bloco | só quando não há tag semântica |
| `<span>` | Contêiner genérico inline | idem |

## Exemplos

```html
<body>
  <header>
    <nav aria-label="Principal">
      <a href="/">Início</a> | <a href="/posts">Posts</a>
    </nav>
  </header>

  <main>
    <article>
      <h1>Título do post</h1>
      Publicado em <time datetime="2026-08-21">21/08/2026</time>
      <p>Conteúdo do artigo...</p>
    </article>
    <aside>Posts relacionados</aside>
  </main>

  <footer>
    <address>contato@blog.dev</address>
  </footer>
</body>
```

## Boas práticas

- Use apenas **um** `<main>` e um único `<h1>` por página.
- Prefira a tag semântica mais específica; recorra a `div` só como último recurso.
- Cada `<section>` deve ter um título (`h2`–`h6`); sem título, provavelmente é uma `div`.
- Use `<details>` para FAQs e acordeões simples — funciona sem JavaScript.
- Estrutura consistente (`header` > `nav` > `main` > `footer`) ajuda SEO e leitores de tela.

## Armadilhas comuns

- Fazer tudo com `div class="header"` — buscadores não entendem o papel do bloco.
- Colocar o menu fora de `<nav>` ou usar vários `<main>`.
- Usar `<article>` para blocos que não fazem sentido sozinhos.
- Aninhar `<section>` dentro de `<footer>` sem sentido estrutural.
- Achar que semântica é "enfeite": ela impacta ranking no Google e acessibilidade real.

## Relacionadas

- [[Estudos-HTML]]
- [[Estrutura-do-Documento]]
