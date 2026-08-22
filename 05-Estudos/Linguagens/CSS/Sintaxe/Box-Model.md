---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Box Model

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Todo elemento é uma caixa composta por content, padding, border e margin — e `box-sizing` decide se width inclui ou não essas camadas.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `content` | Conteúdo (texto, imagem) | área interna da caixa |
| `padding` | Espaço interno entre conteúdo e borda | `padding: 1rem 2rem;` |
| `border` | Borda com espessura/estilo/cor | `border: 2px solid #333;` |
| `margin` | Espaço externo entre caixas | `margin: 0 auto;` |
| `box-sizing: content-box` | width = só o conteúdo (padrão) | soma padding/border ao width |
| `box-sizing: border-box` | width inclui padding + border | mais previsível |
| Margem negativa | Aproxima/sobrepõe elementos | `margin-top: -10px` |
| Colapso de margens | Margens verticais adjacentes somem | 30px + 20px = 30px |
| `width` / `height` | Dimensões da caixa | `width: 100%` |
| `min-width / max-width` | Limites de dimensionamento | `max-width: 1200px` |
| `outline` | Contorno fora da borda, sem ocupar espaço | foco de teclado |

## Exemplos

```css
/* Reset moderno: border-box em tudo */
*, *::before, *::after {
  box-sizing: border-box;
}

.card {
  /* com border-box, a largura final É 320px */
  width: 320px;
  padding: 16px;
  border: 4px solid #ddd;
  margin-inline: auto;
  outline-offset: 2px;
}

/* Centralizar bloco com largura máxima */
.container {
  max-width: 1100px;
  margin: 0 auto;
}
```

## Boas práticas

- Aplique `border-box` globalmente no início de todo projeto.
- Centralize blocos com `margin: auto` + `max-width`.
- Use `outline` para indicar foco — ele não afeta o layout.
- Prefira `gap` a margens quando usar flex/grid.
- Inspecione no DevTools (aba Layout) para ver cada camada da caixa.

## Armadilhas comuns

- Sem `border-box`, `width: 100%` + padding estoura o pai.
- Margens verticais "colapsam" entre pai e primeiro filho — use padding ou gap.
- `margin: 0 auto` não centra elemento inline nem com position absolute.
- Achando que padding aumenta o clique do botão sem aumentar o tamanho visual.
- Usar margens negativas sem entender stacking context — gera sobreposição inesperada.

## Relacionadas

- [[Estudos-CSS]]
- [[Flexbox]]
