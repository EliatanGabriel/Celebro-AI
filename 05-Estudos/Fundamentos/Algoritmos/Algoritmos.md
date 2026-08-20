---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Algoritmos

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Sequências finitas de passos bem definidos que transformam uma entrada em uma saída, resolvendo um problema de forma determinística.

## Conceitos-chave
- **Passos finitos:** todo algoritmo termina após um número limitado de operações; se não termina, é um processo infinito, não um algoritmo.
- **Entrada e saída:** recebe dados de entrada (pode ser zero) e produz uma saída esperada.
- **Determinismo:** para a mesma entrada, o mesmo algoritmo produz sempre a mesma saída.
- **Correção:** um algoritmo está correto quando resolve o problema para todos os casos válidos de entrada.
- **Eficiência:** avaliada por tempo de execução e uso de memória, medida com notação Big-O.
- **Pseudocódigo:** representação intermediária entre linguagem natural e código, usada para desenhar a lógica sem se prender à sintaxe.

## Exemplos
```text
// Pseudocódigo: encontrar o maior valor de uma lista
funcao maior(lista):
    se lista vazia:
        retorne erro
    m = lista[0]
    para cada elemento x em lista:
        se x > m:
            m = x
    retorne m
```

```text
// Pseudocódigo: busca linear
funcao busca_linear(lista, alvo):
    para i de 0 até tamanho(lista) - 1:
        se lista[i] == alvo:
            retorne i
    retorne -1
```

## Boas práticas
- Desenhar o algoritmo em pseudocódigo antes de codificar.
- Definir claramente a entrada, a saída e as restrições do problema.
- Testar casos de borda: lista vazia, um único elemento, valores repetidos.
- Escolher a estrutura de dados adequada antes de otimizar o algoritmo.
- Analisar a complexidade para prever comportamento em entradas grandes.

## Armadilhas comuns
- Confundir algoritmo com implementação: o mesmo algoritmo pode ser codificado de formas diferentes.
- Esquecer o caso base ou casos de borda, gerando erros em entradas válidas.
- Otimizar prematuramente sem antes garantir a correção.
- Tratar a complexidade teórica como medida absoluta, ignorando constantes e hardware.
- Escrever pseudocódigo tão detalhado quanto código, perdendo a vantagem de abstração.

## Relacionadas
- [[Big-O]]
- [[Estruturas-de-Dados]]
- [[Estudos-Complexidade]]
- [[Estudos-Ordenacao]]
- [[Estudos-Recursao]]
- [[Logica-de-Programacao]]
- [[Programacao]]
- [[Ciencia-da-Computacao]]