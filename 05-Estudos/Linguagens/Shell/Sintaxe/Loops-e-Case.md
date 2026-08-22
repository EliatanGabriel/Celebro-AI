---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Loops e Case em Shell

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** `for` percorre listas e globbing, `while`/`until` repetem por condição, e `case/esac` direciona por padrões com blocos terminados em `;;`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `for var in lista; do ... done` | Percorre cada item da lista | `for f in *.txt; do` |
| `{1..10}` | Intervalo de números (Bash) | `for i in {1..10}; do` |
| `seq inicio fim` | Gera sequência de números | `for i in $(seq 1 5)` |
| `for ((i=0;i<10;i++))` | For estilo C (Bash) | Contadores numéricos |
| `while cond; do ... done` | Repete enquanto a condição for verdadeira | `while [ $i -lt 5 ]; do` |
| `while read linha` | Lê entrada linha a linha | `while IFS= read -r l; do` |
| `until cond; do ... done` | Repete até a condição ficar verdadeira | `until ping -c1 host; do` |
| `case var in pad) ... ;; esac` | Desvio múltiplo por padrões | `case $op in start) ;; esac` |
| `*)` no case | Padrão curinga (nenhum caso anterior) | Opção inválida |
| `break` / `continue` | Sai do laço / pula iteração | `break 2` sai de dois níveis |

## Exemplos

```sh
#!/bin/bash
set -euo pipefail

# Renomeia .jpeg para .jpg usando globbing
for arquivo in *.jpeg; do
    [[ -e "$arquivo" ]] || continue      # nenhum arquivo casou
    mv -- "$arquivo" "${arquivo%.jpeg}.jpg"
done

# Menu com case/esac
read -rp "Ação (start/stop/status): " acao
case "$acao" in
    start|iniciar)   echo "Iniciando serviço..." ;;
    stop|parar)      echo "Parando serviço..." ;;
    status)          systemctl is-active nginx || true ;;
    *)               echo "Opção inválida: $acao" >&2; exit 1 ;;
esac
```

```sh
# Lê um arquivo linha a linha preservando espaços
while IFS= read -r linha; do
    echo "-> $linha"
done < usuarios.txt

for i in {1..5}; do echo "volta $i"; done
```

## Boas práticas

- Cite as variáveis dentro dos laços: `"$arquivo"` protege nomes com espaços.
- Prefira globbing (`*.txt`) a parsear a saída de `ls`.
- Use `read -r` sempre: sem ele, barras invertidas são interpretadas.
- Agrupe padrões equivalentes no case: `start|iniciar)`.
- Garanta um caminho de saída no while (`break`) para evitar laços infinitos.

## Armadilhas comuns

- `for x in $(ls)` quebra com nomes contendo espaços.
- Esquecer o `;;` entre os casos do `case` causa erro de sintaxe.
- Variáveis alteradas dentro de `cmd | while read` rodam em subshell e se perdem.
- `{1..10}` não existe em sh POSIX; use `seq` ou `for (( ))`.
- Sem `[[ -e $f ]] || continue`, o literal `*.jpeg` vira iteração quando nada casa.

## Relacionadas

- [[Condicionais-e-Testes]]
- [[Entrada-Saida-e-Redirecionamento]]
- [[Funcoes-e-Argumentos]]
- [[Shell]]
