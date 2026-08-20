---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Git Branch Strategy

#area/trabalho #trabalho/git-branch-strategy #conceito

**Resumo:** Convenções de branches para organização do desenvolvimento.

## Conceitos-chave
- Estratégia de branches define como o time trabalha com main, develop, feature, release e hotfix.
- Modelos comuns: Git Flow, GitHub Flow e trunk-based.
- A estratégia influencia CI/CD, revisão e o fluxo de release.

## Exemplos
```bash
# Git Flow: branches por propósito
git checkout -b feature/US-123-carrinho main
git checkout -b release/v1.4.0 develop
git checkout -b hotfix/fix-cupom main

# GitHub Flow: branch curta a partir da main
git checkout -b feat/nova-busca
# abrir PR -> revisar -> merge na main
```
```
main (estável) <- hotfix/*
develop (integração) <- feature/*
release/* (candidata a produção)
```

## Boas práticas
- Escolher a estratégia conforme o tamanho do time e a frequência de release.
- Branch curta e descritiva, com prefixo por tipo (feat, fix, hotfix).
- Exigir pull request e revisão antes do merge.
- Manter `main` sempre deployável e sincronizada com o que está em produção.

## Armadilhas comuns
- Misturar estratégias sem definição, criando conflitos e confusão.
- Branches longas demais que divergem muito da main.
- Merge direto na main sem revisão nem testes.
- `main` desatualizada em relação a produção (mentira o "main deployável").

## Relacionadas
- [[Conflitos]]
- [[Ciclo-de-Release]]
- [[Deploy]]