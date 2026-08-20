---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Stack-Heap

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Duas regiões da memória do processo com finalidades diferentes: a stack gerencia chamadas de função e variáveis locais (LIFO), enquanto o heap é usado para alocação dinâmica.

## Conceitos-chave
- **Stack:** região LIFO que cresce a cada chamada de função (empilha frame com locais e endereço de retorno) e encolhe no retorno; acesso muito rápido.
- **Heap:** região de memória de alocação dinâmica, controlada pelo programador (`malloc`/`new`) ou pelo garbage collector; mais lenta e sem ordem.
- **Escopo:** variáveis locais vivem na stack e morrem ao sair do escopo; objetos alocados no heap sobrevivem até serem liberados.
- **Stack overflow:** estouro da stack por recursão sem caso base ou chamadas infinitas.
- **Garbage collector (GC):** mecanismo que identifica e libera objetos do heap sem referências (Java, Go, Python).
- **Vazamentos:** objetos no heap sem referência (com GC, removidos) ou nunca liberados (sem GC, permanecem).
- **Referências:** variáveis da stack podem guardar endereços para objetos no heap (ponteiros/referências).

## Exemplos
```c
void funcao(int n) {
    int local = n;              // na stack, morre ao retornar
    int *obj = malloc(8);       // no heap, vive até free()
    *obj = local;
    free(obj);                  // libera manualmente
}

// Chamada em cadeia empilha frames na stack:
// main() → funcaoA() → funcaoB()
// Ao retornar de funcaoB, seu frame é removido (LIFO)
```

```go
func criar() *Item {
    i := &Item{Valor: 1}   // alocado no heap (escape), rastreado pelo GC
    return i               // sobrevive ao retorno da função
}
```

```text
// Resumo comparativo
             Stack              Heap
Ordem        LIFO               livre/dinâmica
Velocidade   muito rápida       mais lenta
Gerenciamento automático        manual ou GC
Tamanho      limitado, fixo     grande, até memória disponível
Risco comum   stack overflow     vazamento / fragmentação
```

## Boas práticas
- Preferir alocação na stack (valores) quando o tamanho é conhecido e o escopo é curto.
- Liberar objetos do heap (ou garantir referência para o GC) para evitar vazamentos.
- Evitar recursão muito profunda, que esgota a stack.
- Entender o custo de cópia vs. referência ao passar dados entre funções.

## Armadilhas comuns
- Recursão sem caso base causando stack overflow.
- Esquecer `free`/`delete` (vazamento) ou liberar duas vezes (double free) em C/C++.
- Retornar referência/ponteiro para variável local da stack (uso após o escopo).
- Confundir a stack de memória com a estrutura de dados "pilha".
- Assumir que objetos do heap são limpos automaticamente em linguagens sem GC.

## Relacionadas
- [[Memoria]]
- [[Ponteiros]]
- [[Estudos-Recursao]]
- [[Estudos-Variaveis]]
- [[Pilhas]]
- [[Performance]]
- [[Sistemas]]