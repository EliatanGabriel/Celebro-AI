---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Coleções (Kotlin)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Kotlin separa coleções em imutáveis (List/Set/Map de leitura) e mutáveis (Mutable*), com operações funcionais como map, filter, fold e utilitários first/take/drop.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `listOf(...)` | List imutável | `listOf(1, 2)` |
| `mutableListOf(...)` | List mutável | `ml.add(3)` / `ml.remove(1)` |
| `setOf(...)` | Set sem duplicatas | `setOf("a", "b")` |
| `mutableSetOf(...)` | Set mutável | `ms.add("c")` |
| `mapOf(a to 1)` | Map imutável | `mapa["a"]` |
| `mutableMapOf()` | Map mutável | `mm["k"] = v` |
| `.map { }` / `.filter { }` | Transformar/filtrar | nova coleção |
| `.reduce {}` / `.fold {}` | Agregar valor único | fold tem inicial |
| `.first{}`/`.take(n)`/`.drop(n)` | Fatiar e buscar | seleção parcial |

## Exemplos

```kotlin
fun main() {
    val lista = listOf("kotlin", "java")
    println(lista[0])                     // kotlin (acesso por índice)
    // lista.add("x")                     // não existe: imutável

    val mutavel = mutableListOf(1, 2)
    mutavel.add(3)                        // [1, 2, 3]
    mutavel.remove(1)                     // [2, 3]
    println(mutavel.contains(2))          // true

    val mapa = mapOf("py" to 1991, "kt" to 2011)
    println(mapa["kt"])                   // 2011

    val config = mutableMapOf("tema" to "escuro")
    config["fonte"] = "mono"              // inserir/atualizar
}
```

```kotlin
fun main() {
    val notas = listOf(10.0, 5.0, 8.0, 9.5)

    val aprovadas = notas.filter { it >= 7.0 }      // [10.0, 8.0, 9.5]
    val ajustadas = notas.map { it + 0.5 }          // soma 0.5 a todas
    val maiorNota = notas.reduce { acc, n -> if (n > acc) n else acc }
    val somaPonderada = notas.fold(0.0) { acc, n -> acc + n * 0.25 }

    println(aprovadas)
    println(ajustadas)
    println(maiorNota)                              // 10.0
    println(somaPonderada)                          // 8.125

    println(notas.first { it > 6 })                 // 10.0
    println(notas.take(2))                          // [10.0, 5.0]
    println(notas.drop(1))                          // [5.0, 8.0, 9.5]
}
```

## Boas práticas

- Exponha tipos imutáveis (`List`) em APIs; crie mutável só internamente.
- Prefira `to` para construir Maps de forma legível.
- Use `fold` quando precisar de valor inicial ou tipo diferente do acumulador.
- Encadeie `filter().map()` com parcimônia para não criar listas demais.
- Use `getOrNull`/`getOrElse` em vez de indexar às cegas.

## Armadilhas comuns

- Achar que `val lista` impede mudanças: imutabilidade depende da interface, não do val.
- Usar `reduce` em lista vazia: lança exceção; prefira `fold`.
- Esquecer que `setOf` descarta duplicatas silenciosamente.
- Confundir `remove(valor)` com remover por índice em MutableList.
- Esperar ordem garantida em `Set`: use LinkedHashSet/setOf se ordem importa.

## Relacionadas

- [[Kotlin]]
- [[Loops]]
- [[Data-Classes-e-Sealed]]
