---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Loops em JavaScript

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** JavaScript repete tarefas com `for` clássico, `for...of` (valores), `for...in` (chaves), `while`, `do...while`, além de `break`/`continue` e o método `forEach`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `for (i; cond; passo)` | Loop com contador | `for (let i = 0; i < n; i++) {}` |
| `for (const v of arr)` | Itera valores de iteráveis (array, string) | `for (const item of lista) {}` |
| `for (const k in obj)` | Itera chaves enumeráveis de objeto | `for (const chave in obj) {}` |
| `while (cond)` | Repete enquanto a condição for verdadeira | `while (saldo > 0) {}` |
| `do {} while (cond)` | Executa ao menos uma vez antes de testar | `do { ... } while (x < 10);` |
| `break` / `continue` | Interrompe o loop / pula para a próxima volta | `if (x === alvo) break;` |
| `arr.forEach(fn)` | Executa callback para cada item (sem retorno) | `arr.forEach((v, i) => ...)` |

## Exemplos

```js
// for clássico e for...of vs for...in
const frutas = ["maçã", "uva", "pera"];

for (let i = 0; i < frutas.length; i++) {
  console.log(i, frutas[i]);
}

for (const fruta of frutas) console.log(fruta);   // valores

const precos = { uva: 8, pera: 5 };
for (const chave in precos) {
  console.log(chave, precos[chave]);              // chaves do objeto
}
```

```js
// while, break/continue e forEach
let tentativas = 0;
while (true) {
  tentativas++;
  if (tentativas >= 3) break;       // sai do loop
}

for (const n of [1, 2, 3, 4]) {
  if (n % 2 !== 0) continue;        // pula ímpares
  console.log(n);                   // 2, 4
}

frutas.forEach((fruta, indice) => console.log(indice + 1, fruta));
```

## Boas práticas

- Prefira `for...of` para percorrer arrays: mais legível que o índice manual.
- Use `for...in` apenas para objetos simples, nunca para arrays.
- Prefira `map`/`filter`/`reduce` quando precisar transformar o resultado.
- Sempre declare o contador com `let` dentro do `for`.
- Use `forEach` quando não houver necessidade de interromper a iteração.

## Armadilhas comuns

- `for...in` sobre array entrega índices como strings e inclui propriedades extras.
- `continue` dentro de `forEach` não existe: use `return` no callback.
- Loop infinito se a condição nunca virar falsa (esquecer de incrementar).
- `do...while` executa pelo menos uma vez mesmo com condição falsa.
- Modificar o array enquanto itera com `forEach` causa comportamento imprevisível.

## Relacionadas

- [[Arrays-e-Metodos]]
- [[Controle-de-Fluxo]]
- [[JavaScript]]
