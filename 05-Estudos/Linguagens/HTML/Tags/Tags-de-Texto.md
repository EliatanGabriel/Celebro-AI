---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Tags de Texto

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** As tags de texto estruturam títulos, parágrafos e trechos com significado (ênfase, citação, código), indo além da simples apresentação visual.

## Referência rápida

| Tag/Sintaxe | O que faz | Exemplo |
|---|---|---|
| `<h1>`–`<h6>` | Títulos por hierarquia (h1 mais importante) | `<h1>Título principal</h1>` |
| `<p>` | Parágrafo de texto | `<p>Texto corrido.</p>` |
| `<span>` | Trecho inline genérico (sem sentido próprio) | `<span class="destaque">x</span>` |
| `<strong>` | Importância forte (renderiza em negrito) | `<strong>Atenção</strong>` |
| `<em>` | Ênfase no tom (renderiza em itálico) | `<em>muito</em>` |
| `<mark>` | Texto destacado/marcado | `<mark>trecho chave</mark>` |
| `<small>` | Observações menores (letras miúdas) | `<small>*termos aplicam</small>` |
| `<br>` | Quebra de linha forçada | `Linha 1<br>Linha 2` |
| `<hr>` | Separador temático de conteúdo | `<hr>` |
| `<blockquote>` | Citação em bloco | `<blockquote cite="url">...</blockquote>` |
| `<cite>` | Título da obra citada | `<cite>Dom Casmurro</cite>` |
| `<code>` | Código inline | `<code>let x = 1</code>` |
| `<pre>` | Preserva espaços e quebras | `<pre><code>...</code></pre>` |
| `<abbr>` | Abreviação com título explicativo | `<abbr title="Hypertext">HTML</abbr>` |
| `<sub>` / `<sup>` | Subscrito / sobrescrito | `H<sub>2</sub>O`, `x<sup>2</sup>` |

## Exemplos

```html
<article>
  <h1>Guia de HTML</h1>
  <p>Escreva <strong>HTML semântico</strong> e use <code>&lt;section&gt;</code>
     para agrupar conteúdos relacionados. Isso é <em>essencial</em> para
     acessibilidade.</p>

  <blockquote cite="https://developer.mozilla.org">
    HTML descreve a estrutura do conteúdo. — <cite>MDN Web Docs</cite>
  </blockquote>

  <p>Fórmula: E = mc<sup>2</sup>, escrito em
     <mark>menos de uma linha</mark>.</p>
</article>
```

## Boas práticas

- Use apenas um `<h1>` por página e mantenha a hierarquia sem pular níveis.
- Prefira `<strong>`/`<em>` a `<b>`/`<i>` quando houver significado.
- Envolva `<code>` em `<pre>` para blocos multilinha.
- `<br>` só para quebras poéticas/endereço; separação de parágrafo usa `<p>`.
- Use `<abbr title>` na primeira ocorrência da sigla.

## Armadilhas comuns

- Escolher nível de título pelo tamanho visual em vez da hierarquia.
- Usar `<span>` com estilos onde caberia uma tag semântica (`<strong>`, `<em>`).
- Colocar elementos de bloco dentro de `<p>` (inválido).
- Esquecer de escapar `<` como `&lt;` dentro de exemplos de código.
- Abusar de `<br>` para "dar espaço" entre blocos.

## Relacionadas

- [[Estudos-HTML]]
- [[Estrutura-do-Documento]]
