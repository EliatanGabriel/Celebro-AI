---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Condicionais e Testes em Shell

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** `if` decide com base em testes entre `[ ]` ou `[[ ]]`, que comparam números, strings e propriedades de arquivos; `&&` e `||` são os atalhos.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `if [ cond ]; then ... fi` | Condicional básica POSIX | `[ "$n" -eq 10 ]` |
| `if ... elif ... else ... fi` | Cadeia de alternativas | `elif [ "$n" -gt 10 ]; then` |
| `[[ cond ]]` | Versão Bash: aceita `\|\|`, `&&`, regex, sem word splitting | `[[ $s == *ok* ]]` |
| `-eq -ne -lt -le -gt -ge` | Comparações numéricas inteiras | `[ $n -lt 5 ]` |
| `= !=` | Igualdade / diferença de strings | `[ "$s" = "sim" ]` |
| `-z` / `-n` | String vazia / não vazia | `[ -z "$vazio" ]` |
| `-f` / `-d` | É arquivo regular / é diretório | `[ -d /etc ]` |
| `-e -r -w -x` | Existe / legível / gravável / executável | `[ -r "$cfg" ]` |
| `cmd1 && cmd2` | Executa o segundo só se o primeiro passar | `[ -f cfg ] && source cfg` |
| `cmd1 \|\| cmd2` | Executa o segundo só se o primeiro falhar | `cd dir \|\| exit 1` |

## Exemplos

```sh
#!/bin/bash
set -euo pipefail

ARQ="${1:-}"

if [[ -z "$ARQ" ]]; then
    echo "Uso: $0 <arquivo>" >&2
    exit 1
fi

if [[ ! -f "$ARQ" ]]; then
    echo "'$ARQ' não existe." >&2
elif [[ ! -r "$ARQ" ]]; then
    echo "Sem permissão de leitura." >&2
else
    linhas=$(wc -l < "$ARQ")
    if (( linhas > 100 )); then
        echo "$ARQ é grande ($linhas linhas)"
    fi
fi

[[ -d logs ]] && echo "logs/ já existe" || mkdir -p logs
```

```sh
# Guardas em uma linha antes do bloco principal
[ $# -eq 0 ] && { echo "Nenhum argumento" >&2; exit 1; }
```

## Boas práticas

- Deixe espaços dentro dos colchetes: `[ "$x" = "y" ]`, sempre.
- Cite as variáveis nos testes para evitar erros quando vierem vazias.
- Em Bash, prefira `[[ ]]`: mais seguro e mais recursos.
- Use `-z "${VAR:-}"` para testar variável possivelmente indefinida.
- `&&`/`||` são ótimos para guardas curtas; blocos complexos merecem `if`.

## Armadilhas comuns

- `[` sem espaços internos gera mensagens enigmáticas como "command not found".
- Dentro de `[ ]`, `<` e `>` comparam strings (e precisam de escape), não números.
- Variável vazia sem aspas vira erro de sintaxe: "unary operator expected".
- `-eq` compara inteiros; usar com strings falha ("integer expression expected").
- `a && b || c` não é ternário: se `b` falhar, `c` também roda.

## Relacionadas

- [[Variaveis-e-Expansoes]]
- [[Loops-e-Case]]
- [[Funcoes-e-Argumentos]]
- [[Shell]]
