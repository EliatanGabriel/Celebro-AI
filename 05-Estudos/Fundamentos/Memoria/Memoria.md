---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Memoria

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Dispositivo que armazena dados e instruções para que a CPU os acesse durante a execução; o gerenciamento adequado é essencial para correção e performance.

## Conceitos-chave
- **RAM:** memória principal volátil, rápida e endereçável por byte; armazena o programa em execução e seus dados.
- **Hierarquia de memória:** registradores → cache (L1/L2/L3) → RAM → disco; cada nível é mais lento e maior.
- **Stack:** região LIFO usada para chamadas de função e variáveis locais; cresce e encolhe automaticamente.
- **Heap:** região de alocação dinâmica, controlada pelo programador ou pelo garbage collector.
- **Gerenciamento:** em C/C++ é manual (`malloc`/`free`); em linguagens com GC (Java, Go, Python) é automático.
- **Endereçamento:** cada byte tem um endereço; ponteiros e referências guardam esses endereços.
- **Vazamentos (memory leaks):** memória alocada e nunca liberada, consumindo recursos até a falha.

## Exemplos
```c
// Gerenciamento manual de memória em C
int *arr = malloc(10 * sizeof(int));   // aloca no heap
if (arr == NULL) { /* tratar erro */ }
arr[0] = 42;
free(arr);                              // libera; esquecer = vazamento
```

```go
// Garbage collector libera objetos sem referência
func criar() []int {
    v := make([]int, 1000)   // alocado no heap, rastreado pelo GC
    return v
}
```

```text
// Hierarquia: latência aproximada
Registradores:  ~1ns
Cache L1:       ~1ns
Cache L3:       ~10ns
RAM:            ~100ns
SSD:            ~100µs
```

## Boas práticas
- Parear cada alocação com sua liberação quando o gerenciamento é manual.
- Usar estruturas e coleções com espaço alocado adequadamente para reduzir realocações.
- Considerar a localidade de referência: acessar dados próximos melhora o uso de cache.
- Medir o uso de memória (profiling) quando a aplicação cresce.
- Preferir GC quando a produtividade importa; controle manual quando a previsibilidade importa.

## Armadilhas comuns
- Vazamento de memória por não liberar alocação manual (C/C++).
- Use-after-free: acessar memória já liberada, causando comportamento indefinido.
- Buffer overflow: escrever além do espaço alocado, corrompendo a memória.
- Alocar objetos grandes em loop sem reuso, pressionando o GC.
- Confundir memória física com memória virtual e assumir que sempre cabe tudo na RAM.

## Relacionadas
- [[Stack-Heap]]
- [[Ponteiros]]
- [[Performance]]
- [[Estudos-Variaveis]]
- [[Tipos-de-Dados]]
- [[Arrays]]
- [[Sistemas]]