---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Figma

#area/trabalho #trabalho/ferramentas #conceito

**Resumo:** Como o QA usa o Figma no trabalho: inspecionar designs, medir dimensões e comparar a implementação com o protótipo aprovado.

## Conceitos-chave
- **Frame / Artboard:** tela que representa a visão a ser testada.
- **Inspect panel:** painel que mostra posição, tamanho, espaçamento, tipografia e cor dos elementos.
- **Variants e States:** estados de componentes (hover, disabled, erro) que definem os cenários de teste visual.
- **Prototype / Flow:** navegação entre telas, base para o teste de fluxo.
- **Comentários e pins:** onde o design recebe feedback; o QA acompanha para saber o que mudou.
- **Componente (design token):** padrões reutilizáveis; divergência entre implementação e componente indica bug de consistência.

## Exemplos
- Medir espaçamento: selecionar o elemento no Figma, abrir Inspect e conferir `padding`, `margin` e `gap` esperados.
- Conferir contraste de cor: ler o código hex no Inspect e comparar com o valor aplicado no CSS.
- Validar estados: checar as variants do botão e testar hover/focus/disabled na implementação.
- Mapear responsividade: comparar o frame mobile e desktop com o layout renderizado.

## Boas práticas
- Confirmar no Figma qual é a versão/link oficial do layout antes de validar (evitar design desatualizado).
- Anotar no bug o caminho do frame (`Page > Tela > Componente`) para o dev localizar rápido.
- Usar a régua e o Inspect para dar medidas exatas nas evidências do bug.
- Conferir texto real no design (contraste de fonte, alinhamento) além de apenas cores e tamanhos.
- Comparar o protótipo clicável com o fluxo real para cobrir navegação e estados intermediários.

## Armadilhas comuns
- Testar contra um frame desatualizado ou com redlines desalinhadas.
- Basear-se apenas em screenshots, ignorando interações e estados definidos nas variants.
- Não considerar breakpoints responsivos definidos no protótipo.
- Achar que a medida do design é regra absoluta: espaçamento visual pode ter tolerância definida pelo time.
- Confundir cores de sobreposição (opacity) com cores sólidas no Inspect.

## Relacionadas
- [[Trabalho]]
- [[Bug-Report]]
- [[Expected-vs-actual]]
- [[Code-Review]]