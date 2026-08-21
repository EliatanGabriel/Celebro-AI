---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Best-practices

#area/trabalho #trabalho/code-review #conceito

**Resumo:** Boas práticas de codificação adotadas para legibilidade e qualidade.

## Conceitos-chave
- Clean code: código simples, claro e com intenção.
- Nomes expressivos e consistentes.
- Funções curtas com uma única responsabilidade.
- DRY: evitar duplicação de lógica.
- Convenções do time: formatação, imports, estrutura.

## Exemplos
```
// Padrão de função curta e nomeada
function calcularDesconto(total) {
  if (total < 0) throw new Error('Total inválido');
  return total >= 100 ? total * 0.1 : 0;
}

// Evitar duplicação (DRY)
function formatarMoeda(valor) {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(valor);
}
```

## Boas práticas
- Seguir o estilo e as convenções já adotadas no repositório.
- Preferir código explícito a truques ou abreviações.
- Manter funções pequenas e testáveis.
- Validar entradas no início das funções.
- Tratar erros de forma consistente com o resto do sistema.

## Armadilhas comuns
- Forçar refatoração "limpa" sem contexto do domínio.
- DRY levado ao extremo, criando abstrações precoces.
- Copiar padrões de outra linguagem sem adaptar.
- Estilo divergente entre arquivos do mesmo projeto.
- Ignorar testes ao adotar boas práticas de estrutura.

## Relacionadas
- [[Readability]]
- [[Padroes]]
- [[Refatoracao]]