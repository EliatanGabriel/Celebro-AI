---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Severidade

#area/trabalho #trabalho/bug-report #conceito

**Resumo:** Grau de impacto do bug no funcionamento do sistema.

## Conceitos-chave
- Severidade mede a **intensidade do impacto técnico** do bug: o quanto impede o uso do sistema.
- É atribuída pelo QA com base na análise do comportamento, independente de prioridade.
- Classificação comum: Crítico, Alto, Médio, Baixo.

## Estrutura de um bom bug report
- **Crítico:** sistema fora do ar, perda de dados, falha de segurança, funcionalidade principal inutilizável.
- **Alto:** funcionalidade importante quebrada sem workaround aceitável.
- **Médio:** funcionalidade parcialmente afetada com workaround.
- **Baixo:** defeito estético, mensagem errada ou cenário raro sem impacto relevante.
- Justificativa curta: qual parte do sistema e quantos usuários são impactados.

## Boas práticas
- Basear a severidade em evidência e critérios objetivos definidos com o time.
- Reavaliar a severidade se o impacto real for diferente do reportado.
- Registrar o fluxo completo afetado, não apenas o erro isolado.
- Alinhar a escala de severidade com o time para evitar divergências.

## Armadilhas comuns
- Classificar tudo como crítico, perdendo o sinal dos bugs realmente graves.
- Atribuir severidade por emoção do reporte, não pelo impacto técnico.
- Confundir severidade (impacto) com prioridade (urgência de correção).
- Não revisar severidade após a triagem do dev.

## Relacionadas
- [[Prioridade]]
- [[Expected-vs-actual]]
- [[Bug-Report]]