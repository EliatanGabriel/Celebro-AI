---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Programacao-Funcional

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Paradigma de programação baseado em funções puras, imutabilidade e composição, tratando a computação como a avaliação de expressões em vez de sequência de comandos que mutam estado.

## Conceitos-chave
- **Função pura:** mesmo argumento sempre produz o mesmo resultado e não causa efeitos colaterais (não altera estado externo, não faz I/O).
- **Imutabilidade:** dados não são modificados após a criação; operações criam novos valores, facilitando raciocínio e concorrência.
- **Funções de alta ordem:** funções que recebem ou retornam outras funções (`map`, `filter`, `reduce`).
- **Composição:** combinar funções pequenas para construir comportamentos maiores.
- **Transparência referencial:** uma expressão pode ser substituída pelo seu valor sem mudar o comportamento — propriedade das funções puras.
- **Recursão:** substitui loops no estilo funcional puro (ex.: percorrer listas recursivamente).
- **Currying e closures:** transformar funções e capturar escopo, técnicas típicas do paradigma.

## Exemplos
```javascript
// Função pura: sem efeitos colaterais, resultado determinístico
function soma(a, b) {
  return a + b;
}

// Alta ordem + imutabilidade: transformar arrays sem mutar
const numeros = [1, 2, 3, 4];
const pares = numeros.filter(n => n % 2 === 0);  // [2, 4]
const dobrados = pares.map(n => n * 2);          // [4, 8]
const total = dobrados.reduce((acc, n) => acc + n, 0);  // 12
// numeros permanece [1, 2, 3, 4]
```

```haskell
-- Recursão como alternativa a loop
soma [] = 0
soma (x:xs) = x + soma xs

-- Composição de funções
dobrarESomar = soma . map (*2)
```

```python
# Recursão + pureza
def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)
```

## Boas práticas
- Escrever funções puras sempre que possível; mover efeitos colaterais para a fronteira do sistema.
- Usar `map`/`filter`/`reduce` em vez de loops que mutam acumuladores.
- Preferir dados imutáveis (tuplas, frozen collections, spread/rest).
- Compor funções pequenas com responsabilidade única.
- Beneficiar-se da transparência referencial para testar e paralelizar com facilidade.

## Armadilhas comuns
- Achar que código funcional é sempre superior; há trade-offs de performance e legibilidade.
- Escrever funções que parecem puras mas mutam objetos passados por referência.
- Recursão excessiva causando stack overflow sem otimização de cauda (tail call).
- Abusar de closures e currying, prejudicando a legibilidade.
- Usar `reduce` em casos que seriam mais claros com loop simples.

## Relacionadas
- [[Paradigmas]]
- [[Orientacao-a-Objetos]]
- [[Programacao-Procedural]]
- [[Estudos-Funcoes]]
- [[Estudos-Recursao]]
- [[Estudos-Variaveis]]
- [[Programacao]]