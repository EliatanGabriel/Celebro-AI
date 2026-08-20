---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Metodos-HTTP

#area/trabalho #trabalho/api-rest #conceito

**Resumo:** Verbos que definem a operação a executar sobre um recurso.

## Conceitos-chave
- GET: ler recurso, sem efeitos colaterais, idempotente.
- POST: criar recurso ou disparar ação.
- PUT: substituir recurso por completo, idempotente.
- PATCH: atualizar parcialmente o recurso.
- DELETE: remover recurso.

## Exemplos
```
Método  | Operação            | Idempotente | Seguro
GET     | Leitura             | Sim         | Sim
POST    | Criação/ação        | Não         | Não
PUT     | Substituição        | Sim         | Não
PATCH   | Atualização parcial | Não         | Não
DELETE  | Remoção             | Sim         | Não
```

## Boas práticas
- Usar o verbo semanticamente correto para a operação.
- Manter GET sem efeitos colaterais.
- Respeitar idempotência: repetir PUT/DELETE não deve divergir.
- Retornar status code compatível (201 para POST, 204 para DELETE).
- Definir payload de PATCH como campos a alterar, não o objeto completo.

## Armadilhas comuns
- Usar POST para tudo, perdendo semântica e cache.
- GET com efeitos colaterais (alterar dados).
- Trocar PUT e PATCH (PUT parcial, PATCH completo).
- DELETE não idempotente (404 na segunda chamada sem tratamento).
- Payload de PATCH idêntico ao PUT, sem clareza de intenção.

## Relacionadas
- [[Endpoints]]
- [[Status-Codes]]
- [[Serializacao]]