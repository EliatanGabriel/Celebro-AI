---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Responsividade

#area/estudos #estudos/frontend #conceito

**Resumo:** Capacidade de uma interface se adaptar a diferentes tamanhos e orientações de tela, priorizando uma abordagem mobile-first e layouts fluidos.

## Conceitos-chave
- **Media queries:** regras CSS que aplicam estilos conforme características do dispositivo, principalmente largura (`min-width`, `max-width`).
- **Mobile-first:** escrever estilos para telas pequenas primeiro e escalar com `min-width` — reduz CSS e prioriza o essencial.
- **Breakpoints:** pontos de mudança do layout; o ideal é defini-los pelo conteúdo, não por dispositivos específicos.
- **Layouts fluidos:** unidades relativas (`%`, `fr`, `vw`, `rem`) e `clamp()` permitem que o layout se ajuste continuamente.
- **Flexbox e Grid:** sistemas de layout que reorganizam elementos sem media queries em muitos casos (`flex-wrap`, `grid-template-columns: repeat(auto-fit, minmax(...))`).
- **Imagens responsivas:** `srcset` e `sizes` entregam a versão adequada de imagem para cada tela.
- **Viewport meta tag:** `width=device-width` é o que habilita o layout responsivo em navegadores mobile.

## Exemplos

```css
/* mobile-first: base para telas pequenas */
.cards {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

@media (min-width: 640px) {
  .cards {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .cards {
    grid-template-columns: repeat(3, 1fr);
  }
}

/* tipografia fluida */
h1 {
  font-size: clamp(1.5rem, 4vw, 3rem);
}
```

```html
<!-- viewport obrigatória -->
<meta name="viewport" content="width=device-width, initial-scale=1" />

<!-- imagem responsiva com srcset -->
<img
  src="foto-800.jpg"
  srcset="foto-400.jpg 400w, foto-800.jpg 800w, foto-1600.jpg 1600w"
  sizes="(max-width: 640px) 100vw, 800px"
  alt="Foto"
/>
```

## Boas práticas
- Adotar mobile-first e testar em telas reais, não só no DevTools.
- Usar unidades relativas (`rem`, `%`, `vw`) e `clamp()` em vez de `px` rígidos.
- Definir breakpoints pelo conteúdo (ex.: quando os cards ficam estreitos demais), não por modelos de celular.
- Garantir alvos de toque com pelo menos 44px e espaçamento confortável.
- Testar orientação, telas grandes (tablets) e zoom do navegador.

## Armadilhas comuns
- Criar breakpoints para cada aparelho específico, gerando CSS impossível de manter.
- Usar `px` fixos em fontes e containers, estourando em telas pequenas ou com zoom.
- Esquecer a viewport meta tag — o mobile renderiza a versão desktop comprimida.
- Inputs com `font-size` menor que 16px em iOS, que acionam zoom automático ao focar.
- Overflow horizontal causado por imagens sem `max-width: 100%` ou grids com largura fixa.

## Relacionadas
- [[Frontend]]
- [[Bootstrap]]
- [[Tailwind]]
- [[CSS-Modules]]
- [[Sass]]