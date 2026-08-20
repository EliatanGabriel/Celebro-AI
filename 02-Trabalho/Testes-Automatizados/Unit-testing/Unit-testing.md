---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Unit-testing

#area/trabalho #trabalho/testes-automatizados #conceito

**Resumo:** Testes de unidades isoladas de código (funções, classes).

## Conceitos-chave
- Testam a menor unidade de código de forma isolada: funções, classes, métodos.
- Asserções diretas sobre entradas e saídas esperadas.
- Execução rápida, permitindo rodar a cada salvamento (watch mode).
- Base de testes com Jest, Vitest, Mocha, JUnit, pytest.
- Dependências externas são substituídas por mocks/stubs.

## Exemplos
```
// calculadora.js
export function soma(a, b) {
  return a + b;
}

// calculadora.test.js
import { soma } from './calculadora';

test('soma 2 + 3', () => {
  expect(soma(2, 3)).toBe(5);
});
```

## Boas práticas
- Testar comportamento e contrato, não detalhes internos de implementação.
- Nomear testes descrevendo o cenário e o resultado esperado.
- Manter cada teste independente e determinístico.
- Cobrir casos de borda: vazio, nulo, negativo, limite.
- Rodar rápido e com frequência no fluxo de desenvolvimento.

## Armadilhas comuns
- Mockar tudo e acabar testando o próprio mock.
- Acoplar o teste a nomes internos, quebrando a cada refatoração.
- Tratar cobertura como meta cega, sem avaliar casos relevantes.
- Testes com estado global compartilhado (variáveis, timers).
- Não atualizar testes quando o comportamento muda de propósito.

## Relacionadas
- [[Mocks]]
- [[Integration-testing]]
- [[Test-frameworks]]