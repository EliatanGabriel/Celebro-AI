---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Estruturas-de-Dados

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Formas de organizar e armazenar dados em memória para permitir operações eficientes de inserção, acesso, busca e remoção.

## Conceitos-chave
- **Finalidade:** escolher a estrutura certa reduz a complexidade das operações, impactando diretamente o desempenho do algoritmo.
- **Arrays:** acesso aleatório O(1), tamanho fixo ou dinâmico; inserção/remoção no meio custa O(n).
- **Listas encadeadas:** inserção/remoção O(1) nas pontas, acesso sequencial O(n), sem realocação.
- **Pilhas:** LIFO, com push/pop O(1); útil para chamadas de função, desfazer/refazer e backtracking.
- **Filas:** FIFO, com enqueue/dequeue O(1); útil para buffers e escalonamento de processos.
- **Hash tables:** mapeiam chaves para valores com acesso O(1) médio; usam funções de hash e tratam colisões.
- **Árvores:** estrutura hierárquica; BSTs e árvores balanceadas oferecem O(log n) para busca e inserção.
- **Grafos:** nós e arestas para modelar redes, rotas e dependências; percorridos com BFS e DFS.

## Exemplos
```text
// Como escolher a estrutura
Necessidade                          → Estrutura ideal
Acesso por índice (leitura rápida)   → Array
Muitas inserções/remoções no início  → Lista encadeada
Processar no modelo LIFO             → Pilha
Processar no modelo FIFO             → Fila
Buscar por chave em O(1) médio       → Hash table
Dados hierárquicos com busca rápida  → Árvore de busca
Relacionamentos entre entidades      → Grafo
```

```python
from collections import deque

# Fila FIFO
fila = deque()
fila.append('a')       # enqueue O(1)
fila.popleft()         # dequeue O(1)

# Pilha LIFO
pilha = []
pilha.append(1)        # push O(1)
pilha.pop()            # pop O(1)
```

## Boas práticas
- Escolher a estrutura com base nas operações mais frequentes do problema.
- Analisar o custo amortizado, não apenas o caso individual.
- Considerar trade-offs: espaço extra (hash, árvores) em troca de velocidade.
- Preferir abstrações prontas da linguagem (list, dict, collections) quando suficientes.

## Armadilhas comuns
- Usar array para muitas inserções no início quando uma lista encadeada seria melhor.
- Assumir que toda estrutura de "lista" tem as mesmas garantias de complexidade.
- Ignorar o custo de realocação em arrays dinâmicos.
- Confundir a pilha (estrutura) com a stack de memória usada em chamadas de função.
- Escolher estrutura complexa (árvore, grafo) onde um array ou hash resolve.

## Relacionadas
- [[Arrays]]
- [[Listas]]
- [[Pilhas]]
- [[Filas]]
- [[Arvores]]
- [[Grafos]]
- [[Hash]]
- [[Algoritmos]]
- [[Estudos-Complexidade]]
- [[Memoria]]