---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# Cobertura de Código

#area/estudos #estudos/testes #conceito

**Resumo:** Métrica que mede quais partes do código foram executadas pelos testes; útil para achar buracos, mas não garante qualidade.

## Referência rápida

| Métrica | O que mede | Exemplo |
|---|---|---|
| Statement/Line | Linhas executadas | 80/100 linhas rodaram = 80% |
| Branch | Caminhos de decisão (if/else, ternário) | Ambos os lados do `if` testados |
| Function | Funções chamadas ao menos uma vez | `calcularFrete()` nunca invocada |
| Mutation score | Mutantes mortos / mutantes gerados | Mede se os testes realmente assertam |

## Ferramentas

| Ferramenta | Ecossistema |
|---|---|
| Istanbul / c8 | JavaScript (via [[Jest]] ou `c8 node --test`) |
| pytest-cov | Python ([[Pytest]]) |
| JaCoCo | Java ([[JUnit]]) |
| @vitest/coverage-v8 | [[Vitest]] |
| PIT | Mutation testing em Java |
| Stryker | Mutation testing em JS/TS |

## Exemplos

```bash
# Jest com relatorio de cobertura
npx jest --coverage

# Pytest com cobertura e limiar minimo
pytest --cov=app --cov-report=term-missing --cov-fail-under=80
```

```java
// JUnit + JaCoCo via plugin Maven (trecho do pom.xml)
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
</plugin>
```

## Por que cobertura alta não significa testes bons

- Um teste sem `assert` executa 100% das linhas e valida zero comportamento.
- Código trivialmente executável infla o número sem proteger nada.
- 100% como meta incentiva testes vazios e mocks excessivos.

## Mutation testing

- PIT (Java) e Stryker (JS) alteram o código (trocam `+` por `-`, invertem condições).
- Se a suíte continua verde após a mutação, o "mutante sobreviveu": teste fraco.
- O score de mutação mede qualidade real; cobertura mede apenas execução.

## Boas práticas

- Use cobertura para localizar trechos sem nenhum teste.
- Defina limiares realistas por módulo, não globais arbitrários.
- Combine com revisão: leia os testes, não só o percentual.

## Armadilhas comuns

- Tratar cobertura como KPI de time ("mínimo 90%" cegamente).
- Escrever testes só para pintar linhas verdes no relatório.
- Ignorar branches: 90% de linhas pode esconder metade dos caminhos.
- Achar que 100% elimina bugs: nem todos os cenários estão codificados.

## Relacionadas

- [[Testes]]
- [[Boas-Praticas-de-Testes]]
- [[Piramide-de-Testes]]
- [[Jest]]
- [[Pytest]]
- [[JUnit]]
