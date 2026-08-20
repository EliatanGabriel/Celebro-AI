---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Zsh

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Shell moderna e poderosa (padrão no macOS desde Catalina), extensível via plugins e temas; frequentemente usada com Oh My Zsh, oferecendo autocompletar aprimorado, correção de erros e glóbulos (globbing) avançado.

## Conceitos-chave
- **Zsh vs. bash**: sintaxe compatível na maior parte, com melhorias em globbing, autocompletar, arrays e configuração interativa.
- **Oh My Zsh**: framework de configuração com temas e centenas de plugins (git, docker, kubectl, z) que definem aliases e functions.
- **Globbing estendido**: `**` recursivo, `*.(js|ts)` seletores e qualificadores de arquivo (`*.log(N)`, `*(mh-1)`).
- **Prompt e temas**: `PS1` customizado e frameworks (powerlevel10k, starship) com git status no prompt.
- **Autocompletar e history**: completion context-aware, `Ctrl+R` com pesquisa fuzzy (se habilitado), `setopt` para opções como `autocd`.
- **Dotfiles e configuração**: `~/.zshrc` (interativo), `~/.zprofile` (login), plugins via `zplug`/`antigen`/nativo.

## Exemplos
Ativação de opções úteis:

```zsh
setopt auto_cd               # digita o diretório e navega
setopt hist_ignore_all_dups  # histórico sem duplicados
setopt correct_all           # corrige comandos com erro de digitação
```

Globbing avançado:

```zsh
ls **/*.log                 # todos os .log recursivos
rm *.(tmp|bak)              # remove por extensão (extended glob)
print -l *.txt(N)           # (N) evita erro se não houver match
```

Aliases comuns do Oh My Zsh:

```zsh
alias gs='git status'
alias gd='git diff'
alias ll='ls -lah'
alias ..='cd ..'
```

## Boas práticas
- Versionar o `~/.zshrc` e usar um framework (Oh My Zsh) com plugins apenas do que você usa.
- Habilite `autocd`, globs estendidos e histórico com deduplicação para produtividade.
- Customize o prompt para mostrar branch git e diretório atual (powerlevel10k/starship).
- Teste mudanças do `.zshrc` em um shell separado antes de aplicar em todos.
- Use `zsh` interativo + scripts com shebang explícito; scripts críticos em bash/posix são mais portáveis.

## Armadilhas comuns
- `set -euo pipefail` e outras opções do bash não têm o mesmo comportamento no zsh — use shebang correto.
- Globbing estendido não ativo por padrão; scripts dependendo dele quebram sem `setopt extended_glob`.
- Configurar plugins demais deixa o shell lento ao iniciar.
- Compartilhar `.zshrc` com bash sem checar diferenças de sintaxe.
- Comandos com `&&`/`||` com opções interativas do zsh podem exigir `setopt` específicos para retornar corretamente.

## Relacionadas
- [[Terminal]]
- [[Linux]]
- [[Ferramentas-CLI]]
- [[Vim]]