---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Lambdas e Scope Functions (Kotlin)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Lambdas em Kotlin usam a sintaxe `{ x -> x * 2 }` com `it` implícito, alimentam higher-order functions e trailing lambdas, e as scope functions (let, apply, run, with, also) organizam o acesso a objetos.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `{ p -> expr }` | Lambda explícita | `val d = { x: Int -> x * 2 }` |
| `it` | Parâmetro único implícito | `lista.map { it * 2 }` |
| `fun f(op: (Int) -> Int)` | Higher-order function | recebe função |
| `f(1) { ... }` | Trailing lambda | último arg fora dos parênteses |
| `::metodo` | Reference de função | `nums.forEach(::println)` |
| `.let { }` | Transforma/evita null | retorna resultado do bloco |
| `.apply { }` | Configura objeto | retorna o próprio objeto |
| `.run { }` / `.with(x) { }` | Calcula sobre contexto | retorna resultado |
| `.also { }` | Efeito colateral (log) | retorna o próprio objeto |

## Exemplos

```kotlin
fun main() {
    val dobrar = { x: Int -> x * 2 }
    println(dobrar(21))                       // 42

    val nums = listOf(1, 2, 3)
    println(nums.map { it * 10 })             // [10, 20, 30]

    fun processar(n: Int, transformar: (Int) -> Int): Int =
        transformar(n)

    // trailing lambda: função por último fica fora dos ()
    val r = processar(5) { it + 1 }
    println(r)                                // 6

    nums.forEach(::println)                   // referência ::funcao
}
```

```kotlin
data class Cliente(var nome: String = "", var email: String = "")

fun main() {
    val c = Cliente().apply {                 // configura e retorna ele
        nome = "Ana"
        email = "ana@x.com"
    }.also { log("criado: $it") }             // efeito colateral

    val nomeMaiusculo = c.let { it.nome.uppercase() }  // transforma
    val resumo = with(c) { "$nome <$email>" }          // contexto direto
    val tamanho = c.run { nome.length }

    println(nomeMaiusculo); println(resumo); println(tamanho)
}

fun log(msg: String) = println("[LOG] $msg")
```

## Boas práticas

- Use `it` para lambdas curtas; nomeie o parâmetro quando houver aninhamento.
- Prefira `apply` para inicialização/configuração de objetos.
- Use `let` combinado com safe call (`?.`) para executar só se não-nulo.
- Aproveite trailing lambda para APIs declarativas legíveis.
- Escolha scope function pelo retorno desejado: próprio objeto ou resultado.

## Armadilhas comuns

- Aninhar lambdas e perder de vista o que `it` representa.
- Usar `apply` quando queria o valor calculado (use `run`).
- Esquecer que `with` precisa de argumento e não é null-safe.
- Chamar `::funcao` com assinatura incompatível esperando adaptação automática.
- Abusar de scope functions encadeadas e tornar o fluxo ilegível.

## Relacionadas

- [[Kotlin]]
- [[Funcoes]]
- [[Colecoes]]
