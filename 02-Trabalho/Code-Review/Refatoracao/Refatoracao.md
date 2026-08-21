---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Refatoracao

#area/trabalho #trabalho/code-review #conceito

**Resumo:** Melhoria da estrutura do código sem alterar seu comportamento.

## Conceitos-chave
- Extrair: quebrar blocos em funções/métodos nomeados.
- Renomear: dar nomes claros e expressivos.
- Simplificar: reduzir condicionais e complexidade.
- Eliminar duplicação e código morto.
- Segurança: refatorar apoiado em testes automatizados.

## Exemplos
```
// Antes
function processar(usuario) {
  if (usuario && usuario.nome) {
    const nome = usuario.nome.trim().toUpperCase();
    console.log(nome);
  }
}

// Depois: extrair e renomear com intenção
function obterNomeMaiusculo(usuario) {
  if (!usuario?.nome) return '';
  return usuario.nome.trim().toUpperCase();
}
```

## Boas práticas
- Refatorar em mudanças pequenas e verificáveis.
- Ter testes cobrindo o comportamento antes de refatorar.
- Manter o comportamento funcional idêntico após a mudança.
- Combinar refatoração com revisão de legibilidade e padrões.
- Separar refatoração de mudança de funcionalidade.

## Armadilhas comuns
- Refatorar e mudar comportamento no mesmo commit.
- Refatorar sem testes, introduzindo regressões silenciosas.
- Extrair abstrações precoces e desnecessárias.
- Renomear símbolos amplamente usados sem cuidado.
- Refatoração grande demais para ser revisada.

## Relacionadas
- [[Readability]]
- [[Best-practices]]