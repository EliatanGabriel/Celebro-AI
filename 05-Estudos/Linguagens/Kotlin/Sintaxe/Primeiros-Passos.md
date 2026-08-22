---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Primeiros Passos (Kotlin)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Todo programa Kotlin começa em `fun main()`, com variáveis declaradas por `val` (imutável) ou `var` (mutável) e tipos inferidos automaticamente na maioria dos casos.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `fun main()` | Ponto de entrada | `fun main() { ... }` |
| `val` | Variável imutável | `val x = 10` |
| `var` | Variável mutável | `var y = 20` |
| `: Int` | Anotação explícita | `val z: Int = 5` |
| `println` / `print` | Imprime com/sem quebra | `println("oi")` |
| `//` e `/* */` | Comentários | `// nota` |
| `/** */` | Doc comment | `/** descrição */` |
| `;` opcional | Nova linha separa statements | sem ponto e vírgula |

## Exemplos

```kotlin
fun main() {
    val nome = "Eliatan"          // inferido como String
    var idade: Int = 25           // anotação explícita
    idade = idade + 1             // ok, é var
    // nome = "Outro"             // erro: val não reatribui

    println("Olá, $nome!")        // template string
    print("Idade: ")
    println(idade)
}
```

```kotlin
/**
 * Calcula o dobro de um número.
 * Doc comments alimentam a documentação oficial.
 */
fun dobro(n: Int): Int = n * 2

fun main() {
    // comentário de linha
    /* comentário
       de bloco */
    println(dobro(21))            // 42
}
```

## Boas práticas

- Use `val` por padrão; troque para `var` só quando realmente precisar.
- Confie na inferência; anote tipos só em APIs públicas ou casos ambíguos.
- Prefira interpolação (`"$nome"`) à concatenação com `+`.
- Rode experimentos rápidos no Kotlin Playground antes de criar projeto.
- Escreva doc comments (`/** */`) em funções públicas.
- Deixe o ponto e vírgula de fora; use apenas em linhas múltiplas raras.

## Armadilhas comuns

- Declarar `var` por hábito do JavaScript e perder imutabilidade.
- Achar que `val` congela o objeto: a referência é fixa, o conteúdo pode mudar.
- Usar `main` fora de função top-level ou com assinatura errada ao rodar no JVM.
- Esquecer `$` no template e imprimir literalmente `{nome}`.
- Colocar `;` após cada linha "por garantia": funciona, mas foge da convenção.

## Relacionadas

- [[Kotlin]]
- [[Java]]
- [[Tipos-e-Null-Safety]]
- [[Funcoes]]
