---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Controle de Fluxo (Kotlin)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Em Kotlin, `if` e `when` são expressões que retornam valor, e o `when` substitui o switch sem fall-through, aceitando múltiplos valores, ranges e um ramo `else`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `if (...) ... else ...` | Condicional clássica | `if (a > b) a else b` |
| `val x = if (...) a else b` | If como expressão | atribui o resultado |
| `when (x) { }` | Seleção multi-ramo | `when (op) { 1 -> ... }` |
| `->` | Ramo do when | `1 -> println("um")` |
| `1, 2 ->` | Múltiplos valores num ramo | agrupa casos |
| `in 1..10 ->` | Ramo por range | `in 'a'..'z' ->` |
| `else ->` | Ramo padrão | cobre o resto |
| `when { cond -> }` | Sem assunto | when como if/else-if |

## Exemplos

```kotlin
fun main() {
    val idade = 17
    val categoria = if (idade < 18) "menor" else "maior" // expressão!
    println(categoria)

    val nota = 85
    val conceito = if (nota >= 90) {
        "A"   // último valor do bloco é retornado
    } else {
        "B"
    }
    println(conceito)
}
```

```kotlin
fun classificar(n: Int): String = when (n) {
    0, 1 -> "neutro"              // múltiplos valores
    in 2..9 -> "baixo"            // range no ramo
    in 10..99 -> "alto"
    else -> "fora da faixa"       // obrigatório p/ exaustividade
}

fun descrever(x: Any): String = when {
    x is Int && x > 0 -> "inteiro positivo"
    x is String -> "texto de ${x.length} letras"
    else -> "outra coisa"
}

fun main() {
    println(classificar(5))       // baixo
    println(descrever("olá"))     // texto de 3 letras
}
```

## Boas práticas

- Prefira `val x = if/when (...)` a variável declarada antes e reatribuída.
- Use `when` como expressão para mapear valores diretamente em resultados.
- Agrupe valores com vírgula (`1, 2 ->`) em vez de ramos duplicados.
- Combine `is`, `in` e condições no `when` sem assunto para lógica rica.
- Cubra todos os casos quando o `when` precisa retornar valor.

## Armadilhas comuns

- Procurar `break` nos ramos do `when`: não há fall-through, cada ramo termina sozinho.
- Esquecer o `else` num `when` usado como expressão: erro de compilação.
- Usar `when` sobre `Int` esperando match de tipo genérico: comparação é estrutural.
- Atribuir resultado de `if` sem `else`: não compila, expressão ficaria incompleta.
- Confundir `->` do when com lambda; contexto muda o significado.

## Relacionadas

- [[Kotlin]]
- [[Operadores-e-Ranges]]
- [[Loops]]
