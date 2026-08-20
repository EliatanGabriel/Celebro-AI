---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# GitHub-Actions

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Sistema de CI/CD integrado ao GitHub, onde workflows declarados em YAML rodam em runners na nuvem ou self-hosted, acionados por eventos do repositório.

## Conceitos-chave
- **Workflow:** automação definida em `.github/workflows/*.yml`, acionada por eventos (push, pull_request, schedule).
- **Job:** conjunto de steps que roda em um runner; jobs podem rodar em paralelo ou encadear via `needs`.
- **Step:** ação unitária (comando shell ou action reutilizável).
- **Runner:** máquina onde o job roda (GitHub-hosted `ubuntu-latest` etc. ou self-hosted).
- **Actions:** blocos reutilizáveis publicados no Marketplace (checkout, setup-node, deploy).
- **Trigger/Eventos:** push, PR, schedule (cron), workflow_dispatch (manual), tags.
- **Contextos e segredos:** `github`, `env`, `secrets` para parametrizar sem expor credenciais.
- **Caching:** cache de dependências entre execuções via action `actions/cache`.

## Exemplos

Workflow de CI com teste e build:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm test

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run build
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - run: aws s3 sync dist s3://meu-bucket
```

## Boas práticas
- Guardar credenciais apenas em secrets do repositório/organização.
- Quebrar fluxos em jobs pequenos com `needs` para paralelizar e reusar.
- Usar actions oficiais e pinar versão por SHA para segurança (supply chain).
- Adicionar `permissions:` mínimas no workflow (princípio do menor privilégio).
- Testar o fluxo com `workflow_dispatch` antes de expor a pushes.

## Armadilhas comuns
- Versionar secrets em texto puro no workflow — vaza credenciais no histórico.
- Workflow com passos monolíticos e sem paralelismo, deixando o CI lento.
- Rodar deploy em todo push sem gate de ambiente/PR.
- Usar `pull_request_target` sem cuidado (permite executar código não confiável).
- Ignorar o limite de minutos em repositórios privados (custo).

## Relacionadas
- [[CI-CD-Conceito]]
- [[Pipeline]]
- [[Jenkins]]
- [[DevOps]]