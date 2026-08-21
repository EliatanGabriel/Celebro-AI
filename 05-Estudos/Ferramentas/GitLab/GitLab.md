---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# GitLab

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Plataforma Git com CI/CD integrado, autohospedável (Community e Enterprise Edition), que oferece merge requests, pipelines, containers registry e gerenciamento de todo o ciclo de vida do DevOps em um só lugar.

## Conceitos-chave
- **Merge Requests (MR)**: equivalente ao Pull Request do GitHub, com review, discussões e pipelines associados.
- **CI/CD como código**: pipelines definidos em `.gitlab-ci.yml` com stages, jobs, caches e artifacts.
- **GitLab Runner**: executor que roda os jobs; pode ser compartilhado ou específico por projeto/grupo.
- **Auto DevOps**: pipelines predefinidos (build, test, deploy) para projetos padrão.
- **Self-hosted**: o GitLab pode rodar no seu próprio servidor/container (omnibus, helm), diferente do GitHub.
- **Registry e Pages**: container registry integrado para imagens Docker e Pages para sites estáticos.
- **Groups e Projects**: hierarquia que organiza permissões e políticas por time.

## Exemplos
Pipeline simples (`.gitlab-ci.yml`):

```yaml
stages:
  - test
  - deploy

test:
  stage: test
  image: node:20
  script:
    - npm ci
    - npm test

deploy:
  stage: deploy
  image: node:20
  script:
    - npm run build
  artifacts:
    paths:
      - dist/
  only:
    - main
```

Rodar um job manualmente com variáveis:

```bash
# via pipeline UI ou CLI
gitlab-rails runner "..."   # execução em instância self-hosted
```

## Boas práticas
- Defina variáveis (CI/CD > Variables) em vez de hardcodar chaves no pipeline.
- Use caching e artifacts corretamente para reduzir o tempo dos jobs.
- Proteja a branch `main` com approvers (Code Owners) e pipelines obrigatórios.
- Version formatado com `pre-commit` ou lint nos jobs para manter a qualidade.
- Em self-hosted, mantenha backups e upgrades com estratégia; o runner precisa de atualizações regulares.

## Armadilhas comuns
- Secrets de CI vazados via echo em scripts ou variáveis não mascaradas.
- Runners indisponíveis/lentos que atrasam pipelines; monitore a fila de jobs.
- Confundir `only`/`rules` — a sintaxe de `rules` é mais expressiva e recomendada.
- Imagens grandes e sem cache que tornam os pipelines lentos e caros.
- Permissões mal configuradas em grupos (qualquer um pode criar projetos ou fazer deploy).

## Relacionadas
- [[Git]]
- [[GitHub]]
- [[Kubernetes-CLI]]