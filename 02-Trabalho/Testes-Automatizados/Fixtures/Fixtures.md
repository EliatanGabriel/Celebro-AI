---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Fixtures

#area/trabalho #trabalho/testes-automatizados #conceito

**Resumo:** Dados fixos usados para manter testes determinísticos.

## Conceitos-chave
- Dados fixos e determinísticos usados como entrada dos testes.
- Arquivos em JSON, YAML, CSV ou código, versionados com o projeto.
- Garantem repetibilidade e isolamento entre execuções.
- Reaproveitados em testes unitários, de integração e E2E.
- Em frameworks como Cypress, carregados com cy.fixture.

## Exemplos
```
// fixtures/usuarios.json
{
  "valido": { "email": "qa@exemplo.com", "senha": "123456" },
  "invalido": { "email": "qa", "senha": "" }
}

// cypress/e2e/login.cy.js
cy.fixture('usuarios').then((usuarios) => {
  cy.get('[data-testid="email"]').type(usuarios.valido.email);
});
```

## Boas práticas
- Manter dados realistas e pequenos, cobrindo cada cenário.
- Agrupar fixtures por recurso ou contexto de uso.
- Versionar as fixtures junto com o código-fonte.
- Atualizar as fixtures quando o schema dos dados mudar.
- Reutilizar fixtures para montar estado inicial e asserções.

## Armadilhas comuns
- Fixtures enormes que dificultam leitura e manutenção.
- Dados irreais que não refletem o comportamento em produção.
- Duplicação entre fixtures e código, gerando divergências.
- Não atualizar após mudança de schema, quebrando testes.
- Compartilhar fixtures com credenciais ou dados pessoais.

## Relacionadas
- [[Mocks]]
- [[Test-frameworks]]
- [[Testes-Automatizados]]