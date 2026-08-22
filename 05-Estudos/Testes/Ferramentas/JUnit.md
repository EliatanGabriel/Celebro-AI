---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# JUnit

#area/estudos #estudos/testes #ferramenta

**Resumo:** Framework de testes padrão do Java; a versão 5 trouxe extensões, testes parametrizados e display names legíveis.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `@Test` | Marca método de teste | `@Test void soma()` |
| `@BeforeEach` / `@AfterEach` | Roda antes/depois de cada teste | Instanciar objeto |
| `@BeforeAll` / `@AfterAll` | Uma vez por classe (método estático) | Conexão de DB |
| `@DisplayName` | Nome legível no relatório | "deve recusar cupom expirado" |
| `assertEquals` | Igualdade | `assertEquals(5, calc.soma(2,3))` |
| `assertTrue` | Condição booleana | `assertTrue(lista.isEmpty())` |
| `assertThrows` | Captura exceção esperada | `assertThrows(IllegalArgumentException.class, ...)` |
| `assertAll` | Agrupa asserts (reporta todos os erros) | Validações múltiplas juntas |
| `@ParameterizedTest` | Teste com múltiplos dados | Combinado com sources abaixo |
| `@ValueSource` / `@CsvSource` | Fontes de dados parametrizados | ints, strings, CSV |

## Exemplos

```java
class CalculadoraTest {

    private Calculadora calc;

    @BeforeAll
    static void iniciaSuite() { /* recurso caro uma vez */ }

    @BeforeEach
    void prepara() { calc = new Calculadora(); }

    @Test
    @DisplayName("deve somar dois numeros")
    void deveSomar() {
        assertEquals(5, calc.soma(2, 3));
    }

    @Test
    void deveValidarCamposDePedido() {
        Pedido p = novoPedido();
        assertAll(
            () -> assertTrue(p.temItens()),
            () -> assertEquals("ANA", p.cliente())
        );
    }

    @ParameterizedTest
    @CsvSource({ "2,3,5", "0,0,0", "-1,1,0" })
    void somaVariada(int a, int b, int esperado) {
        assertEquals(esperado, calc.soma(a, b));
    }
}
```

```java
// Mockito em resumo
when(repo.buscar(1L)).thenReturn(usuario);
verify(repo, times(1)).buscar(1L);
```

## Integração

- Maven Surefire executa os testes em `mvn test`.
- Spring Boot: `spring-boot-starter-test` já traz JUnit 5, Mockito e AssertJ.

## Boas práticas

- Use `@DisplayName` para descrever comportamento em português.
- Prefira `assertAll` quando vários campos precisam ser validados juntos.
- Parametrize casos com só os dados mudando.

## Armadilhas comuns

- Esquecer `static` no `@BeforeAll` sem ciclo de vida por instância.
- Misturar JUnit 4 e 5 no mesmo classpath.
- Verificações Mockito excessivas acoplando à implementação.

## Relacionadas

- [[Testes]]
- [[Unittest-Python]]
- [[Mocks-Stubs-e-Fakes]]
- [[Boas-Praticas-de-Testes]]
- [[Cobertura-de-Codigo]]
