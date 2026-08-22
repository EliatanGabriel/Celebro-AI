---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Classe e Método Main em Java

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Todo programa Java começa em uma classe com o método `public static void main(String[] args)`, compilado por `javac` e executado pela JVM com `java`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `public class Nome {}` | Declara classe pública; arquivo deve ter o mesmo nome | `public class App {}` → `App.java` |
| `public static void main(String[] args)` | Ponto de entrada do programa | `public static void main(String[] args) {}` |
| `System.out.println(x)` | Imprime com quebra de linha | `System.out.println("Olá");` |
| `System.out.print(x)` | Imprime sem quebra de linha | `System.out.print("a");` |
| `javac App.java` | Compila gerando o bytecode `.class` | Terminal: `javac App.java` |
| `java App` | Executa o programa na JVM | Terminal: `java App` |
| `package br.com.app;` | Primeira linha: define o pacote da classe | `package br.com.app;` |
| `import java.util.List;` | Importa classes de outros pacotes | `import java.util.*;` |

## Exemplos

```java
// Estrutura mínima de um programa Java
package br.com.app;

import java.time.LocalDate;

public class App {
    public static void main(String[] args) {
        String nome = "Ana";
        int ano = LocalDate.now().getYear();
        System.out.println("Bem-vinda, " + nome + "! Ano: " + ano);
    }
}
```

```bash
# Compilar e executar no terminal
javac App.java        # gera App.class (bytecode)
java App              # executa: Bem-vinda, Ana! Ano: 2026
```

## Boas práticas

- Classes em `PascalCase`, métodos e variáveis em `camelCase`.
- Constantes em `MAIÚSCULAS_COM_UNDERSCORE`: `MAX_TENTATIVAS`.
- O arquivo `.java` público deve ter exatamente o nome da classe.
- Declare sempre o `package`; evite deixar classes no pacote padrão.
- Use imports individuais em vez de curingas (`*`) para clareza.

## Armadilhas comuns

- Assinatura errada do main (sem `static`, sem `String[] args`) não roda.
- Nome do arquivo diferente do nome da classe pública causa erro de compilação.
- Esquecer ponto e vírgula ou chaves é o erro nº 1 de iniciante.
- Java diferencia maiúsculas: `String` ok, `string` não compila.
- Rodar `java App.java` direto só funciona a partir do Java 11.

## Relacionadas

- [[Variaveis-e-Tipos]]
- [[Metodos]]
- [[Java]]
