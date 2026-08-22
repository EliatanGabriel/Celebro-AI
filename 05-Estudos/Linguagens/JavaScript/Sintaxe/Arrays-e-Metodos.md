---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Arrays e Métodos em JavaScript

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Arrays em JavaScript são dinâmicos e vêm com métodos poderosos para adicionar, remover, transformar, filtrar, buscar e agregar dados.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `push` / `pop` | Adiciona no fim / remove do fim | `arr.push(4); arr.pop();` |
| `unshift` / `shift` | Adiciona no início / remove do início | `arr.unshift(0); arr.shift();` |
| `splice(i, n, ...itens)` | Remove/substitui/insere (altera o array) | `arr.splice(1, 1, "novo");` |
| `slice(a, b)` | Copia um trecho sem alterar o original | `arr.slice(0, 2);` |
| `map(fn)` | Transforma cada item e retorna novo array | `nums.map(n => n * 2);` |
| `filter(fn)` | Retorna só os itens que passam no teste | `nums.filter(n => n > 0);` |
| `reduce(fn, inicial)` | Reduz o array a um único valor | `nums.reduce((a, b) => a + b, 0);` |
| `find` / `some` / `every` | Primeiro que passa / algum / todos | `users.find(u => u.id === 3);` |
| `[...arr].sort()` | Ordena cópia (sort altera o original!) | `[...nomes].sort();` |
| `includes` / `indexOf` | Verifica existência / posição | `arr.includes("uva");` |
| `join(sep)` / `flat()` | Junta em string / achata níveis | `arr.join(", "); arr.flat();` |

## Exemplos

```js
// map/filter/reduce encadeados
const vendas = [120, 340, 90, 500];

const total = vendas
  .filter(v => v > 100)
  .map(v => v * 0.9)               // desconto de 10%
  .reduce((soma, v) => soma + v, 0);

console.log(total); // 864
```

```js
// splice/slice e sort seguro
const tarefas = ["estudar", "treinar", "dormir"];
tarefas.splice(1, 1, "ler");       // substitui "treinar"

const ordenadas = [...tarefas].sort();   // copia antes!
console.log(tarefas.length, ordenadas);

[10, 9, 100].sort();                        // [10, 100, 9] ordem de string!
[10, 9, 100].sort((a, b) => a - b);         // [9, 10, 100] numérica
```

## Boas práticas

- Prefira os métodos imutáveis (`map`, `filter`, `slice`) aos mutadores.
- Sempre copie com spread antes de usar `sort`, `reverse` ou `splice`.
- Passe comparador `(a, b) => a - b` ao ordenar números.
- Use `find` em vez de `filter(...)[0]` quando quer apenas um item.
- Nomeie callbacks com arrow curta; extraia funções maiores.
- Use `reduce` para totais e agrupamentos, não para tudo.

## Armadilhas comuns

- `sort()` sem comparador ordena como strings: `100` vem antes de `9`.
- `splice` altera o array original; `slice` não — confundir causa bugs.
- `indexOf` retorna `-1` quando não encontra; `includes` é mais claro.
- `map` usado só por efeito colateral deve ser `forEach`.
- Comparar arrays com `===` compara referência, mesmo com conteúdo igual.

## Relacionadas

- [[Funcoes]]
- [[Objetos-e-Destructuring]]
- [[JavaScript]]
