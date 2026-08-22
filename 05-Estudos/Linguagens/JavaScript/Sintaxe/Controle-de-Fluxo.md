---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Controle de Fluxo em JavaScript

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** O fluxo de um programa em JavaScript é decidido por `if/else`, `switch`, ternário e valores truthy/falsy, com optional chaining para acessos seguros.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `if (cond) {}` | Executa bloco se a condição for truthy | `if (idade >= 18) {}` |
| `else if` / `else` | Caminhos alternativos encadeados | `else if (x > 0) {} else {}` |
| `switch (v)` | Compara valor exato com cada `case` | `case 1: ... break;` |
| `break` | Sai do switch (sem ele cai pro próximo case) | `break;` |
| `cond ? a : b` | Ternário: expressão condicional curta | `n > 0 ? "+" : "-"` |
| `obj?.prop` | Encadeamento opcional: evita erro se obj é null | `user?.email` |
| `arr?.[i]` / `fn?.()` | Acesso opcional por índice ou chamada | `lista?.[0]?.id` |

## Exemplos

```js
// if/else if/else e truthy/falsy
const senha = "";

if (!senha) {
  console.log("Senha obrigatória");     // "" é falsy
} else if (senha.length < 6) {
  console.log("Senha muito curta");
} else {
  console.log("Senha válida");
}

// Falsy: false, 0, "", null, undefined, NaN
// Truthy: todo o resto, inclusive [] e {}
```

```js
// switch com break e ternário
function diaUtil(dia) {
  switch (dia) {
    case "sábado":
    case "domingo":
      return "folga";        // cases agrupados
    default:
      return "dia útil";
  }
}

const acesso = dia?.toLowerCase?.() === "sabado" ? "livre" : "restrito";
```

## Boas práticas

- Sempre coloque `default` no switch para cobrir casos inesperados.
- Prefira `===`; o `==` dentro de condições gera coerções surpresas.
- Use `?.` ao acessar dados que podem vir nulos (API, input do usuário).
- Extraia condições longas para variáveis booleanas bem nomeadas.
- Ternário só para escolhas simples; use `if` quando houver efeitos.
- Agrupe cases iguais empilhando-os sem código entre eles.

## Armadilhas comuns

- Esquecer o `break` no switch faz a execução "vazar" para os próximos cases.
- `0` e `""` são falsy: `if (quantidade)` falha silenciosamente para zero.
- `typeof x === "undefined"` é necessário se `x` pode nem ter sido declarado.
- Optional chaining não funciona em atribuições: `obj?.prop = 1` dá erro.
- Comparar objetos com `===` compara referência, não conteúdo.

## Relacionadas

- [[Operadores]]
- [[Loops]]
- [[JavaScript]]
