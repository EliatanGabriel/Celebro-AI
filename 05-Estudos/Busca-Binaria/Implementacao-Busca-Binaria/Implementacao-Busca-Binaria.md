---
type: concept
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Busca Binária na Prática

#area/estudos #busca-binaria #conceito #algoritmos #busca #implementacao

**Resumo:** Implementação da busca binária em vetores ordenados usando ponteiros de limite e invariantes para garantir correção e complexidade O(log n).

## Conceitos-chave
- **Invariante de loop:** o alvo, se existir, está sempre dentro do intervalo corrente.
- **Meio do intervalo:** calculado como `mid = low + (high - low) // 2` para evitar overflow de inteiros.
- **Critério de parada:** o loop termina quando o intervalo fica vazio (low >= high) ou quando o elemento é encontrado.
- **Atualização dos limites:** se `arr[mid] < alvo`, descarta a metade esquerda (`low = mid + 1`); caso contrário, `high = mid`.
- **Complexidade:** O(log n) no tempo e O(1) de espaço na versão iterativa.

## Exemplos
```python
def busca_binaria(arr, alvo):
    low, high = 0, len(arr)
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] == alvo:
            return mid
        if arr[mid] < alvo:
            low = mid + 1
        else:
            high = mid
    return -1

nums = [2, 5, 8, 12, 16, 23, 38, 56]
print(busca_binaria(nums, 23))  # 5
print(busca_binaria(nums, 7))   # -1
```

Versão recursiva:

```python
def busca_recursiva(arr, alvo, low, high):
    if low >= high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == alvo:
        return mid
    if arr[mid] < alvo:
        return busca_recursiva(arr, alvo, mid + 1, high)
    return busca_recursiva(arr, alvo, low, mid)
```

## Boas práticas
- Usar `low + (high - low) // 2` em vez de `(low + high) // 2`.
- Trabalhar com intervalos semiabertos `[low, high)` para reduzir erros de off-by-one.
- Testar com vetores de tamanho 0, 1 e com o alvo nas bordas.

## Armadilhas comuns
- Overflow de `(low + high) // 2` em linguagens com inteiros de tamanho fixo.
- Loop infinito quando `mid` nunca avança, por exemplo usando `low = mid` sem o `+1`.
- Retornar índice incorreto quando os critérios de parada não acompanham o tipo de intervalo escolhido.

## Relacionadas
- [[Complexidade-Busca-Binaria]]
- [[Variacoes-Busca-Binaria]]
- [[Arrays]]