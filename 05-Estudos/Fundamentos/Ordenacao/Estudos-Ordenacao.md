---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Ordenacao

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Algoritmos que reorganizam elementos em ordem crescente ou decrescente, com diferentes trade-offs de tempo, espaço e estabilidade.

## Conceitos-chave
- **Bubble sort:** compara pares adjacentes e troca quando estão fora de ordem; O(n²), simples de entender, ineficiente em grande escala.
- **Insertion sort:** constrói a ordem inserindo cada elemento na posição correta; O(n²) no pior caso, O(n) em listas quase ordenadas.
- **Selection sort:** seleciona o menor a cada passo e coloca na posição; O(n²) sempre, in-place, instável.
- **Merge sort:** divide e conquista; O(n log n) garantido, estável, mas usa O(n) de espaço extra.
- **Quick sort:** particiona em torno de um pivô; O(n log n) médio, O(n²) no pior caso, in-place.
- **Estabilidade:** um algoritmo estável preserva a ordem relativa de elementos iguais — importante em ordenações múltiplas.
- **Ordenação in-place:** usa espaço extra constante; relevante para memória.

## Exemplos
```python
# Bubble sort — O(n²)
def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
    return vetor
```

```python
# Merge sort — O(n log n), estável
def merge_sort(vetor):
    if len(vetor) <= 1:
        return vetor
    meio = len(vetor) // 2
    esq = merge_sort(vetor[:meio])
    dir = merge_sort(vetor[meio:])
    return intercalar(esq, dir)
```

```text
// Resumo comparativo
             Pior caso   Melhor caso   Espaço extra   Estável
Bubble sort  O(n²)       O(n)          O(1)           sim
Insertion    O(n²)       O(n)          O(1)           sim
Selection    O(n²)       O(n²)         O(1)           não
Merge sort   O(n log n)  O(n log n)    O(n)           sim
Quick sort   O(n²)       O(n log n)    O(log n)       não
```

## Boas práticas
- Usar a ordenação nativa da linguagem (`sort` em Python/JS, que costuma ser introspective/TimSort) quando não há requisito especial.
- Escolher stable sort quando a ordem relativa de iguais importa.
- Preferir quick sort in-place em vetores grandes com memória limitada.
- Analisar se o problema realmente exige ordenação (ex.: heap pode ser suficiente).
- Para dados quase ordenados, insertion sort é surpreendentemente eficiente.

## Armadilhas comuns
- Usar bubble/selection sort em dados grandes por "simplicidade", sofrendo com O(n²).
- Assumir estabilidade em quick sort ou selection sort.
- Esquecer que o pior caso do quick sort é O(n²) (pivô ruim, ex.: lista já ordenada).
- Comparar strings/objetos sem critério definido, gerando ordenação inesperada.
- Ignorar o espaço extra de merge sort ao ordenar estruturas grandes.

## Relacionadas
- [[Algoritmos]]
- [[Estudos-Complexidade]]
- [[Big-O]]
- [[Arrays]]
- [[Listas]]
- [[Estudos-Recursao]]
- [[Estudos-Funcoes]]
- [[Estruturas-de-Dados]]