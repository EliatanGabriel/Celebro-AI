---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Ciclo de Release

#area/trabalho #trabalho/ciclo-de-release #conceito

**Resumo:** Processo de levar mudanças de desenvolvimento até produção.

## Conceitos-chave
- Release é a entrega de um conjunto de mudanças aprovadas a um ambiente.
- Envolve versionamento (semver), branch de release, changelog e janela de deploy.
- Etapas típicas: desenvolvimento -> integração -> staging -> produção -> monitoramento.

## Exemplos
```bash
# Tagging de release (semver)
git tag -a v1.4.0 -m "Release 1.4.0"
git push origin v1.4.0
# Changelog (conventional commits)
v1.4.0
- feat: nova busca por filtro
- fix: erro ao salvar cupom
```
```yaml
# GitHub Actions: deploy acionado por tag de release
on:
  push:
    tags: ["v*"]
```

## Boas práticas
- Definir cadência (semanal, mensal) e critérios de entrada/saída da release.
- Congelar (freeze) mudanças de risco perto da data de publicação.
- Versionar com semver e gerar changelog a partir dos commits.
- Manter a release curta para reduzir risco e facilitar investigação de bugs.

## Armadilhas comuns
- Release gigante com meses de mudanças, difícil de testar e reverter.
- Publicar sem verificar a branch de release em staging.
- Changelog desatualizado ou ausente.
- Freeze sem comunicação, gerando conflitos de última hora.

## Relacionadas
- [[Deploy]]
- [[Versionamento-API]]
- [[Git-Branch-Strategy]]