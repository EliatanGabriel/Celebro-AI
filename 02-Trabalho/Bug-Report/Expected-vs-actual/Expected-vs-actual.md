---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Expected-vs-actual

#area/trabalho #trabalho/bug-report #conceito

**Resumo:** Comparação entre o comportamento esperado e o observado.

## Conceitos-chave
- O bug é definido pela **diferença** entre o que deveria acontecer (expected) e o que aconteceu (actual).
- Descrever o esperado dá ao dev o critério de correção e o critério de verificação.
- O esperado deve vir do requisito, especificação ou comportamento histórico.

## Estrutura de um bom bug report
- **Comportamento esperado (expected):** descrição objetiva, citando o requisito quando houver.
- **Comportamento atual (actual):** descrição do que ocorreu, com evidência.
- **Critério de aceite:** como saber que está corrigido ("ao salvar, mensagem de sucesso exibida").
- Diferença explícita entre os dois para eliminar ambiguidade.

## Boas práticas
- Escrever expected e actual como sentenças completas e mensuráveis.
- Basear o expected em especificação, protótipo ou versão anterior que funcionava.
- Quando não houver especificação, marcar como "a definir" em vez de omitir.
- Usar o expected como base para o teste de verificação da correção.

## Armadilhas comuns
- Descrever o actual sem dizer qual era o expected.
- Esperado subjetivo ("deveria funcionar melhor") sem critério verificável.
- Supor que o dev conhece o comportamento correto.
- Confundir workaround (contorno) com comportamento esperado.

## Relacionadas
- [[Steps-to-reproduce]]
- [[Severidade]]
- [[Prioridade]]