---
type: concept
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# CI/CD

#area/estudos #devops #conceito #integracao #entrega #automacao

**Resumo:** Práticas de integração contínua (build e teste a cada commit) e entrega contínua (publicação automatizada) para reduzir riscos e acelerar entregas.

## Conceitos-chave
- **Integração Contínua (CI):** cada push dispara build, testes e análise de qualidade automaticamente.
- **Entrega Contínua (CD):** artefatos prontos para produção ficam sempre disponíveis para deploy.
- **Deploy contínuo:** publicações em produção ocorrem automaticamente após a aprovação dos testes.
- **Pipeline:** sequência de estágios (checkout, build, teste, deploy) que define o fluxo do código até a produção.
- **Feedback rápido:** falhas detectadas em minutos evitam o acúmulo de erros de integração.

## Exemplos
```yaml
name: CI

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest
```

## Boas práticas
- Commitar pequenas mudanças com frequência.
- Manter o build e os testes rápidos e confiáveis.
- Versionar a configuração do pipeline junto com o código.
- Tratar o pipeline como parte do sistema: monitorar falhas e corrigi-las rápido.

## Armadilhas comuns
- Rodar testes apenas localmente e quebrar o build na CI.
- Criar pipelines lentos que desencorajam o feedback frequente.
- Fazer deploy manual mesmo com CI/CD configurado, perdendo rastreabilidade.
- Ignorar testes flaky (que falham de forma intermitente), gerando desconfiança no processo.

## Relacionadas
- [[Docker]]
- [[Kubernetes]]
- [[Pipeline]]
- [[CI-CD-Conceito]]
- [[GitHub-Actions]]