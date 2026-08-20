---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Testes-API

#area/trabalho #trabalho/api-rest #conceito

**Resumo:** Verificação de que endpoints respondem corretamente em diversos cenários.

## Conceitos-chave
- Verificam endpoints: status, headers, payload e contratos.
- Níveis: funcional, contrato, performance, segurança.
- Automação com Postman/Newman, supertest, REST Assured, Karate.
- Data-driven: múltiplos cenários com dados variados.
- Integram-se à regressão e à pipeline de CI.

## Exemplos
```
import request from 'supertest';
import app from '../app';

test('GET /api/usuarios retorna lista', async () => {
  const res = await request(app)
    .get('/api/usuarios')
    .set('Authorization', `Bearer ${token}`);

  expect(res.status).toBe(200);
  expect(Array.isArray(res.body)).toBe(true);
});
```

## Boas práticas
- Validar status, schema e valores-chave da resposta.
- Cobrir erros: 400, 401, 403, 404, 422, 500.
- Parametrizar ambientes e credenciais (variáveis).
- Testar contratos com validação de schema.
- Rodar na pipeline para pegar regressões cedo.

## Armadilhas comuns
- Testar somente o caminho feliz (status 200).
- Hardcode de dados, tokens e URLs.
- Ignorar headers, autenticação e casos de erro.
- Testes acoplados à ordem de execução.
- Não versionar os testes de API no repositório.

## Relacionadas
- [[Endpoints]]
- [[Status-Codes]]
- [[Testes-Automatizados]]