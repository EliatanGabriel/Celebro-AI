---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Bootstrap

#area/estudos #estudos/frontend #conceito

**Resumo:** Framework CSS clássico com grid responsivo de 12 colunas, componentes prontos (navbar, cards, modais) e utilitários para desenvolvimento rápido de interfaces.

## Conceitos-chave
- **Grid de 12 colunas:** `.container > .row > .col-*` distribui o layout em 12 frações, com `col-md-*` para colunas responsivas.
- **Breakpoints:** `sm`, `md`, `lg`, `xl`, `xxl` controlam onde o layout muda de disposição.
- **Componentes prontos:** navbar, buttons, forms, modais, dropdowns e alerts com comportamento JS já incluso (via Popper).
- **Utilitários:** classes de espaçamento (`m-2`, `p-3`), display (`d-flex`, `d-none`) e tipografia agilizam ajustes finos.
- **Customização via Sass:** variáveis como `$primary` e `$border-radius` permitem alterar o tema antes da compilação.
- **Quando usar:** MVPs, painéis administrativos e protótipos onde velocidade supera design único.

## Exemplos

```html
<div class="container">
  <div class="row">
    <div class="col-12 col-md-6">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Título</h5>
          <p class="card-text">Conteúdo do card.</p>
          <a href="#" class="btn btn-primary">Ação</a>
        </div>
      </div>
    </div>
    <div class="col-12 col-md-6">
      <!-- segunda coluna -->
    </div>
  </div>
</div>
```

```scss
// customizando o tema com Sass (antes de compilar)
$primary: #2b6cb0;
$enable-rounded: true;
@import "bootstrap/scss/bootstrap";
```

## Boas práticas
- Usar `col-*` responsivos com breakpoints mobile-first (`col-12` base, `col-md-6` a partir do médio).
- Customizar com Sass em vez de sobrescrever classes via CSS depois.
- Importar apenas os componentes necessários no build para reduzir o bundle.
- Aproveitar utilitários para consistência rápida, mas sem misturar com custom CSS desnecessário.
- Ajustar variáveis de tema para fugir do "visual padrão do Bootstrap".

## Armadilhas comuns
- Resultado "carimbado", idêntico a qualquer outro site com Bootstrap sem customização.
- Sobrescrever `.btn` e `.card` com regras próprias, gerando specificity difícil de manter.
- Usar versões antigas (v3/v4) que dependem de jQuery, carregando peso desnecessário.
- Não entender breakpoints e ver o layout "quebrar" em telas intermediárias.
- Misturar Bootstrap com Tailwind/CSS-Modules no mesmo projeto, causando conflitos de reset e utilities.

## Relacionadas
- [[Frontend]]
- [[Sass]]
- [[Estudos-Responsividade]]
- [[Tailwind]]
- [[CSS-Modules]]