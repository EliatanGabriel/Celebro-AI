---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Pilhas

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Estrutura de dados LIFO (Last In, First Out): o último elemento inserido é o primeiro a ser removido, como uma pilha de pratos.

## Conceitos-chave
- **LIFO:** a remoção acontece no topo, invertendo a ordem de inserção.
- **Push:** operação de inserir no topo, O(1).
- **Pop:** operação de remover do topo, O(1).
- **Top/peek:** inspecionar o elemento do topo sem removê-lo.
- **Usos clássicos:** controle de chamadas de função (call stack), desfazer/refazer (undo/redo), parsing de expressões e avaliação com notação polonesa, backtracking e DFS.
- **Implementação:** facilmente construída sobre arrays (usando o fim) ou listas encadeadas.

## Exemplos
```python
pilha = []
pilha.append('a')       # push
pilha.append('b')
pilha.append('c')
pilha.pop()             # 'c' — remove o último (LIFO)
pilha[-1]               # 'b' — topo atual (peek)
```

```text
// Validar parênteses balanceados com pilha
funcao balanceada(expressao):
    pilha = []
    para cada caractere c em expressao:
        se c em "([{":
            pilha.push(c)
        senão se c em ")]}":
            se pilha vazia: retorne false
            topo = pilha.pop()
            se topo não corresponde a c: retorne false
    retorne pilha vazia   // não pode sobrar abertura

// Exemplo: "([{}])" → true; "([)]" → false
```

```text
// Call stack: pilha de chamadas durante execução
main() → funcaoA() → funcaoB() → funcaoB retorna → funcaoA retorna → main retorna
(no topo está a função em execução; ao retornar, o topo é desempilhado)
```

## Boas práticas
- Usar pilha quando a regra é "processar o mais recente primeiro" (LIFO).
- Preferir implementações prontas da linguagem (`list` do Python, `Stack` de Java/C#).
- Combinar pilha com recursão para problemas de backtracking e DFS.
- Para validar parênteses e expressões, tratar também o caso de sobra de abertura ao final.

## Armadilhas comuns
- Confundir pilha (LIFO) com fila (FIFO); a ordem de saída é invertida.
- `pop`/`peek` em pilha vazia sem verificar o tamanho, causando erro.
- Esquecer que a recursão também usa a stack de memória; recursão muito profunda causa stack overflow.
- Usar a pilha correta mas implementar `pop` removendo do início, tornando a operação O(n).
- Confundir a estrutura "pilha" com a região de memória "stack" (chamadas de função).

## Relacionadas
- [[Estruturas-de-Dados]]
- [[Listas]]
- [[Filas]]
- [[Arrays]]
- [[Estudos-Recursao]]
- [[Stack-Heap]]
- [[Grafos]]