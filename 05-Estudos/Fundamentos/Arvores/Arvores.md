---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Arvores

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Estrutura de dados hierárquica formada por nós conectados por arestas, sem ciclos, com um único nó raiz.

## Conceitos-chave
- **Raiz:** o nó no topo da árvore; todo nó é alcançado a partir dela seguindo as arestas.
- **Nós e arestas:** cada nó guarda um valor; as arestas definem a relação pai-filho.
- **Folhas:** nós sem filhos, localizados na base da hierarquia.
- **Altura e profundidade:** altura é o maior caminho da raiz até uma folha; profundidade é a distância de um nó até a raiz.
- **Árvore binária:** cada nó tem no máximo dois filhos (esquerdo e direito).
- **BST (Binary Search Tree):** para cada nó, os valores da subárvore esquerda são menores e os da direita, maiores; permite busca, inserção e remoção em O(log n) médio.
- **Percursos:** pré-ordem (raiz, esquerda, direita), em-ordem (esquerda, raiz, direita) e pós-ordem (esquerda, direita, raiz).

## Exemplos
```text
// Árvore binária de busca
        8
       / \
      3   10
     / \    \
    1   6    14
       / \
      4   7

// Busca do valor 7:
// 7 < 8  -> subárvore esquerda
// 7 > 3  -> subárvore direita
// 7 > 6  -> subárvore direita
// 7 == 7 -> encontrado
```

```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def buscar(no, alvo):
    if no is None:
        return False
    if alvo == no.valor:
        return True
    if alvo < no.valor:
        return buscar(no.esquerda, alvo)
    return buscar(no.direita, alvo)
```

## Boas práticas
- Usar árvores quando a relação dos dados é hierárquica (diretórios, organizações, sintaxe).
- Preferir BST balanceadas (AVL, Red-Black) para garantir O(log n) mesmo no pior caso.
- Recorrer à recursão para percursos, já que a estrutura é naturalmente recursiva.
- Garantir a propriedade da BST ao inserir, evitando degenerar em lista encadeada.

## Armadilhas comuns
- Inserir valores em ordem crescente em uma BST, o que a degenera em lista encadeada (O(n)).
- Esquecer os casos `None` (nó vazio) em funções recursivas, causando `AttributeError`.
- Confundir altura com profundidade.
- Tratar qualquer grafo como árvore: árvores não têm ciclos nem nós com múltiplos pais.
- Ignorar o balanceamento e assumir que toda BST é O(log n) no pior caso.

## Relacionadas
- [[Grafos]]
- [[Estruturas-de-Dados]]
- [[Algoritmos]]
- [[Estudos-Recursao]]
- [[Pilhas]]