---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Comprehensions em Python

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Comprehensions constroem listas, dicts e sets em uma expressão declarativa, e a versão entre parênteses cria geradores preguiçosos.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `[expr for x in seq]` | List comprehension | `[x * 2 for x in nums]` |
| `[expr for x in seq if cond]` | List com filtro | `[x for x in nums if x % 2 == 0]` |
| `{k: v for ...}` | Dict comprehension | `{w: len(w) for w in palavras}` |
| `{expr for x in seq}` | Set comprehension | `{c.lower() for c in texto}` |
| `(x for x in seq)` | Expressão geradora (avalia sob demanda) | `sum(x * x for x in nums)` |
| `if/else` dentro da expr | Transforma condicionalmente | `[x if x > 0 else 0 for x in vals]` |

## Exemplos

```python
numeros = range(1, 11)

pares_ao_quadrado = [n ** 2 for n in numeros if n % 2 == 0]
# [4, 16, 36, 64, 100]

palavras = ["ana", "bruno", "carla"]
tamanhos = {p: len(p) for p in palavras}      # dict palavra -> tamanho
iniciais = {p[0].upper() for p in palavras}   # set de iniciais
total_letras = sum(len(p) for p in palavras)  # geradora: sem criar lista
```

```python
# Aninhada moderada: matriz transposta
matriz = [[1, 2], [3, 4], [5, 6]]
transposta = [list(coluna) for coluna in zip(*matriz)]
print(transposta)   # [[1, 3, 5], [2, 4, 6]]
```

## Boas práticas

- Use para transformações simples que cabem em uma linha legível.
- Prefira expressões geradoras ao processar grandes volumes de dados.
- Nomeie bem a variável de iteração (`usuario`, não `u`).
- Filtre cedo (`if`) para reduzir trabalho das etapas seguintes.
- Se precisar de dois ou mais níveis de laço complexos, volte ao `for` tradicional.

## Armadilhas comuns

- Comprehension longa demais vira código ilegível: o ganho se perde.
- Colocar efeitos colaterais (`print`, `append` externo) dentro da comprehension abusa da sintaxe.
- Geradores só podem ser consumidos uma vez; a segunda leitura vem vazia.
- Trocar `[...]` por `(...)` muda o resultado de lista para gerador.
- O `if` depois do `for` filtra elementos; `if/else` antes do `for` transforma: confundir os dois muda a lógica.

## Relacionadas

- [[Loops-e-Iteracao]]
- [[Estruturas-de-Dados]]
- [[Strings-e-Formatacao]]
- [[Python]]
