---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Logica-de-Programacao

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Capacidade de estruturar sequências de instruções — usando sequência, decisão e repetição — para transformar um problema em um algoritmo executável.

## Conceitos-chave
- **Sequência:** instruções executadas na ordem em que aparecem.
- **Condicionais (decisão):** `if`/`else` desviam o fluxo com base em uma condição; permitem caminhos alternativos.
- **Repetição (loop):** `for`, `while` e `do-while` executam um bloco várias vezes, com condição de parada.
- **Abstração:** quebrar um problema grande em subproblemas menores (funções, módulos).
- **Pseudocódigo:** notação simplificada para expressar a lógica antes de traduzir para uma linguagem real.
- **Entrada, processamento, saída:** o padrão básico de um programa; dados entram, são transformados e saem.

## Exemplos
```text
// Pseudocódigo: soma dos números de 1 a n
funcao soma_ate(n):
    total = 0
    para i de 1 até n:
        total = total + i
    retorne total
```

```python
# Condicional + repetição: contar pares de uma lista
def contar_pares(numeros):
    contador = 0
    for n in numeros:
        if n % 2 == 0:
            contador += 1
    return contador

# Validação com repetição (repete até receber entrada válida)
while True:
    nota = int(input("Nota (0 a 10): "))
    if 0 <= nota <= 10:
        break
    print("Valor inválido, tente novamente.")
```

## Boas práticas
- Escrever pseudocódigo ou fluxograma antes do código para problemas não triviais.
- Testar cada caso: condição falsa, loop que não executa e loop que nunca termina.
- Dar nomes descritivos a variáveis e funções.
- Quebrar a lógica em funções pequenas com responsabilidade única.
- Validar entradas antes de processar, garantindo o caminho esperado.

## Armadilhas comuns
- Loop infinito por condição de parada que nunca se torna verdadeira.
- Erro de off-by-one (percorrer até `n` quando deveria ser `n-1`, ou vice-versa).
- Usar `=` em vez de `==` dentro de uma condição.
- Não tratar a entrada inválida, deixando o programa quebrar.
- Escrever condicionais aninhadas demais, dificultando a leitura (buscar early return).

## Relacionadas
- [[Logica]]
- [[Algoritmos]]
- [[Estudos-Variaveis]]
- [[Estudos-Funcoes]]
- [[Programacao]]
- [[Debug]]
- [[JSON]]