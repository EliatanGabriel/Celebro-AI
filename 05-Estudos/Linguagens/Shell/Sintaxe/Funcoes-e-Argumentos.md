---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Funções e Argumentos em Shell

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Funções organizam o script em blocos reutilizáveis que recebem `$1`, `$2`, ... e sinalizam sucesso ou falha pelo código de retorno.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `nome() { ... }` | Define uma função | `uso() { echo "..."; }` |
| `nome arg1 arg2` | Chama a função com argumentos | `copiar origem dest` |
| `$1 $2 ... ${10}` | Argumentos posicionais da função | `local alvo="$1"` |
| `$#` | Quantidade de argumentos recebidos | `[ $# -eq 2 ]` |
| `"$@"` | Cada argumento como palavra separada | `cp -- "$@" destino/` |
| `"$*"` | Todos os argumentos numa única string | `log "$*"` |
| `local var` | Restringe a variável à função | `local tmp=$(mktemp)` |
| `return N` | Código de saída da função (0 = ok) | `return 1` |
| `$?` | Status do último comando/função | `[ $? -eq 0 ]` |
| `exit N` | Encerra o script inteiro com status | `exit 2` |

## Exemplos

```sh
#!/bin/bash
set -euo pipefail

uso() {
    echo "Uso: $0 <origem> <destino>"
    return 1
}

copiar() {
    local origem="$1" destino="$2"
    if [[ ! -f "$origem" ]]; then
        echo "'$origem' não encontrado" >&2
        return 1
    fi
    cp -- "$origem" "$destino"
}

[[ $# -eq 2 ]] || uso

if copiar "$1" "$2"; then
    echo "Copiado: $1 -> $2"
else
    echo "Falhou com código $?" >&2
fi
```

```sh
# Função que repassa todos os argumentos intactos
log() {
    printf '[%s] %s\n' "$(date +%T)" "$*" >> app.log
}
log "processo iniciado" "com vários" "argumentos"
```

## Boas práticas

- Valide `$1`/`$#` no início da função antes de usá-los.
- Declare tudo possível com `local` para não vazar variáveis globais.
- Retorne 0 em sucesso e valores diferentes de zero em falhas.
- Use a função direto na condição: `if copiar a b; then`.
- Defina as funções antes de chamá-las no fluxo do script.

## Armadilhas comuns

- `return` só aceita números de 0 a 255; para devolver texto, use `echo`.
- Ler `$?` depois de outro comando perde o valor anterior.
- `"$*"` junta os argumentos em uma string e estraga nomes com espaços.
- Faltou `local`: a variável sobrescreveu uma global com o mesmo nome.
- Função chamada antes de ser definida simplesmente não existe ainda.

## Relacionadas

- [[Condicionais-e-Testes]]
- [[Loops-e-Case]]
- [[Estrutura-do-Script]]
- [[Shell]]
