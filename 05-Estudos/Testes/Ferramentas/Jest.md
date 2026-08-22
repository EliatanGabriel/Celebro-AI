---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# Jest

#area/estudos #estudos/testes #ferramenta

**Resumo:** Framework de testes para JavaScript e TypeScript com runner, assertions, mocks e cobertura integrados em um único pacote.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `describe` | Agrupa testes relacionados | `describe("Carrinho", () => {})` |
| `it` / `test` | Define um caso de teste | `it("soma itens", () => {})` |
| `expect().toBe` | Igualdade primitiva/referência | `expect(x).toBe(10)` |
| `expect().toEqual` | Igualdade estrutural profunda | `expect(obj).toEqual({ a: 1 })` |
| `expect().toThrow` | Verifica exceção lançada | `expect(fn).toThrow("inválido")` |
| `toBeTruthy` | Valor truthy | `expect(res).toBeTruthy()` |
| `toMatchObject` | Subconjunto de propriedades | `expect(o).toMatchObject({ id: 1 })` |
| `beforeEach` | Roda antes de cada teste | Resetar fixtures |
| `afterAll` | Roda uma vez ao final do bloco | Fechar conexão de DB |
| `jest.fn()` | Cria função mock | `const f = jest.fn()` |
| `--coverage` | Relatório de cobertura | `npx jest --coverage` |

## Exemplos

```js
describe("calculadora", () => {
  let calc;

  beforeEach(() => {
    calc = new Calculadora();
  });

  afterAll(() => {
    db.fechar();
  });

  it("soma dois numeros", () => {
    expect(calc.somar(2, 3)).toBe(5);
  });

  it("lanca erro ao dividir por zero", () => {
    expect(() => calc.dividir(1, 0)).toThrow();
  });
});

// Mocks
const salvar = jest.fn().mockResolvedValue({ id: 1 });
jest.mock("../services/api");

// Snapshot
expect(componente.toJSON()).toMatchSnapshot();
```

## Comandos úteis

```bash
npx jest                 # roda toda a suite
npx jest --watch         # watch mode: retesta arquivos alterados
npx jest --coverage      # relatorio de cobertura
npx jest usuario.test.js # roda arquivo especifico
```

## Boas práticas

- Um comportamento por `it`, com nomes descritivos.
- Use `toBe` para primitivos e `toEqual` para objetos.
- Limpe mocks entre testes (`clearMocks: true` no config).
- Prefira testes de comportamento a snapshots gigantes.

## Armadilhas comuns

- Snapshot demais: ninguém revisa e tudo vira "update all".
- Esquecer de aguardar promises: use `async/await` no teste.
- Mockar módulos internos e acoplar à implementação.
- `toBe` em objetos: compara referência, não conteúdo.

## Relacionadas

- [[Testes]]
- [[Vitest]]
- [[Testing-Library]]
- [[Mocks-Stubs-e-Fakes]]
- [[Boas-Praticas-de-Testes]]
- [[Cobertura-de-Codigo]]
