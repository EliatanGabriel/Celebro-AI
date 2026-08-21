---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Versionamento-API

#area/trabalho #trabalho/api-rest #conceito

**Resumo:** Estratégias para evoluir uma API sem quebrar consumidores.

## Conceitos-chave
- Evolui a API sem quebrar consumidores existentes.
- SemVer: major (breaking), minor (compatível), patch.
- Estratégias: URL (/v1, /v2), header (Accept), query.
- Deprecação com aviso e janela de migração.
- Compatibilidade retroativa e changelog.

## Exemplos
```
# Versionamento por URL
GET /api/v1/usuarios
GET /api/v2/usuarios

# Versionamento por header (media type)
Accept: application/json; version=2

# Deprecação
- marcar o campo como deprecated na documentação
- manter funcional por N releases
- remover apenas após a janela definida
```

## Boas práticas
- Adotar versionamento desde o início, mesmo na v1.
- Preferir mudanças não-breaking (adicionar campos, nunca remover).
- Publicar changelog e documentar breaking changes.
- Definir política clara de deprecação e remoção.
- Alinhar com o ciclo de release da organização.

## Armadilhas comuns
- Mudanças breaking sem aviso e fora de major.
- Manter versões indefinidamente sem deprecação.
- Remover campos/endpoints abruptamente.
- Versionamento por data sem semântica clara.
- Esquecer de atualizar a documentação por versão.

## Relacionadas
- [[Documentacao-API]]
- [[Endpoints]]
- [[Git-Branch-Strategy]]
- [[Ciclo-de-Release]]