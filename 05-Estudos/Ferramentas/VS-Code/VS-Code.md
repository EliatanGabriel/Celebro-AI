---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# VS-Code

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Editor de código da Microsoft, leve e extensível, construído sobre Electron e com Language Server Protocol (LSP); é o editor mais popular da atualidade, com terminal integrado, debug e Git embutidos.

## Conceitos-chave
- **Extensões**: marketplace que adiciona suporte a linguagens, linters, formatters, temas e ferramentas (Remote, Docker, GitLens).
- **IntelliSense / LSP**: autocompletar, go-to-definition e diagnósticos por Language Server; extensões como Pylance, vscode-go, tsserver.
- **Terminal integrado**: shells (bash, zsh, PowerShell) com múltiplas abas e integração com o workspace.
- **Debug**: launch configurations (`launch.json`) com breakpoints, watches, variáveis e consoles por linguagem.
- **Git integrado**: view de source control, staging, diffs, branches e resolução de conflitos.
- **Tasks e Dev Containers**: tasks.json automatiza comandos; Dev Containers rodam ambientes completos em containers.
- **Settings e workspace**: `settings.json`, `.vscode/` versionado no projeto, keybindings e perfis.

## Exemplos
`launch.json` para debugar Node.js:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Iniciar app",
      "program": "${workspaceFolder}/src/index.js",
      "outFiles": ["${workspaceFolder}/dist/**/*.js"]
    }
  ]
}
```

Task de build:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "testes",
      "type": "shell",
      "command": "npm test",
      "group": "test"
    }
  ]
}
```

Settings recomendadas por projeto (`.vscode/settings.json`):

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "files.exclude": { "**/node_modules": true }
}
```

## Boas práticas
- Versionar `.vscode/` (settings, extensions.json) para padronizar o ambiente do time.
- Manter poucas extensões e habilitar apenas as necessárias ao projeto.
- Aprender os atalhos-chave: `Ctrl+Shift+P` (paleta), `Ctrl+P` (arquivos), `F5` (debug).
- Usar workspaces multi-root para monorepos e Dev Containers para ambientes reprodutíveis.
- Configurar formatadores/linters no save para manter código consistente sem esforço.

## Armadilhas comuns
- Extensões desatualizadas ou conflitantes quebrando IntelliSense de forma silenciosa.
- `formatOnSave` com formatter errado sobrescrevendo o estilo do projeto.
- `launch.json` com caminhos absolutos que não funcionam em outra máquina.
- Esquecer de sincronizar settings quando muda o time/idioma da base de código.
- Terminal integrado usando shell/config de usuário diferente do esperado nos scripts.

## Relacionadas
- [[Terminal]]
- [[Git]]
- [[Ferramentas]]
- [[Editor]]