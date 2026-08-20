---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Big-O

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Notação matemática que descreve o limite superior assintótico do crescimento de uma função, usada para comparar a eficiência de algoritmos conforme a entrada cresce.

## Conceitos-chave
- **Crescimento assintótico:** comportamento quando o tamanho da entrada `n` tende ao infinito; constantes e termos menores são ignorados.
- **O(1):** tempo constante, independe de `n` (acesso a array, operações aritméticas simples).
- **O(log n):** crescimento logarítmico, típico de busca binária e árvores balanceadas.
- **O(n):** crescimento linear, percorrer uma estrutura uma vez.
- **O(n log n):** típico de ordenações eficientes como merge sort e quick sort.
- **O(n²):** crescimento quadrático, comum em loops aninhados e ordenações simples.
- **Pior caso:** Big-O normalmente descreve o pior cenário de execução, dando uma garantia de limite superior.

## Exemplos
```text
// O(1)
acessar array[indice]

// O(log n) — busca binária
enquanto (inicio <= fim):
    meio = (inicio + fim) / 2
    se vetor[meio] == alvo: retorne meio
    senão se vetor[meio] < alvo: inicio = meio + 1
    senão: fim = meio - 1

// O(n) — percorrer uma lista
para cada elemento em lista:
    processar(elemento)

// O(n²) — loops aninhados
para i em 0..n:
    para j em 0..n:
        comparar(i, j)
```

## Boas práticas
- Analisar primeiro o pior caso e depois verificar se o caso médio é relevante.
- Focar no termo dominante, ignorando constantes (2n é O(n)).
- Considerar a complexidade de espaço além da de tempo.
- Escolher o algoritmo pela taxa de crescimento, não por benchmarks em entradas pequenas.

## Armadilhas comuns
- Confundir O(log n) com O(n log n).
- Ignorar chamadas a funções dentro de loops: uma função O(n) dentro de um loop O(n) resulta em O(n²).
- Assumir que menor tempo em uma execução significa melhor algoritmo; medir várias execuções.
- Esquecer que o Big-O descreve assíntota: para entradas pequenas, um algoritmo O(n²) pode ser mais rápido que um O(n log n).
- Usar Big-O para prever tempo em segundos — ele mede crescimento, não tempo absoluto.

## Relacionadas
- [[Algoritmos]]
- [[Estudos-Complexidade]]
- [[Busca-Binaria]]
- [[Estruturas-de-Dados]]
- [[Performance]]