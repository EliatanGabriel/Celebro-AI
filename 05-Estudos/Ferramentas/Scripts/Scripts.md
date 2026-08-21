---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Scripts

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Programas pequenos (shell, Python, etc.) que automatizam tarefas repetitivas de desenvolvimento e operação — builds, backups, deploys, processamento de dados —, muitas vezes agendados por cron ou invocados por Makefile.

## Conceitos-chave
- **Shebang**: primeira linha (`#!/usr/bin/env bash` ou `#!/usr/bin/env python3`) que define o interpretador.
- **Exit codes**: `0` sucesso, diferente de `0` erro; usado por chamadores (cron, CI, make) para decidir.
- **Argumentos e opções**: `$@`, `$1..$n`, `getopts`/`argparse` para parâmetros e flags.
- **Robustez**: `set -euo pipefail` (bash) para abortar em erro, tratar variáveis não definidas e falhas de pipe.
- **Pipes e redirecionamento**: composição de comandos e captura de saída/erro (`>`, `2>&1`, `| tee`).
- **Ambiente**: PATH, variáveis, cwd; scripts devem ser explícitos sobre o ambiente em que rodam.
- **Agendamento**: integração com cron, Makefile, systemd timers ou CI para execução recorrente.

## Exemplos
Script bash robusto:

```bash
#!/usr/bin/env bash
set -euo pipefail

ORIGEM=${1:-./build}
DESTINO=${2:-/backup}

if [[ ! -d "$ORIGEM" ]]; then
  echo "Diretório $ORIGEM não existe" >&2
  exit 1
fi

tar -czf "$DESTINO/$(date +%F).tar.gz" -C "$ORIGEM" .
echo "Backup criado em $DESTINO"
```

Script Python com argparse:

```python
#!/usr/bin/env python3
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("origem")
parser.add_argument("destino")
args = parser.parse_args()

shutil.copytree(args.origem, args.destino, dirs_exist_ok=True)
print(f"Copiado {args.origem} -> {args.destino}")
```

## Boas práticas
- Use `set -euo pipefail` e valide argumentos de entrada com mensagens claras.
- Faça logs com timestamps e redirecione stderr para capturar erros em arquivo.
- Teste o script manualmente antes de agendar com cron/CI (mesmas variáveis de ambiente).
- Mantenha scripts pequenos e um objetivo por script; refatore funções para reuso.
- Trate caminhos relativos com base no diretório do próprio script (`$(dirname "$0")`).

## Armadilhas comuns
- Rodar script com `sh` (dash) que usa sintaxe de bash (`[[ ]]`, arrays) e falhar.
- Comandos com espaços ou globs que expandem inesperadamente sem aspas corretas.
- Esquecer de checar exit code fazendo a automação "passar" mesmo com erro.
- Depender de PATH de usuário que não existe no cron/CI.
- Fazer `rm -rf` com variáveis vazias ou globs não expandidos, apagando diretórios errados.

## Relacionadas
- [[Cron]]
- [[Makefile]]
- [[Terminal]]
- [[Ferramentas-CLI]]
- [[Wget]]