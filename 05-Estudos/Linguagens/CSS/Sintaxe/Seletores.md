---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Seletores

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Seletores definem quais elementos recebem os estilos, combinando tipos, classes, atributos e estados (pseudo-classes) com precisão crescente.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `p` | Todos elementos do tipo | `p { margin: 0; }` |
| `.classe` | Elementos com aquela classe | `.btn { }` |
| `#id` | O elemento com aquele id | `#topo { }` |
| `*` | Seletor universal (todos) | `* { box-sizing: border-box; }` |
| `A, B` | Agrupamento (mesmos estilos) | `h1, h2 { }` |
| `A B` | Descendente (qualquer nível) | `.card p { }` |
| `A > B` | Filho direto | `.menu > li { }` |
| `A + B` | Irmão imediatamente seguinte | `h2 + p { }` |
| `A ~ B` | Qualquer irmão seguinte | `img ~ figcaption { }` |
| `[attr]` / `[attr="x"]` | Presença / valor exato | `input[type="email"]` |
| `:hover` / `:focus` | Estado de mouse / teclado | `a:hover { }` |
| `:first-child` / `:nth-child()` | Posição entre irmãos | `li:nth-child(2n)` |
| `:not(X)` | Negação do seletor X | `li:not(.ativo)` |
| `::before` / `::after` | Conteúdo gerado antes/depois | `.tag::before { content: "#"; }` |
| `::placeholder` | Estiliza o placeholder do input | ver exemplo abaixo |

## Exemplos

```css
/* Todo link dentro da navegação, exceto o ativo */
nav a:not(.ativo):hover {
  color: #09f;
}

/* Linhas alternadas da tabela */
tbody tr:nth-child(odd) {
  background: #f5f5f5;
}

/* Parágrafo logo após cada título */
h2 + p {
  margin-top: 0;
}

/* Placeholder translúcido em inputs de busca */
input[type="search"]::placeholder {
  color: rgba(0, 0, 0, 0.4);
}
```

## Boas práticas

- Prefira classes; reserve id para âncoras/JS, não para estilo.
- Mantenha especificidade baixa (1 classe) para facilitar sobrescritas.
- Use combinadores (`>`, `+`) para contexto sem criar classes extras.
- `:focus-visible` para estilizar foco só via teclado.
- Teste seletores complexos no DevTools antes de commitar.

## Armadilhas comuns

- Exagerar no encadeamento (`.header .nav ul li a`) — frágil e específico demais.
- Confundir `A > B` (filho direto) com `A B` (descendente qualquer).
- Esquecer que `:nth-child` conta TODOS os irmãos, não só do mesmo tipo.
- Usar `::before/after` sem `content` — nada aparece.
- Depender de `:hover` como única interação (não existe em touch).

## Relacionadas

- [[Estudos-CSS]]
- [[Regras-e-Cascata]]
