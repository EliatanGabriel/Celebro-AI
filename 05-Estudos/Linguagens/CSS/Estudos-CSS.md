---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# CSS

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem de estilo (não de programação) que define a apresentação visual de páginas web — layout, cores, tipografia e responsividade — interpretada pelo navegador.

## Conceitos-chave
- Paradigma declarativo: regras `seletor { propriedade: valor; }` descrevem como o HTML deve ser exibido.
- Sem tipagem e sem execução imperativa; não é uma linguagem de programação.
- Interpretada pelo navegador: folhas de estilo são carregadas via `<link>` ou bloco `<style>`.
- Cascata e especificidade determinam qual regra vence quando há conflito.
- Box model: todo elemento é uma caixa com `content`, `padding`, `border` e `margin`.
- Flexbox e Grid são os principais sistemas de layout; media queries garantem responsividade.
- Particularidade: variáveis customizadas (custom properties) e funções modernas (`clamp()`, `calc()`) no CSS atual.

## Exemplos
```css
:root {
  --cor-primaria: #2563eb;
  --espaco: 1rem;
}

.card {
  display: flex;
  flex-direction: column;
  gap: var(--espaco);
  padding: var(--espaco);
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  color: var(--cor-primaria);
}

@media (min-width: 768px) {
  .grade {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
  }
}
```

## Boas práticas
- Prefira classes a IDs ou seletores de tipo para manter especificidade baixa e reutilização alta.
- Use unidades relativas (`rem`, `%`, `vh`) para acessibilidade e responsividade.
- Organize com custom properties e uma arquitetura de nomenclatura (BEM, utility-first).
- Sempre defina `alt`/contraste e respeite estados de foco para acessibilidade.
- Adote Flexbox/Grid modernos em vez de `float` para layout.

## Armadilhas comuns
- Confundir cascata e especificidade: um seletor mais específico vence mesmo se vier antes.
- Usar `margin` quando o efeito desejado exige `padding` (e vice-versa), quebrando o box model.
- Supor que `position: absolute` se ancorar na página; ele se ancora no ancestral com `position` definido.
- Ignorar `box-sizing: border-box`, causando larguras imprevisíveis.
- Esquecer prefixos/vendedor e suporte a recursos modernos em navegadores antigos (use `@supports`).

## Relacionadas
- [[Frontend]]