---
type: concept
area: faculdade
status: active
progresso: "estudando"
created: "2026-08-19"
updated: "2026-08-19"
---

# variaveis.py

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Exercício de variáveis e desvio condicional em Python: recebe nome e função do usuário e exibe uma saudação de acordo com o papel (Professor ou Aluno).

## Código

```python
nome:str = input("Nome: ")
role:str = input("Sua função: ")
# print(f"Olá {nome}")

if role == "Professor":
    print(f" Olá professor {nome}")
elif role == "Aluno":
    print(f"Ola aluno {nome}")
else:
    print("Errouuuuu")
```

## O que o código faz

- Recebe o nome e a função do usuário.
- Verifica a função com `if/elif/else`.
- Exibe a saudação apropriada para cada papel.

## Tópicos
- 

## Relacionadas

- [[POO]]
- [[Fundamentos de Python]]
- [[Desvio Condicional]]