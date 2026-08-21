---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Build

#area/trabalho #trabalho/ci-cd #conceito

**Resumo:** Compilação e empacotamento do código em artefatos executáveis.

## Conceitos-chave
- Build transforma código-fonte em artefatos prontos para deploy (binários, bundles, imagens).
- Etapa inicial do pipeline de CI; se falhar, o pipeline para antes de testar e publicar.
- Deve ser **reprodutível**: mesmo commit gera o mesmo artefato.

## Exemplos
```yaml
# GitHub Actions: etapa de build
- name: Build
  run: |
    npm ci
    npm run build
  env:
    NODE_ENV: production
```
```bash
# CLI (npm)
npm ci && npm run build
# Docker
docker build -t minha-app:1.2.3 .
```

## Boas práticas
- Instalar dependências de forma determinística (`npm ci`, lockfile versionado).
- Cachear dependências e artefatos intermediários para acelerar o build.
- Versionar e rotular artefatos (tag, hash do commit) para rastreabilidade.
- Separar build de teste e de deploy em etapas independentes.

## Armadilhas comuns
- Build que depende do estado local da máquina (não reprodutível).
- Falta de lockfile, gerando builds diferentes a cada execução.
- Cache incorreto reaproveitando dependências velhas.
- Build lento demais que desestimula rodar em cada commit.

## Relacionadas
- [[Artefatos]]
- [[Deploy]]
- [[Pipeline]]