---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Variáveis e Tipos em Java

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Java é estaticamente tipado: toda variável declara seu tipo, com primitivos de tamanho fixo, `String` imutável, casting explícito e wrappers para objetos.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `int` / `long` | Inteiros (32 bits / 64 bits) | `int idade = 25; long pop = 8_000_000_000L;` |
| `double` / `float` | Ponto flutuante (padrão / 32 bits) | `double preco = 9.90; float f = 1.5f;` |
| `boolean` | Verdadeiro ou falso (só `true`/`false`) | `boolean ativo = true;` |
| `char` | Um único caractere Unicode com aspas simples | `char letra = 'A';` |
| `byte` / `short` | Inteiros menores (8 / 16 bits) | `byte b = 100; short s = 30000;` |
| `String` | Texto imutável, aspas duplas | `String nome = "Ana";` |
| `var x = valor` | Inferência de tipo local (Java 10+) | `var lista = new ArrayList<String>();` |
| `(tipo) x` | Cast explícito entre tipos compatíveis | `int n = (int) 3.99; // 3` |
| `final tipo x` | Constante: valor não pode mudar | `final double PI = 3.14159;` |
| `Integer` / `Double` | Wrappers que embrulham primitivos | `Integer n = 10; // autoboxing` |

## Exemplos

```java
// Primitivos, casting e final
public class Tipos {
    public static void main(String[] args) {
        int inteiro = 42;
        double decimal = 7.5;
        boolean ativo = true;
        char inicial = 'A';
        String nome = "Ana";

        long grande = inteiro;              // widening implícito
        int truncado = (int) decimal;       // narrowing exige cast
        final int MAX_USUARIOS = 100;

        System.out.println(truncado + " " + MAX_USUARIOS);
    }
}
```

```java
// Wrappers e autoboxing/unboxing
Integer numeroObjeto = 10;      // autoboxing: int -> Integer
int primitivo = numeroObjeto;   // unboxing: Integer -> int

Integer nulo = null;
System.out.println(nulo);       // wrappers aceitam null
```

## Boas práticas

- Use o menor tipo necessário, mas prefira `int` e `double` por padrão.
- Marque valores fixos como `final` e nomeie-os em MAIÚSCULAS.
- Prefira `double` a `float`, salvo em APIs que exijam float.
- Use `var` só quando o tipo for óbvio pela inicialização.
- Para dinheiro, considere `BigDecimal` em vez de `double`.

## Armadilhas comuns

- Casting de `double` para `int` trunca sem arredondar: `(int) 3.99` vira 3.
- Literais `long` e `float` precisam do sufixo: `10L` e `1.5f`.
- Comparar wrappers com `==` compara referências fora do cache (-128 a 127).
- `String` é imutável: concatenações em loop geram muitos objetos.
- Variável local não inicializada não compila (diferente de campos de classe).

## Relacionadas

- [[Classe-e-Main]]
- [[Operadores]]
- [[Java]]
