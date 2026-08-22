---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Funções em Python

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** `def` cria funções reutilizáveis com parâmetros default, argumentos nomeados, `*args`/`**kwargs`, retorno múltiplo via tupla, `lambda` e type hints.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `def nome():` | Define uma função | `def saudar():` |
| `return valor` | Devolve o resultado e encerra a função | `return a + b` |
| `def f(x=10)` | Parâmetro com valor default | `def log(msg, nivel="INFO"):` |
| `f(x=5)` | Argumento nomeado (keyword arg) | `log("oi", nivel="DEBUG")` |
| `*args` | Recebe posicionais extras como tupla | `def soma(*nums):` |
| `**kwargs` | Recebe nomeados extras como dict | `def config(**opcoes):` |
| `lambda x: expr` | Função anônima de uma única expressão | `sorted(d, key=lambda t: t[1])` |
| `-> tipo` | Type hint do retorno | `def f(x: int) -> str:` |
| `"""docstring"""` | Documenta propósito e parâmetros | Primeira linha do corpo |

## Exemplos

```python
# Defaults, keyword args e retorno múltiplo
def estatisticas(numeros: list[float]) -> tuple[float, float]:
    """Retorna (média, máximo) da lista."""
    return sum(numeros) / len(numeros), max(numeros)

media, maior = estatisticas([7, 9, 10])
print(f"Média {media:.1f}, maior {maior}")
```

```python
# *args/**kwargs e lambda
def relatorio(titulo, *linhas, **metadados):
    print(titulo)
    for linha in linhas:
        print("-", linha)
    for chave, valor in metadados.items():
        print(f"{chave}: {valor}")

relatorio("Vendas", "jan: 10", "fev: 15", autor="Ana", ano=2026)

nomes = ["carla", "ana", "bruno"]
print(sorted(nomes, key=lambda n: len(n)))
```

## Boas práticas

- Uma função deve fazer uma coisa só e ter nome que revele isso.
- Escreva docstring curta explicando o quê, não o como.
- Use type hints: documentam e melhoram o autocomplete.
- Retorne valores em vez de imprimir dentro da função.
- Escopo segue LEGB: Local, Enclosing, Global, Built-in; evite depender de globais.

## Armadilhas comuns

- Default mutável é compartilhado entre chamadas: `def f(x=[])`; use `x=None`.
- Confundir `return` com `print`: função sem `return` devolve `None`.
- Parâmetros default devem vir depois dos obrigatórios na assinatura.
- Modificar uma lista/dict recebido altera o objeto original fora da função.
- `lambda` com lógica complexa fica ilegível; prefira um `def` normal.

## Relacionadas

- [[Estruturas-de-Dados]]
- [[Comprehensions]]
- [[POO]]
- [[Python]]
