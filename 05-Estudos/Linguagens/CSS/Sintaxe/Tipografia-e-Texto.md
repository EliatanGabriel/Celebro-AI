---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Tipografia e Texto

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** As propriedades de tipografia controlam família, tamanho, peso e alinhamento do texto, definindo a identidade visual e a legibilidade da página.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `font-family` | Lista de fontes em ordem de tentativa (stack) | `Arial, sans-serif` |
| `@font-face` | Carrega fonte local/web personalizada | ver exemplo abaixo |
| Google Fonts | Fontes via `<link>` ou `@import` | `<link href="fonts.googleapis...">` |
| `font-size` | Tamanho do texto | `font-size: 1.125rem` |
| `font-weight` | Peso (100–900, normal, bold) | `font-weight: 700` |
| `font-style` | Estilo (normal, italic) | `font-style: italic` |
| `line-height` | Altura entre linhas | `line-height: 1.6` |
| `letter-spacing` | Espaço entre letras | `letter-spacing: .05em` |
| `text-align` | Alinhamento horizontal | `text-align: center` |
| `text-decoration` | Linha decorativa (sublinhado etc.) | `text-decoration: underline` |
| `text-transform` | Caixa forçada (CSS, não conteúdo) | `text-transform: uppercase` |
| `color` | Cor do texto | `color: #333` |
| `white-space` | Como tratar espaços/quebras | `nowrap`, `pre` |
| `overflow` + `text-overflow` | Trunca com reticências | `text-overflow: ellipsis` |

## Exemplos

```css
/* Fonte externa + stack segura */
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap");

body {
  font-family: Inter, system-ui, sans-serif;
  line-height: 1.6;
  color: hsl(220 15% 20%);
}

/* Truncar título longo em uma linha */
.titulo-card {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

## Boas práticas

- Sempre termine o `font-family` com uma genérica (`sans-serif`, `serif`, `monospace`).
- Use `line-height` sem unidade (1.4–1.7) para acompanhar qualquer font-size.
- Limite largura de leitura com `max-width: 60ch`.
- `display=swap` no Google Fonts evita texto invisível durante o carregamento.
- Use `text-transform` para caixa visual — mantenha o HTML legível.

## Armadilhas comuns

- Depender de fonte não carregada sem fallback na stack.
- Usar CAPS direto no HTML quando `text-transform` resolve.
- `line-height: 16px` fixo quebra quando o usuário aumenta a fonte.
- Esquecer que `text-decoration: none` remove o sublinhado de links (afeta usabilidade).
- Carregar muitos pesos de fonte que não usa — peso desnecessário no download.

## Relacionadas

- [[Estudos-CSS]]
- [[Cores-Unidades-Funcoes]]
