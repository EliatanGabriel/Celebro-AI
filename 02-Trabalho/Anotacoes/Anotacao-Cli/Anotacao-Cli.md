---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Anotacao-Cli

#area/trabalho #trabalho/anotacoes #conceito

**Resumo:** Nota-modelo para registrar comandos de terminal que o QA usa com frequência.

## Como usar
- Criar uma nota por comando ou por grupo de comandos (ambiente, teste, git, docker).
- Registrar o comando exatamente como é executado, com os parâmetros reais do projeto.
- Explicar em uma linha o que o comando faz e quando usá-lo.
- Atualizar quando a versão do projeto mudar os comandos de teste.

## Estrutura
- **Comando:** o texto completo, pronto para copiar.
- **O que faz:** descrição curta do propósito.
- **Quando usar:** situação e contexto (ex.: "antes de iniciar a regressão").
- **Exemplo de saída:** o que esperar ver ao rodar.
- **Variações:** flags úteis e comandos relacionados.

## Dicas
- Teste o comando antes de anotar: um comando errado registrado vira armadilha.
- Anote o diretório de execução quando o comando depender do caminho.
- Agrupe comandos por contexto para achar rápido no vault.
- Converta os comandos mais usados em scripts ou tasks do projeto para reduzir erros de digitação.

## Relacionadas
- [[Terminal]]
- [[Trabalho-Git]]
- [[Docker]]
- [[Trabalho]]