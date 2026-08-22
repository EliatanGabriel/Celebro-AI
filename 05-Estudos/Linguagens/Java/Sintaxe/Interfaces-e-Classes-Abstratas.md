---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Interfaces e Classes Abstratas em Java

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Interfaces definem contratos que classes implementam (com herança múltipla de tipo), enquanto classes abstratas compartilham código parcial entre subclasses relacionadas.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `interface Nome {}` | Define um contrato de comportamentos | `public interface Pagavel {}` |
| `implements` | Classe assina uma ou mais interfaces | `class Boleto implements Pagavel` |
| `default` | Método com corpo dentro da interface (Java 8+) | `default void log() {...}` |
| `CONSTANTE` | Campos de interface são públicos, estáticos e finais | `double TAXA = 0.02;` |
| `abstract class Nome` | Classe-base que não pode ser instanciada | `public abstract class Forma {}` |
| `abstract metodo();` | Declara método sem corpo para os filhos preencherem | `abstract double area();` |

## Exemplos

```java
// Interface com default method e constantes
public interface MeioPagamento {
    double TAXA_MINIMA = 1.0;                 // public static final implícito

    double calcularTaxa(double valor);        // contrato abstrato

    default boolean taxaValida(double taxa) { // método pronto p/ todos
        return taxa >= TAXA_MINIMA;
    }
}

public class Cartao implements MeioPagamento {
    @Override
    public double calcularTaxa(double valor) {
        return valor * 0.03;
    }
}
```

```java
// Classe abstrata com estado compartilhado
public abstract class Forma {
    protected String nome;

    public abstract double area();            // cada filho define

    public String descrever() {               // código reaproveitado
        return nome + " tem área " + area();
    }
}

public class Circulo extends Forma {
    private double raio;
    public Circulo(double r) { nome = "círculo"; raio = r; }
    @Override public double area() { return Math.PI * raio * raio; }
}
```

## Boas práticas

- Prefira interface para contratos ("o quê"); abstrata para código compartilhado.
- Uma classe pode implementar várias interfaces, mas estender só uma.
- Mantenha interfaces pequenas e focadas (princípio da segregação).
- Adicione `default methods` com cautela para não sujar o contrato.

## Armadilhas comuns

- Interface não pode ser instanciada com `new`.
- Filho concreto precisa implementar TODOS os métodos abstratos.
- Campos em interface são constantes; não servem para estado mutável.
- Confundir `extends` (classe) com `implements` (interface).

## Comparativo

| Aspecto | Interface | Classe abstrata |
|---|---|---|
| Herança múltipla | Sim (várias) | Não (uma) |
| Campos de instância | Não (só constantes) | Sim |
| Construtor | Não | Sim (chamado pelos filhos) |
| Métodos com corpo | `default` / `static` | Livremente |
| Quando usar | Contrato de capacidades | Base comum com código |

## Relacionadas

- [[POO-e-Heranca]]
- [[Excecoes]]
- [[Java]]
