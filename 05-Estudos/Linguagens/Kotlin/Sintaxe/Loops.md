---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Loops (Kotlin)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** O `for` de Kotlin itera qualquer coisa iterável (ranges, listas, com índice via withIndex), enquanto while/do-while, break/continue com labels e forEach completam o arsenal de repetição.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `for (x in lista)` | Itera elementos | `for (n in nums)` |
| `for (i in 1..10)` | Itera range | contagem simples |
| `.withIndex()` | Elemento + índice | `for ((i, v) in ...)` |
| `.indices` | Só os índices | `for (i in lista.indices)` |
| `while (cond)` | Enquanto verdadeiro | `while (!pronto)` |
| `do { } while (cond)` | Executa ao menos uma vez | menus interativos |
| `break` / `continue` | Interrompe / pula iteração | dentro do loop |
| `loop@ for (...)` | Label para break/continue | `break@loop` |
| `forEach { }` | Função de extensão | `lista.forEach { }` |

## Exemplos

```kotlin
fun main() {
    val linguagens = listOf("Kotlin", "TS", "Python")

    for (l in linguagens) print("$l ")          // Kotlin TS Python
    println()

    for ((indice, valor) in linguagens.withIndex()) {
        println("$indice -> $valor")
    }

    for (i in linguagens.indices) {             // só índices
        print("[$i]")
    }
}
```

```kotlin
fun main() {
    // Labels permitem sair/pular loops aninhados
    externo@ for (i in 1..3) {
        for (j in 1..3) {
            if (i * j > 4) continue@externo
            if (i == 3) break@externo
            print("($i,$j) ")
        }
    }
    // (1,1) (1,2) (2,1)

    var tentativas = 0
    do {
        tentativas++
        println("tentativa $tentativas")
    } while (tentativas < 3)

    listOf(1, 2, 3).forEach { n -> print(n * 2) } // 246
}
```

## Boas práticas

- Prefira `for (x in coleção)` a indexar manualmente com `[i]`.
- Use `withIndex()` quando precisar do índice e do valor juntos.
- Reserve labels para loops aninhados; em código plano, `break` basta.
- Considere funções (`map`, `filter`) antes de escrever um loop manual.
- Use `do-while` só quando a primeira execução deve acontecer sempre.

## Armadilhas comuns

- Procurar `for (int i = 0; ...)` clássico: não existe em Kotlin.
- Usar `forEach` e precisar de `return`: o comportamento difere do loop.
- Esquecer que `break` sem label sai apenas do loop mais interno.
- Modificar a lista durante `for (x in lista)`: gera ConcurrentModificationException.
- Confundir `indices` (índices) com os próprios valores da lista.

## Relacionadas

- [[Kotlin]]
- [[Colecoes]]
- [[Controle-de-Fluxo]]
