---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Template-Bug

#area/trabalho #trabalho/bug-report #conceito

**Resumo:** Modelo padronizado para reportar bugs de forma completa e clara.

## Conceitos-chave
- Template como contrato mínimo de informação que um bug report deve ter.
- Campos padronizados garantem consistência entre relatórios e previsibilidade para quem tria.
- O template é base para abertura de tickets no Jira/Trello e para o fluxo QA.

## Estrutura de um bom bug report
1. **Título:** resumo curto (ex.: "Falha ao salvar pedido com cupom vencido").
2. **Ambiente:** SO, navegador, versão do sistema, ambiente (staging/produção).
3. **Passos para reproduzir:** sequência numerada e mínima.
4. **Comportamento esperado:** o que deveria acontecer.
5. **Comportamento atual:** o que aconteceu de fato.
6. **Evidências:** print, vídeo, log, request/response.
7. **Classificação:** severidade, prioridade, área afetada.

## Boas práticas
- Manter um campo por linha e preencher todos os campos obrigatórios.
- Incluir link do ticket, commit ou versão quando houver.
- Revisar o template periodicamente com o time para remover campos inúteis.
- Usar o mesmo template em todos os canais de reporte (Jira, Trello, Slack).

## Armadilhas comuns
- Campos em branco que obrigam retrabalho de triagem.
- Título genérico ("erro no sistema") que dificulta busca e deduplicação.
- Template tão longo que desestimula o reporter a preencher.
- Copiar e colar sem adaptar ao contexto do bug.

## Relacionadas
- [[Bug-Report]]
- [[Steps-to-reproduce]]
- [[Severidade]]
- [[Prioridade]]