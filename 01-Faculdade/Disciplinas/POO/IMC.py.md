---
type: concept
area: faculdade
status: active
progresso: "estudando"
created: "2026-08-19"
updated: "2026-08-19"
---

# IMC.py

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Exercício de cálculo de IMC em Python: recebe nome, peso e altura, calcula o índice e classifica o resultado.

## Código

```python
nome:str = input("Nome: ")
peso: float = float(input("Peso (kg): "))
altura: float = float(input("Altura (m): "))

imc:float = peso/(altura**2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Sua classificação é {classificacao}")
```

## O que o código faz

- Recebe nome, peso e altura.
- Calcula o IMC com a fórmula `peso / altura²`.
- Classifica o resultado com `if/elif/else`.

## Tópicos
- 

## Relacionadas

- [[POO]]
- [[Fundamentos de Python]]
- [[Desvio Condicional]]