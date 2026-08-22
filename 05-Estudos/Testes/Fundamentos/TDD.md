---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# TDD (Test-Driven Development)

#area/estudos #estudos/testes #conceito

**Resumo:** Prática de escrever o teste antes do código, guiando o design por ciclos curtos de Red → Green → Refactor.

## Referência rápida

| Etapa | O que faz | Regra |
|---|---|---|
| Red | Escreve um teste que falha | Teste antes de existir código |
| Green | Escreve o mínimo para passar | Sem perfeição, só fazer passar |
| Refactor | Melhora código e teste | Verde sempre; passos pequenos |

## Exemplos

Passo a passo para uma função de FizzBuzz:

```js
// 1. RED: teste que falha (funcao ainda nao existe)
test("retorna Fizz para multiplo de 3", () => {
  expect(fizzbuzz(3)).toBe("Fizz");
});

// 2. GREEN: implementacao minima
function fizzbuzz(n) {
  return "Fizz";
}

// 3. RED de novo: proximo caso
test("retorna Buzz para multiplo de 5", () => {
  expect(fizzbuzz(5)).toBe("Buzz");
});

// GREEN + REFACTOR: generalizar e limpar duplicacao
function fizzbuzz(n) {
  if (n % 15 === 0) return "FizzBuzz";
  if (n % 3 === 0) return "Fizz";
  if (n % 5 === 0) return "Buzz";
  return String(n);
}
```

## Benefícios

- Design orientado a uso: a API nasce da chamada pelo cliente, não por suposição.
- Rede de segurança: suíte verde permite refatorar sem medo.
- Feedback imediato: bug aparece segundos depois de introduzido.
- Documentação viva: os testes mostram como usar o código.

## Quando NÃO usar

- Protótipos descartáveis onde o requisito ainda é incerto.
- UI exploratória: ajuste visual raramente cabe em assert.
- Código legado sem testes: comece com testes de caracterização, não TDD puro.

## Escolas: clássica vs mockista

| Chicago (clássico) | London (outside-in/mockista) |
|---|---|
| Estado e resultados reais | Interações verificadas com mocks |
| Começa pelo núcleo/domínio | Começa pela borda (UI/API) para fora |
| Menos acoplado à implementação | Define contratos cedo entre módulos |

## Boas práticas

- Passos minúsculos: um comportamento novo por ciclo.
- Rode os testes após cada etapa, não no fim do dia.
- Deixe o Refactor tão sagrado quanto o Green.
- Use [[Mocks-Stubs-e-Fakes]] apenas em fronteiras.

## Armadilhas comuns

- Escrever vários testes de uma vez antes de qualquer código.
- Pular o Red: teste que nunca falhou pode estar testando nada.
- Mockar demais na escola London e acoplar testes à implementação.
- Forçar TDD em protótipos e concluir que "não funciona".

## Relacionadas

- [[Testes]]
- [[Boas-Praticas-de-Testes]]
- [[Mocks-Stubs-e-Fakes]]
- [[BDD]]
- [[Jest]]
- [[Pytest]]
