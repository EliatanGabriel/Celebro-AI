---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Linguagens Formais

#area/estudos #estudos/teoria-da-computacao #conceito #teoria #computacao #linguagens

**Resumo:** Conjuntos de cadeias definidas por gramáticas e autômatos, classificados pela hierarquia de Chomsky segundo o poder gerador.

## Conceitos-chave
- **Linguagem:** conjunto de cadeias sobre um alfabeto; pode ser finito ou infinito.
- **Expressões regulares:** descrevem linguagens regulares com concatenação, união e estrela de Kleene.
- **Gramáticas:** regras de produção que geram as cadeias de uma linguagem.
- **Hierarquia de Chomsky:** tipo 3 (regulares), tipo 2 (livres de contexto), tipo 1 (sensíveis ao contexto) e tipo 0 (recursivamente enumeráveis).
- **Relação com autômatos:** cada nível corresponde a uma máquina: AF, AP e Máquina de Turing.

## Exemplos
```text
Gramática livre de contexto para a linguagem {aⁿbⁿ | n ≥ 0}:
S -> a S b
S -> ε

Exemplos de cadeias geradas: "", "ab", "aabb", "aaabbb"
```

```python
import re

# Expressão regular: strings binárias com pelo menos um "1"
regex = re.compile(r"0*1[01]*")
print(bool(regex.fullmatch("00101")))  # True
print(bool(regex.fullmatch("0000")))   # False
```

## Boas práticas
- Identificar o nível da linguagem antes de escolher a ferramenta (regex, parser, autômato).
- Testar linguagens com cadeias de fronteira (vazia, mínima e inválida).
- Derivar cadeias passo a passo a partir da gramática para validar a geração.

## Armadilhas comuns
- Tentar reconhecer linguagens não regulares (como aⁿbⁿ) apenas com expressões regulares.
- Confundir a linguagem com a gramática que a gera: uma linguagem pode ter várias gramáticas.
- Ignorar que a hierarquia de Chomsky é inclusiva: linguagem regular também é livre de contexto.

## Relacionadas
- [[Automatos]]
- [[Complexidade]]
- [[Computacao]]