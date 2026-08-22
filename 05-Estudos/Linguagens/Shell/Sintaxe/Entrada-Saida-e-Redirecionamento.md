---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Entrada, Saída e Redirecionamento em Shell

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Scripts conversam via stdin/stdout/stderr; `read` captura entradas, e operadores como `>`, `>>`, `2>&1` e pipes diretam esses fluxos.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `echo "txt"` | Imprime uma linha | `echo "Olá, $USER"` |
| `printf "fmt" args` | Saída formatada, sem `\n` automático | `printf "%s=%s\n" k v` |
| `read var` | Lê uma linha do stdin | `read nome` |
| `read -p "msg" var` | Lê exibindo um prompt | `read -p "Senha: " senha` |
| `>` / `>>` | Redireciona stdout sobrescrevendo / anexando | `ls > lista.txt` |
| `< arquivo` | Redireciona stdin a partir de arquivo | `wc -l < notas.txt` |
| `2> arquivo` / `2>&1` | Captura stderr / junta stderr ao stdout | `cmd > tudo.log 2>&1` |
| `&>/dev/null` | Descarta stdout e stderr juntos | `ping -c1 host &>/dev/null` |
| `cmd1 \| cmd2` | Pipe: stdout vira stdin do próximo | `cat log \| grep erro` |
| `tee arquivo` | Mostra na tela e grava ao mesmo tempo | `make 2>&1 \| tee build.log` |
| `<<EOF ... EOF` | Heredoc: bloco de texto multilinha | Gerar arquivos de config |

Fluxos padrão: `0` é stdin, `1` é stdout, `2` é stderr.

## Exemplos

```sh
#!/bin/bash
set -euo pipefail

read -rp "Nome do projeto: " projeto
printf "Criando '%s'...\n" "$projeto"
mkdir -p "$projeto"

cat <<EOF > "$projeto/README.md"
# $projeto

Gerado em $(date +%F) por $USER.
EOF

echo "Concluído." | tee -a "$projeto/log.txt"
```

```sh
grep -i erro app.log > erros.txt      # só stdout vai para o arquivo
grep -i erro app.log 2> falhas.log    # erros vão para outro arquivo
ls pasta_inexistente &>/dev/null || echo "Pasta ausente"
```

## Boas práticas

- Prefira `printf` em scripts portáveis; `echo` varia entre shells.
- Use `>>` para logs acumulados; `>` apaga o conteúdo anterior.
- Separe stderr (`2>`) quando depurar; mantenha o stdout limpo para pipes.
- Use `tee` para ver a saída e salvar ao mesmo tempo.
- Feche heredocs com `EOF` sozinho na linha, sem indentação.

## Armadilhas comuns

- `>` sobrescreve o destino sem aviso nem confirmação.
- `cmd > out 2>&1` e `cmd 2>&1 > out` fazem coisas diferentes: a ordem importa.
- Variável sem aspas no `echo` colapsa espaços múltiplos da saída.
- `read -p` não existe em sh POSIX; use `printf "msg"; read var`.
- Esquecer o fluxo `2` faz mensagens de erro aparecerem misturadas no pipe.

## Relacionadas

- [[Variaveis-e-Expansoes]]
- [[Loops-e-Case]]
- [[Comandos-Essenciais]]
- [[Shell]]
