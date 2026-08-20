---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Filas

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Estrutura de dados FIFO (First In, First Out): o primeiro elemento inserido é o primeiro a ser removido, como uma fila de pessoas.

## Conceitos-chave
- **FIFO:** a ordem de remoção segue exatamente a ordem de inserção.
- **Enqueue:** operação de inserir no fim da fila, O(1).
- **Dequeue:** operação de remover do início da fila, O(1).
- **Front e rear:** referências para o início (próximo a sair) e o fim (último a entrar).
- **Buffers:** filas modelam buffers de dados, como filas de impressão e streaming.
- **Escalonamento:** sistemas operacionais e message brokers usam filas para gerenciar tarefas e processos.
- **BFS:** a busca em largura em grafos usa uma fila para controlar a ordem de visita.

## Exemplos
```python
from collections import deque

fila = deque()
fila.append('tarefa1')      # enqueue
fila.append('tarefa2')
fila.append('tarefa3')

while fila:
    proxima = fila.popleft()   # dequeue
    print('processando', proxima)
# Saída: tarefa1, tarefa2, tarefa3 (ordem FIFO)
```

```text
// Implementação com array circular (pseudocódigo)
enqueue(f):
    se f.tamanho == f.capacidade: erro (fila cheia)
    f.itens[f.rear] = valor
    f.rear = (f.rear + 1) % f.capacidade

dequeue(f):
    se f.rear == f.front: erro (fila vazia)
    valor = f.itens[f.front]
    f.front = (f.front + 1) % f.capacidade
    retorne valor
```

## Boas práticas
- Usar filas quando a ordem de processamento é por chegada (FIFO).
- Preferir estruturas prontas (`collections.deque` em Python, `Queue` em C#/Java) para evitar erros de implementação.
- Escolher fila circular ou lista encadeada para evitar o custo de deslocar elementos.
- Usar filas com limites de capacidade em produtores/consumidores para evitar consumo excessivo de memória.

## Armadilhas comuns
- Confundir fila (FIFO) com pilha (LIFO); a ordem de remoção é o oposto.
- Implementar fila sobre array e deslocar todos os elementos a cada dequeue, tornando a operação O(n).
- Dequeue em fila vazia ou enqueue em fila cheia sem tratar os casos de borda.
- Usar `pop()` (do fim) em vez de `popleft()` em Python, quebrando a semântica FIFO.
- Ignorar a necessidade de sincronização em filas compartilhadas entre threads/processos.

## Relacionadas
- [[Listas]]
- [[Estruturas-de-Dados]]
- [[Pilhas]]
- [[Algoritmos]]
- [[Grafos]]
- [[Sistemas]]