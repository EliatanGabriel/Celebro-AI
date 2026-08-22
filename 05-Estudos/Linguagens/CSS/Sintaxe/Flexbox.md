---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Flexbox

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Flexbox distribui elementos em uma dimensão (linha ou coluna), controlando alinhamento, direção e proporção de espaço entre itens.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `display: flex` | Ativa o contexto flex no container | `.nav { display: flex; }` |
| `flex-direction` | Direção do eixo principal | `row` (padrão) ou `column` |
| `flex-wrap` | Permite quebra de linha | `wrap` |
| `justify-content` | Alinha no eixo principal | `center`, `space-between` |
| `align-items` | Alinha no eixo cruzado | `center`, `stretch` |
| `align-content` | Alinha as múltiplas linhas | usado com `wrap` |
| `gap` | Espaço fixo entre itens | `gap: 1rem` |
| `flex-grow` | Quanto o item cresce | `flex-grow: 1` |
| `flex-shrink` | Quanto o item encolhe | padrão 1 |
| `flex-basis` | Tamanho inicial antes de distribuir | `flex-basis: 200px` |
| `flex: 1` | Atalho: grow=1, shrink=1, basis=0% | item ocupa espaço igual |
| `align-self` | Sobrepõe align-items num item | `align-self: flex-end` |
| `order` | Reordena visualmente os itens | `order: -1` |

## Exemplos

```css
/* Navbar centralizada: logo à esquerda, menu à direita */
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 2rem;
  padding: 0.75rem 1.5rem;
}

.navbar .links {
  display: flex;
  gap: 1rem;
}

/* Cards com larguras iguais que quebram a linha */
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
.card {
  flex: 1 1 260px; /* cresce, encolhe, base de 260px */
}
```

## Boas práticas

- Use `gap` em vez de margens entre itens — sem hacks de `margin: -x`.
- `justify-content: space-between` + `margin-left: auto` para empurrar um único item.
- `flex-wrap: wrap` para responsividade sem media queries.
- Prefira Grid quando o layout for bidimensional (linhas E colunas).
- Centralização completa: `justify-content` + `align-items: center`.

## Armadilhas comuns

- Confundir eixos: com `column`, `justify-content` vira vertical.
- Esquecer que `flex` no atalho reseta `basis` para 0% se não informado.
- `min-width` implícito de textos impede o item de encolher — use `min-width: 0`.
- Usar `order` para tudo: muda só o visual, não a leitura por leitores de tela.
- Aplicar propriedades de item (`flex-grow`) no container — não têm efeito lá.

## Relacionadas

- [[Estudos-CSS]]
- [[Grid-e-Posicionamento]]
