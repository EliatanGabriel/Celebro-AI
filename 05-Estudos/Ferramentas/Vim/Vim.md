---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Vim

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Editor de texto modal, leve e altamente configurável, presente no terminal em praticamente qualquer Unix; baseia-se em modos (normal, insert, visual, command) e em composição de atalhos para edição extremamente rápida.

## Conceitos-chave
- **Modos**: Normal (navegação/comandos), Insert (digitação), Visual (seleção), Command-line (`:`).
- **Composição**: atalhos como verbo + objeto/movimento (ex.: `d2w` = delete 2 words); `d`=delete, `c`=change, `y`=yank, `p`=paste.
- **Movimentos**: `h j k l`, `w`/`b` (palavras), `{`/`}` (parágrafos), `gg`/`G` (início/fim), `0`/`$`.
- **Configuração**: arquivo `~/.vimrc` (ou `init.vim`/`init.lua` no Neovim) com options, mappings e plugins.
- **Plugins**: gerenciadores como vim-plug, lazy.nvim; Neovim é o fork moderno com Lua e LSP integrado.
- **Registers e macros**: registro (`"a`) armazena texto; `q` grava e reproduz macros de comandos.
- **Modos de busca/substituição**: `/pattern`, `:s/antigo/novo/g` com regex.

## Exemplos
Abrir e salvar:

```bash
vim arquivo.txt
# Esc (modo normal) e:
:wq   # salva e sai
:q!   # sai sem salvar
```

Edição rápida:

```vim
" no modo normal:
dd        " apaga a linha atual
yy p      " copia a linha e cola
ciw       " altera a palavra sob o cursor
:%s/foo/bar/g   " substitui todas as ocorrências
gg=G      " reindenta o arquivo inteiro
```

Configuração mínima (`~/.vimrc`):

```vim
set number
set tabstop=2 shiftwidth=2 expandtab
set hlsearch
filetype plugin indent on
```

## Boas práticas
- Pratique movimentos antes de plugins: a base de Vim é a composição de comandos.
- Configure de forma incremental e versionada (dotfiles); evite configs gigantes sem entendimento.
- Use Neovim ou Vim + plugins para LSP (completar, diagnóstico) se for trabalhar com projetos grandes.
- Aprenda a sair: `:q`, `:q!`, `:wq` — e `:wqa` para vários buffers.
- Use registradores e macros para edições repetitivas em vez de recomeçar.

## Armadilhas comuns
- Ficar preso no modo Insert sem saber voltar (`Esc`); use `jj` ou `Ctrl+C` como mapping.
- Editar sem `expandtab` mistura tabs/espaços e quebra o lint do projeto.
- Plugins sem gerenciador deixam o vimrc frágil e difícil de migrar.
- Atalhos do modo Normal vs. Insert confusos para iniciantes; prática é essencial.
- Esquecer que `d` é destrutivo (a palavra vai para o registro) — verifique antes de macros.

## Relacionadas
- [[Terminal]]
- [[Linux]]
- [[Editor]]
- [[Zsh]]