---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Evidencias

#area/trabalho #trabalho/bug-report #conceito

**Resumo:** Registros (prints, vídeos, logs) que comprovam a ocorrência do bug.

## Conceitos-chave
- Evidência é a prova objetiva do comportamento incorreto observado.
- Complementa os passos de reprodução, reduzindo ambiguidade e retrabalho.
- Pode ser visual (print/vídeo), textual (log/console) ou de rede (request/response).

## Estrutura de um bom bug report
- **Screenshot/gravação** do momento do erro, destacando o elemento relevante.
- **Console do navegador:** mensagens de erro, warnings e stack traces.
- **Logs de servidor** e resposta HTTP (status code, corpo da requisição/resposta).
- Descrição do contexto: quando a evidência foi capturada e em qual ambiente.
- Dados sensíveis mascarados antes de anexar.

## Boas práticas
- Capturar evidência sempre que possível, mesmo que o bug não reproduza de novo.
- Preferir gravação curta que mostre o passo que dispara o erro.
- Incluir data/hora e versão do sistema na evidência.
- Mascarar senhas, tokens e dados pessoais.

## Armadilhas comuns
- Print de tela cheia sem destacar onde está o problema.
- Log colado sem contexto (data, endpoint, usuário).
- Evidência de ambiente diferente do descrito no report.
- Anexar arquivo ilegível, cortado ou de baixa resolução.

## Relacionadas
- [[Steps-to-reproduce]]
- [[Ambiente]]
- [[Expected-vs-actual]]