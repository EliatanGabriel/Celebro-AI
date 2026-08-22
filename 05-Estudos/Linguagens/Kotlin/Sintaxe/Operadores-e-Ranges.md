---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Operadores e Ranges (Kotlin)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Kotlin usa operadores aritméticos familiares com divisão dependente de tipo, distingue igualdade estrutural (`==`) da referencial (`===`), e oferece ranges expressivos com `..`, `until`, `downTo` e `step`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `+ - * / %` | Aritmética básica | `7 % 3 // 1` |
| `Int / Int` | Divisão inteira (trunca) | `7 / 2 // 3` |
| `Double / Int` | Divisão real | `7.0 / 2 // 3.5` |
| `==` / `!=` | Igualdade estrutural (equals) | `"a" == s` |
| `===` / `!==` | Igualdade referencial | `obj1 === obj2` |
| `1..10` | Range inclusivo | `for (i in 1..10)` |
| `until` | Exclusivo no fim | `0 until n` |
| `downTo` | Decrescente | `10 downTo 1` |
| `step` | Passo do range | `1..10 step 2` |
| `in` | Pertencimento | `if (x in 1..100)` |

## Exemplos

```kotlin
fun main() {
    println(7 / 2)        // 3  -> divisão inteira entre Int
    println(7 % 2)        // 1
    println(7.0 / 2)      // 3.5 -> Double propaga ponto flutuante

    val a = listOf("k")
    val b = listOf("k")
    println(a == b)       // true  -> mesmo conteúdo
    println(a === b)      // false -> objetos diferentes na memória
}
```

```kotlin
fun main() {
    for (i in 1..5) print(i)          // 12345
    println()
    for (i in 0 until 5) print(i)     // 01234 (exclui o fim)
    println()
    for (i in 10 downTo 1 step 2) print("$i ") // 10 8 6 4 2

    val nota = 85
    if (nota in 90..100) println("Excelente")
    else if (nota in 70 until 90) println("Bom")

    val letra = 'm'
    println(letra in 'a'..'z')        // true
}
```

## Boas práticas

- Use ranges (`in 1..n`) em vez de comparações duplas encadeadas.
- Prefira `until` para limites exclusivos típicos de índices.
- Reserve `===` para depuração de identidade; o dia a dia é `==`.
- Combine `downTo`/`step` para loops decrescentes legíveis.
- Use `charRange` e `longRange` naturalmente; ranges funcionam com Comparable.

## Armadilhas comuns

- Calcular média com `Int / Int` e se surpreender com o truncamento.
- Usar `1..n` quando queria excluir o último valor (use `until`).
- Confundir `==` do Kotlin com referência do Java: aqui é equals por padrão.
- Escrever `10..1` esperando loop decrescente: range vazio, precisa `downTo`.
- Aplicar `%` em Double esperando resto inteiro exato.

## Relacionadas

- [[Kotlin]]
- [[Tipos-e-Null-Safety]]
- [[Controle-de-Fluxo]]
- [[Loops]]
