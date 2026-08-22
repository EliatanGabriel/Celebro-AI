---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# POO e Herança (Kotlin)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Classes em Kotlin têm constructor primário com init, propriedades com get/set customizados, herança explícita via `open` e `: Super()`, além de abstract, interfaces com default methods e visibilidade granular.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `class X(val a: T)` | Constructor primário | parâmetros viram props |
| `init { }` | Bloco de inicialização | roda na instanciação |
| `var x get() set(v)` | Accessors customizados | lógica no acesso |
| `open class S` | Permite herança | classes fecham por padrão |
| `class F : S()` | Herda chamando super() | `:` + parênteses |
| `override fun m()` | Sobrescreve membro aberto | obrigatório marcar |
| `abstract class A` | Base incompleta | não instanciável |
| `interface I { fun m() {} }` | Contrato + default impl | corpo permitido |
| `private/internal/public` | Visibilidade | internal = módulo |

## Exemplos

```kotlin
interface Autenticavel {
    val usuario: String
    fun autenticar(senha: String): Boolean = senha.length >= 4 // default
}

abstract class Conta(open val saldo: Double) : Autenticavel {
    override val usuario = "conta-${this.hashCode()}"
    abstract fun taxa(): Double
    open fun resumo() = "saldo=${"%.2f".format(saldo)}"
}

class Poupanca(override var saldo: Double) : Conta(saldo) {
    override fun taxa() = 0.01            // override obrigatório
    override fun resumo(): String {
        return super.resumo() + " tipo=poupanca"
    }
}
```

```kotlin
class Temperatura(celsius: Double) {
    private var interna = celsius

    var celsius: Double
        get() = interna
        set(valor) { interna = valor.coerceIn(-273.15, 1_000.0) }

    val fahrenheit: Double
        get() = interna * 9 / 5 + 32      // computed property

    init {
        println("criada com $celsius°C")  // roda após o constructor
    }
}

fun main() {
    val t = Temperatura(25.0)             // "criada com 25.0°C"
    t.celsius = 30.0                      // passa pelo set validado
    println(t.fahrenheit)                 // 86.0
}
```

## Boas práticas

- Lembre: sem `open`, nenhuma classe/método pode ser herdado/sobrescrito.
- Use accessors customizados para validar ou derivar valores.
- Prefira interfaces com default methods a classes utilitárias herdadas.
- Marque membros de API como `internal` quando uso é só do seu módulo.
- Chame implementações pai com `super.metodo()` ao estender comportamento.

## Armadilhas comuns

- Esquecer `open` na superclasse: erro "this type is final".
- Esquecer os parênteses em `: Super()`: chama constructor inexistente.
- Usar `this` em propriedades do constructor primário dentro de `val` do init incorretamente.
- Declarar `override` sem que o membro base seja `open`.
- Esperar `private` igual ao Java: em Kotlin, o padrão é `public`.

## Relacionadas

- [[Kotlin]]
- [[Java]]
- [[Data-Classes-e-Sealed]]
