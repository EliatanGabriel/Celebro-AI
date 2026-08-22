---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Operadores em JavaScript

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** JavaScript oferece operadores aritméticos, de atribuição composta, comparação estrita, lógicos com short-circuit, nullish coalescing, ternário e spread/rest.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `+ - * / % **` | Aritméticos (resto e potência) | `2 ** 3  // 8` |
| `+= -= *=` | Atribuição composta | `x += 5;` |
| `??=` `&&=` `\|\|=` | Atribui só se for nullish / truthy / falsy | `nome ??= "Anônimo";` |
| `===` `!==` | Comparação estrita (valor + tipo) | `1 === "1"  // false` |
| `==` `!=` | Comparação com coerção (evite) | `"5" == 5  // true` |
| `&& \|\| !` | E, OU lógico com short-circuit | `ativo && salvar();` |
| `??` | Retorna o lado direito se o esquerdo for null/undefined | `porta ?? 8080;` |
| `cond ? a : b` | Operador ternário | `idade >= 18 ? "ok" : "não";` |
| `...` | Spread (expandir) ou rest (agrupar) | `[...arr]`, `function f(...args)` |

## Exemplos

```js
// Comparação estrita vs coerção e operador nullish
console.log(5 === "5");   // false
console.log(5 == "5");    // true  (coerção)

const porta = 0;
const config = porta ?? 3000;   // 0 (só pega fallback em null/undefined)
const nome = "" || "Anônimo";   // "Anônimo" ("") é falsy
```

```js
// Short-circuit, ternário e spread/rest
const usuario = { nome: "Ana", tags: ["js"] };
usuario.ativo && console.log("logado!");        // não executa
const status = usuario.ativo ? "on" : "off";

const copia = [...usuario.tags, "web"];          // spread
function somar(...nums) {                        // rest
  return nums.reduce((a, b) => a + b, 0);
}
somar(1, 2, 3); // 6
```

## Boas práticas

- Use sempre `===` e `!==`; reserve `==` para comparar com `null` conscientemente.
- Prefira `??` quando `0` ou `""` forem valores válidos, não ausência.
- Use `&&` para executar algo condicionalmente sem bloco `if`.
- Copie arrays/objetos com spread antes de ordenar ou modificar.
- Nomeie condições complexas em variáveis booleanas antes do ternário.
- Evite encadear muitos ternários: vira código ilegível.

## Armadilhas comuns

- `||` trata `0` e `""` como falsy e pode descartar valores válidos.
- `NaN === NaN` é `false`: use `Number.isNaN()` para detectar NaN.
- `"3" * 4` dá `12`, mas `"3" + 4` dá `"34"`: o `+` tem comportamento duplo.
- Spread copia raso: objetos aninhados continuam compartilhando referência.
- `x ??= y` não roda se `x` for qualquer valor não-nullish, mesmo `false`.

## Relacionadas

- [[Variaveis-e-Tipos]]
- [[Controle-de-Fluxo]]
- [[JavaScript]]
