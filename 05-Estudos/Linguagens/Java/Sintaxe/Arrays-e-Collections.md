---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Arrays e Collections em Java

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Java oferece arrays de tamanho fixo e o Collections Framework (List, Set, Map) com estruturas dinâmicas para os usos mais comuns do dia a dia.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `int[] a = new int[5]` | Array fixo com valores padrão (0) | `int[] idades = new int[5];` |
| `int[] a = {1, 2, 3}` | Inicializador com valores | `String[] nomes = {"Ana"};` |
| `a.length` | Tamanho do array (campo, sem parênteses) | `for (int i = 0; i < a.length; i++)` |
| `int[][] m` | Matriz bidimensional | `m[1][2] = 7;` |
| `list.add/get/remove` | ArrayList: adiciona/acessa/remove | `nomes.add("Ana"); nomes.get(0);` |
| `list.size()` | Quantidade de elementos da lista | `nomes.size()` |
| `list.contains(x)` | Verifica se elemento existe | `nomes.contains("Ana")` |
| `set.add(x)` | HashSet: sem duplicatas, ordem não garantida | `cpfs.add("123");` |
| `map.put(k, v)` / `map.get(k)` | HashMap: associa chave a valor | `estoque.put("uva", 8);` |
| `map.getOrDefault(k, padrao)` | Retorna valor ou padrão se ausente | `map.getOrDefault(k, 0)` |
| `List.of(...)` / `Arrays.asList(...)` | Listas imutáveis / fixas de fábrica | `List.of("a", "b")` |

## Exemplos

```java
// Array fixo e matriz
import java.util.Arrays;

public class ArraysDemo {
    public static void main(String[] args) {
        int[] notas = {8, 5, 10};
        Arrays.sort(notas);
        System.out.println(Arrays.toString(notas)); // [5, 8, 10]

        int[][] tabuleiro = new int[3][3];
        tabuleiro[1][2] = 9;
    }
}
```

```java
// ArrayList, HashSet e HashMap
import java.util.*;

List<String> tarefas = new ArrayList<>();
tarefas.add("estudar");
tarefas.add("treinar");
System.out.println(tarefas.contains("estudar")); // true

Set<String> emails = new HashSet<>();
emails.add("a@x.com");
emails.add("a@x.com");                 // ignorado: duplicata

Map<String, Integer> estoque = new HashMap<>();
estoque.put("uva", 8);
estoque.put("pera", estoque.getOrDefault("pera", 0) + 1);
```

## Boas práticas

- Programe contra a interface: declare `List<String> l = new ArrayList<>()`.
- Prefira coleções dinâmicas quando o tamanho pode variar.
- Use `getOrDefault` em vez de checar null manualmente no Map.
- Escolha `LinkedHashSet`/`TreeSet` quando a ordem importar.
- Use `List.of()` para constantes que nunca mudam.

## Armadilhas comuns

- `length` em array é campo; em String e List é método (`length()`, `size()`).
- `Arrays.asList` tem tamanho fixo: `add` lança exceção.
- `List.of` é imutável: qualquer mutação lança `UnsupportedOperationException`.
- Acessar índice fora do array lança `ArrayIndexOutOfBoundsException`.
- `HashSet` não garante ordem de iteração dos elementos.

## Relacionadas

- [[Loops]]
- [[POO-e-Heranca]]
- [[Java]]
