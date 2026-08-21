---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Shell

#area/estudos #estudos/linguagens #conceito

**Resumo:** Interface de linha de comando e linguagem de script dos sistemas Unix-like (sh, bash, zsh), usada para automação, pipelines e administração de sistemas.

## Conceitos-chave
- Paradigma imperativo de script, orientado a comandos externos e utilitários POSIX.
- Tipagem dinâmica fraca: variáveis são textos; números são tratados por utilitários como `test`/`awk`.
- Interpretada pelo shell (POSIX sh, bash, zsh, dash); cada shell tem extensões próprias.
- Uso principal em automação de rotinas, inicialização de sistemas, pipelines e tarefas de DevOps.
- Composição de comandos via pipes (`|`), redirecionamento (`>`, `>>`, `<`, `2>&1`) e subshells.
- Código de saída (`$?`), globbing e variáveis especiais (`$1`, `$@`, `$$`, `$HOME`).
- Particularidade: shell é ao mesmo tempo um REPL interativo e uma linguagem de scripting completa.

## Exemplos
```sh
#!/bin/sh
# Pipeline: arquivos mais recentes
ls -lt /var/log/*.log | head -5

# Condicional com teste
if [ -f "/etc/config.conf" ]; then
    echo "Configuração existe"
else
    echo "Faltando configuração" >&2
fi

# Loop com lista
for servidor in web01 web02 db01; do
    ping -c 1 "$servidor" >/dev/null 2>&1 && echo "$servidor ok" || echo "$servidor fora"
done
```

## Boas práticas
- Prefira scripts POSIX (`#!/bin/sh`) quando precisar de portabilidade entre shells.
- Cite variáveis (`"$1"`) e use `set -eu` para falhar em erros não tratados.
- Verifique sempre o código de saída (`&&`, `||`, `$?`) em comandos críticos.
- Use `trap` para limpeza (temporários, processos) ao sair do script.
- Documente one-liners complexos ou quebre-os em funções.

## Armadilhas comuns
- Esquecer espaços em `[ condição ]` — `[a=b]` falha como comando inválido.
- Variáveis sem aspas se expandem com globbing, quebrando nomes com espaços.
- Em dash/sh, `[[ ]]` e arrays não existem (são do bash); usar `[ ]`.
- Confundir `>` (redirecionar) com `|` (pipe): `cmd > file` grava no arquivo, `cmd | cmd2` encadeia.
- `=` em `if var = valor` gera erro de comando; no `[` a sintaxe é `[ "$var" = "valor" ]`.

## Relacionadas
- [[Bash]]