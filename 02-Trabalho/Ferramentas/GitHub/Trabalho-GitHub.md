---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# GitHub

#area/trabalho #trabalho/ferramentas #conceito

**Resumo:** Como o QA usa o GitHub no trabalho: pull requests, issues, Actions e estratégia de branches para dar visibilidade e rastrear a qualidade.

## Conceitos-chave
- **Pull Request (PR):** proposta de mudança que passa por code review e CI antes do merge; é onde o QA valida mudanças junto com os devs.
- **Issue:** tarefa ou bug rastreado; boa prática associar o PR ao número da issue (`Closes #123`).
- **GitHub Actions:** CI/CD que roda testes automaticamente a cada push/PR; gera os relatórios que o QA consulta.
- **Branches:** fluxo como git-flow ou trunk-based define onde cada mudança vai (feature, main, release).
- **Releases:** tags que marcam versões prontas para produção; o QA usa para saber o que vai para o ambiente de homologação.
- **Code owners / requerido de review:** regras que garantem aprovação obrigatória antes do merge.

## Exemplos
- Associar teste ao PR: abrir o PR e checar a aba de checks (Actions) para confirmar que a suíte passou.
- Comentar no PR quando um teste de regressão falha só depois do merge: informar o número do PR e a evidência.
- Criar issue de bug com repro em markdown e linkar ao PR da correção.
- Rodar testes localmente contra a branch do PR antes do merge: `git fetch origin pull/123/head` e criar uma branch de teste.

## Boas práticas
- Sempre revisar o diff do PR junto com os testes: mudança de schema, rota ou dependência exige ajuste nos testes.
- Exigir que o PR traga testes novos ou atualizados para a mudança.
- Consultar o histórico de CI dos últimos commits quando um teste flaky aparecer.
- Manter issues de QA (bugs, débitos técnicos) atualizadas com status e evidências.
- Usar o tab "Files changed" para marcar pontos que precisam de teste manual complementar.

## Armadilhas comuns
- Testar na branch errada: confirmar o checkout antes de rodar a suíte.
- Ignorar o relatório de CI e só confiar no teste local.
- Acreditar que CI verde garante qualidade: cobertura não garante cenários de negócio.
- Merge sem teste do fluxo completo quando há mudança de banco ou integração.
- Não registrar o commit/release testado na evidência do relatório.

## Relacionadas
- [[Trabalho]]
- [[GitHub-Actions]]
- [[Git-Branch-Strategy]]
- [[Code-Review]]
- [[Trabalho-CI-CD]]