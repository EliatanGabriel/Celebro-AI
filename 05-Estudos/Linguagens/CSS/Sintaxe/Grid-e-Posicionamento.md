---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Grid e Posicionamento

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** CSS Grid organiza layouts em duas dimensões (linhas e colunas), enquanto `position` controla o deslocamento e a sobreposição individual de elementos.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `display: grid` | Ativa o contexto de grade | `.layout { display: grid; }` |
| `grid-template-columns` | Define as colunas | `1fr 2fr 1fr` |
| `grid-template-rows` | Define as linhas | `auto 1fr auto` |
| `repeat()` / `minmax()` | Repete trilhas com limites | `repeat(3, minmax(0, 1fr))` |
| `fr` | Fração do espaço disponível | `grid-template-columns: repeat(4, 1fr)` |
| `gap` | Espaço entre linhas/colunas | `gap: 1rem` |
| `grid-column` / `grid-row` | Posiciona/expande item | `grid-column: span 2` |
| `grid-template-areas` | Layout por áreas nomeadas | ver exemplo abaixo |
| `position: static` | Padrão; fluxo normal | — |
| `position: relative` | Referência + offsets relativos a si | `top: 10px` desloca visualmente |
| `position: absolute` | Sai do fluxo, ancorado ao ancestral relative | badge em canto do card |
| `position: fixed` | Fixo na viewport | header fixo no topo |
| `position: sticky` | Cola ao rolar até o offset | thead da tabela |
| `z-index` | Ordem de sobreposição | precisa de position ≠ static |
| `float` | Legado: texto contorna imagem | evite para layout |

## Exemplos

```css
/* Layout com áreas nomeadas */
.layout {
  display: grid;
  grid-template-areas:
    "cabecalho cabecalho"
    "menu      conteudo";
  grid-template-columns: 220px 1fr;
  gap: 1rem;
}
.layout > header { grid-area: cabecalho; }
.layout > nav    { grid-area: menu; }

/* Badge absoluto dentro do card relativo */
.card { position: relative; }
.card .badge {
  position: absolute;
  top: -8px;
  right: -8px;
  z-index: 1;
}
```

## Boas práticas

- Use `minmax(0, 1fr)` para colunas que respeitam o conteúdo sem estourar.
- Grid para estrutura da página; Flexbox para componentes internos.
- Ancore elementos absolutos num pai `relative` próximo e claro.
- Reserve `z-index` altos (100+) para modais/dropdowns.
- `sticky` exige que o pai tenha altura suficiente para "colar".

## Armadilhas comuns

- `absolute` sem ancestral `relative`: âncora vira o body inteiro.
- Mudar `z-index` sem resultado porque o elemento é `static`.
- Usar `float` para montar layout moderno — legado problemático.
- Esquecer `grid-area` de algum filho com áreas nomeadas (item some da grade).
- Confundir `fixed` (viewport) com `sticky` (dentro do scroll do pai).

## Relacionadas

- [[Estudos-CSS]]
- [[Flexbox]]
