---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# C

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem procedural, compilada e de baixo nível, base dos sistemas operacionais, de softwares embarcados e de praticamente todas as linguagens modernas.

## Conceitos-chave
- Paradigma imperativo/procedural com funções como unidade principal de organização.
- Tipagem estática e fraca: conversões entre tipos (int, float, char, ponteiros) são automáticas e permissivas.
- Compilada: o gcc/clang gera código de máquina nativo, proporcionando alta performance e controle total.
- Uso principal em kernels (Linux), drivers, sistemas embarcados, interpretadores e bibliotecas de alto desempenho.
- Gerenciamento manual de memória via `malloc()`/`free()`, sem garbage collector.
- Ponteiros permitem manipular memória diretamente e criar estruturas de dados arbitrárias.
- Uso principal de tipos: `int`, `float`, `double`, `char`, `struct`, `union`, `enum`, `void`.

## Exemplos
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char nome[50];
    int idade;
} Pessoa;

int main(void) {
    Pessoa *p = malloc(sizeof(Pessoa));
    if (p == NULL) return 1;

    p->idade = 25;
    printf("Idade: %d\n", p->idade);

    free(p);
    return 0;
}
```

## Boas práticas
- Sempre verifique o retorno de `malloc()` e libère memória com `free()` em todo caminho.
- Inicialize variáveis e use `const` sempre que um valor não deve mudar.
- Prefira limites explícitos em loops e funções de cópia (`snprintf`, `strncpy`) a operações sem tamanho.
- Organize o código em arquivos `.h` (declarações) e `.c` (implementação) com `#include` adequado.
- Compile com `-Wall -Wextra -Werror` e valide com sanitizers (`-fsanitize=address`) em desenvolvimento.

## Armadilhas comuns
- Estouro de buffer: escrever além do tamanho de um array é comportamento indefinido (undefined behavior).
- Double free, use-after-free e memory leak por não liberar memória alocada.
- Desreferenciar ponteiro nulo ou inválido, causando segmentation fault.
- Confundir `=` (atribuição) com `==` (comparação) dentro de condicionais.
- Aritmética de ponteiros fora do array alocado e cast de tipos incompatíveis.

## Relacionadas
- [[C++]]