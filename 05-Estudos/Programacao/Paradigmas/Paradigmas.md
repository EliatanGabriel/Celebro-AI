---
type: concept
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Paradigmas de Programação

#area/estudos #programacao #conceito #programacao #paradigmas #conceitos

**Resumo:** Diferentes formas de estruturar o pensamento e o código, cada uma com regras próprias de organização, estado e fluxo.

## Conceitos-chave
- **Imperativo:** descreve passo a passo como o programa deve executar, com comandos que mudam o estado.
- **Orientado a objetos:** organiza código em classes e objetos, combinando dados e comportamento, com encapsulamento, herança e polimorfismo.
- **Funcional:** trata a computação como avaliação de funções puras, evitando estado mutável e efeitos colaterais.
- **Declarativo:** descreve o que se deseja, deixando o "como" para a implementação (ex.: SQL e HTML).
- **Multiparadigma:** a maioria das linguagens combina estilos conforme o problema.

## Exemplos
```python
# Imperativo
soma = 0
for n in numeros:
    soma += n
print(soma)

# Funcional
from functools import reduce
soma = reduce(lambda a, b: a + b, numeros, 0)
print(soma)

# Declarativo (SQL)
# SELECT SUM(valor) FROM vendas;
```

## Boas práticas
- Escolher o paradigma segundo o domínio: dados → declarativo; regras de negócio → OO ou funcional.
- Preferir funções puras em partes críticas para facilitar o teste.
- Não misturar paradigmas no mesmo módulo sem clareza de intenção.

## Armadilhas comuns
- Acreditar que um paradigma é universalmente superior; cada um resolve bem um tipo de problema.
- Usar estado global em código funcional, quebrando a imutabilidade.
- Confundir programação funcional apenas com "usar lambdas".
- Forçar herança profunda quando composição seria mais simples.

## Relacionadas
- [[SOLID]]
- [[Clean-Code]]
- [[Orientacao-a-Objetos]]
- [[Programacao-Funcional]]
- [[Programacao-Procedural]]