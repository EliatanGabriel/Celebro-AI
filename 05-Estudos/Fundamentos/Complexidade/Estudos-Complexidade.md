---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Complexidade

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Medida de eficiência de um algoritmo em termos de tempo e espaço, expressa em notação assintótica (Big-O) conforme o tamanho da entrada cresce.

## Conceitos-chave
- **Complexidade de tempo:** número de operações fundamentais em função de `n`.
- **Complexidade de espaço:** memória extra usada pelo algoritmo (excluindo a entrada).
- **Notação Big-O:** limite superior do crescimento; O(1), O(log n), O(n), O(n log n), O(n²).
- **Crescimento:** a taxa de crescimento importa mais que constantes quando `n` é grande.
- **Melhor, pior e caso médio:** o pior caso dá garantia; o caso médio reflete o uso típico.
- **Análise de loops:** um loop sobre `n` é O(n); loops aninhados multiplicam: O(n²).
- **Análise de recursão:** o custo depende do número de chamadas e do trabalho por chamada (ex.: merge sort O(n log n)).

## Exemplos
```text
// Exemplos de complexidade de tempo
Acesso a array[i]                       → O(1)
Busca binária em lista ordenada          → O(log n)
Busca linear                            → O(n)
Merge sort / quicksort (médio)          → O(n log n)
Bubble sort / loops duplos              → O(n²)
```

```python
# Análise: loop aninhado
def pares_unicos(vetor):        # O(n²)
    for i in range(len(vetor)):
        for j in range(i + 1, len(vetor)):
            print(vetor[i], vetor[j])

# Recursão: exemplo de complexidade
def fib(n):                      # O(2^n) sem memoização
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

```text
// Espaço
Ordenação in-place (quick sort) → O(1) espaço extra (desconsiderando stack)
Merge sort                     → O(n) espaço extra (arrays auxiliares)
```

## Boas práticas
- Analisar o pior caso primeiro e depois avaliar o caso médio relevante.
- Contar as operações dominantes e ignorar constantes e termos menores.
- Avaliar também a complexidade de espaço, não só de tempo.
- Identificar o gargalo do algoritmo (o termo de maior crescimento).
- Medir com benchmarks para confirmar a análise teórica em dados reais.

## Armadilhas comuns
- Analisar só o melhor caso e ter surpresas em produção.
- Esquecer que chamadas de função dentro de loops somam/multiplicam a complexidade.
- Confundir O(log n) com O(n log n).
- Ignorar a complexidade de espaço, que pode ser o fator limitante.
- Achar que "n pequeno roda rápido" justifica algoritmo O(n²) — o crescimento domina conforme a entrada cresce.

## Relacionadas
- [[Big-O]]
- [[Algoritmos]]
- [[Estruturas-de-Dados]]
- [[Estudos-Ordenacao]]
- [[Estudos-Recursao]]
- [[Performance]]
- [[Arvores]]
- [[Grafos]]