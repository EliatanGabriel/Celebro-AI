---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Ponteiros

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Variáveis que armazenam o endereço de memória de outra variável, permitindo acesso e manipulação indireta de dados, comuns em C e C++.

## Conceitos-chave
- **Endereço:** cada variável ocupa uma região na memória; o operador `&` obtém o endereço.
- **Dereferência:** o operador `*` acessa o valor no endereço guardado pelo ponteiro.
- **Ponteiro nulo (NULL):** valor especial que indica "não aponta para nada"; dereferenciar nulo causa erro.
- **Aritmética de ponteiros:** avançar o ponteiro percorre a memória por blocos do tipo apontado (`ptr + 1` avança um elemento).
- **Ponteiros e arrays:** o nome de um array decai para o ponteiro do primeiro elemento; acesso por índice é aritmética de ponteiros.
- **Passagem por referência:** usar ponteiros como parâmetros permite modificar a variável original dentro da função.
- **Alocação dinâmica:** `malloc`/`new` retornam ponteiros para o heap; exigem `free`/`delete`.

## Exemplos
```c
int x = 42;
int *p = &x;        // p guarda o endereço de x
*p = 10;            // dereferencia: altera x para 10
printf("%d", x);    // 10

// Passagem por referência
void incrementar(int *n) {
    (*n)++;          // modifica a variável original
}
int main() {
    int valor = 5;
    incrementar(&valor);
    printf("%d", valor);   // 6
}

// Alocação dinâmica no heap
int *arr = malloc(5 * sizeof(int));
arr[0] = 1;                 // acessa como array
free(arr);                  // libera a memória
```

```text
// Relação ponteiro/array
int a[3] = {10, 20, 30};
int *p = a;        // p == &a[0]
*(p + 1) == 20     // a[1]
*(a + 2) == 30     // a[2]
```

## Boas práticas
- Inicializar ponteiros com NULL e verificar antes de usar/dereferenciar.
- Liberar memória alocada dinamicamente sempre que não for mais necessária.
- Fazer uma atribuição por linha e manter o código simples de revisar.
- Usar referências (C++) quando não houver necessidade de aritmética ou ponteiro nulo.
- Em linguagens gerenciadas, preferir referências da própria linguagem ao invés de ponteiros crus.

## Armadilhas comuns
- Dereferenciar ponteiro nulo ou não inicializado, causando segfault.
- Vazamento de memória por não chamar `free`/`delete`.
- Aritmética de ponteiros fora dos limites, gerando acesso inválido à memória.
- Confundir `*` de declaração com `*` de dereferência.
- Esquecer que ponteiros apontam para um tipo; conversão incorreta corrompe os dados.

## Relacionadas
- [[Memoria]]
- [[Stack-Heap]]
- [[Arrays]]
- [[Listas]]
- [[Estudos-Variaveis]]
- [[Tipos-de-Dados]]
- [[Debug]]