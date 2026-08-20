---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Acessibilidade

#area/estudos #estudos/frontend #conceito

**Resumo:** Conjunto de práticas para tornar interfaces utilizáveis por todas as pessoas, incluindo usuários de leitores de tela, navegação por teclado e baixa visão.

## Conceitos-chave
- **HTML semântico:** elementos nativos (`header`, `nav`, `main`, `button`, `label`) já trazem acessibilidade embutida — é a base antes de qualquer ARIA.
- **ARIA:** atributos (`aria-label`, `aria-hidden`, `role`) que complementam a semântica quando não há elemento nativo adequado.
- **Leitores de tela:** softwares como NVDA, VoiceOver e JAWS convertem a página em áudio; dependem de ordem de leitura e rótulos corretos.
- **Contraste:** texto legível requer razão de contraste mínima (4.5:1 para texto normal, 3:1 para grandes, conforme WCAG AA).
- **Navegação por teclado:** todas as ações devem ser alcançáveis com `Tab`, `Enter` e `Espaço`, com foco visível.
- **WCAG:** diretrizes organizadas em princípios (Percebível, Operável, Compreensível, Robusto) e níveis de conformidade A, AA e AAA.

## Exemplos

```html
<!-- Botão acessível: elemento nativo com label claro -->
<button type="button" onclick="salvar()">Salvar alterações</button>

<!-- Campo de formulário com label associado -->
<label for="email">E-mail</label>
<input id="email" name="email" type="email" autocomplete="email">

<!-- Ícone apenas decorativo, oculto do leitor de tela -->
<button aria-label="Fechar diálogo">
  <span aria-hidden="true">&times;</span>
</button>
```

```css
/* Skip link para pular navegação repetitiva */
.skip-link {
  position: absolute;
  left: -9999px;
}
.skip-link:focus {
  left: 16px;
  top: 16px;
  z-index: 100;
}
```

## Boas práticas
- Preferir elementos nativos a divs/ARIA — `button` já é focável e acionável por teclado.
- Garantir foco visível em todos os elementos interativos (não remover `outline` sem substituto).
- Escrever `alt` descritivo em imagens e vazio (`alt=""`) para imagens decorativas.
- Testar com leitor de tela, navegação só por teclado e ferramentas como Lighthouse/aXe.
- Manter ordem de leitura coerente com a ordem visual usando layout, não `tabindex` positivo.

## Armadilhas comuns
- Usar `div` com `onclick` em vez de `button`, quebrando teclado e foco.
- Esconder conteúdo com `display: none` para "economizar" espaço — some também da árvore de acessibilidade; use `sr-only`/`visually-hidden` quando precisar manter leitura.
- Confiar apenas em cor para indicar erro ou estado (ex.: vermelho sem mensagem de texto).
- `aria-label` em elementos que já têm texto visível, causando leitura duplicada ou conflitante.
- Ignorar `label` em inputs, deixando campos sem nome para leitores de tela.

## Relacionadas
- [[Frontend]]
- [[Eventos]]
- [[SEO]]
- [[Performance-Frontend]]