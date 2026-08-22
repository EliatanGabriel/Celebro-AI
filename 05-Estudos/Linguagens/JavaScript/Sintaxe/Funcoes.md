---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Funções em JavaScript

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Funções em JavaScript são valores de primeira classe e podem ser declaradas, expressas ou arrow functions, com parâmetros default, rest e closures.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `function nome() {}` | Declaração de função (sofre hoisting) | `function somar(a, b) { return a + b; }` |
| `const f = function () {}` | Expressão de função (sem hoisting) | `const dobrar = function (n) {...};` |
| `const f = () => {}` | Arrow function, corpo curto com retorno implícito | `const dobro = n => n * 2;` |
| `(a, b) => ({ a })` | Arrow que retorna objeto exige parênteses | `const novo = id => ({ id });` |
| `param = valor` | Parâmetro padrão quando o argumento é undefined | `function log(msg = "ok") {}` |
| `(...args)` | Rest: agrupa argumentos num array | `function total(...valores) {}` |
| `this` em arrow | Herda o `this` de onde foi criada (léxico) | `setTimeout(() => this.salvar(), 100)` |

## Exemplos

```js
// Declaração, arrow e parâmetros default
function saudar(nome, cumprimento = "Olá") {
  return `${cumprimento}, ${nome}!`;
}

const aoQuadrado = n => n ** 2;
const somarTudo = (...nums) => nums.reduce((a, b) => a + b, 0);

console.log(saudar("Ana"));            // Olá, Ana!
console.log(somarTudo(1, 2, 3));       // 6
```

```js
// Callback e closure: a função interna lembra o escopo externo
function criarContador() {
  let contador = 0;                    // vive apenas dentro da closure
  return () => ++contador;
}

const proximo = criarContador();
proximo(); // 1
proximo(); // 2

document.querySelector("#btn").addEventListener("click", () => {
  console.log(this);                   // this léxico: o mesmo do escopo externo
});
```

## Boas práticas

- Uma função deve fazer uma coisa só; se precisa de "e" no nome, divida.
- Prefira arrow functions para callbacks curtos e métodos utilitários.
- Use `function` declarada quando quiser hoisting ou `this` dinâmico.
- Sempre retorne um valor explícito em funções não triviais.
- Limite parâmetros: mais de 3, considere receber um objeto.
- Nomeie funções com verbos no infinitivo: `calcularTotal`, `validarEmail`.

## Armadilhas comuns

- Arrow functions não têm `this` próprio nem `arguments`.
- Retornar objeto literal em arrow sem parênteses dá erro: `() => {}` é bloco vazio.
- Esquecer o `return` faz a função devolver `undefined`.
- Parâmetros default só ativam com `undefined`, não com `null` ou `""`.
- Closures seguram referências na memória: cuidado em loops longos.

## Relacionadas

- [[Arrays-e-Metodos]]
- [[Async-Promises-Fetch]]
- [[JavaScript]]
