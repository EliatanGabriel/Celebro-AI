---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Terminal

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Interface de linha de comando (CLI) para interagir com o sistema operacional por meio de um shell (bash, zsh); essencial para desenvolvimento, automação, gerenciamento de servidores e operação de ferramentas como git, docker e kubernetes.

## Conceitos-chave
- **Emulador de terminal vs. shell**: o emulador (GNOME Terminal, iTerm2, kitty) desenha a tela; o shell interpreta os comandos.
- **Shell**: bash, zsh, fish — oferecem scripting, history, autocompletar e variáveis de ambiente.
- **Comandos básicos**: `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`, `cat`, `less`, `man`.
- **Pipes e redirecionamento**: `|` encadeia comandos; `>`, `>>`, `2>&1` redirecionam saída e erro.
- **Variáveis e PATH**: `export`, `$VAR`, `PATH` define onde o shell procura binários.
- **Processos e jobs**: `&` (background), `Ctrl+C` (interromper), `Ctrl+Z`/`fg`/`bg`, `jobs`, `kill`.
- **Produtividade**: aliases, functions, `Ctrl+R` (reverse search), `fzf`, `tmux` para multiplexação de sessões.

## Exemplos
Navegar e manipular arquivos:

```bash
pwd
ls -lah ~/projeto
cd /tmp && mkdir -p trabalho && touch trabalho/nota.txt
cp -r projeto/ projeto-backup/
find . -name "*.log" -mtime +7 -delete
```

Pipelines:

```bash
ps aux | grep nginx | awk '{print $2}'
cat acesso.log | sort | uniq -c | sort -rn | head -20
```

Gerenciar processos:

```bash
my-server &           # roda em background
jobs                  # lista jobs
kill -9 $(pgrep my-server)
```

## Boas práticas
- Aprenda e use `man`, `--help` e `tldr` para descobrir opções sem sair do terminal.
- Crie aliases/functions para comandos longos e mantenha dotfiles versionados.
- Use `Ctrl+R` e `fzf` para reutilizar comandos anteriores sem redigitar.
- Tenha cuidado com `rm -rf`; use `trash-cli` ou confirme caminhos antes de apagar.
- Trabalhe com tmux/screen para manter sessões persistentes em servidores.

## Armadilhas comuns
- Globs que não expandem quando se espera (aspas vs. `*`) gerando argumentos errados.
- Confundir `>` (sobrescreve) com `>>` (anexa) e destruir arquivos.
- Uso de `sudo` em comandos que não precisam, criando arquivos de propriedade errada.
- Achar que `Ctrl+C` cancela tudo — processos em background podem continuar rodando.
- Ficar preso em editores (vim/nano) sem saber sair; `:q!` e `Ctrl+X` são básicos.

## Relacionadas
- [[Linux]]
- [[Zsh]]
- [[Scripts]]
- [[Ferramentas-CLI]]
- [[Curl]]