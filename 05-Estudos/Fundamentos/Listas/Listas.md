---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Listas

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Estrutura de dados dinâmica que armazena elementos em sequência, permitindo inserção e remoção eficientes; a lista encadeada (linked list) é a forma clássica.

## Conceitos-chave
- **Lista encadeada (linked list):** elementos (nós) conectados por referências; cada nó guarda o valor e o ponteiro para o próximo.
- **Dinamicidade:** cresce e encolhe sem realocar toda a estrutura, ao contrário de arrays de tamanho fixo.
- **Inserção/remoção:** O(1) nas extremidades quando se conhece o nó; no meio, O(n) para chegar até o ponto.
- **Acesso:** sequencial — para chegar ao nó `i` é preciso percorrer desde o início (O(n)).
- **Cabeça e cauda:** a cabeça é o primeiro nó; manter referência à cauda torna a inserção no fim O(1).
- **Tipos:** lista simplesmente encadeada, duplamente encadeada (com ponteiro anterior/próximo) e circular.
- **Em muitas linguagens:** `list` do Python e `ArrayList` do Java são arrays dinâmicos, não listas encadeadas; a abstração `LinkedList`/`collections.deque` se aproxima mais.

## Exemplos
```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_no_inicio(self, valor):      # O(1)
        novo = No(valor)
        novo.proximo = self.cabeca
        self.cabeca = novo

    def buscar(self, alvo):                   # O(n)
        atual = self.cabeca
        while atual:
            if atual.valor == alvo:
                return atual
            atual = atual.proximo
        return None

    def remover_inicio(self):                 # O(1)
        if self.cabeca:
            self.cabeca = self.cabeca.proximo
```

```text
// Sequência de referências
[cabeca] -> [10 | *] -> [20 | *] -> [30 | null]
            valor  prox   valor  prox   valor  prox (fim)
```

## Boas práticas
- Usar lista encadeada quando há muitas inserções/remoções no início e acesso sequencial é suficiente.
- Guardar referência à cauda se a inserção no fim for frequente.
- Validar o caso de lista vazia em todas as operações.
- Preferir estruturas prontas da linguagem para evitar erros de ponteiro.
- Documentar a complexidade das operações ao implementar a própria estrutura.

## Armadilhas comuns
- Confundir `list` do Python ou `Array` do JS com lista encadeada; são arrays dinâmicos.
- Perder o nó ao inserir/remover por não atualizar os ponteiros na ordem certa.
- Esquecer de tratar lista vazia, causando erro ao acessar `cabeca.proximo`.
- Assumir acesso aleatório O(1) — em linked list, acessar o nó `i` é O(n).
- Criar referência circular acidentalmente (nó apontando para si mesmo), quebrando a iteração.

## Relacionadas
- [[Arrays]]
- [[Estruturas-de-Dados]]
- [[Filas]]
- [[Pilhas]]
- [[Ponteiros]]
- [[Algoritmos]]
- [[Estudos-Complexidade]]