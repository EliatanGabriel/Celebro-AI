---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Loops e Iteração em Python

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** O `for` percorre iteráveis, o `while` repete por condição, e `range()`, `enumerate()`, `zip()` e `break`/`continue` controlam cada repetição.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `for x in iteravel:` | Percorre cada elemento | `for letra in "abc":` |
| `range(inicio, fim, passo)` | Sequência de números (fim exclusivo) | `range(0, 10, 2)` |
| `while cond:` | Repete enquanto a condição for verdadeira | `while vidas > 0:` |
| `break` | Interrompe o loop imediatamente | `if achou: break` |
| `continue` | Pula para a próxima iteração | `if vazio: continue` |
| `else:` (no loop) | Executa só se o loop terminar sem `break` | `for ... else:` |
| `enumerate(seq)` | Entrega índice e valor juntos | `for i, v in enumerate(lista):` |
| `zip(a, b)` | Percorre duas sequências em paralelo | `for n, t in zip(nomes, tels):` |
| `d.items()` | Itera dicionário por chave e valor | `for k, v in estoque.items():` |

## Exemplos

```python
# enumerate e zip evitam índices manuais
nomes = ["Ana", "Bruno", "Carla"]
notas = [9.0, 7.5, 8.0]

for posicao, (nome, nota) in enumerate(zip(nomes, notas), start=1):
    print(f"{posicao}. {nome}: {nota}")

estoque = {"café": 12, "leite": 3}
for produto, quantidade in estoque.items():
    print(produto, quantidade)
```

```python
# while com busca e o else do loop
senhas = ["123", "abc", "segredo"]
tentativa = "abc"
i = 0
while i < len(senhas):
    if senhas[i] == tentativa:
        print("Encontrada na posição", i)
        break
    i += 1
else:
    print("Não encontrada")   # roda só se o while acabou sem break
```

## Boas práticas

- Prefira `for` quando souber o que percorrer; `while` para condições abertas.
- Use `enumerate()` no lugar de `range(len(lista))`.
- Use `zip()` para percorrer listas paralelas do mesmo comprimento.
- Extraia corpos longos para funções e mantenha o loop enxuto.
- O `else` de loop é pouco conhecido: comente bem quando usar.

## Armadilhas comuns

- `range(1, 10)` vai até 9: o limite superior é sempre exclusivo.
- `while True` sem `break` interno trava o programa em loop infinito.
- Remover itens da lista durante o `for` faz pular elementos; itere sobre uma cópia.
- `zip()` descarta silenciosamente os itens excedentes da sequência maior.
- Esquecer de atualizar a variável de controle no `while` cria laço infinito.

## Relacionadas

- [[Controle-de-Fluxo]]
- [[Comprehensions]]
- [[Estruturas-de-Dados]]
- [[Python]]
