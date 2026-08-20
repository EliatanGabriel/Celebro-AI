---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Python

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem de alto nível, interpretada e multiparadigma, famosa pela sintaxe limpa, biblioteca padrão abrangente e enorme ecossistema em dados, inteligência artificial, web e automação.

## Conceitos-chave
- Multiparadigma: imperativa, orientada a objetos, funcional e procedural.
- Tipagem dinâmica e forte: tipos resolvidos em runtime, com operações inválidas barradas.
- Interpretada: compilada para bytecode na primeira execução e executada pela VM CPython.
- Uso principal em análise de dados, machine learning, automação, scripts, web (Django, FastAPI) e ciência.
- Indentação define blocos (4 espaços); sem chaves ou palavras-chave de fim.
- Gerenciamento de memória automático com garbage collector e reference counting.
- Particularidade: "batteries included" — biblioteca padrão ampla e o GIL limitando threads CPU-bound em CPython.

## Exemplos
```python
from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    idade: int

def maiores_de_idade(usuarios: list[Usuario]) -> list[str]:
    return [u.nome for u in usuarios if u.idade >= 18]

usuarios = [Usuario("Ana", 30), Usuario("Bruno", 16)]
print(maiores_de_idade(usuarios))  # ['Ana']

# Iteração e compreensão
quadrados = [n**2 for n in range(5)]
print(quadrados)  # [0, 1, 4, 9, 16]
```

## Boas práticas
- Siga o PEP 8 e use `snake_case` para variáveis/funções.
- Escreva docstrings e type hints (`int`, `str`, `Optional`) para clareza e ferramentas.
- Prefira list/dict comprehensions a loops simples, mas mantenha a legibilidade.
- Use `with` para gerenciar recursos (arquivos, conexões) e garantir liberação.
- Isole ambientes com `venv`/`uv` e fixe dependências (requirements/lockfile).

## Armadilhas comuns
- Mutabilidade como default: argumentos padrão `def f(x=[])` são compartilhados entre chamadas.
- Erro de indentação ao misturar tabs e espaços.
- Confundir `==` (valor) com `is` (identidade de objeto) — `is` compara referências.
- `copy()` rasa: listas aninhadas ainda compartilham referências; use `copy.deepcopy`.
- Engolir exceções com `except:` vazio, escondendo falhas.

## Relacionadas
- [[JavaScript]]
- [[Java]]
- [[Backend]]