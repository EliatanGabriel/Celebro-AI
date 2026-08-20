---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Integration-testing

#area/trabalho #trabalho/testes-automatizados #conceito

**Resumo:** Testes que verificam a integração entre módulos ou sistemas.

## Conceitos-chave
- Validam a integração entre módulos: banco de dados, APIs, filas, serviços.
- Mais lentos que unitários por envolver I/O real.
- Garantem que os contratos entre camadas se mantêm corretos.
- Podem usar banco de teste, transações e fixtures.
- Em APIs, verificam a requisição completa com o stack real.

## Exemplos
```
import request from 'supertest';
import app from '../app';

test('cria um usuário', async () => {
  const res = await request(app)
    .post('/api/usuarios')
    .send({ nome: 'QA', email: 'qa@exemplo.com' });

  expect(res.status).toBe(201);
  expect(res.body).toMatchObject({ nome: 'QA' });
});
```

## Boas práticas
- Usar um banco de teste isolado ou transações com rollback.
- Controlar dados iniciais com fixtures/seeds por cenário.
- Testar caminhos de sucesso e de erro (validação, 404, conflito).
- Rodar em CI com ambiente reprodutível.
- Isolar serviços externos com mocks na fronteira.

## Armadilhas comuns
- Estado global contaminando testes (dados vazando entre eles).
- Depender de serviços externos reais (pagamentos, e-mails).
- Testes acoplados à ordem de execução.
- Ignorar limpeza do banco entre execuções.
- Confundir com E2E: aqui a interação é por código, não navegador.

## Relacionadas
- [[Unit-testing]]
- [[E2E]]
- [[Testes-API]]