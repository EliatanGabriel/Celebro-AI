---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Logica

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Raciocínio estruturado baseado em proposições verdadeiras ou falsas e regras de inferência, que fundamenta a tomada de decisão na programação.

## Conceitos-chave
- **Proposições:** afirmações que podem ser avaliadas como verdadeiras (true) ou falsas (false).
- **Operadores booleanos:** `AND` (e), `OR` (ou) e `NOT` (não) combinam proposições; existem tabelas-verdade para definir os resultados.
- **Operadores de comparação:** `==`, `!=`, `>`, `<`, `>=`, `<=` produzem valores booleanos.
- **Condicionais:** `if`/`else`/`elif` desviam o fluxo de execução conforme uma condição.
- **Curto-circuito:** em `A and B`, se A é falso, B não é avaliado; em `A or B`, se A é verdadeiro, B não é avaliado — útil e também causa de bugs.
- **Lógica booleana na prática:** validação de entradas, flags de estado, permissões e filtros.
- **De Morgan:** `not (A and B)` equivale a `not A or not B`; `not (A or B)` equivale a `not A and not B`.

## Exemplos
```javascript
const idade = 20;
const temCarteira = true;

// Condicional composta
if (idade >= 18 && temCarteira) {
  console.log("Pode dirigir");
} else {
  console.log("Não pode dirigir");
}

// Curto-circuito: sem o curto-circuito, se lista for null,
// acessar .length lançaria erro
if (lista && lista.length > 0) {
  console.log("Tem itens");
}
```

```text
// Tabela-verdade de AND e OR
A     B     A AND B    A OR B
true  true  true       true
true  false false      true
false true  false      true
false false false      false

// De Morgan
not (A and B) = (not A) or (not B)
not (A or B)  = (not A) and (not B)
```

## Boas práticas
- Simplificar condições complexas usando De Morgan e extraindo funções nomeadas.
- Usar parênteses explícitos em expressões longas para evitar ambiguidade.
- Aproveitar o curto-circuito para proteção contra null/undefined.
- Escrever condições na ordem mais provável/barata primeiro.

## Armadilhas comuns
- Confundir atribuição (`=`) com comparação (`==`/`===`).
- Aplicar De Morgan de forma errada e inverter os operadores.
- Esquecer que `not` tem precedência menor que comparações e operadores aritméticos.
- Assumir que `||` sempre retorna booleano; em JS retorna o primeiro valor truthy.
- Ignorar o curto-circuito e avaliar operandos com efeitos colaterais.

## Relacionadas
- [[Algoritmos]]
- [[Logica-de-Programacao]]
- [[Programacao]]
- [[Tipos-de-Dados]]
- [[Debug]]
- [[Computacao]]