---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Java

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem compilada para a JVM, orientada a objetos e fortemente tipada, amplamente usada em sistemas enterprise, backend (Spring) e Android.

## Conceitos-chave
- Paradigma orientado a objetos (classes, herança, polimorfismo, interfaces) com suporte a lambdas/Streams.
- Tipagem estática e forte, com compilação para bytecode executado pela JVM (JIT).
- "Write once, run anywhere": o bytecode roda em qualquer plataforma com JVM.
- Uso principal em aplicações enterprise, microserviços (Spring Boot), Android e sistemas legados de grande porte.
- Garbage collector gerencia a memória automaticamente.
- Particularidade: enorme ecossistema de bibliotecas (Maven, Gradle) e forte presença em big tech.
- Estruturas modernas: records, sealed classes, pattern matching e virtual threads (Java 21+).

## Exemplos
```java
import java.util.List;

public class Main {
    public static void main(String[] args) {
        var nomes = List.of("Ana", "Bruno", "Carlos");

        nomes.stream()
             .filter(n -> n.startsWith("A"))
             .forEach(System.out::println);  // Ana

        Pessoa p = new Pessoa("Ana", 30);
        System.out.println(p);  // Pessoa[nome=Ana, idade=30]
    }
}

public record Pessoa(String nome, int idade) {}
```

## Boas práticas
- Prefira records e imutabilidade para dados; evite getters/setters excessivos.
- Trate exceções no nível adequado; não engula `Exception` com catch vazio.
- Use interfaces e composição em vez de herança profunda.
- Aproveite o GC, mas evite referências desnecessárias que atrasam a coleta de lixo.
- Padronize com o Guia de Estilo (Google Java Style) e ferramentas como SpotBugs/Checkstyle.

## Armadilhas comuns
- Comparar Strings com `==` em vez de `.equals()`, gerando resultados incorretos.
- NullPointerException por não validar referências; use `Optional` com moderação.
- Mutabilidade de coleções expostas publicamente, quebrando encapsulamento.
- Confundir `==` com `.equals()` também para Integer (cache de -128 a 127).
- Bloquear threads com `synchronized` em excesso, reduzindo a escalabilidade (prefira estruturas concorrentes e virtual threads).

## Relacionadas
- [[Python]]
- [[C++]]
- [[Backend]]