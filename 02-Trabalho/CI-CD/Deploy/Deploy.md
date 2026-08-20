---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Deploy

#area/trabalho #trabalho/ci-cd #conceito

**Resumo:** Publicação de uma versão do software em um ambiente.

## Conceitos-chave
- Deploy entrega uma versão testada a um ambiente: staging, homologação ou produção.
- Objetivo é publicar com risco controlado e possibilidade de rollback rápido.
- Estratégias comuns: blue-green, canary, rolling e recreação (recreate).

## Exemplos
```bash
# Deploy simples de imagem Docker já publicada
docker pull ghcr.io/org/app:${VERSION}
docker service update --image ghcr.io/org/app:${VERSION} app
```
```yaml
# Kubernetes: rolling update
kubectl set image deploy/app app=ghcr.io/org/app:${VERSION}
kubectl rollout status deploy/app
```

## Boas práticas
- Deployar o mesmo artefato validado, sem rebuild no ambiente.
- Promover artefato por ambientes: staging aprovado vai para produção.
- Automatizar o deploy e gerar logs/rastreabilidade do que foi publicado.
- Planejar rollback e janela antes de cada deploy de produção.

## Armadilhas comuns
- Deploy manual em produção sem registro, impossível saber o que rodou.
- Deployar código diferente do testado.
- Deploy sem monitoramento pós-publicação (verificar erro e métricas).
- Estratégia de deploy sem rollback definido.

## Relacionadas
- [[Producao]]
- [[Staging]]
- [[Rollback]]