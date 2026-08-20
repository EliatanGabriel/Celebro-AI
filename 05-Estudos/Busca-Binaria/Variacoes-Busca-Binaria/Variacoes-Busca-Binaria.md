---
type: concept
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Variações da Busca Binária

#area/estudos #busca-binaria #conceito #algoritmos #busca

**Resumo:** Adaptações da busca binária para encontrar o primeiro ou o último elemento igual ao alvo (lower_bound e upper_bound), além de buscas em intervalos e sobre o espaço de resposta.

## Conceitos-chave
- **Lower bound:** primeiro índice onde `arr[i] >= alvo`.
- **Upper bound:** primeiro índice onde `arr[i] > alvo`.
- **Contagem de ocorrências:** `upper_bound - lower_bound` conta quantas vezes um valor aparece em O(log n).
- **Busca em resposta (binary search on answer):** busca o maior/menor valor que satisfaz uma condição monotônica.
- **Busca em intervalo:** verifica se existe elemento dentro de [a, b] combinando lower_bound e upper_bound.

## Exemplos
```python
def lower_bound(arr, alvo):
    low, high = 0, len(arr)
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < alvo:
            low = mid + 1
        else:
            high = mid
    return low

def upper_bound(arr, alvo):
    low, high = 0, len(arr)
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] <= alvo:
            low = mid + 1
        else:
            high = mid
    return low

nums = [1, 2, 2, 2, 3, 5]
lb = lower_bound(nums, 2)   # 1
ub = upper_bound(nums, 2)   # 4
print("ocorrencias:", ub - lb)  # 3
```

## Boas práticas
- Preferir funções nativas das bibliotecas padrão (`bisect` em Python, `lower_bound`/`upper_bound` no C++ STL).
- Usar busca binária na resposta apenas quando a função de avaliação for monotônica.
- Validar que a resposta está dentro do espaço de busca antes de começar.

## Armadilhas comuns
- Confundir lower_bound com upper_bound quando o valor não existe no vetor.
- Esquecer que, sem o valor presente, o lower_bound retorna `len(arr)`.
- Aplicar busca binária na resposta a problemas sem monotonicidade, produzindo respostas incorretas.

## Relacionadas
- [[Implementacao-Busca-Binaria]]
- [[Complexidade-Busca-Binaria]]
- [[Arrays]]