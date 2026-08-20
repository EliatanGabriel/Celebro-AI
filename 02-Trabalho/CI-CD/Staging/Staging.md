---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Staging

#area/trabalho #trabalho/ci-cd #conceito

**Resumo:** Ambiente de testes que espelha produção antes do deploy final.

## Conceitos-chave
- Staging reproduz produção em configuração, versão e, idealmente, dados/volume próximos.
- É a última etapa de validação antes do deploy em produção.
- Permite executar testes de regressão, smoke e homologação sem risco ao usuário.

## Exemplos
```bash
# Promover artefato de staging para produção
docker pull ghcr.io/org/app:${VERSION}
docker tag ghcr.io/org/app:${VERSION} ghcr.io/org/app:prod-candidata
```
```yaml
# GitHub Actions: gate de aprovação antes do deploy em produção
  deploy_prod:
    needs: [test, deploy_staging]
    environment: production   # requer aprovação manual
    steps:
      - run: ./deploy.sh production
```

## Boas práticas
- Manter staging o mais próximo possível de produção (paridade de configuração).
- Definir critérios de saída: o que precisa passar para liberar produção.
- Usar dados sintéticos representativos, nunca dados reais sensíveis.
- Promover o mesmo artefato testado em staging para produção.

## Armadilhas comuns
- Staging muito diferente de produção, validando cenário irreal.
- Testar funcionalidades só em produção porque "staging não tem dado".
- Ambiente de staging sem manutenção, quebrado ou fora da versão atual.
- Validar em staging e recompilar em produção, quebrando a paridade.

## Relacionadas
- [[Producao]]
- [[Deploy]]
- [[Testes-API]]