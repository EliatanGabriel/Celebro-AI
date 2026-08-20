---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Tailwind

#area/estudos #estudos/frontend #conceito

**Resumo:** Framework CSS utility-first que gera classes utilitárias sob demanda, permitindo construir interfaces rápidas e consistentes diretamente no HTML.

## Conceitos-chave
- **Utility classes:** classes atômicas como `flex`, `p-4`, `text-center` e `bg-blue-500` compõem o visual sem escrever CSS próprio.
- **Geração sob demanda:** o Tailwind varre o código (`content` no config) e gera apenas as classes realmente usadas no CSS final — arquivo enxuto.
- **Responsivo:** prefixos de breakpoint (`sm:`, `md:`, `lg:`) aplicam variantes por largura, seguindo mobile-first.
- **Variants:** `hover:`, `focus:`, `disabled:`, `dark:` modificam o estilo por estado.
- **Configuração:** `tailwind.config.js` define cores, fontes, espaçamentos e extensões do tema (design tokens).
- **@apply e @layer:** `@apply` embute utilitários em classes CSS customizadas; `@layer` organiza cascata.
- **Tailwind 4:** configurado via CSS (`@theme`) e detecção automática de conteúdo, sem arquivo JS obrigatório.
- **Quando usar:** protótipos rápidos e projetos em que a consistência de design tokens supera a separação HTML/CSS.

## Exemplos

```html
<!-- card construído só com utilitários -->
<div class="max-w-sm rounded-lg border border-gray-200 p-4 shadow-sm">
  <h2 class="text-lg font-semibold text-gray-800">Título</h2>
  <p class="mt-1 text-sm text-gray-600">Conteúdo do card.</p>
  <button class="mt-3 rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400">
    Ação
  </button>
</div>
```

```css
/* tailwind.config.js (v3) — tema customizado */
module.exports = {
  content: ['./src/**/*.{html,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: { brand: '#0ea5e9' },
      spacing: { 18: '4.5rem' },
    },
  },
};
```

## Boas práticas
- Centralizar cores, fontes e espaçamentos no tema em vez de usar valores arbitrários soltos.
- Criar componentes reutilizáveis (classes utilitárias dentro do componente) em vez de copiar blocos grandes.
- Conferir o glob de `content` para não "podar" classes usadas dinamicamente.
- Combinar com `@apply` com parcimônia — preferir utilitários diretos.
- Consultar a documentação dos prefixos responsivos antes de escrever media queries próprias.

## Armadilhas comuns
- HTML verboso com cadeias enormes de classes, difíceis de ler e reutilizar sem componentes.
- Classes montadas dinamicamente (`bg-${cor}`) que o content scan não detecta — o CSS não é gerado.
- Conflito com CSS-Modules ou Bootstrap no mesmo projeto, sobrepondo resets e utilities.
- Diferenças entre v3 (config JS) e v4 (config via CSS) confundindo quem migra.
- Abusar de `!important` ou valores arbitrários (`w-[123px]`) que quebram a consistência do design system.

## Relacionadas
- [[Frontend]]
- [[Componentes]]
- [[CSS-Modules]]
- [[Bootstrap]]
- [[Sass]]
- [[Estudos-Responsividade]]