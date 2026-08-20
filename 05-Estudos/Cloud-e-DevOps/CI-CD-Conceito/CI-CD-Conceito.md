---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# CI-CD-Conceito

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Práticas de Integração Contínua (CI) e Entrega/Implantação Contínua (CD) que automatizam build, testes e deploy, garantindo feedback rápido e qualidade constante.

## Conceitos-chave
- **Continuous Integration (CI):** integrar mudanças de código com frequência e validar automaticamente via build + testes a cada push.
- **Continuous Delivery (CD):** manter o software sempre em estado prontamente implantável, com artefatos versionados e deploy automatizado em ambientes de staging.
- **Continuous Deployment:** extensão do CD onde todo commit aprovado pelos testes é implantado em produção automaticamente.
- **Pipeline:** sequência de estágios (build, teste, análise, deploy) que materializa a automação.
- **Feedback rápido:** falhas detectadas em minutos, reduzindo o custo da correção.
- **Artefato:** resultado versionado do build (imagem de container, pacote, binário) promovido entre ambientes.
- **Gates de qualidade:** checagens (cobertura, lint, segurança) que podem bloquear a promoção do artefato.

## Exemplos

Fluxo conceitual de um pipeline CI/CD:

```text
push/PR → CI: lint → unit tests → build → gerar imagem/artefato
        → CD: deploy em staging → testes de integração → aprovação
        → deploy em produção (automático ou manual)
```

Pipeline simplificado no GitHub Actions:

```yaml
name: CI/CD
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
      - run: npm run build
```

## Boas práticas
- Commits pequenos e frequentes para reduzir conflitos e acelerar feedback.
- Testes rodando em ambiente o mais próximo possível de produção.
- Manter o pipeline rápido (paralelizar etapas) para incentivar o uso.
- Tratar a pipeline como código (pipeline-as-code) e versioná-la.
- Usar a mesma esteira para todos os ambientes, mudando apenas a configuração.

## Armadilhas comuns
- Confundir CD com deploy automático: entrega contínua permite deploy manual com um clique.
- Pipeline lento demais que leva a commits "batch" e integrações raras.
- Testes flaky que quebram a CI sem motivo real, minando a confiança.
- Build não reprodutível (depende de máquina do desenvolvedor) em vez de artefato imutável.
- Pular a etapa de staging e só testar em produção.

## Relacionadas
- [[Pipeline]]
- [[GitHub-Actions]]
- [[Jenkins]]
- [[Docker]]
- [[DevOps]]