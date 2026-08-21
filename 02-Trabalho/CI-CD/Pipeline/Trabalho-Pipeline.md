---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Pipeline

#area/trabalho #trabalho/ci-cd #conceito

**Resumo:** Sequência automatizada de etapas de integração, teste e entrega.

## Conceitos-chave
- Pipeline encadeia etapas: checkout, build, teste, análise, empacotamento e deploy.
- Gates (portões) bloqueiam a progressão quando um critério falha (teste, cobertura, aprovação).
- Etapas podem rodar em paralelo para acelerar; deploys costumam ser sequenciais.
- Quanto antes um defeito é detectado, menor o custo de correção.

## Exemplos
```yaml
# GitHub Actions: pipeline com gates
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm test
  deploy:
    needs: test          # gate: só roda se test passar
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

## Boas práticas
- Manter o pipeline versionado junto com o código (as code).
- Falhar rápido: build e testes unitários antes de etapas caras.
- Definir poucos gates, claros e acionáveis.
- Cachear dependências e artefatos entre execuções.

## Armadilhas comuns
- Pipeline com muitas etapas manuais que viram gargalo.
- Gates sem critério objetivo (aprovação vaga, cobertura sem sentido).
- Etapas duplicadas entre pipelines (Jenkins e Actions) divergindo.
- Falhas intermitentes ignoradas, gerando desconfiança no pipeline.

## Relacionadas
- [[Build]]
- [[Deploy]]
- [[GitHub-Actions]]
- [[Jenkins]]