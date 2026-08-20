---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Arrays

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Estrutura de dados de tamanho fixo que armazena elementos do mesmo tipo em posições contíguas de memória, acessados por índice.

## Conceitos-chave
- **Índice:** posição do elemento, geralmente começando em 0; o acesso é direto e em O(1).
- **Contiguidade:** elementos ficam em endereços de memória sequenciais, o que favorece a localidade de cache.
- **Homogeneidade:** normalmente todos os elementos têm o mesmo tipo e tamanho fixo em memória.
- **Tamanho fixo:** em linguagens de baixo nível (C), o tamanho é definido na criação; linguagens como JavaScript e Python oferecem arrays dinâmicos.
- **Custo das operações:** acesso O(1), inserção/remoção no meio O(n) por deslocar elementos, inserção no fim O(1) amortizado (arrays dinâmicos).
- **Iteração:** percorrer por índice ou por `for...of`/`foreach`, preservando a ordem.

## Exemplos
```c
int nums[5] = {10, 20, 30, 40, 50};
printf("%d\n", nums[2]);   // 30, acesso O(1)
nums[2] = 99;              // atribuição direta por índice
```

```javascript
const frutas = ['maca', 'banana', 'uva'];
console.log(frutas[0]);           // 'maca'
frutas.push('laranja');           // insere no fim (O(1) amortizado)
frutas.splice(1, 1);              // remove 'banana' (O(n))
```

## Boas práticas
- Preferir arrays quando o acesso aleatório por índice é frequente e o tamanho é estável.
- Percorrer com `for...of` ou métodos como `map`/`filter` em vez de loops manuais quando possível.
- Cuidar com índices fora do intervalo, sempre validar antes de acessar.
- Usar tamanho fixo quando a quantidade de elementos é conhecida, evitando realocações desnecessárias.

## Armadilhas comuns
- Acessar `array[length]` ou índice negativo, causando erros de memória ou `undefined`.
- Confundir índice com posição: `array.length` é o número de elementos, o último índice é `length - 1`.
- Assumir que arrays em todas as linguagens são de tamanho fixo.
- Esquecer que inserir/remover no início ou meio desloca todos os elementos seguintes (O(n)).
- Comparar arrays com `==`/`===` por valor; em muitas linguagens isso compara referências.

## Relacionadas
- [[Listas]]
- [[Estruturas-de-Dados]]
- [[Algoritmos]]
- [[Estudos-Variaveis]]
- [[Tipos-de-Dados]]
- [[Memoria]]