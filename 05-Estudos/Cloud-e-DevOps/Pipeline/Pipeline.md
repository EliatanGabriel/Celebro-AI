---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Pipeline

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Sequência automatizada de etapas (build, teste, deploy) que transforma código em software em produção com qualidade, repetibilidade e feedback rápido.

## Conceitos-chave
- **Estágio (stage):** fase lógica do pipeline (lint, build, teste, análise, deploy).
- **Step/atividade:** unidade executável dentro do estágio (comando, script, action).
- **Gatilhos (triggers):** push, PR, agendamento, tags, aprovação manual.
- **Artefato:** produto do build (imagem, pacote) promovido entre estágios e ambientes.
- **Ambientes:** dev, staging, prod — cada um com gates e regras próprias.
- **Pipeline-as-code:** definição versionada no repositório (Jenkinsfile, workflow YAML, .gitlab-ci.yml).
- **Feedback rápido:** quanto antes a falha aparece, menor o custo de correção.
- **Caching e paralelismo:** acelerar execução reaproveitando dependências e rodando estágios em paralelo.

## Exemplos

Pipeline genérico:

```text
[ push/PR ]
   └─> lint ─> unit test ─> build ─> imagem/artefato
        └─> integração (staging) ─> [gate] ─> deploy prod
```

Pipeline no GitLab CI:

```yaml
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - npm ci
    - npm run build
  artifacts:
    paths: [dist]

test:
  stage: test
  script:
    - npm test

deploy:
  stage: deploy
  script:
    - ./deploy.sh
  only:
    - main
```

## Boas práticas
- Manter o pipeline rápido: paralelizar e usar cache de dependências.
- Tratar a pipeline como código versionado e revisado em PR.
- Promover o mesmo artefato entre ambientes (build uma vez, use em tudo).
- Incluir gates de qualidade (cobertura, scan de segurança) que bloqueiam promoção.
- Monitorar a saúde do pipeline (taxa de sucesso, tempo de fila) como métrica de negócio.

## Armadilhas comuns
- Rebuildar em cada ambiente, gerando artefatos diferentes por estágio.
- Pipeline monolítico e lento que desestimula o uso do CI/CD.
- Falhas intermitentes (flaky) que quebram o pipeline sem motivo.
- Deploy automático sem gate em produção, em ambientes críticos.
- Ignorar logs de falha e artefatos para diagnóstico — o pipeline precisa ser auditável.

## Relacionadas
- [[CI-CD-Conceito]]
- [[GitHub-Actions]]
- [[Jenkins]]
- [[IaC]]
- [[DevOps]]