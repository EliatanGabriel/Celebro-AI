---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# VS-Code

#area/trabalho #trabalho/ferramentas #conceito

**Resumo:** Editor de código leve e extensível da Microsoft, usado pelo QA para depurar testes, inspecionar código e validar mudanças antes de reportar bugs.

## Conceitos-chave
- **Extensões:** complementos que adicionam lint, formatação, suporte a idiomas e integração com ferramentas de teste.
- **IntelliSense:** autocompletar e navegação de símbolos; ajuda a ler o código que valida.
- **Debug (launch.json):** breakpoints e inspeção de variáveis para investigar por que um teste falha.
- **Terminal integrado:** rodar comandos, testes e docker sem sair do editor.
- **Git integrado:** diff, blame e criação de PRs direto no editor.
- **Workspace settings / tasks:** configurações do projeto e atalhos de build/teste compartilhados pelo time.

## Exemplos
- Rodar um teste do Playwright com breakpoint: criar `launch.json` com `"program": "node_modules/.bin/playwright"` e debugar o teste que falha.
- Investigar erro de seletor: usar `F12` (Go to Definition) no seletor CSS para conferir o elemento no código.
- Comparar duas versões: `View: Compare with Saved` para ver o diff de arquivos alterados.
- Buscar onde um texto é usado: `Ctrl+Shift+F` em toda a workspace antes de assumir que a string mudou.

## Boas práticas
- Instalar extensões úteis para QA: ESLint, Prettier, Docker, REST Client, GitLens e as extensões oficiais do Playwright/Cypress.
- Configurar `launch.json` e `tasks.json` no `.vscode` para o time compartilhar os mesmos comandos de teste.
- Usar o terminal integrado com o projeto já aberto na raiz, evitando erros de caminho relativo.
- Ativar `editor.formatOnSave` apenas se o time adotar o mesmo formatter.
- Aproveitar o Debug Console para avaliar expressões e confirmar hipóteses antes de reportar o bug.

## Armadilhas comuns
- Confundir o workspace de um projeto com outro quando há múltiplas pastas abertas.
- Rodar testes no terminal errado (PowerShell vs bash no Windows).
- Depender de extensões que não estão no `extensions.json` do projeto, causando ambiente divergente.
- Modificar arquivos com auto-fix que alteram código além da mudança em questão.
- Esquecer de recarregar a janela após instalar extensão ou alterar settings.

## Relacionadas
- [[Trabalho]]
- [[Terminal]]
- [[Playwright]]
- [[Cypress]]
- [[GitHub-Actions]]