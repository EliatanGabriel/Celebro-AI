---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Kotlin

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem moderna da JetBrains para a JVM, oficial para desenvolvimento Android, concisa, segura contra nulos e totalmente interoperável com Java.

## Conceitos-chave
- Multiparadigma: orientada a objetos com forte influência funcional (funções de alta ordem, imutabilidade).
- Tipagem estática e forte, com inferência de tipos.
- Compilada para bytecode JVM; também compila para JavaScript e código nativo (Kotlin/Native).
- Uso principal em Android (oficial do Google) e backend (Spring Boot, Ktor).
- Null safety: tipos não anuláveis por padrão (`String?` marca anulável), evitando NPE em tempo de compilação.
- data classes, coroutines (concorrência estruturada) e extension functions.
- Particularidade: interoperabilidade bidirecional com Java sem custo de migração.

## Exemplos
```kotlin
data class Usuario(val nome: String, val idade: Int?)

fun main() {
    val usuarios = listOf(Usuario("Ana", 30), Usuario("Bruno", null))

    usuarios.filter { it.idade != null }
        .forEach { println("${it.nome} tem ${it.idade} anos") }

    val total = usuarios
        .map { it.idade ?: 0 }
        .sum()
    println("Total: $total")
}

fun List<Int>.dobro() = this.map { it * 2 }  // extension function
```

## Boas práticas
- Use null safety de forma explícita: `?.`, `?:`, `!!` apenas quando garantido.
- Prefira `val` (imutável) a `var` sempre que possível.
- Aproveite data classes e `copy()` para imutabilidade de dados.
- Use coroutines com `suspend` em vez de threads para operações concorrentes.
- Interopere com Java preservando anotações de nullability (`@Nullable`/`@NotNull`).

## Armadilhas comuns
- Abusar de `!!`, reintroduzindo NullPointerException que a linguagem evita.
- Usar `lateinit` sem inicializar, gerando UninitializedPropertyAccessException.
- Confundir `==` (estrutural, chama `equals`) com `===` (identidade de referência).
- Ignorar o resultado de funções de coleção (listas são imutáveis por padrão quando usadas como `List`).
- Combinar coroutines com código bloqueante, travando o dispatcher.

## Relacionadas
- [[Java]]
- [[Swift]]
- [[Backend]]