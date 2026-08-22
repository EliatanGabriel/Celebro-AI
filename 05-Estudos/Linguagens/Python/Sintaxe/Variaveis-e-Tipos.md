---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Variáveis e Tipos em Python

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Em Python as variáveis não têm tipo fixo: o nome aponta para um objeto e o tipo é decidido dinamicamente em tempo de execução.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `x = valor` | Atribuição dinâmica (sem declaração de tipo) | `x = 10` |
| `type(x)` | Retorna o tipo do objeto | `type(x)  # <class 'int'>` |
| `int(x)` | Converte para inteiro | `int("42")` |
| `float(x)` | Converte para ponto flutuante | `float("3.14")` |
| `str(x)` | Converte para string | `str(99)` |
| `bool(x)` | Converte para booleano | `bool(0)  # False` |
| `None` | Ausência de valor (tipo NoneType) | `resultado = None` |
| `a, b = 1, 2` | Múltiplas atribuições em uma linha | `a, b = b, a` |
| `f"..."` | f-string: interpola expressões no texto | `f"total: {x}"` |

## Exemplos

```python
# Tipos básicos e conversões
idade = 25              # int
altura = 1.75           # float
nome = "Ana"            # str
ativo = True            # bool
endereco = None         # NoneType
print(type(idade))      # <class 'int'>

numero = int("100") + float("2.5")   # 102.5
mensagem = f"{nome} tem {idade} anos"
```

```python
# Múltiplas atribuições e troca de valores
a, b = 1, 2
a, b = b, a             # swap idiomático
x = y = z = 0           # mesmo valor para vários nomes
```

## Boas práticas

- Use `snake_case` para variáveis e funções, conforme a PEP 8.
- Prefira nomes descritivos: `total_vendas` diz mais que `tv`.
- Constantes ficam em MAIÚSCULAS: `PI = 3.14159`.
- Prefira f-strings a concatenação com `+` para montar textos.
- Converta explicitamente valores vindos de `input()` antes de calcular.
- Evite trocar o tipo de uma mesma variável no meio do programa.

## Armadilhas comuns

- `"2" + 3` gera `TypeError`: string não soma com número sem conversão.
- `int("3.14")` falha: passe antes por `float()` quando houver ponto.
- `input()` sempre retorna `str`; sem `int()`, comparações numéricas quebram.
- `bool("")` e `bool(0)` são `False`: cuidado ao usar valores como condição.
- Misturar tabs e espaços na indentação causa `IndentationError`.

## Relacionadas

- [[Operadores]]
- [[Strings-e-Formatacao]]
- [[Python]]
