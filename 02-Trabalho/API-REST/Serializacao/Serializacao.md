---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Serializacao

#area/trabalho #trabalho/api-rest #conceito

**Resumo:** Conversão de objetos em formato de dados transferível (JSON, XML).

## Conceitos-chave
- Converte objetos em formato transferível (JSON, XML, Protobuf).
- JSON é o padrão dominante em APIs REST.
- DTOs controlam quais campos são expostos.
- Convenção de naming: snake_case, camelCase, PascalCase.
- Envelope de dados, nulls e tipos precisam ser consistentes.

## Exemplos
```
# Resposta serializada em JSON (camelCase)
{
  "usuarioId": 42,
  "nomeCompleto": "Ana QA",
  "email": "ana@exemplo.com",
  "roles": ["admin", "qa"]
}

# Campos omitidos em vez de null
{ "usuarioId": 42, "nomeCompleto": "Ana QA" }
```

## Boas práticas
- Padronizar o naming em toda a API.
- Omitir campos null ou documentar a regra.
- Não expor campos internos (senhas, hashes, metadados).
- Manter consistência de tipos entre endpoints.
- Versionar mudanças de schema de forma compatível.

## Armadilhas comuns
- Expor campos sensíveis no JSON de resposta.
- Inconsistência de naming entre endpoints.
- Tipos instáveis (número vira string) quebram clientes.
- Envelope desnecessário ou inconsistente.
- Ignorar o schema ao evoluir campos.

## Relacionadas
- [[Endpoints]]
- [[Metodos-HTTP]]