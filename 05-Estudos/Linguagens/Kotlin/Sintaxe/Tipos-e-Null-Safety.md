---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Tipos e Null Safety (Kotlin)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** O sistema de tipos do Kotlin distingue tipos anuláveis com `?` e força tratamento explícito de null através de safe calls, Elvis, `!!` e `lateinit`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `Int`, `Double`, `Boolean` | Primitivos tipados | `val i: Int = 1` |
| `Char`, `String`, `Long` | Caractere/texto/longo | `val s = "txt"` |
| `toX()` | Conversão explícita | `"42".toInt()`, `d.toInt()` |
| `String?` | Tipo anulável | `var n: String? = null` |
| `?.` | Safe call (null-safe) | `nome?.length` |
| `?:` | Elvis (valor padrão) | `nome ?: "anônimo"` |
| `!!` | Not-null assertion | `nome!!.length` |
| `lateinit var` | Inicialização tardia (var) | `lateinit var repo: Repo` |

## Exemplos

```kotlin
fun main() {
    val inteiro: Int = 7
    val decimal: Double = 3.14
    val longo: Long = 10_000_000_000L
    val letra: Char = 'K'
    val texto = "Kotlin"
    val ativo: Boolean = true

    // Sem coerção implícita: conversão é sempre explícita
    val comoDouble = inteiro.toDouble()   // 7.0
    val deVolta = decimal.toInt()         // 3 (trunca)
    val deTexto = "123".toIntOrNull()     // Int? — seguro

    println("$inteiro $decimal $longo $letra $texto $ativo")
    println("$comoDouble $deVolta $deTexto")
}
```

```kotlin
fun comprimento(nome: String?): Int {
    return nome?.length ?: 0   // safe call + Elvis
}

fun main() {
    println(comprimento(null))      // 0
    println(comprimento("Ana"))     // 3

    val configuracao: String? = carregar()
    // configuracao!!.length  -> crash se for null; evite
}

fun carregar(): String? = null
```

## Boas práticas

- Deixe o compilador reclamar de nulls: é um aliado, não um obstáculo.
- Prefira `?.` combinado a `?:` antes de recorrer a `!!`.
- Use `toIntOrNull()` e similares para entrada externa não confiável.
- Reserve `!!` para invariantes que você garante por design.
- Use `lateinit` só em campos injetados/configurados após a criação.

## Armadilhas comuns

- Esperar `"5" + 2` funcionar: sem coerção implícita entre tipos numéricos.
- Usar `!!` "para compilar" e produzir NullPointerException em produção.
- Aplicar `lateinit` em tipo primitivo ou `val`: só vale para `var` de classe.
- Confundir `Int?` com `Int`: métodos exigem tratamento do null.
- Esquecer que `?.` em cadeia retorna `null` no primeiro elo vazio.

## Relacionadas

- [[Kotlin]]
- [[Java]]
- [[Primeiros-Passos]]
- [[Operadores-e-Ranges]]
