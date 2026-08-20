---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Metodo-de-Revisao

#area/estudos #estudos/revisao #conceito

**Resumo:** Método de revisão espaçada para fixar os conceitos estudados, com intervalos crescentes e revisão ativa.

## Conceitos-chave
- **Revisão espaçada:** revisitar o conteúdo em intervalos crescentes (1, 3, 7, 14, 30 dias) para combater a curva do esquecimento.
- **Recordação ativa (active recall):** em vez de reler, tentar recordar o conteúdo de memória antes de conferir a nota.
- **Campo `progresso`:** cada conceito tem `estudando` → `revisar` → `dominado`; a fila de revisão vive no MOC [[Revisao]].
- **Repetição:** cada revisão bem-sucedida aumenta o próximo intervalo; cada erro reinicia o ciclo.

## Exemplo de cronograma
1. Dia 1 — estuda e cria a nota (`estudando`).
2. Dia 2 — 1ª revisão (recordação ativa). Acertou → `revisar`.
3. Dia 4 — 2ª revisão. Acertou → mantém `revisar`.
4. Dia 11 — 3ª revisão.
5. Dia 25 — 4ª revisão. Acertou → `dominado`.

## Boas práticas
- Revisar ao abrir o vault: consulte a fila em [[Revisao]] e gaste 10-15 min.
- Para cada conceito, tente explicar com as próprias palavras (técnica Feynman).
- Crie um exemplo próprio de código em cada revisão, não só releia o da nota.
- Vincule o conceito a outras notas: a seção `## Relacionadas` mais rica melhora a retenção.

## Armadilhas comuns
- Reler em vez de recordar ativamente (falsa sensação de domínio).
- Marcar `dominado` cedo demais, antes dos 30 dias.
- Acumular fila sem revisar diariamente.

## Relacionadas
- [[Revisao]]