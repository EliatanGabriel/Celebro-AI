---
type: concept
area: faculdade
status: active
progresso: "estudando"
created: "2026-08-19"
updated: "2026-08-19"
---

# Desvio Condicional

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Desvio condicional em Python: if, if/else, if/elif/else, aninhamento, operador ternário, match/case, truthy/falsy e guard clauses.

## 1. if

O `if` executa determinado bloco somente quando uma condição é verdadeira (`True`).

```python
if idade >= 18:
    print("Maior de idade")
```

Uma característica importante do Python é a utilização da **indentação** para definir o bloco de código, em vez das `{}` utilizadas em linguagens como Java.

## 2. if/else

O `else` cria um segundo caminho para quando a condição do `if` for falsa.

```python
if saldo >= valor:
    print("Saque liberado")
else:
    print("Saldo insuficiente")
```

Assim, o programa possui dois possíveis caminhos.

## 3. if/elif/else

Quando existem várias possibilidades, podemos utilizar `elif`.

```python
if temperatura < 15:
    print("Frio")
elif temperatura < 25:
    print("Agradável")
else:
    print("Calor")
```

O Python verifica as condições em ordem e executa apenas o primeiro bloco cuja condição seja verdadeira.

## 4. Aninhamento

É possível colocar um `if` dentro de outro `if`, mas o excesso de aninhamento torna o código difícil de entender.

A aula recomenda evitar mais de três níveis de aninhamento e, quando possível, utilizar `elif`, operadores lógicos ou dividir a lógica em funções.

## 5. Operador ternário

O operador ternário permite escrever um `if/else` de maneira compacta, geralmente para atribuições simples:

```python
status = "Aprovado" if nota >= 7 else "Reprovado"
```

Ele é útil quando a condição é simples e a lógica continua fácil de compreender.

## 6. match/case

O `match/case`, disponível a partir do Python 3.10, é utilizado para roteamento e correspondência de padrões.

```python
match status:
    case 200:
        print("Sucesso")
    case 404:
        print("Não encontrado")
    case _:
        print("Erro")
```

O `_` funciona como um caso padrão para situações que não foram especificadas.

## 7. Truthy e Falsy

Python consegue interpretar determinados valores diretamente como verdadeiros ou falsos.

Por exemplo, estruturas vazias como:

```python
""
[]
```

são consideradas **Falsy**.

Já valores preenchidos, como uma string ou uma lista com elementos, são considerados **Truthy**.

Isso permite escrever condições de maneira mais Pythonica, sem comparações desnecessárias.

## 8. Guard Clauses

As **Guard Clauses**, ou retornos antecipados, ajudam a reduzir aninhamentos.

Em vez de colocar toda a lógica dentro de vários `if`, podemos verificar primeiro as situações de erro:

```python
if not pedido.valido:
    return "Erro"

if not pedido.pago:
    return "Pendente"

return "Sucesso"
```

Isso deixa o código mais plano, limpo e fácil de ler.

## 9. Aplicação prática

A aula mostra que sistemas reais combinam diferentes estruturas condicionais. Um caixa eletrônico, por exemplo, pode utilizar:

- `if/else` para autenticação
- `if/elif/else` para regras de saque
- `match/case` para diferentes opções do sistema

## 10. Exercícios propostos

A aula sugere desafios como:

- Classificar um triângulo
- Classificar uma faixa etária
- Criar uma calculadora
- Identificar um ano bissexto
- Criar um jogo de Pedra, Papel e Tesoura

**Ideia principal:** a programação deixa de ser apenas sequencial e passa a tomar decisões com base em condições, utilizando `if`, `elif`, `else`, operador ternário e `match/case`.

## Tópicos
- 

## Relacionadas

- [[POO]]
- [[Faculdade]]