---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# BDD (Behavior-Driven Development)

#area/estudos #estudos/testes #conceito

**Resumo:** Prática de descrever comportamentos em linguagem estruturada (Given/When/Then) junto com o negócio, antes do código.

## Referência rápida

| Conceito | O que faz | Exemplo |
|---|---|---|
| Given / Dado | Estado inicial do cenário | `Dado que o usuário está logado` |
| When / Quando | Ação disparada | `Quando ele adiciona um item ao carrinho` |
| Then / Então | Resultado esperado | `Então o total é atualizado` |
| Feature | Agrupa cenários de uma funcionalidade | `Funcionalidade: carrinho de compras` |
| Scenario Outline | Cenário com exemplos parametrizados | `Exemplos:` com tabela |
| Background | Passos comuns a todos os cenários | Pré-condições compartilhadas |

## Exemplos

```gherkin
Funcionalidade: Saque no caixa eletrônico

  Cenário: Saque com saldo suficiente
    Dado que a conta tem saldo de R$ 100
    E o cartão é válido
    Quando o cliente saca R$ 50
    Então o saldo final deve ser R$ 50
    E a nota deve ser entregue

  Esquema do Cenário: Saque acima do limite diário
    Dado que a conta tem saldo de R$ 1000
    Quando o cliente saca <valor>
    Então deve ver a mensagem "<erro>"

    Exemplos:
      | valor | erro                      |
      | 2000  | Limite diário excedido    |
      | -10   | Valor inválido            |
```

```python
# passo correspondente (Behave, Python)
@given("que a conta tem saldo de {valor:d}")
def conta_com_saldo(context, valor):
    context.conta = Conta(saldo=valor)
```

## Ferramentas

- **Cucumber**: Java, JS, Ruby e outras.
- **Behave**: Python, com decorators given/when/then.
- **SpecFlow**: .NET (sucessor Reqnroll).

## BDD como conversa

- O coração do BDD acontece ANTES do código: negócio, dev e QA escrevem os cenários juntos.
- Os arquivos .feature são documentação executável e contrato compartilhado.
- Diferença para TDD: TDD foca no design de unidades de código; BDD foca no comportamento observável do sistema e no vocabulário do domínio. São complementares.

## Boas práticas

- Escreva cenários na linguagem do negócio, sem detalhes técnicos.
- Um comportamento por cenário; título declarativo.
- Use Esquema do Cenário para variar só os dados.
- Mantenha passos reutilizáveis e genéricos.

## Armadilhas comuns

- Usar Gherkin apenas como script frágil de UI (seletores XPath nos passos).
- Cenários gigantes com muitos When encadeados.
- Duplicar lógica nos steps em vez de chamar o sistema.
- Adotar a ferramenta sem a conversa: vira TDD com sintaxe mais longa.

## Relacionadas

- [[Testes]]
- [[TDD]]
- [[Boas-Praticas-de-Testes]]
- [[Tipos-de-Teste]]
- [[Pytest]]
