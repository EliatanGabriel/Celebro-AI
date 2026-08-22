---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Data Classes e Sealed (Kotlin)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Data classes geram automaticamente equals, hashCode, copy e toString para dados puros, enquanto sealed classes restringem hierarquias e habilitam `when` exaustivo; `object` cria singletons.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `data class X(val a: T)` | Dados + métodos gerados | equals/hashCode/copy/toString |
| `.copy(a = novo)` | Cópia com alterações | imutável-friendly |
| `val (a, b) = par` | Destructuring | desmonta em variáveis |
| `sealed class Y` | Hierarquia fechada | subclasses no mesmo arquivo |
| `when` exaustivo | Todos os ramos cobertos | sem else obrigatório |
| `object Z { }` | Singleton nativo | instância única |
| `companion object` | Estáticos da classe | fábricas e constantes |

## Exemplos

```kotlin
data class Ponto(val x: Int, val y: Int)

fun main() {
    val p1 = Ponto(1, 2)
    val p2 = p1.copy(y = 9)          // Ponto(x=1, y=9)

    println(p1 == Ponto(1, 2))       // true: compara conteúdo
    println(p1.toString())           // Ponto(x=1, y=2)

    val (x, y) = p1                  // destructuring
    println("$x $y")                 // 1 2
}
```

```kotlin
sealed class Resultado {
    data class Sucesso(val dados: List<String>) : Resultado()
    data class Erro(val codigo: Int) : Resultado()
    object Carregando : Resultado()
}

object Cache {
    val itens = mutableListOf<String>()
}

class Servico {
    companion object {
        const val TIMEOUT = 30
        fun criar() = Servico()      // factory estática
    }
}
fun render(r: Resultado): String = when (r) { // exaustivo: sem else
    is Resultado.Sucesso -> "OK: ${r.dados.size}"
    is Resultado.Erro -> "Falha ${r.codigo}"
    Resultado.Carregando -> "..."
}

fun main() {
    Cache.itens.add("a")
    println(render(Resultado.Sucesso(listOf("a", "b"))))
    println(Servico.TIMEOUT)
}
```

## Boas práticas

- Use data class para modelos de dados (DTOs, valores de domínio).
- Prefira propriedades `val` em data classes e evolua via `copy`.
- Modele estados de UI/rede com sealed class + when exaustivo.
- Use `object` para utilitários stateless e caches simples.
- Reserve `companion object` para constantes e factories da classe.

## Armadilhas comuns

- Colocar lógica pesada em data class: ela existe para dados.
- Usar vararg ou propriedades não primárias: só o constructor primário entra nos métodos gerados.
- Declarar subclasse de sealed fora do arquivo/pacote permitido.
- Esquecer que `copy` é raso: listas internas continuam compartilhadas.
- Confundir `object` com classe estática de Java: ele é uma instância real e lazy.

## Relacionadas

- [[Kotlin]]
- [[Colecoes]]
- [[POO-e-Heranca]]
