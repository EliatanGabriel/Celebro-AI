---
type: concept
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Complexidade da Busca Binária

#area/estudos #busca-binaria #conceito #algoritmos #complexidade

**Resumo:** A busca binária reduz o espaço de busca pela metade a cada iteração, resultando em tempo O(log n) em um vetor de n elementos, desde que o vetor esteja ordenado.

## Conceitos-chave
- **Dividir e conquistar:** a cada passo o intervalo é dividido ao meio e apenas uma das metades é explorada.
- **Logaritmo na base 2:** com n elementos são necessárias no máximo ⌊log₂ n⌋ + 1 comparações.
- **Comparação com busca linear:** a busca linear é O(n); em um array de 1 milhão de elementos ela faz até 1.000.000 de comparações, a binária cerca de 20.
- **Custo por passo:** cada comparação é O(1), portanto o custo total é O(log n).
- **Memória:** espaço auxiliar O(1) na versão iterativa; a recursiva usa O(log n) de pilha de chamadas.

## Exemplos
```python
import math

n = 1_000_000
passos = math.ceil(math.log2(n)) + 1
print(passos)  # 20 comparações no pior caso
```

| Tamanho n | Busca linear | Busca binária |
|-----------|--------------|---------------|
| 1.000     | 1.000        | 10            |
| 1.000.000 | 1.000.000    | 20            |
| 1.000.000.000 | 1e9      | 30            |

## Boas práticas
- Confirmar que o vetor está ordenado antes de aplicar a busca binária.
- Preferir a versão iterativa para evitar estouro da pilha em entradas grandes.
- Tratar explicitamente o caso de vetor vazio.

## Armadilhas comuns
- Aplicar busca binária em dados não ordenados produz resultado indefinido.
- Pensar que a base do logaritmo importa: na notação Big-O, log₂ n e log₁₀ n são equivalentes.
- Esquecer que apenas a busca é O(log n); a ordenação prévia do vetor custa O(n log n).

## Relacionadas
- [[Implementacao-Busca-Binaria]]
- [[Variacoes-Busca-Binaria]]
- [[Big-O]]
- [[Estudos-Complexidade]]