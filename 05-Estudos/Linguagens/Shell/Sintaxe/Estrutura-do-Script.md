---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Estrutura do Script em Shell

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Todo script começa com um shebang que define o intérprete, precisa de permissão de execução e ganha robustez com `set -euo pipefail`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `#!/bin/bash` | Shebang: roda com Bash (arrays, `[[ ]]`) | Primeira linha do script |
| `#!/bin/sh` | Shebang POSIX: mais portável, menos recursos | Scripts simples e portáveis |
| `chmod +x script.sh` | Concede permissão de execução | `chmod +x backup.sh` |
| `./script.sh` | Executa respeitando o shebang | Exige `+x` |
| `bash script.sh` | Executa passando ao Bash explicitamente | Dispensa permissão |
| `source script.sh` | Executa no shell atual (sem subprocesso) | Recarregar aliases/vars |
| `# comentário` | Comentário até o fim da linha | `# TODO: validar entrada` |
| `set -euo pipefail` | Modo estrito: sai em erro, var indefinida, pipe falho | Topo do script |
| `.sh` | Extensão convencional de scripts shell | `deploy.sh` |

## Exemplos

```sh
#!/bin/bash
# backup.sh - copia as configs para ~/backups com data no nome
set -euo pipefail

DESTINO="$HOME/backups"
mkdir -p "$DESTINO"
cp -r "$HOME/.config" "$DESTINO/config-$(date +%F)"
echo "Backup concluído em $DESTINO"
```

```sh
# Formas de executar o mesmo script
chmod +x backup.sh   # concede execução (uma vez só)
./backup.sh          # usa o shebang da primeira linha
bash backup.sh       # força o intérprete, dispensa chmod
source ~/.bashrc     # roda no shell atual, sem processo novo
```

## Boas práticas

- Comece sempre com shebang; sem ele o comportamento depende do chamador.
- Ative `set -Eeuo pipefail` no topo para falhar cedo e alto.
- Comente o porquê das decisões, não o que já é óbvio.
- Sempre cite variáveis: `"$ARQUIVO"` evita surpresas com espaços.
- Nomeie scripts com verbo + objeto: `limpar_logs.sh`, `backup_db.sh`.

## Armadilhas comuns

- `./script.sh` sem `chmod +x` dá "Permission denied".
- Usar recursos do Bash (`[[ ]]`, arrays) sob `#!/bin/sh` quebra no dash.
- Arquivos salvos com fins de linha Windows (CRLF) fazem o shebang falhar.
- `source` roda no seu shell: pode sobrescrever variáveis e funções atuais.
- Script sem shebang funciona "de vez em quando" dependendo de quem chama.

## Relacionadas

- [[Variaveis-e-Expansoes]]
- [[Condicionais-e-Testes]]
- [[Shell]]
