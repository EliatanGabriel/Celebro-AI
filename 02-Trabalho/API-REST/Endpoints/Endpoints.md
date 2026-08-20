---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Endpoints

#area/trabalho #trabalho/api-rest #conceito

**Resumo:** URLs que representam recursos e ações disponíveis em uma API.

## Conceitos-chave
- URLs que representam recursos e operações da API.
- Nomeados por substantivos plurais: /usuarios, /pedidos.
- Métodos HTTP definem a operação sobre o recurso.
- Parâmetros de rota e query para identificar/filtrar.
- Hierarquia de recursos: /pedidos/{id}/itens.

## Exemplos
```
# Exemplo de design RESTful
GET    /api/v1/usuarios        -> lista
POST   /api/v1/usuarios        -> cria
GET    /api/v1/usuarios/{id}   -> detalhe
PUT    /api/v1/usuarios/{id}   -> substitui
PATCH  /api/v1/usuarios/{id}   -> atualiza parcial
DELETE /api/v1/usuarios/{id}   -> remove
```

## Boas práticas
- Usar substantivos no plural e evitar verbos na URL.
- Incluir a versão na URL desde o início.
- Manter parâmetros de filtro em query string.
- Evitar aninhamentos profundos além do necessário.
- Manter consistência de naming em toda a API.

## Armadilhas comuns
- URLs com verbos (getUsuario, createOrder).
- Misturar singular e plural entre endpoints.
- Aninhamento excessivo criando rotas complexas.
- Método errado para a operação (POST para leitura).
- Naming inconsistente entre endpoints semelhantes.

## Relacionadas
- [[Metodos-HTTP]]
- [[Status-Codes]]
- [[Documentacao-API]]
- [[API-REST]]