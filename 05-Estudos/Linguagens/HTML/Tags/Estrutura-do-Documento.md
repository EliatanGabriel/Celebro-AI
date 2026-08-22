---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Estrutura do Documento HTML

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Todo documento HTML segue uma estrutura base que declara o tipo de documento, define idioma, carrega metadados e estilos, e contém o conteúdo visível da página.

## Referência rápida

| Tag/Sintaxe | O que faz | Exemplo |
|---|---|---|
| `<!DOCTYPE html>` | Declara que é HTML5 (obrigatória) | `<!DOCTYPE html>` |
| `<html lang="pt-BR">` | Raiz do documento e idioma | `<html lang="pt-BR">` |
| `<head>` | Metadados invisíveis ao usuário | `<head>...</head>` |
| `<meta charset="UTF-8">` | Codificação de caracteres (acentos) | `<meta charset="UTF-8">` |
| `<meta name="viewport">` | Adapta a página a telas móveis | `<meta name="viewport" content="width=device-width, initial-scale=1.0">` |
| `<title>` | Título da aba do navegador | `<title>Início</title>` |
| `<link>` | Importa CSS externo | `<link rel="stylesheet" href="style.css">` |
| `<script defer>` | JS externo executado após o parse | `<script src="app.js" defer></script>` |
| `<body>` | Conteúdo visível da página | `<body>...</body>` |
| `<!-- -->` | Comentário (não aparece na página) | `<!-- cabeçalho -->` |

## Exemplos

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meu Portfólio</title>
  <!-- CSS carregado em paralelo -->
  <link rel="stylesheet" href="style.css">
  <!-- defer: executa só quando o HTML terminar de ser lido -->
  <script src="app.js" defer></script>
</head>
<body>
  <!-- conteúdo principal vai aqui -->
  <h1>Bem-vindo!</h1>
</body>
</html>
```

## Boas práticas

- Sempre comece com `<!DOCTYPE html>` para ativar o modo padrão.
- Use `lang` correto: leitores de tela e tradutores dependem dele.
- Deixe `charset` como primeira linha dentro de `<head>`.
- Prefira `defer` em scripts; use `async` apenas para scripts independentes (anúncios, analytics).
- Comente trechos complexos, não coisas óbvias.

## Armadilhas comuns

- Esquecer o viewport faz o site ficar minúsculo no celular.
- Colocar `<div>` ou texto direto fora de `<body>` gera HTML inválido.
- Usar `<script>` sem `defer` no `<head>` bloqueia a renderização da página.
- Esquecer UTF-8 causa acentos quebrados ("Ã§", "�").
- Fechar `<html>` antes de `</body>` invalida o documento.

## Relacionadas

- [[Estudos-HTML]]
- [[Semantica]]
