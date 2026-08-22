---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Variáveis e Expansões em Shell

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Variáveis guardam textos sem espaços no `=`, são expandidas com `$VAR` ou `${VAR}`, e aspas controlam quando a expansão acontece.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `VAR=valor` | Atribuição (sem espaços ao redor do `=`) | `NOME="Ana"` |
| `$VAR` / `${VAR}` | Expansão; chaves delimitam o nome | `"${ARQ}_old.txt"` |
| `"$VAR"` | Aspas duplas preservam espaços e expandem | `echo "$MSG"` |
| `'$VAR'` | Aspas simples: tudo literal, sem expansão | `echo '$HOME'` |
| `$HOME $PATH $USER` | Variáveis de ambiente do sistema | `cd "$HOME"` |
| `$(comando)` | Substituição de comando (captura a saída) | `HOJE=$(date +%F)` |
| `$(( expressao ))` | Aritmética inteira | `TOTAL=$((preco * qtd))` |
| `${VAR:-padrao}` | Usa padrão se VAR vazia/inexistente | `"${PORTA:-8080}"` |
| `readonly VAR` | Torna a variável somente leitura | `readonly VERSAO="1.0"` |
| `export VAR` | Exporta para processos filhos | `export EDITOR=vim` |

## Exemplos

```sh
#!/bin/bash
set -euo pipefail

USUARIO="${1:-$USER}"          # argumento recebido ou usuário atual
SAUDACAO="Olá, ${USUARIO}!"    # ${} delimita o nome ao concatenar
HOJE=$(date +%F)               # saída do date vira valor da variável
DIAS=$((7 * 4))                # aritmética inteira

echo "$SAUDACAO Hoje é $HOJE. Total: $DIAS dias."
export APP_ENV="producao"      # visível para subprocessos
readonly VERSAO="1.0"          # constante do script
```

```sh
ARQUIVO="relatorio final.txt"
cp "$ARQUIVO" "${ARQUIVO%.txt}_backup.txt"   # remove sufixo .txt
echo '$HOME imprime literal'                 # sem expansão
```

## Boas práticas

- Nunca deixe espaços ao redor do `=` na atribuição.
- Sempre use aspas duplas nas expansões: `"$VAR"` evita quebra com espaços.
- Use `${VAR}` quando concatenar com outros caracteres: `"${ARQ}.bak"`.
- Convenção: MAIÚSCULAS para ambiente/export, minúsculas para locais.
- Exporte apenas o necessário; `readonly` protege constantes.

## Armadilhas comuns

- `VAR = valor` tenta executar o comando `VAR`: espaços quebram a atribuição.
- `rm $ARQUIVO` com nome contendo espaços vira dois argumentos distintos.
- Aspas simples impedem toda expansão: `'$HOME'` sai literal na tela.
- `$(( ))` só faz inteiros: divisão `10/3` resulta em `3`.
- Esquecer `export` faz a variável existir só no script, invisível aos filhos.

## Relacionadas

- [[Estrutura-do-Script]]
- [[Entrada-Saida-e-Redirecionamento]]
- [[Condicionais-e-Testes]]
- [[Shell]]
