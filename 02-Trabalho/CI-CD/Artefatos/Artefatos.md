---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Artefatos

#area/trabalho #trabalho/ci-cd #conceito

**Resumo:** Produtos gerados pelo build que são armazenados e usados em deploys.

## Conceitos-chave
- Artefato é o resultado do build: binário, pacote npm, JAR, imagem Docker, bundle.
- Fica em repositório de artefatos (Nexus, Artifactory, GHCR, ECR) para reuso em deploys.
- Deve ser **imutável** e versionado: o que foi testado é exatamente o que vai a produção.

## Exemplos
```bash
# Publicar imagem Docker em registry
docker build -t ghcr.io/org/app:${GITHUB_SHA} .
docker push ghcr.io/org/app:${GITHUB_SHA}

# Usar o mesmo artefato no deploy (sem rebuild)
docker pull ghcr.io/org/app:${GITHUB_SHA}
docker run ghcr.io/org/app:${GITHUB_SHA}
```

## Boas práticas
- Versionar artefatos com tag ou hash do commit e nunca sobrescrever.
- Reutilizar o mesmo artefato em staging e produção (promoção de artefato).
- Definir política de retenção e limpeza do repositório.
- Assinar/verificar integridade de artefatos sensíveis.

## Armadilhas comuns
- Rebuildar em cada ambiente, testando código diferente do que foi aprovado.
- Artefato sem versão, impossível saber o que está em produção.
- Guardar artefato dentro do CI em vez de repositório dedicado.
- Registry sem limpeza acumulando espaço e custo.

## Relacionadas
- [[Build]]
- [[Deploy]]
- [[Staging]]