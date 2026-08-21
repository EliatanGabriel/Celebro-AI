---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Documentacao-API

#area/trabalho #trabalho/api-rest #conceito

**Resumo:** Guia que descreve endpoints, parâmetros, respostas e erros de uma API.

## Conceitos-chave
- Descreve endpoints, parâmetros, respostas, erros e autenticação.
- OpenAPI/Swagger como padrão para especificação.
- Exemplos reais de requisição e resposta.
- Geração automática a partir de annotations/contratos.
- Versionada junto com o código e a própria API.

## Exemplos
```
openapi: 3.0.0
info:
  title: API de QA
  version: 1.0.0
paths:
  /usuarios:
    get:
      summary: Lista usuários
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items: { type: object }
```

## Boas práticas
- Gerar a doc a partir do código para não divergir.
- Incluir exemplos de requisição e resposta por endpoint.
- Documentar erros, status codes e autenticação.
- Manter a doc atualizada em todo code review.
- Disponibilizar a doc em ambiente de staging para consumo.

## Armadilhas comuns
- Documentação desatualizada em relação ao código.
- Exemplos incorretos que induzem o consumidor ao erro.
- Sem documentação de erros e códigos de status.
- Documentar apenas o caminho feliz.
- Ocultar a doc atrás de autenticação sem acesso de consumo.

## Relacionadas
- [[Endpoints]]
- [[Versionamento-API]]
- [[Confluence]]