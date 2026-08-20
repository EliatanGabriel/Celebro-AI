---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# HTML

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem de marcação (não de programação) que estrutura o conteúdo de páginas web por meio de tags, formando a base de todo documento acessível no navegador.

## Conceitos-chave
- Paradigma declarativo de marcação: tags aninhadas descrevem títulos, parágrafos, listas, imagens, links e formulários.
- Não possui tipagem nem lógica de execução; a semântica é definida pela estrutura dos elementos.
- Interpretada pelo navegador: o documento é transformado em árvore DOM (Document Object Model).
- HTML5 traz tags semânticas (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`), `<video>`, `<canvas>` e novos inputs.
- Acessibilidade e SEO dependem diretamente da semântica e de atributos como `alt`, `lang` e `aria-*`.
- Particularidade: HTML é combinado com CSS (estilo) e JavaScript (comportamento) para formar uma página completa.

## Exemplos
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meu site</title>
</head>
<body>
  <header>
    <nav>
      <a href="/">Início</a>
      <a href="/sobre">Sobre</a>
    </nav>
  </header>

  <main>
    <h1>Olá, mundo</h1>
    <p>Este é um parágrafo <strong>semântico</strong>.</p>
    <img src="foto.jpg" alt="Descrição da imagem">

    <form action="/cadastro" method="post">
      <label for="nome">Nome:</label>
      <input type="text" id="nome" name="nome" required>
      <button type="submit">Enviar</button>
    </form>
  </main>
</body>
</html>
```

## Boas práticas
- Use tags semânticas em vez de `<div>` para tudo: melhora SEO e leitores de tela.
- Forneça `alt` descritivo em imagens e `lang` no documento.
- Estruture cabeçalhos (`h1`–`h6`) em hierarquia lógica, sem pular níveis.
- Associe `<label>` a inputs para formulários acessíveis e clicáveis.
- Valide o documento no W3C Validator e mantenha o `doctype` correto.

## Armadilhas comuns
- Confundir HTML (estrutura) com CSS (estilo) e JavaScript (comportamento).
- Fechar tags incorretamente ou usar aninhamento inválido (ex.: `<p>` dentro de `<p>`).
- Usar tags de apresentação obsoletas como `<font>` e `<center>`.
- Esquecer `alt` em imagens, prejudicando acessibilidade e SEO.
- Duplicar `id` no documento — `id` deve ser único; use `class` para repetição.

## Relacionadas
- [[Frontend]]
- [[HTTP]]