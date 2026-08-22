---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Cores, Unidades e Funções

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** CSS oferece várias notações de cor e unidades de medida — absolutas como px e relativas como rem/% — além de funções que calculam valores em tempo real.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| Nome da cor | ~148 cores nomeadas | `color: tomato;` |
| `#fff` / `#ffffff` | Hexadecimal (3 ou 6 dígitos) | `background: #1e88e5;` |
| `rgb()` / `rgba()` | Vermelho-verde-azul + alpha | `rgba(0,0,0,.5)` |
| `hsl()` / `hsla()` | Matiz-saturação-luminosidade + alpha | `hsl(210, 80%, 50%)` |
| `currentColor` | Usa a cor do `color` atual | `border: 1px solid currentColor` |
| `px` | Absoluta (não escala com usuário) | `width: 200px` |
| `%` | Relativa ao pai | `width: 50%` |
| `em` | Relativa ao font-size do próprio elemento | `padding: 1em` |
| `rem` | Relativa à raiz (`html`, geralmente 16px) | `font-size: 1.25rem` |
| `vh` / `vw` | % da altura/largura da viewport | `height: 100vh` |
| `ch` | Largura do caractere "0" | `max-width: 60ch` |
| `fr` | Fração do espaço livre (grid) | `grid-template-columns: 1fr 2fr` |
| `calc()` | Operação entre unidades | `calc(100% - 2rem)` |
| `min()` / `max()` / `clamp()` | Limita valor entre extremos | `clamp(1rem, 4vw, 2rem)` |
| `var(--nome)` | Lê custom property definida | `color: var(--cor-primaria)` |

## Exemplos

```css
:root {
  --cor-primaria: hsl(220, 90%, 55%);
  --espaco: 1rem;
}

.card {
  color: var(--cor-primaria);
  border-color: currentColor;
  /* fluido: nunca menor que 16px nem maior que 24px */
  font-size: clamp(1rem, 4vw, 1.5rem);
  width: calc(100% - var(--espaco) * 2);
}
```

## Boas práticas

- Use `rem` para fontes e espaçamentos: respeita as preferências do usuário.
- Defina paleta e tokens em `--custom-properties` no `:root`.
- `clamp(min, ideal, max)` resolve tipografia fluida sem media queries.
- `ch` é ótimo para limitar largura de leitura (~60–75 caracteres).
- Prefira HSL para gerar variações de uma mesma matiz.

## Armadilhas comuns

- Usar `px` em font-size, ignorando zoom/acessibilidade.
- Confundir `em` (elemento atual) com `rem` (raiz) — aninhados, `em` compõe.
- `100vh` no mobile inclui área sob a barra do navegador; considere `dvh`.
- Esquecer espaço ao redor dos operadores no `calc()` (`calc(100%-2rem)` falha).
- Declarar `--var` num elemento e tentar usar num irmão (não herda).

## Relacionadas

- [[Estudos-CSS]]
- [[Box-Model]]
