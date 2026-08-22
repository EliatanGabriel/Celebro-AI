---
type: verbete
area: referencias
status: active
created: "2026-08-22"
updated: "2026-08-22"
---

# API-REST

#area/referencias #referencias/glossario

**Definição:** estilo de arquitetura para APIs web: recursos nomeados por URL, manipulados pelos verbos HTTP — GET (ler), POST (criar), PUT/PATCH (atualizar), DELETE (remover). Sem estado entre requisições: cada chamada carrega tudo que o servidor precisa. Respostas geralmente em [[JSON]] com códigos de status semânticos (200 ok, 404 não existe, 422 validação).

**Exemplo:** `GET /usuarios/42` lê o usuário 42; `DELETE /usuarios/42` remove. RESTful bem feito usa substantivos no plural, nunca verbos na rota (`/deletarUsuario` é anti-padrão).

**Ver também:** [[cURL-testar-APIs]] · [[JSON]]
