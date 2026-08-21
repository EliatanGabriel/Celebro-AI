---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Test-frameworks

#area/trabalho #trabalho/testes-automatizados #conceito

**Resumo:** Bases que fornecem estrutura, asserções e execução de testes.

## Conceitos-chave
- Infraestrutura para escrever, executar e reportar testes.
- Runner: descobre, executa e coleta resultados dos testes.
- Biblioteca de asserções: expect, assert, should.
- Estrutura com describe/it/test e hooks de ciclo de vida (beforeEach, afterAll).
- Exemplos: Jest, Vitest, Mocha, Jasmine, JUnit, pytest, NUnit.

## Exemplos
```
// npm script
"scripts": { "test": "vitest run" }

// teste básico
describe('Calculadora', () => {
  beforeEach(() => {
    calc = new Calculadora();
  });

  it('soma números', () => {
    expect(calc.somar(1, 2)).toBe(3);
  });
});
```

## Boas práticas
- Adotar o framework padrão do ecossistema do projeto (Jest/Vitest no JS, JUnit no Java).
- Padronizar nomes de arquivos e a estrutura de pastas de testes.
- Usar hooks para setup e teardown, evitando repetição.
- Configurar cobertura e reporters conforme a necessidade do time.
- Integrar a execução ao pipeline de CI.

## Armadilhas comuns
- Misturar frameworks concorrentes no mesmo projeto.
- Testes dependentes da ordem de execução ou de estado global.
- Configurar cobertura de forma incorreta (medindo arquivos errados).
- Ignorar hooks de limpeza e deixar estado vazando.
- Não padronizar, criando padrões divergentes entre times.

## Relacionadas
- [[Unit-testing]]
- [[Mocks]]
- [[Cypress]]