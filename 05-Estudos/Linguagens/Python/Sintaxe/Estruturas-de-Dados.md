---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Estruturas de Dados em Python

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** `list`, `tuple`, `set` e `dict` cobrem quase todas as necessidades; escolher a estrutura certa simplifica o código e melhora o desempenho.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `lista.append(x)` | Adiciona ao final | `nums.append(4)` |
| `lista.insert(i, x)` | Insere na posição `i` | `nums.insert(0, 9)` |
| `lista.pop(i)` | Remove e retorna item (último se sem índice) | `nums.pop()` |
| `lista.remove(x)` | Remove a primeira ocorrência do valor | `nums.remove(3)` |
| `lista.sort()` | Ordena no lugar (retorna None) | `nums.sort(reverse=True)` |
| `lista[a:b]` | Slicing: fatia com fim exclusivo | `nums[1:3]` |
| `(1, 2)` | Tupla: imutável, boa para registros fixos | `coord = (-23.5, -46.6)` |
| `{1, 2}` | Set: únicos e sem ordem | `unicos = set(nums)` |
| `a.union(b)` / `a & b` | União de sets (`&` interseção) | `{1,2}.union({2,3})` |
| `d[chave]` / `d.get(k, padrao)` | Acesso direto / seguro ao dict | `estoque.get("café", 0)` |
| `d.keys() .values() .items()` | Visões de chaves, valores e pares | `for k, v in d.items():` |

Quando usar: `list` para coleção ordenada mutável; `tuple` para registro fixo ou chave de dict; `set` para unicidade e teste rápido de existência; `dict` para mapeamento chave → valor.

## Exemplos

```python
# Lista: operações e slicing
tarefas = ["ler", "escrever", "testar"]
tarefas.append("publicar")
tarefas.remove("ler")
print(tarefas[1:])          # ['escrever', 'testar', 'publicar']
print(len(tarefas), max([3, 7, 1]))

# Set: união e interseção
python_devs = {"ana", "bruno"}
sql_devs = {"bruno", "carla"}
print(python_devs | sql_devs)   # {'ana', 'bruno', 'carla'}
print(python_devs & sql_devs)   # {'bruno'}
```

```python
import copy

original = {"itens": [1, 2], "ativo": True}
rasa = original.copy()          # cópia rasa: itens internos compartilhados
profunda = copy.deepcopy(original)   # clona também os objetos aninhados
original["itens"].append(3)
print(rasa["itens"])        # [1, 2, 3] -> foi afetada!
print(profunda["itens"])    # [1, 2]
```

## Boas práticas

- Prefira `get()` com padrão a acessar chaves que podem não existir.
- Use `in` para testar existência: O(1) em `dict` e `set`.
- Tuplas comunicam "isto não muda"; aproveite isso no design.
- Para copiar estruturas aninhadas, pense em rasa vs `deepcopy`.

## Armadilhas comuns

- `remove(x)` levanta `ValueError` se `x` não existe na lista.
- `sort()` ordena no lugar e retorna `None`: `l = l.sort()` destrói a lista.
- Tupla de um elemento exige vírgula: `(1,)`, senão é apenas parêntese.
- `=` não copia lista: cria outro nome apontando ao mesmo objeto.
- Set não tem ordem nem aceita indexação: `s[0]` dá `TypeError`.

## Relacionadas

- [[Loops-e-Iteracao]]
- [[Comprehensions]]
- [[POO]]
- [[Python]]
