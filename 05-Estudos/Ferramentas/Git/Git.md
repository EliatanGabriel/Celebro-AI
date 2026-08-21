---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Git

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Sistema de controle de versão distribuído criado por Linus Torvalds, padrão da indústria; cada clone contém o histórico completo e o fluxo gira em torno de commits, branches e merges.

## Conceitos-chave
- **Snapshot vs. delta**: o Git guarda snapshots do conteúdo (blobs) mais árvores de diretórios; commits apontam para a árvore e para o commit pai.
- **Áreas**: working tree (arquivos), index/staging (área de preparação) e repositório (objetos e refs).
- **Commit**: unidade de mudança com hash SHA-1, autor, mensagem e metadados; imutável após criado.
- **Branches**: ponteiros móveis para commits; `main`/`master` é a branch padrão, o HEAD indica a branch atual.
- **Merge e rebase**: integrar ramos; `rebase` reescreve histórico (não fazer em branches compartilhadas).
- **Remotes**: repositórios remotos (origin) com `push`/`pull`/`fetch`; no push, `-u` define o upstream.
- **Stash e reset**: `git stash` guarda mudanças temporárias; `git reset --soft/--mixed/--hard` move o HEAD e o index de formas diferentes.

## Exemplos
Fluxo básico:

```bash
git init
git add arquivo.txt
git commit -m "Adiciona arquivo.txt"
git branch -M main
git remote add origin https://github.com/usuario/repo.git
git push -u origin main
```

Branches e histórico:

```bash
git checkout -b feature/novo-recurso
git log --oneline --graph --all
git diff HEAD~1 -- arquivo.txt
git merge --no-ff feature/novo-recurso
```

Corrigir erros:

```bash
git stash push -m "wip temporario"
git reset --hard HEAD~1        # descarta o último commit (cuidado)
git revert <hash>              # desfaz de forma segura com novo commit
```

## Boas práticas
- Faça commits pequenos e atômicos, com mensagens claras no padrão do time (ex.: Conventional Commits).
- Commit apenas mudanças relacionadas; revise com `git diff` e `git status` antes de `git add`.
- Use `git pull --rebase` para manter histórico linear e evitar merges acidentais.
- Nunca force push em branches compartilhadas; prefira `revert` para desfazer.
- Adicione um `.gitignore` adequado (vendor, node_modules, `.env`) para não versionar artefatos e segredos.

## Armadilhas comuns
- `git pull` criando merge commits desnecessários quando a branch local diverge.
- Confundir `reset` (move HEAD) com `revert` (novo commit que desfaz).
- Mensagens de commit genéricas ("update", "fix") que dificultam o rastreamento (git blame/bisect).
- Commit de arquivos sensíveis (`.env`) que vazam segredos — o histórico precisa ser reescrito.
- `git push` com conflito de upstream ou fast-forward recusado; entenda a mensagem de erro antes de forçar.

## Relacionadas
- [[GitHub]]
- [[GitLab]]
- [[VS-Code]]