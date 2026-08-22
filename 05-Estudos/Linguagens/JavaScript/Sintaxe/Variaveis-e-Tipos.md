---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Variáveis e Tipos em JavaScript

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Em JavaScript `let` e `const` declaram variáveis de escopo de bloco, os tipos são dinâmicos e a coerção implícita exige atenção em comparações.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `let x` | Variável mutável com escopo de bloco | `let x = 10;` |
| `const PI` | Constante: não pode ser reatribuída | `const PI = 3.14;` |
| `var x` | Escopo de função (evite) | `var antigo = true;` |
| `typeof v` | Retorna o tipo como string | `typeof "oi"  // "string"` |
| `Number(v)` | Converte para número | `Number("42")  // 42` |
| `String(v)` | Converte para string | `String(99)  // "99"` |
| `Boolean(v)` | Converte para booleano | `Boolean("")  // false` |
| `` `texto ${x}` `` | Template literal com interpolação | `` `Olá, ${nome}!` `` |
| `null` / `undefined` | Ausência intencional / valor não atribuído | `let n = null;` |

## Exemplos

```js
// let, const e tipos primitivos
let nome = "Ana";        // string
let idade = 25;          // number
let ativo = true;        // boolean
let salario = null;      // null (ausência intencional)
let telefone;            // undefined (nunca atribuído)

console.log(typeof nome);   // "string"
console.log(typeof idade);  // "number"
```

```js
// Conversões explícitas e template literals
const entrada = "150";
const total = Number(entrada) + 50;          // 200
const mensagem = `${nome} tem ${idade} anos`;

console.log(String(true), Boolean("texto")); // "true" true
```

## Boas práticas

- Use `const` por padrão; troque para `let` só quando precisar reatribuir.
- Nunca use `var`: seu escopo de função causa bugs difíceis de rastrear.
- Prefira conversões explícitas (`Number()`, `String()`) à coerção automática.
- Use template literals em vez de concatenar strings com `+`.
- Diferencie `null` (vazio proposital) de `undefined` (não inicializado).
- Nomeie variáveis em `camelCase`: `totalVendas`, `usuarioLogado`.

## Armadilhas comuns

- `typeof null` retorna `"object"`: bug histórico da linguagem.
- `"5" + 2` dá `"52"` mas `"5" - 2` dá `3`: o `+` concatena quando há string.
- Comparar com `==` converte tipos: `"0" == 0` é `true`; prefira `===`.
- `const obj = {}` permite alterar propriedades; o que trava é a reatribuição.
- Esquecer de inicializar gera `undefined` e quebra operações posteriores.

## Relacionadas

- [[Operadores]]
- [[Controle-de-Fluxo]]
- [[JavaScript]]
