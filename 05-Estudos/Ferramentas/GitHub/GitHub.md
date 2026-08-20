---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# GitHub

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Plataforma de hospedagem de repositórios Git da Microsoft, com colaboração via pull requests, issues, GitHub Actions para CI/CD, Pages para sites e um grande ecossistema de open source.

## Conceitos-chave
- **Repositórios e remotes**: hospeda clones Git com acesso via HTTPS/SSH; `origin` aponta para o remote.
- **Pull Requests (PR)**: proposta de mudança entre branches com review, comentários inline e checks de CI.
- **Issues e Projects**: rastreamento de bugs, tarefas e planejamento com quadros kanban e milestones.
- **GitHub Actions**: CI/CD como código em `.github/workflows/*.yml` com triggers, jobs e steps.
- **GitHub Pages**: hospedagem estática de sites/documentação a partir de branches ou Actions.
- **Fork e contribuição**: fork cria cópia para PRs; é a base do fluxo de contribuição em projetos open source.
- **Branch protection**: regras que exigem review, checks e impedem push direto em branches protegidas.

## Exemplos
Workflow de CI simples (`.github/workflows/ci.yml`):

```yaml
name: CI
on: [push, pull_request]
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
```

Clonar com SSH e criar PR via CLI:

```bash
gh repo clone usuario/repo
git checkout -b correcao
git push -u origin correcao
gh pr create --title "Corrige bug X" --body "Descrição"
```

## Boas práticas
- Proteja a branch `main` com review obrigatório e status checks.
- Use PRs pequenos e descritivos; divida grandes mudanças para facilitar review.
- Automatize o que for repetitivo no Actions (lint, testes, build, deploy em preview).
- Siga os templates de issue/PR para padronizar a comunicação do time.
- Use segredos do Actions (secrets) e nunca exponha tokens no código.

## Armadilhas comuns
- PRs gigantes que ficam semanas abertas e quebram por conflitos constantes.
- Rodar Actions com inputs não sanitizados pode executar código arbitrário em forks.
- Expor `GITHUB_TOKEN` ou chaves em logs de CI.
- Confundir `git push` para o fork (origin) com o repositório upstream em projetos open source.
- Ignorar branch protection e fazer push direto em produção por "praticidade".

## Relacionadas
- [[Git]]
- [[GitLab]]
- [[VS-Code]]