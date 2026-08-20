---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Report

#area/trabalho #trabalho/testes-automatizados #conceito

**Resumo:** Relatório que consolida resultados e evidências dos testes.

## Conceitos-chave
- Relatório que consolida resultados, métricas e evidências de uma execução de testes.
- Métricas: passou, falhou, pulado, duração, cobertura de código.
- Evidências: screenshots, vídeos, logs e traces de falhas.
- Formatos: HTML, JUnit XML, Allure, JSON, dashboards de CI.
- Suporta análise de tendências e rastreabilidade entre execuções.

## Exemplos
```
# Gerar relatório Allure a partir dos resultados
npx allure generate ./allure-results --clean -o ./allure-report
npx allure open ./allure-report

# Reporters no Jest
"reporters": ["default", ["jest-junit", { "outputDirectory": "reports" }]]
```

## Boas práticas
- Gerar relatórios legíveis para o time, não só para máquinas.
- Anexar evidências sempre que um teste falhar.
- Integrar relatórios como artefatos da pipeline de CI.
- Manter histórico para acompanhar a tendência de estabilidade.
- Revisar relatórios e converter falhas recorrentes em bugs ou tarefas.

## Armadilhas comuns
- Relatório sem contexto, apenas números de passou/falhou.
- Evidências ausentes dificultando o debug de falhas.
- Dashboards sem ação: métricas que ninguém monitora.
- Artefatos enormes sobrecarregando o armazenamento da CI.
- Confundir cobertura de código com qualidade dos testes.

## Relacionadas
- [[Test-frameworks]]
- [[Monitoramento]]
- [[Testes-API]]
- [[Documentacao-de-Testes]]