---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Readability

#area/trabalho #trabalho/code-review #conceito

**Resumo:** Facilidade de ler e compreender o código por outros desenvolvedores.

## Conceitos-chave
- Clareza: intenção evidente ao ler o código.
- Nomes expressivos para variáveis, funções e classes.
- Comentários que explicam o porquê, não o que.
- Estrutura organizada com funções pequenas e coesas.
- Simplicidade sobre complexidade desnecessária.

## Exemplos
```
// Difícil de ler
if (u) { if (u.a > 0 && u.b !== null) { return true; } }
return false;

// Legível
const usuarioTemEnderecoCompleto = (usuario) =>
  usuario.ativo && usuario.endereco != null;
```

## Boas práticas
- Nomear pelo propósito: calcularTotal, obterUsuarioAtivo.
- Quebrar funções longas em funções menores e nomeadas.
- Manter consistência de estilo e convenções do time.
- Remover código morto e comentários redundantes.
- Revisar como se o autor não estivesse disponível para explicar.

## Armadilhas comuns
- Código "esperto" e compacto demais para ser legível.
- Comentários que repetem o código e enganam quando o código muda.
- Nomes abreviados ou genéricos (dados, x, tmp).
- Funções com muitas responsabilidades.
- Adiar a melhoria de legibilidade "para depois" na revisão.

## Relacionadas
- [[Best-practices]]
- [[Padroes]]
- [[Refatoracao]]