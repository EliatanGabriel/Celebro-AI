---
type: verbete
area: referencias
status: active
created: "2026-08-22"
updated: "2026-08-22"
---

# Git-Rebase

#area/referencias #referencias/glossario

**Definição:** re-aplica seus commits sobre outro ponto da história, como se você tivesse começado dali. Diferente do merge (que junta duas linhas com um commit extra), o rebase reescreve a linha do tempo linearmente. Regra de ouro: **nunca rebasie commits já publicados e compartilhados** — só branches locais ou seu PR pessoal.

**Exemplo:** `git pull --rebase origin main` na sua feature pega os commits novos da main e empilha os seus em cima, sem commit de merge poluindo o histórico.

**Ver também:** [[Git-comandos-dia-a-dia]]
