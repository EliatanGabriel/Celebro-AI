---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Métodos em Java

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Métodos em Java declaram modificador, tipo de retorno, nome e parâmetros; suportam sobrecarga (overload), varargs e vivem no contexto da classe (`static`) ou da instância.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `public double area(double r)` | Modificador + retorno + nome + parâmetros | Assinatura completa do método |
| `void` | Método sem retorno | `public void log(String msg) {}` |
| `return valor;` | Devolve o resultado ao chamador | `return a + b;` |
| `return;` | Encerra método void antecipadamente | `if (!valido) return;` |
| overload | Mesmo nome, assinaturas diferentes | `somar(int,int)` e `somar(double,double)` |
| `static` | Pertence à classe, não à instância | `static int contador() {}` |
| método de instância | Precisa de objeto para ser chamado | `obj.calcular();` |
| `Tipo... args` | Varargs: quantidade variável de argumentos | `soma(int... valores)` |

## Exemplos

```java
// Retorno, sobrecarga e varargs
public class Matematica {

    public static int somar(int a, int b) {          // versão int
        return a + b;
    }

    public static double somar(double a, double b) { // overload
        return a + b;
    }

    public static int somar(int... valores) {        // varargs
        int total = 0;
        for (int v : valores) total += v;
        return total;
    }
}
```

```java
// static vs instância
public class Contador {
    private int totalInstancias = 0;
    private static int totalGeral = 0;

    public void incrementar() {          // método de instância
        totalInstancias++;
        totalGeral++;
    }

    public static int getTotalGeral() {  // chamado na classe
        return totalGeral;
    }
}
```

## Boas práticas

- Um método deve fazer uma única coisa bem definida.
- Nomeie com verbos: `calcularTotal`, `validarCpf`, `buscarPorId`.
- Prefira retorno explícito a modificar variáveis globais.
- Use varargs quando o número de parâmetros varia naturalmente.
- Evite mais de 3 ou 4 parâmetros; agrupe num objeto se precisar.

## Armadilhas comuns

- Sobrecarga exige assinatura diferente; só mudar o retorno não basta.
- Acessar campo de instância dentro de método `static` não compila.
- Esquecer o `return` em método não-void dá erro de compilação.
- Varargs precisa ser o último parâmetro da lista.
- Chamar método de instância sem criar objeto causa NullPointerException.

## Relacionadas

- [[Classe-e-Main]]
- [[POO-e-Heranca]]
- [[Java]]
