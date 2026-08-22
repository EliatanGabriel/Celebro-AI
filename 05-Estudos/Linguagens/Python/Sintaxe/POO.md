---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Programação Orientada a Objetos em Python

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Classes agrupam dados e comportamento com `__init__` e `self`; herança, properties e dataclasses completam o kit básico de POO.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `class Nome:` | Declara uma classe (CapWords) | `class Conta:` |
| `__init__(self, ...)` | Construtor chamado na criação | `def __init__(self, titular):` |
| `self` | Referência à instância atual | `self.saldo = 0.0` |
| `__str__` | Texto amigável usado pelo `print()` | `return f"Conta de {self.titular}"` |
| `__repr__` | Representação técnica para debug | `return f"Conta({self.titular!r})"` |
| `class Filha(Pai):` | Herança simples | `class ContaCorrente(Conta):` |
| `super().__init__(...)` | Reaproveita o construtor do pai | `super().__init__(titular)` |
| `@property` | Método acessado como atributo | `conta.saldo` sem parênteses |
| `_x` / `__x` | Privado por convenção / name mangling | `self.__saldo` |
| `@dataclass` | Gera `__init__`, `__repr__` e comparações | `@dataclass class Ponto:` |

## Exemplos

```python
class Conta:
    banco = "Banco Azul"            # atributo de classe: igual para todas

    def __init__(self, titular, saldo=0.0):
        self.titular = titular      # atributos de instância: únicos por objeto
        self.__saldo = saldo        # "privado" por convenção

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("depósito deve ser positivo")
        self.__saldo += valor

    def __str__(self):
        return f"Conta de {self.titular}: R$ {self.saldo:.2f}"


conta = Conta("Ana")
conta.depositar(150)
print(conta)
```

```python
from dataclasses import dataclass

class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0.0, limite=200.0):
        super().__init__(titular, saldo)
        self.limite = limite
@dataclass
class Ponto:
    x: float
    y: float

print(Ponto(1.0, 2.0))  # Ponto(x=1.0, y=2.0) gerado automaticamente
```

## Boas práticas

- Classes recebem substantivos em CapWords; métodos recebem verbos.
- Use `@property` para expor cálculos como se fossem atributos.
- Prefira composição a herança quando a relação não for "é um".
- `_privado` basta para sinalizar uso interno; `__nome` só evita colisão em herança.
- Use `@dataclass` para classes que apenas carregam dados.

## Armadilhas comuns

- Esquecer o `self` na assinatura do método gera `TypeError` na chamada.
- Listas/dicts mutáveis como atributo de classe ficam compartilhados entre instâncias.
- Não chamar `super().__init__()` deixa a parte herdada sem inicializar.
- Acessar `objeto.__atributo` de fora da classe falha por causa do name mangling.
- Confundir `__str__` com `__repr__`: containers exibem seus itens via `__repr__`.

## Relacionadas

- [[Funcoes]]
- [[Erros-e-Excecoes]]
- [[Estruturas-de-Dados]]
- [[Python]]
