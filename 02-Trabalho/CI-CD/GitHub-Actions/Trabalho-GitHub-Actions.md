---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# GitHub-Actions

#area/trabalho #trabalho/ci-cd #conceito

**Resumo:** Plataforma de CI/CD integrada ao GitHub via workflows.

## Conceitos-chave
- Workflows são definidos em `.github/workflows/*.yml` e versionados com o código.
- Disparam por eventos: push, pull_request, schedule, tags, manual (`workflow_dispatch`).
- Compostos de jobs com steps; jobs podem depender uns dos outros (`needs`) e rodar em paralelo.
- Runners executam os jobs (GitHub-hosted ou self-hosted).

## Exemplos
```yaml
name: QA
on:
  pull_request:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - run: npm ci
      - run: npm test
      - uses: actions/upload-artifact@v4
        with: { name: reports, path: test-results }
```

## Boas práticas
- Pinarlar ações por tag/commit (SHA) para evitar mudanças quebradas.
- Usar segredos do GitHub para credenciais, nunca valores em texto.
- Aproveitar cache (`actions/cache`) para dependências.
- Dividir jobs pequenos e paralelizáveis para reduzir o tempo do workflow.

## Armadilhas comuns
- Ações de terceiros sem revisão e sem versionar (tag móvel).
- Workflow gigante e monolítico difícil de depurar e reusar.
- Segredo vazado em log ou em contexto de workflow.
- Depender de runner self-hosted sem manutenção e seguro.

## Relacionadas
- [[Pipeline]]
- [[Deploy]]
- [[Build]]