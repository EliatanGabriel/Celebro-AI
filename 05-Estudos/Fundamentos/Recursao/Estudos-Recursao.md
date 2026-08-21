---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Recursao

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Técnica em que uma função chama a si mesma para resolver um problema, reduzindo-o a versões menores de si mesmo, com um caso base que encerra a recursão.

## Conceitos-chave
- **Caso base:** condição que encerra a recursão; sem ele, a função chama-se infinitamente e estoura a pilha.
- **Caso recursivo:** passo que reduz o problema e faz a chamada a si mesma com entrada menor.
- **Pilha de chamadas:** cada chamada empilha um frame na stack; ao retornar, o frame é desempilhado.
- **Dividir e conquistar:** quebrar o problema em subproblemas, resolver e combinar (merge sort, quicksort, busca binária).
- **Backtracking:** exploração de soluções parciais com desfazimento (tentar, voltar, tentar outro caminho).
- **Recursão de cauda (tail recursion):** a chamada recursiva é a última operação; permite otimização em algumas linguagens.
- **Memoização:** guardar resultados já calculados para evitar recomputação (ex.: Fibonacci).

## Exemplos
```python
# Fatorial — caso base + caso recursivo
def fatorial(n):
    if n <= 1:
        return 1                    # caso base
    return n * fatorial(n - 1)      # caso recursivo

# Fibonacci — sem memoização é O(2^n)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# Fibonacci com memoização — O(n)
from functools import lru_cache
@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)
```

```text
// Percurso recursivo de árvore (em-ordem)
funcao percorrer(no):
    se no é nulo: retorne          // caso base
    percorrer(no.esquerda)         // subproblema menor
    processar(no.valor)
    percorrer(no.direita)
```

## Boas práticas
- Garantir que o caso base sempre será alcançado (entrada diminui a cada chamada).
- Preferir recursão para problemas naturalmente recursivos (árvores, divisão e conquista).
- Usar memoização quando houver recomputação de subproblemas repetidos.
- Considerar a profundidade: recursão muito profunda estoura a stack; loops ou iteração podem ser necessários.
- Testar os casos de borda (entrada zero, vazia, negativa).

## Armadilhas comuns
- Esquecer o caso base, causando recursion infinita e stack overflow.
- Caso base inalcançável porque a entrada não diminui corretamente.
- Recomputar os mesmos subproblemas (Fibonacci ingênuo é O(2^n)).
- Confiar em tail-call optimization em linguagens que não a implementam (Python não otimiza por padrão).
- Tentar recursão em problemas com profundidade enorme, esgotando a stack de memória.

## Relacionadas
- [[Estudos-Funcoes]]
- [[Algoritmos]]
- [[Stack-Heap]]
- [[Estudos-Complexidade]]
- [[Arvores]]
- [[Grafos]]
- [[Estudos-Ordenacao]]
- [[Pilhas]]