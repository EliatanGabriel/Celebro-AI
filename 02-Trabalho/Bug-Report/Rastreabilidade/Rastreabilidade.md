---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Rastreabilidade

#area/trabalho #trabalho/bug-report #conceito

**Resumo:** Vínculo do bug com código, versão, ticket e usuário afetado.

## Conceitos-chave
- Rastreabilidade é a capacidade de ligar um bug report a sua origem: commit, branch, versão e ticket.
- Permite responder "desde quando existe?", "qual mudança introduziu?" e "quem mais é afetado?".
- Depende de boas práticas de versionamento e de metadados preenchidos no report.

## Estrutura de um bom bug report
- Campo de **versão** em que o bug foi encontrado e, se possível, a primeira versão afetada.
- Campo de **ambiente** e configuração onde ocorreu.
- Vínculos rastreáveis: número do ticket, PR/commit suspeito, usuário ou segmento afetado.
- Histórico do bug: quando foi reportado, corrigido e verificado.

## Boas práticas
- Sempre registrar versão e hash/commit no report.
- Usar `git bisect` ou logs de release para localizar a introdução do bug.
- Manter o report atualizado ao longo do ciclo (reportado, em análise, corrigido, verificado).
- Relacionar o bug a testes que cobrem o cenário para fechar o loop de rastreabilidade.

## Armadilhas comuns
- Report sem versão, impossibilitando saber se já foi corrigido.
- Vínculo errado (ticket de outra feature, commit de outra mudança).
- Histórico sobrescrito em vez de acumulado, perdendo a evolução da análise.
- Rastrear somente o código e ignorar configuração e dados de ambiente.

## Relacionadas
- [[Reproducao]]
- [[Ambiente]]
- [[Regressao-bug]]