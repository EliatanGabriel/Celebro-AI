---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Strings e Formatação em Python

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Strings são imutáveis; métodos como `split`, `join` e `strip` retornam novas strings, e f-strings são a forma moderna de formatar valores.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `s[i]` / `s[a:b]` | Indexação e fatiamento (fim exclusivo) | `nome[0]`, `nome[1:4]` |
| `.upper()` / `.lower()` | Converte caixa alta / baixa | `"Py".upper()  # 'PY'` |
| `.strip()` | Remove espaços das pontas | `" oi ".strip()` |
| `.split(sep)` | Divide a string em lista | `"a,b".split(",")` |
| `sep.join(lista)` | Junta lista de strings | `", ".join(["a", "b"])` |
| `.replace(antigo, novo)` | Substitui trechos | `"a-b".replace("-", "+")` |
| `.find(sub)` | Índice da 1ª ocorrência (-1 se ausente) | `"py".find("t")` |
| `.startswith(sub)` | Verifica prefixo | `arq.startswith("img_")` |
| `.format(...)` | Formatação por posição/nome | `"{}".format(x)` |
| `f"{x:.2f}"` | f-string com 2 casas decimais | `f"{pi:.2f}  # 3.14"` |
| `"""texto"""` | String multilinha | Textos longos e docstrings |

## Exemplos

```python
# Limpeza e quebra de entrada de usuário
entrada = "  ana;bruno ; carla "
nomes = [n.strip().title() for n in entrada.split(";")]
print(nomes)                       # ['Ana', 'Bruno', 'Carla']

csv = ",".join(nomes)              # montagem eficiente
arquivo = "relatorio_final.pdf"
print(arquivo.startswith("relat"), arquivo.find("_"))
```

```python
# f-strings com formatação numérica e multilinha
produto, preco, qtd = "Café", 34.5, 3
resumo = f"""
Produto: {produto}
Total: R$ {preco * qtd:.2f}
Desconto: {(preco * qtd * 0.9):>8.2f}
"""
print(resumo)
```

## Boas práticas

- Prefira f-strings a `%`, `.format()` e concatenação com `+`.
- Use `"".join()` em vez de `+` dentro de loops (mais rápido).
- Chame `.strip()` antes de validar entradas digitadas pelo usuário.
- Compare textos ignorando caixa com `.lower()` dos dois lados.
- Guarde números formatados apenas na exibição; mantenha dados brutos.

## Armadilhas comuns

- Strings são imutáveis: `texto.upper()` sozinho não altera `texto`.
- `.find()` retorna `-1` quando não encontra (não levanta exceção).
- `s[10]` fora do intervalo dá `IndexError`, mas slicing nunca levanta erro.
- `split()` sem argumento quebra em qualquer espaço e descarta vazios.
- Concatenar muitas strings com `+` em loop tem custo quadrático.

## Relacionadas

- [[Variaveis-e-Tipos]]
- [[Estruturas-de-Dados]]
- [[Funcoes]]
- [[Python]]
