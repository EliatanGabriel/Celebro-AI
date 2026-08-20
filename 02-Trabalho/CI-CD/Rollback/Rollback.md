---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Rollback

#area/trabalho #trabalho/ci-cd #conceito

**Resumo:** Retorno a uma versão anterior quando o deploy apresenta problemas.

## Conceitos-chave
- Rollback reverte a aplicação para a última versão estável em caso de erro pós-deploy.
- Deve ser rápido e seguro, preferencialmente automatizado.
- Complementa o deploy: toda publicação de risco exige plano de reversão.

## Exemplos
```bash
# Voltar para a versão anterior
docker service update --rollback app

# Kubernetes: rollback de deploy
kubectl rollout undo deploy/app
kubectl rollout status deploy/app

# Reversão manual (fallback)
docker run ghcr.io/org/app:${VERSION_ANTERIOR}
```

## Boas práticas
- Manter a versão anterior pronta e acessível (artefato imutável no registry).
- Ter critérios claros de rollback: erro 5xx, latência alta, queda de métrica.
- Preferir rollback via comando automatizado ao processo manual.
- Registrar o incidente e a causa após reverter, para corrigir a raiz.

## Armadilhas comuns
- Não ter a versão anterior disponível quando é preciso reverter.
- Rollback de código sem reverter migração de banco (quebrar dados).
- Demorar para decidir reverter, prolongando o impacto.
- Confundir rollback com `git revert` no código sem republicar o artefato.

## Relacionadas
- [[Deploy]]
- [[Producao]]
- [[Monitoramento]]