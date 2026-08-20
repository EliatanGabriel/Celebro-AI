---
type: concept
area: faculdade
status: active
created: "2026-08-19"
updated: "2026-08-19"
---

# Fundamentos de Python

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Fundamentos de Python: variáveis, tipos de dados, nomenclatura, conversão de tipos, operadores, entrada e saída e execução sequencial.

## 1. Variáveis

Em Python, uma variável é uma referência para um valor armazenado na memória. Diferentemente de linguagens com tipagem estática, não é necessário declarar previamente o tipo da variável.

Python utiliza **tipagem dinâmica**, portanto o tipo é determinado durante a execução.

## 2. Tipos de dados

Os principais tipos apresentados são:

- `int` → números inteiros
- `float` → números decimais
- `str` → textos
- `bool` → True ou False
- `None` → ausência intencional de valor

Também são apresentados os **Type Hints**, que servem para documentar o tipo esperado e facilitar a verificação e compreensão do código.

## 3. Nomenclatura

A aula apresenta as regras de nomenclatura seguindo o padrão **PEP 8**. Para variáveis e funções, é comum utilizar `snake_case`, como:

```python
nome_usuario
idade_usuario
```

Não se deve começar nomes com números ou utilizar palavras reservadas da linguagem.

## 4. Conversão de tipos

Python permite converter valores utilizando funções como:

```python
int()
float()
str()
```

Essa conversão é chamada de **casting**. É necessário ter cuidado porque uma conversão inválida pode gerar um `ValueError`.

## 5. Operadores

Os operadores aritméticos principais são:

- `+` → adição
- `-` → subtração
- `*` → multiplicação
- `/` → divisão
- `//` → divisão inteira
- `%` → resto
- `**` → exponenciação

Uma particularidade importante é que Python não utiliza `++` ou `--` como C/Java.

## 6. Comparação e lógica

Os operadores de comparação permitem verificar relações entre valores, como `==`, `!=`, `>`, `<`, `>=` e `<=`.

Já os operadores lógicos permitem combinar condições. A aula também apresenta:

- `is` / `is not` → identidade
- `in` / `not in` → pertencimento

## 7. Entrada e saída

A função `input()` permite receber informações do usuário. Um ponto importante é que `input()` sempre retorna uma `str`, mesmo quando o usuário digita um número.

Por isso, para realizar operações matemáticas, é necessário converter o valor:

```python
idade = int(input("Digite sua idade: "))
```

Para exibir informações, a aula apresenta o `print()` e as **f-strings**, que permitem inserir variáveis diretamente dentro de textos.

## 8. Execução sequencial

Por padrão, Python executa o programa linha por linha, de cima para baixo.

Esse é o chamado **fluxo sequencial**. Uma instrução precisa terminar para que a próxima seja executada.

**Ideia principal:** antes de ensinar o programa a tomar decisões, é necessário entender como ele armazena dados, realiza operações, recebe informações e executa instruções sequencialmente.

## Tópicos
- 

## Relacionadas

- [[POO]]
- [[Faculdade]]