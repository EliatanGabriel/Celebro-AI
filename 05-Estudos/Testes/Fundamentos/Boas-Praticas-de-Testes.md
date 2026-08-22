---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# Boas Práticas de Testes

#area/estudos #estudos/testes #conceito

**Resumo:** Conjunto de princípios que mantêm a suíte rápida, confiável e legível, independentemente da ferramenta usada.

## Referência rápida

| Prática | O que significa |
|---|---|
| AAA / Given-When-Then | Estruturar em Preparação → Ação → Verificação |
| FIRST | Fast, Independent, Repeatable, Self-validating, Timely |
| Um comportamento por teste | Foco único; falha aponta a causa direto |
| Nomes descritivos | `deve recusar cupom expirado quando data passada` |
| Isolamento | Sem ordem implícita nem estado compartilhado |
| Determinismo | Sem sleep; relógio congelado; seed fixa |
| Testar comportamento público | Não depender de detalhes privados |
| Builders/factories | Dados de teste legíveis e reutilizáveis |

## Exemplos

```js
// AAA + nome descritivo + um comportamento
test("deve aplicar frete gratis quando subtotal acima de 200", () => {
  // Arrange
  const carrinho = criarCarrinho().comItem({ preco: 250 }).construir();
  // Act
  const frete = calcularFrete(carrinho);
  // Assert
  expect(frete).toBe(0);
});
```

```python
# determinismo: congelar o relogio em vez de sleep
@pytest.fixture
def relogio_congelado(monkeypatch):
    monkeypatch.setattr(modulo, "agora", lambda: datetime(2026, 1, 1))
```

## Princípios FIRST em resumo

- **Fast**: testes lentos não rodam com frequência.
- **Independent**: cada teste funciona sozinho e em qualquer ordem.
- **Repeatable**: mesmo resultado em qualquer máquina ou hora.
- **Self-validating**: passa ou falha sem inspeção manual.
- **Timely**: escritos junto com o código, não meses depois.

## Boas práticas

- Um comportamento por teste; se precisa de "e" no nome, divida.
- Nomeie como `deve <resultado> quando <condição>`.
- Limpe estado entre testes (fixtures, beforeEach) em vez de confiar na ordem.
- Congele relógio, fixe seeds de aleatoriedade, mocke rede ([[Mocks-Stubs-e-Fakes]]).
- Use test data builders/factories para objetos complexos legíveis.

## Armadilhas comuns

- Testes que dependem da ordem de execução ou de dados deixados por outros.
- `sleep` para "esperar algo acontecer": instável e lento.
- Assertar sobre métodos privados ou estrutura interna: refatorar quebra tudo.
- Vários asserts de comportamentos diferentes escondendo a falha real.
- Dados mágicos ilegíveis (`x = 3`) sem contexto no Arrange.

## Relacionadas

- [[Testes]]
- [[TDD]]
- [[Piramide-de-Testes]]
- [[Cobertura-de-Codigo]]
- [[Jest]]
- [[Pytest]]
