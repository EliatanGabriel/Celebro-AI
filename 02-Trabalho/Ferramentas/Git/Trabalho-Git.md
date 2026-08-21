---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Git

#area/trabalho #trabalho/ferramentas #conceito

**Resumo:** Sistema de controle de versão distribuído usado em projetos de software.

## Conceitos-chave
- Sistema de controle de versão distribuído.
- Commits formam o histórico; branches isolam o trabalho.
- Merge e rebase integram mudanças; stash guarda trabalho temporário.
- Repositórios remotos permitem colaboração distribuída.
- Tags marcam releases.

## Exemplos
```
git checkout -b feature/qa-novos-testes
git add .
git commit -m "feat(qa): adiciona testes de regressão do checkout"
git push origin feature/qa-novos-testes

git stash          # guarda mudanças temporárias
git log --oneline --graph
git diff --cached  # revisa o que está no stage
```

## Boas práticas
- Commits pequenos e com mensagens descritivas.
- Uma branch por feature/correção, seguindo a estratégia do time.
- Revisar o diff antes de commitar (git diff, git status).
- Manter segredos fora do repositório.
- Integrar com frequência para evitar conflitos grandes.

## Armadilhas comuns
- Commitar arquivos de configuração local e credenciais.
- Force push em branch compartilhada, sobrescrevendo trabalho de outros.
- Commits gigantes difíceis de revisar e reverter.
- Ignorar conflitos de merge e resolver de forma incorreta.
- Commit sem mensagem clara, perdendo rastreabilidade.

## Relacionadas
- [[Git-Branch-Strategy]]
- [[Conflitos]]