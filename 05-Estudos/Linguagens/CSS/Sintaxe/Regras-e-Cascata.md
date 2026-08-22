---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Regras e Cascata

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** O CSS é composto por regras `seletor { propriedade: valor; }` que o navegador resolve pela cascata, considerando origem, especificidade e ordem de declaração.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `seletor { prop: valor; }` | Estrutura básica de uma regra | `p { color: red; }` |
| `<style>` | CSS embutido no HTML | `<style>p{}</style>` no head |
| `<link rel="stylesheet">` | CSS em arquivo externo (recomendado) | `<link rel="stylesheet" href="a.css">` |
| `style=""` | CSS inline no elemento | `<p style="color:red">` |
| Especificidade | inline > id > classe > tag | `#x` vence `.y` |
| `!important` | Sobrepõe tudo (evitar) | `color: red !important;` |
| Herança | Propriedades de texto descem na árvore | `font-family`, `color` herdadas |
| `/* */` | Comentário CSS (não há `//`) | `/* ajuste mobile */` |
| `@media` | Estilos condicionais (ex.: telas) | `@media (max-width: 768px)` |
| `@import` | Importa outro arquivo de estilo | `@import url("tema.css");` |

## Exemplos

```css
/* Base herdada por todos os elementos filhos do body */
body {
  font-family: Arial, sans-serif;
  color: #222;
}

/* Especificidade: 0-1-1 (classe + tag) vence 0-0-1 (só tag) */
p { color: gray; }        /* perde */
.aviso p { color: crimson; } /* ganha */

@media (max-width: 600px) {
  .menu { flex-direction: column; }
}
```

## Boas práticas

- Mantenha todo o CSS em arquivos externos com `<link>`.
- Prefira classes a ids para estilizar (reuso + especificidade baixa).
- Resolva conflito aumentando especificidade, não com `!important`.
- Agrupe regras por componente e use comentários para navegar.
- Organize media queries no fim do arquivo ou junto do componente.

## Armadilhas comuns

- Usar `//` como comentário — só `/* */` funciona em CSS.
- Espalhar `!important` pelo projeto: depois fica impossível sobrescrever nada.
- Achar que ordem importa mais que especificidade (só desempata empates).
- Esperar herança em propriedades de caixa (`margin`, `border` não são herdadas).
- Duplicar estilos entre `<style>` inline e arquivo externo sem saber qual vence.

## Relacionadas

- [[Estudos-CSS]]
- [[Seletores]]
