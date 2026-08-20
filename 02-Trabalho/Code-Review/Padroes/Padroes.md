---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Padroes

#area/trabalho #trabalho/code-review #conceito

**Resumo:** Convenções de código e arquitetura seguidas pelo time.

## Conceitos-chave
- Estilo: formatação, nomenclatura e organização.
- Arquitetura: camadas, separação de responsabilidades.
- Nomenclatura: padrão de nomes para arquivos, funções, variáveis.
- Convenções: imports, tratamento de erros, testes.
- Consistência: mesmo padrão em todo o projeto.

## Exemplos
```
# Exemplos de convenções comuns de time
- Nomes de arquivos em kebab-case ou PascalCase (conforme stack)
- Functions com verbo + substantivo: buscarUsuario, salvarPedido
- Componentes em PascalCase: LoginForm, CartList
- Testes ao lado do código ou em pasta __tests__ (definir e manter)
- Mensagens de commit seguindo Conventional Commits
```

## Boas práticas
- Documentar os padrões adotados pelo time.
- Seguir os padrões existentes mesmo em código novo.
- Aplicar padrões no review de forma consistente.
- Revisar e evoluir os padrões periodicamente.
- Configurar ferramentas automáticas (linters, formatters).

## Armadilhas comuns
- Padrões não documentados, aplicados de forma arbitrária.
- Misturar estilos entre arquivos do mesmo projeto.
- Mudar padrões sem alinhar com o time.
- Bloquear reviews por estilo quando o padrão não é oficial.
- Não usar linters/formatters configurados.

## Relacionadas
- [[Best-practices]]
- [[Refatoracao]]
- [[Readability]]