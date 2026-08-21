---
type: concept
area: faculdade
status: active
progresso: "estudando"
created: "2026-08-19"
updated: "2026-08-19"
---

# Dias da semana.py

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Exercício de `match/case` em Python: recebe um número de 1 a 7 e exibe o dia da semana correspondente.

## Código

```python
dia:int = int(input("Numero do dia da semana (1-7): "))

match dia:
    case 1:
        nome_dia = "Domingo"
    case 2:
        nome_dia = "Segunda-feira"
    case 3:
        nome_dia = "Terça-feira"
    case 4:
        nome_dia = "Quarta-feira"
    case 5:
        nome_dia = "Quinta-feira"
    case 6:
        nome_dia = "Sexta-feira"
    case 7:
        nome_dia = "Sabado"
    case _:
        nome_dia = "Errrouuuu"

print(f"Dia é: {nome_dia}")
```

## O que o código faz

- Recebe um número de 1 a 7.
- Utiliza `match/case` para mapear cada número a um dia da semana.
- O `_` funciona como caso padrão para valores inválidos.

## Tópicos
- 

## Relacionadas

- [[POO]]
- [[Desvio Condicional]]