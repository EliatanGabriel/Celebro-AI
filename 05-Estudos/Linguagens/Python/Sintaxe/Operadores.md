---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Operadores em Python

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Operadores aritméticos, de comparação, lógicos, de identidade (`is`) e de pertencimento (`in`) combinam valores; ainda existem o ternário e o walrus `:=`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `+ - * /` | Aritméticos básicos (`/` sempre devolve float) | `7 / 2  # 3.5` |
| `//` | Divisão inteira (descarta a parte decimal) | `7 // 2  # 3` |
| `%` | Resto da divisão | `7 % 2  # 1` |
| `**` | Potência | `2 ** 10  # 1024` |
| `== != < > <= >=` | Comparação de valores | `x >= 10` |
| `1 < x < 10` | Comparação encadeada | `0 <= nota <= 10` |
| `and or not` | Operadores lógicos | `a and not b` |
| `is` / `is not` | Identidade (mesmo objeto na memória) | `x is None` |
| `in` / `not in` | Pertencimento a coleção/texto | `"py" in "python"` |
| `x if cond else y` | Expressão ternária | `"par" if n % 2 == 0 else "ímpar"` |
| `:=` | Walrus: atribui e retorna o valor | `if (n := len(txt)) > 10:` |

## Exemplos

```python
# Divisão real vs inteira vs módulo
print(7 / 2)     # 3.5
print(7 // 2)    # 3
print(-7 // 2)   # -4 (arredonda para baixo!)
print(7 % 2)     # 1

# Comparação encadeada no lugar de "nota >= 0 and nota <= 10"
nota = 8
if 0 <= nota <= 10:
    print("Nota válida")
```

```python
# Ternário e walrus
numero = 7
paridade = "par" if numero % 2 == 0 else "ímpar"

texto = "banana,maçã,uva"
if (frutas := texto.split(",")) and len(frutas) > 2:
    print(f"{len(frutas)} frutas encontradas")
```

## Boas práticas

- Compare com `None` usando `is None` / `is not None`, nunca `== None`.
- Prefira comparações encadeadas a juntar condições com `and`.
- Use `%` para paridade e ciclos; `//` quando quiser um inteiro garantido.
- Walrus só quando encurtar o código e mantê-lo legível.
- Parênteses extras ajudam a leitura em expressões longas.

## Armadilhas comuns

- `=` atribui, `==` compara: trocar os dois é erro clássico.
- `-7 // 2` resulta em `-4`, não `-3`: a divisão inteira arredonda para baixo.
- `is` compara identidade de objetos, não valor: não use para comparar números ou strings.
- `0.1 + 0.2 == 0.3` é `False` por imprecisão de ponto flutuante.
- `0`, `""` e `[]` são falsy: `if valor:` nem sempre significa "preenchido".

## Relacionadas

- [[Variaveis-e-Tipos]]
- [[Controle-de-Fluxo]]
- [[Python]]
