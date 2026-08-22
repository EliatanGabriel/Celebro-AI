---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Controle de Fluxo em Java

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** O fluxo de execução em Java é controlado por `if/else`, `switch` tradicional ou switch expression (Java 14+) e ternário, com escopo definido pelas chaves.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `if (cond) {}` | Executa o bloco se a condição for `true` | `if (idade >= 18) {}` |
| `else if` / `else` | Caminhos alternativos encadeados | `else if (x > 0) {} else {}` |
| `switch (v) { case x: ... break; }` | Switch tradicional; exige `break` | `case 1: return "a";` |
| `switch (v) { case x -> ... }` | Switch expression (Java 14+): sem fall-through | `case 1 -> "a";` |
| `default` / `default ->` | Caso padrão quando nada casa | `default -> "inválido";` |
| `yield valor` | Retorna valor dentro de bloco do switch expression | `yield n * 2;` |
| `cond ? a : b` | Ternário: expressão condicional curta | `n % 2 == 0 ? "par" : "ímpar"` |

## Exemplos

```java
// if/else if/else e ternário
public class Notas {
    public static String conceito(double nota) {
        if (nota >= 9) {
            return "A";
        } else if (nota >= 7) {
            return "B";
        } else if (nota >= 5) {
            return "C";
        }
        return "Reprovado";

        // versão ternária:
        // return nota >= 5 ? "aprovado" : "reprovado";
    }
}
```

```java
// switch tradicional vs switch expression
String dia = "SABADO";
int numeroDia = 6;

switch (dia) {                       // tradicional
    case "SABADO":
    case "DOMINGO":
        System.out.println("folga");
        break;
    default:
        System.out.println("dia útil");
}

String tipo = switch (numeroDia) {   // expression (Java 14+)
    case 1, 7 -> "fim da semana inicial/final";
    case 2, 3, 4, 5, 6 -> {
        int ordem = numeroDia - 1;
        yield "dia útil nº " + ordem;
    }
    default -> "inválido";
};
```

## Boas práticas

- Prefira switch expression para atribuir valores: mais seguro e conciso.
- Sempre inclua `default` para cobrir casos não previstos.
- Ordene as condições do `if` da mais provável à menos provável.
- Extraia condições longas para variáveis booleanas nomeadas.
- Use ternário apenas em escolhas simples entre dois valores.

## Armadilhas comuns

- Sem `break`, o switch tradicional cai no próximo case (fall-through).
- Switch tradicional não aceita `null`: lança NullPointerException.
- Chaves opcionais no `if` de uma linha causam bugs ao adicionar código depois.
- Variável declarada dentro de um bloco morre fora dele.
- Comparar Strings no switch funciona, mas com `==` fora dele não.

## Relacionadas

- [[Operadores]]
- [[Loops]]
- [[Java]]
