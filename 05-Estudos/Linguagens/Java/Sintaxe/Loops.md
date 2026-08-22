---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Loops em Java

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Java repete tarefas com `for` clássico, for-each (`for (Tipo x : colecao)`), `while` e `do...while`, controlados por `break` e `continue`, inclusive aninhados.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `for (init; cond; passo)` | Loop com contador | `for (int i = 0; i < n; i++) {}` |
| `for (Tipo x : colecao)` | For-each: itera elementos sem índice | `for (String nome : nomes) {}` |
| `while (cond) {}` | Repete enquanto a condição for verdadeira | `while (saldo > 0) {}` |
| `do {} while (cond);` | Executa ao menos uma vez antes de testar | `do { ... } while (opcao != 0);` |
| `break` | Interrompe o loop imediatamente | `if (achou) break;` |
| `continue` | Pula para a próxima iteração | `if (x % 2 != 0) continue;` |
| loops aninhados | Um loop dentro do outro (matrizes, combinações) | `for i { for j { ... } }` |

## Exemplos

```java
// for clássico, for-each e break/continue
public class Loops {
    public static void main(String[] args) {
        int[] notas = {8, 5, 10, 7};

        int soma = 0;
        for (int i = 0; i < notas.length; i++) {
            soma += notas[i];
        }
        System.out.println("média: " + soma / (double) notas.length);

        for (int nota : notas) {           // for-each
            if (nota < 6) continue;        // pula as reprovadas
            System.out.println("aprovado com " + nota);
        }

        int[] busca = {3, 9, 4};
        for (int n : busca) {
            if (n == 9) { System.out.println("achei"); break; }
        }
    }
}
```

```java
// Loops aninhados para percorrer matriz
int[][] matriz = {{1, 2}, {3, 4}};

for (int linha = 0; linha < matriz.length; linha++) {
    for (int coluna = 0; coluna < matriz[linha].length; coluna++) {
        System.out.print(matriz[linha][coluna] + " ");
    }
    System.out.println();
}
```

## Boas práticas

- Prefira for-each quando não precisar do índice.
- Declare o contador no próprio `for`; ele morre ao fim do loop.
- Use `while` quando o número de repetições é desconhecido.
- Extraia o corpo de loops longos para um método bem nomeado.
- Cuidado com limites: prefira `< array.length` a `<=`.

## Armadilhas comuns

- Modificar a coleção dentro do for-each lança `ConcurrentModificationException`.
- `do...while` executa pelo menos uma vez, mesmo com condição falsa.
- Loop infinito se a variável de controle nunca mudar.
- Off-by-one: acessar `array[array.length]` estoura o limite.
- `continue` dentro de loops aninhados afeta só o loop mais interno.

## Relacionadas

- [[Arrays-e-Collections]]
- [[Controle-de-Fluxo]]
- [[Java]]
