---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Sass

#area/estudos #estudos/frontend #conceito

**Resumo:** Pré-processador CSS que adiciona variáveis, aninhamento, mixins, partials e funções para estilos mais organizados, reutilizáveis e mantidos por compilação.

## Conceitos-chave
- **Sass vs SCSS:** SCSS é a sintaxe mais usada (superconjunto do CSS); Sass é a sintaxe indentada, sem chaves e ponto e vírgula.
- **Variáveis:** `$cor-primaria: #3182ce;` permite temas e consistência reutilizando valores.
- **Nesting:** aninhamento de seletores espelha a hierarquia HTML, reduzindo repetição.
- **Mixins:** blocos reutilizáveis com argumentos (`@mixin`/`@include`), ideais para agrupar regras repetidas.
- **Partials e @use:** arquivos `_nome.scss` dividem estilos em módulos, importados com `@use` (que substituiu o obsoleto `@import`).
- **Funções e controle:** `@each`, `@for` e funções próprias geram CSS programaticamente.
- **Compilação:** dart-sass (o implementador oficial) transforma SCSS em CSS; integrado a bundlers via loaders.

## Exemplos

```scss
// _variables.scss
$primary: #3182ce;
$radius: 8px;

// botao.scss
@use "variables";

@mixin botao($bg) {
  display: inline-block;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: variables.$radius;
  background: $bg;
  &:hover {
    filter: brightness(1.1);
  }
}

.btn-primary {
  @include botao(variables.$primary);
}

.card {
  .title {
    font-weight: 700; // nesting espelha a estrutura
  }
}
```

```css
/* CSS compilado */
.btn-primary {
  display: inline-block;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 8px;
  background: #3182ce;
}
.btn-primary:hover {
  filter: brightness(1.1);
}
```

## Boas práticas
- Preferir SCSS (superconjunto do CSS) e compilar com dart-sass.
- Usar `@use`/`@forward` em vez do `@import` (depreciado).
- Organizar com partials (`_variables.scss`, `_mixins.scss`) e pastas por feature.
- Reservar mixins para padrões com parâmetros; `@extend`/placeholder para reuso puro.
- Evitar nesting além de 2–3 níveis e manter a especificidade baixa.

## Armadilhas comuns
- Nesting excessivo, gerando seletores longos e com alta especificidade, difíceis de sobrescrever.
- Usar `@import`, que é lento e permite variáveis globais vazando; `@use` escopa por arquivo.
- Confundir variáveis Sass (compiladas) com CSS custom properties (`--var`, em runtime) — os dois não se substituem.
- Compilar SCSS fora do pipeline de build, produzindo CSS "sujo" ou fora de sincronia com o app.
- Misturar `@extend` com mixins sem critério, criando dependências surpresa entre regras.

## Relacionadas
- [[Frontend]]
- [[Tailwind]]
- [[CSS-Modules]]
- [[Bootstrap]]