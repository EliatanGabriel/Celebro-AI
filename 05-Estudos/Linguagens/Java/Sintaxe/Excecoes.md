---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Exceções em Java

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Java trata erros com exceções checked (obrigatórias de tratar), unchecked (RuntimeException) e blocos `try/catch/finally`, incluindo try-with-resources para fechar recursos.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `try {} catch (Tipo e) {}` | Tenta executar e captura a exceção | `catch (IOException e)` |
| `finally {}` | Executa sempre, com ou sem erro | Fechar conexões |
| `multi-catch` | Captura vários tipos num catch só | `catch (A \| B e)` |
| `throw new X(...)` | Lança uma exceção manualmente | `throw new IllegalArgumentException()` |
| `throws X` na assinatura | Declara que o método pode lançar | `void ler() throws IOException` |
| Checked | Verificada pelo compilador; exige tratamento | `IOException`, `SQLException` |
| Unchecked | Herda de RuntimeException; opcional tratar | `NullPointerException` |
| try-with-resources | Fecha automaticamente objetos AutoCloseable | `try (var r = new FileReader(f)) {}` |

## Exemplos

```java
// try/catch/finally e multi-catch
public class Leitor {
    public static void converter(String texto) {
        try {
            int numero = Integer.parseInt(texto);
            System.out.println(numero * 2);
        } catch (NumberFormatException e) {
            System.out.println("Não é número: " + texto);
        } finally {
            System.out.println("fim da tentativa");
        }
    }
}
```

```java
// Exceção própria e try-with-resources
public class SaldoInsuficienteException extends Exception {
    public SaldoInsuficienteException(double faltou) {
        super("Faltam R$ " + faltou);
    }
}

class Conta {
    public void sacar(double valor, double saldo) throws SaldoInsuficienteException {
        if (valor > saldo) {
            throw new SaldoInsuficienteException(valor - saldo);
        }
    }
}

// try (var leitor = new BufferedReader(new FileReader("dados.txt"))) {
//     System.out.println(leitor.readLine());   // fechado automaticamente
// }
```

## Boas práticas

- Trate apenas o que você pode resolver; deixe subir o restante.
- Prefira exceções específicas a capturar `Exception` genérica.
- Sempre inclua mensagem útil ao lançar (`throw new ...`).
- Use try-with-resources para qualquer recurso externo.
- Crie exceções próprias para regras de negócio importantes.

## Armadilhas comuns

- Bloco `catch` vazio engole o erro silenciosamente.
- Ignorar exceções checked gera erro de compilação.
- `finally` executa mesmo com `return` dentro do `try`.
- Chamar método em referência nula lança NullPointerException.
- Usar exceção para controlar fluxo normal é caro e confuso.

## Relacionadas

- [[Interfaces-e-Classes-Abstratas]]
- [[Arrays-e-Collections]]
- [[Java]]
