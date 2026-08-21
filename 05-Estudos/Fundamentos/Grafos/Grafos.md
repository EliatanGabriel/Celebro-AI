---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Grafos

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Estrutura de dados formada por um conjunto de vértices (nós) conectados por arestas, usada para modelar relações e redes.

## Conceitos-chave
- **Vértices e arestas:** os nós representam entidades; as arestas, as relações entre elas.
- **Grafo direcionado:** arestas têm sentido (u → v difere de v → u); útil para fluxos e dependências.
- **Grafo ponderado:** arestas têm pesos, representando custo, distância ou capacidade.
- **Grafo conectado e ciclos:** um caminho liga vértices; ciclos existem quando há caminho de volta a um nó. Árvores são grafos sem ciclos.
- **Representações:** lista de adjacência (compacta) ou matriz de adjacência (acesso O(1), espaço O(n²)).
- **BFS (busca em largura):** visita por níveis usando uma fila; encontra o caminho mínimo em grafos não ponderados.
- **DFS (busca em profundidade):** explora ao máximo cada ramo usando pilha/recursão; útil para detecção de ciclos e ordenação topológica.
- **Aplicações:** redes sociais, mapas/rotas, dependências de pacotes, fluxo de redes e IA.

## Exemplos
```python
# Grafo com lista de adjacência
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
}

# BFS: visita em ordem de distância a partir de 'A'
from collections import deque

def bfs(grafo, inicio):
    visitados = {inicio}
    fila = deque([inicio])
    while fila:
        no = fila.popleft()
        print(no, end=' ')          # A B C D
        for vizinho in grafo[no]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
```

```text
// Caminho mínimo (não ponderado) — BFS
distancia[inicio] = 0
fila = [inicio]
enquanto fila não vazia:
    atual = remover primeiro da fila
    para cada vizinho v de atual:
        se v não visitado:
            distancia[v] = distancia[atual] + 1
            marcar v visitado e inserir na fila
```

## Boas práticas
- Escolher lista de adjacência para grafos esparsos e matriz para grafos densos.
- Usar BFS quando a distância em número de arestas importa; DFS para explorar toda a estrutura.
- Marcar nós como visitados para evitar loops infinitos em grafos com ciclos.
- Modelar o problema claramente: o que são os vértices e o que representam as arestas.

## Armadilhas comuns
- Esquecer de marcar visitados em grafos com ciclos, causando recursão infinita.
- Confundir BFS com DFS na escolha da estrutura (fila vs pilha).
- Assumir que BFS encontra o caminho mínimo em grafos ponderados — para isso usa-se Dijkstra.
- Usar matriz de adjacência sem necessidade, desperdiçando memória O(n²).
- Tratar todos os grafos como conexos; lidar com componentes desconexas.

## Relacionadas
- [[Arvores]]
- [[Algoritmos]]
- [[Estudos-Complexidade]]
- [[Filas]]
- [[Pilhas]]
- [[Estudos-Recursao]]
- [[Estruturas-de-Dados]]