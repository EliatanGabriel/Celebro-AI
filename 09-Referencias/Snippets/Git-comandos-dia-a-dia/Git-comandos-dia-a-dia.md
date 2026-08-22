---
type: snippet
area: referencias
status: active
created: "2026-08-22"
updated: "2026-08-22"
---

# Git-comandos-dia-a-dia

#area/referencias #referencias/snippets

Comandos Git que resolvem 90% das situações reais de trabalho. Quando usar: qualquer operação além do `add/commit/push` básico.

## Desfazer com segurança

```bash
git restore arquivo.js              # descarta mudanças não commitadas (cuidado: perde tudo)
git restore --staged arquivo.js     # tira do staging, mantém as mudanças
git reset --soft HEAD~1             # desfaz último commit, mantém mudanças staged
git reset --hard HEAD~1             # apaga último commit E as mudanças (destrutivo!)
git revert <hash>                   # cria commit novo desfazendo outro (seguro p/ main)
```

> `--hard` destrói trabalho; em dúvida, `revert`.

## Histórico e investigação

```bash
git log --oneline --graph --all -20     # visual bonito das branches
git log -p caminho/arquivo              # quem mexeu e o quê, linha a linha
git blame arquivo.py                    # autor da última alteração por linha
git bisect start                        # caça binária ao commit que quebrou algo
```

## Stash — guardar sem commitar

```bash
git stash push -m "wip validação"   # guarda com rótulo
git stash list                      # ver o que está guardado
git stash pop                       # recupera o mais recente e apaga da pilha
```

## Corrigindo coisas

```bash
git commit --amend                  # conserta o ÚLTIMO commit (mensagem ou conteúdo)
git checkout -b fix/nome            # nova branch e já muda pra ela
git push --force-with-lease         # force push seguro (falha se alguém empurrou antes)
```

> Nunca `--force` puro em branch compartilhada.
