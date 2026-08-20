---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Orientacao-a-Objetos

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Paradigma de programação que organiza o código em objetos — estruturas que combinam dados (atributos) e comportamento (métodos) — com foco em encapsulamento, herança e polimorfismo.

## Conceitos-chave
- **Classe:** molde/planta que define atributos e métodos; instâncias dela são os objetos.
- **Objeto:** instância concreta de uma classe, com seu próprio estado.
- **Encapsulamento:** esconder o estado interno e expor apenas uma interface; controla acesso (public/private/protected) e mantém invariantes.
- **Herança:** uma classe pode estender outra, reutilizando e especializando comportamento (é um tipo de).
- **Polimorfismo:** tratar objetos de classes diferentes por uma interface comum; a mesma chamada se comporta de forma diferente conforme o tipo real.
- **Abstração:** modelar apenas os aspectos relevantes do domínio, ignorando detalhes.
- **Composição:** alternativa à herança: construir objetos combinando outros (tem um).

## Exemplos
```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo          # encapsulamento: atributo "privado"

    def depositar(self, valor):      # interface pública
        if valor > 0:
            self._saldo += valor

    def saldo(self):
        return self._saldo


class ContaPoupanca(Conta):          # herança
    def render(self, taxa):
        self.depositar(self._saldo * taxa)


def mostrar_saldo(conta):            # polimorfismo: qualquer Conta funciona
    print(conta.titular, conta.saldo())


cc = Conta("Ana", 100)
cp = ContaPoupanca("Bia", 200)
mostrar_saldo(cc)                    # Ana 100
mostrar_saldo(cp)                    # Bia 200
```

## Boas práticas
- Favorecer composição sobre herança quando a relação não é claramente "é um".
- Manter o encapsulamento: expor o mínimo necessário pela interface.
- Seguir princípios como SOLID (responsabilidade única, aberto/fechado).
- Modelar com base no domínio do problema, não em detalhes técnicos.
- Usar polimorfismo via interfaces para reduzir acoplamento.

## Armadilhas comuns
- Herança em cadeia profunda, gerando hierarquias frágeis e acopladas.
- Expor atributos internos sem necessidade, quebrando invariantes.
- Confundir herança (é um) com composição (tem um) e modelar errado.
- Superutilizar padrões de OO em problemas que seriam mais simples em outro paradigma.
- Mutação descontrolada de estado compartilhado entre objetos.

## Relacionadas
- [[Paradigmas]]
- [[Programacao-Funcional]]
- [[Programacao-Procedural]]
- [[Estudos-Funcoes]]
- [[Tipos-de-Dados]]
- [[Debug]]
- [[Programacao]]