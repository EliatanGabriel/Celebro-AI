---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Postman

#area/trabalho #trabalho/ferramentas #conceito

**Resumo:** Cliente de API para testar, documentar e depurar endpoints.

## Conceitos-chave
- Cliente de API para testar, depurar e documentar endpoints.
- Collections agrupam requisições de um módulo ou recurso.
- Environments armazenam variáveis (baseUrl, token) por ambiente.
- Scripts pré-request e de teste (JavaScript) automatizam fluxos.
- Newman roda as collections via CLI na CI.

## Exemplos
```
# Rodar collection na CI com Newman
newman run qa/api.postman_collection.json \
  -e qa/staging.postman_environment.json \
  --reporters cli,htmlextra

// Script de teste em uma requisição
pm.test('Status 200', () => pm.response.to.have.status(200));
pm.test('Schema do pedido', () => {
  pm.response.to.have.jsonBody('id');
});
```

## Boas práticas
- Organizar collections por módulo e manter hierarquia de pastas.
- Parametrizar URLs e credenciais com variáveis de ambiente.
- Escrever testes de status, schema e valores de resposta.
- Versionar as collections no repositório.
- Usar data files para testar múltiplos cenários.

## Armadilhas comuns
- Hardcode de URLs, tokens e dados sensíveis nas requisições.
- Testes frágeis acoplados a detalhes que mudam com frequência.
- Collections desatualizadas em relação ao código.
- Autenticação não parametrizada, quebrando em outro ambiente.
- Não rodar na CI, deixando os testes só em ambiente local.

## Relacionadas
- [[Testes-API]]
- [[Documentacao-API]]
- [[Endpoints]]
- [[Serializacao]]