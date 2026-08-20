---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Editor

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Ferramenta para editar código-fonte, variando de editores leves (VS Code, Vim, Sublime) a IDEs completas (IntelliJ, Eclipse) com IntelliSense, debug, refatoração e integração com o ecossistema da linguagem.

## Conceitos-chave
- **Editor vs. IDE**: editores focam em escrita rápida com plugins; IDEs agregam compilação, análise de código, debug e execução de testes integrados.
- **IntelliSense / Language Server**: autocompletar, go-to-definition e diagnósticos via Language Server Protocol (LSP), padrão usado por VS Code, Neovim e outros.
- **Extensões/Plugins**: funcionalidades adicionais (linters, formatters, snippets, temas, integração com ferramentas).
- **Atalhos e produtividade**: multicursor, busca/replace com regex, formatar documento, renomear símbolos, paleta de comandos.
- **Configuração**: settings JSON, keybindings e dotfiles que tornam o ambiente reproduzível entre máquinas.
- **Integração Git**: view de diff, staging e resolução de conflitos embutida nos editores modernos.

## Exemplos
Atalhos comuns (VS Code / Neovim):

```text
Ctrl+P            # abrir arquivo por nome
Ctrl+Shift+P      # paleta de comandos
Alt+Click         # cursor múltiplo
Shift+Alt+F       # formatar documento (VS Code)
gg=G              # reindentar arquivo inteiro (Vim)
```

Settings.json exemplo (VS Code):

```json
{
  "editor.formatOnSave": true,
  "editor.renderWhitespace": "all",
  "files.trimTrailingWhitespace": true,
  "editor.rulers": [100]
}
```

## Boas práticas
- Versionar as configurações do editor (`.vscode/settings.json`, `.editorconfig`, dotfiles) junto com o projeto.
- Padronizar formatação com Prettier/rustfmt/black e hook de pre-commit para evitar ruído de diffs.
- Aprender e praticar os atalhos principais em vez de navegar só pelo mouse.
- Mantenha poucas extensões ativas e conhecidas; cada uma adiciona superfície de erro e atraso.
- Use o LSP/Debugger nativo em vez de depender de plugins duplicados que conflitam.

## Armadilhas comuns
- Formatação automática com configurações locais divergentes gera diffs gigantes no Git.
- Adotar extensões abandonadas/desatualizadas causa falhas silenciosas no IntelliSense.
- Confundir workspace com editor: o editor certo depende do contexto (CLI vs. GUI, linguagem, projeto).
- Atalhos diferentes entre editores atrapalham a migração; use keymaps de compatibilidade se necessário.
- Rodar muitas ferramentas de análise em paralelo (ESLint + Prettier + TS) pode duplicar ou conflitar correções.

## Relacionadas
- [[Vim]]
- [[VS-Code]]
- [[IntelliJ]]
- [[Eclipse]]