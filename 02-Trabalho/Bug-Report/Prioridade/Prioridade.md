---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Prioridade

#area/trabalho #trabalho/bug-report #conceito

**Resumo:** Urgência relativa de correção de um bug na fila do time.

## Conceitos-chave
- Prioridade define **quando** o bug deve ser corrigido, diferente da severidade, que define **quanto** impacto causa.
- Prioridade combina severidade com contexto de negócio: cliente afetado, data limite, impacto em receita.
- Prioridade pode mudar ao longo do ciclo (vira urgente se bloqueia uma release).

## Estrutura de um bom bug report
- Campo de **prioridade**: Baixa, Média, Alta, Crítica.
- Justificativa: bloqueio de release, cliente específico, perda de dados, workaround disponível.
- Alinhamento com severidade: crítico normalmente é alta, mas bug de baixa severidade pode ser alta por negócio.
- Quem decide: QA sugere, PO/gestão valida na triagem.

## Boas práticas
- Priorizar por impacto no usuário e valor de negócio, não pela ordem de chegada.
- Revisar prioridades em reuniões de triagem periódicas.
- Documentar o motivo da prioridade para evitar questionamentos.
- Combinar com a estimativa de esforço para decidir o que entra na sprint.

## Armadilhas comuns
- Confundir prioridade com severidade e tratar como sinônimos.
- Prioridade "crítica" para todo bug, desvalorizando o escalonamento.
- Bugs de baixa prioridade esquecidos para sempre sem revisão.
- Priorizar bug sem considerar o custo de oportunidade do time.

## Relacionadas
- [[Severidade]]
- [[Prioridade-de-Bugs]]
- [[Bug-Report]]