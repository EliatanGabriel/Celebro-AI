---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# POO e Herança em Java

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Java é orientado a objetos: classes definem estado e comportamento, com encapsulamento via `private` + getters/setters, herança com `extends`, polimorfismo e `record`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `class Nome {}` | Declara uma classe | `public class Pessoa {}` |
| `Nome(...)` | Construtor inicializa o objeto | `public Pessoa(String nome) {...}` |
| `this.campo` / `this(...)` | Referência à instância / chama outro construtor | `this.nome = nome;` |
| `private` + getter/setter | Encapsula o estado interno | `getNome()` / `setNome(v)` |
| `extends` | Herda de outra classe (simples) | `class Aluno extends Pessoa {}` |
| `super()` / `super.metodo()` | Chama construtor/método da superclasse | `super(nome);` |
| `@Override` | Indica sobrescrita de método herdado | `@Override public String toString()` |
| `toString()` | Representação textual do objeto | `@Override public String toString() {...}` |
| `abstract class Nome` | Classe-base incompleta, não instanciável | `abstract class Forma {}` |
| `record Nome(tipo campo)` | Classe imutável de dados (Java 16+) | `record Ponto(int x, int y) {}` |

## Exemplos

```java
// Classe com encapsulamento e herança
public class Pessoa {
    private String nome;
    private int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome.trim(); }

    @Override
    public String toString() {
        return nome + " (" + idade + " anos)";
    }
}

public class Aluno extends Pessoa {
    private String matricula;

    public Aluno(String nome, int idade, String matricula) {
        super(nome, idade);              // construtor pai primeiro
        this.matricula = matricula;
    }
}
```

```java
// Polimorfismo: mesma variável, comportamentos diferentes
Pessoa p1 = new Pessoa("Ana", 30);
Pessoa p2 = new Aluno("Bia", 20, "2024A");

System.out.println(p2);   // usa toString conforme a classe real
```

## Boas práticas

- Campos sempre `private`; exponha só o necessário via métodos.
- Chame `super(...)` na primeira linha do construtor filho.
- Use `@Override` sempre: o compilador avisa erros de assinatura.
- Prefira composição quando a relação não for "é um".
- Use `record` para transportadores de dados imutáveis.

## Armadilhas comuns

- Java não tem herança múltipla de classes (só uma via `extends`).
- Sobrescrever com visibilidade menor que a do pai não compila.
- Esquecer `super()` ainda funciona se o pai tiver construtor sem args.
- Comparar objetos com `==` em vez de `.equals` compara referências.
- Construtor privado sem fábrica estática deixa a classe inutilizável.

## Relacionadas

- [[Interfaces-e-Classes-Abstratas]]
- [[Metodos]]
- [[Java]]
