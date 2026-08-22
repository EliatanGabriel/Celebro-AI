---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Funções (Kotlin)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Funções em Kotlin usam `fun` com parâmetros default, argumentos nomeados, single-expression bodies, `vararg`, e podem ser estendidas via extension functions ou chamadas com infix.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `fun nome(p: T): R` | Declaração completa | `fun soma(a: Int): Int` |
| `p: T = v` | Parâmetro default | `fun oi(nome = "mundo")` |
| `nome(arg = valor)` | Argumento nomeado | `oi(nome = "Ana")` |
| `= expressão` | Single-expression body | `fun dobro(x: Int) = x * 2` |
| `Unit` | Sem retorno útil (implícito) | `fun log(): Unit` |
| `vararg p: T` | Número variável de args | `vararg nums: Int` |
| `fun T.ext()` | Extension function | `fun String.gritar()` |
| `infix fun x.y(z)` | Chamada infix | `2 potencia 3` |

## Exemplos

```kotlin
// Parâmetros default + argumentos nomeados eliminam overloads
fun enviar(destino: String, urgente: Boolean = false, copia: String? = null) {
    println("$destino urg=$urgente copia=$copia")
}

fun main() {
    enviar("ana@email.com")
    enviar("bob@email.com", urgente = true)
    enviar(copia = "ti@x.com", destino = "carol@email.com")
}
```

```kotlin
// Single-expression: corpo é uma única expressão
fun dobro(x: Int) = x * 2

// vararg recebe quantidade variável; dentro vira Array<T>
fun media(vararg notas: Double): Double =
    if (notas.isEmpty()) 0.0 else notas.average()

// Extension function: adiciona comportamento a tipo existente
fun String.gritar(): String = uppercase() + "!!!"

infix fun Int.elevadoA(n: Int): Long = toDouble().pow(n).toLong()

fun main() {
    println(dobro(21))                       // 42
    println(media(7.0, 8.5, 10.0))           // 8.5
    println("kotlin".gritar())               // KOTLIN!!!
    val r = 2 elevadoA 10                    // infix sem ponto/parênteses
    println(r)                               // 1024
}
```

## Boas práticas

- Use defaults e argumentos nomeados no lugar de múltiplos overloads.
- Prefira single-expression functions para lógica direta e legível.
- Escreva extension functions para utilitários de tipos existentes.
- Nomeie bem parâmetros booleanos (`urgente`) para leitura na chamada.
- Use `vararg` quando a API pede lista aberta de valores.

## Armadilhas comuns

- Misturar argumento posicional depois de nomeado: erro de compilação.
- Achar que `Unit` precisa ser declarado: Kotlin infere automaticamente.
- Usar `infix` em função com mais de um parâmetro ou membro de classe não aberta a isso.
- Esperar que extension function sobrescreva método da classe: ela nunca é virtual.
- Passar array para `vararg` sem spread: use `*array`.

## Relacionadas

- [[Kotlin]]
- [[Primeiros-Passos]]
- [[Lambdas-e-Scope-Functions]]
