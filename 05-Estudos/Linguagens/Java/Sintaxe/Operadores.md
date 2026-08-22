---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Operadores em Java

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Java tem operadores aritméticos com divisão inteira, incremento/decremento, atribuição composta, comparação lógica e o ternário; objetos se comparam com `.equals`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `+ - * / %` | Aritméticos básicos (resto incluído) | `7 % 2  // 1` |
| `int / int` | Divisão inteira: trunca a parte decimal | `7 / 2  // 3` |
| `++x` / `x++` | Incrementa antes / depois de usar | `i++;` |
| `--x` / `x--` | Decrementa antes / depois de usar | `i--;` |
| `+= -= *= /= %=` | Atribuição composta com cast implícito | `total += 10;` |
| `== !=` | Compara valores de primitivos (referência em objetos) | `a == b` |
| `equals(Object)` | Compara conteúdo de objetos | `"ab".equals(s)` |
| `&& \|\| !` | E, OU lógicos com short-circuit e negação | `if (a && b)` |
| `cond ? x : y` | Operador ternário | `n >= 0 ? n : -n` |
| `+` com String | Concatenação de texto | `"Total: " + valor` |

## Exemplos

```java
// Aritmética, divisão inteira e ternário
public class Calculos {
    public static void main(String[] args) {
        int total = 17;
        int pessoas = 5;

        System.out.println(total / pessoas);        // 3  (divisão inteira!)
        System.out.println(total % pessoas);        // 2  (resto)
        System.out.println((double) total / pessoas); // 3.4

        int contador = 10;
        contador += 5;                              // 15
        System.out.println(contador++);
        System.out.println(contador);

        String sinal = total >= 0 ? "positivo" : "negativo";
    }
}
```

```java
// Comparação: == vs equals
String a = new String("java");
String b = new String("java");

System.out.println(a == b);          // false (referências diferentes)
System.out.println(a.equals(b));     // true  (conteúdo igual)
```

## Boas práticas

- Use `equals()` sempre para comparar Strings e objetos.
- Faça cast para `double` antes da divisão quando precisar de decimais.
- Prefira `+=` a reescrever a expressão completa.
- Cuidado com precedência: use parênteses para deixar claro.
- Chame `equals` no literal fixo: `"FIXO".equals(valor)` evita NullPointerException.

## Armadilhas comuns

- `7 / 2 == 3`: divisão entre ints descarta decimais silenciosamente.
- `==` em Strings às vezes "funciona" por cache e quebra depois.
- `contador++` retorna o valor antigo; `++contador`, o novo.
- `%` com negativos segue o sinal do dividendo: `-7 % 2` é `-1`.
- `&&` faz short-circuit: o lado direito pode nunca ser executado.

## Relacionadas

- [[Variaveis-e-Tipos]]
- [[Controle-de-Fluxo]]
- [[Java]]
