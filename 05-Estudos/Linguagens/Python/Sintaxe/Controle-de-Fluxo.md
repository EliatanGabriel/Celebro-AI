---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Controle de Fluxo em Python

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** `if/elif/else` e `match/case` escolhem qual bloco executar; os blocos são delimitados por indentação e as condições seguem a lógica truthy/falsy.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `if cond:` | Executa o bloco se a condição for verdadeira | `if idade >= 18:` |
| `elif cond:` | Testa outra condição em sequência | `elif idade >= 65:` |
| `else:` | Bloco padrão quando nada anterior casa | `else:` |
| `match x:` / `case` | Casamento de padrões (Python 3.10+) | `case 404:` |
| `case _:` | Curinga: executa quando nenhum padrão casa | `case _:` |
| `if colecao:` | Truthy/falsy: vazia é falsa | `if fila:` |
| `and or not` | Combinam e invertem condições | `if nome and ativo:` |

## Exemplos

```python
# if/elif/else com indentação obrigatória (4 espaços)
media = float(input("Média: "))
if media >= 7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "recuperação"
else:
    situacao = "reprovado"
print(f"Aluno {situacao}")
```

```python
# match/case (Python 3.10+) tratando códigos HTTP
codigo = 404
match codigo:
    case 200:
        print("OK")
    case 404:
        print("Não encontrado")
    case 500:
        print("Erro interno")
    case _:
        print("Código desconhecido")
```

## Boas práticas

- Indente blocos com 4 espaços e nunca misture tabs com espaços.
- Ordene os `elif` do caso mais específico para o mais genérico.
- Prefira condições diretas: `if item in lista` é mais claro que negações duplas.
- Nomeie condições complexas: `tem_saldo = saldo > 0` antes do `if`.
- Use `match/case` quando comparar um mesmo valor contra várias constantes.

## Armadilhas comuns

- Faltam os dois-pontos no fim da linha do `if`, `elif`, `else` ou `case`.
- Um bloco mal indentado compila, mas executa na hora errada: a indentação é a sintaxe.
- `if valor:` é falso para `0`, `""` e `[]`; às vezes o certo é `if valor is not None`.
- `=` dentro do `if` é erro de sintaxe (a exceção é o walrus `:=`).
- No `match/case`, `case x:` com nome solto captura qualquer valor e engole os casos seguintes.

## Relacionadas

- [[Operadores]]
- [[Loops-e-Iteracao]]
- [[Erros-e-Excecoes]]
- [[Python]]
