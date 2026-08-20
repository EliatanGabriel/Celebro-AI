---
type: concept
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# SOLID

#area/estudos #programacao #conceito #design #principios #orientacao-a-objetos

**Resumo:** Cinco princípios de design de software orientado a objetos que orientam sistemas flexíveis, extensíveis e de fácil manutenção.

## Conceitos-chave
- **S — Single Responsibility:** cada classe tem um único motivo para mudar.
- **O — Open/Closed:** aberto para extensão e fechado para modificação, via interfaces, herança ou estratégias.
- **L — Liskov Substitution:** subtipos devem ser substituíveis pelo tipo base sem alterar o comportamento esperado.
- **I — Interface Segregation:** interfaces pequenas e específicas em vez de uma interface genérica.
- **D — Dependency Inversion:** depender de abstrações, não de implementações concretas.

## Exemplos
```python
# Violação do DIP: classe depende de implementação concreta
class EmailService:
    def enviar(self, msg): ...

class Notificador:
    def __init__(self):
        self._email = EmailService()

# Correto: depender da abstração (interface)
class CanalNotificacao:
    def enviar(self, msg): ...

class Notificador:
    def __init__(self, canal: CanalNotificacao):
        self._canal = canal
```

## Boas práticas
- Aplicar cada princípio em torno de um sintoma concreto: mudanças frequentes, dificuldade de teste, acoplamento.
- Usar composição e injeção de dependência para o DIP.
- Escrever testes que validem o contrato dos subtipos (LSP).

## Armadilhas comuns
- Aplicar SOLID dogmaticamente, gerando abstrações desnecessárias para código simples.
- Confundir Single Responsibility com "classe faz só uma coisa"; trata-se de um único motivo de mudança.
- Criar hierarquias que violam Liskov (ex.: `Quadrado` herdando de `Retangulo` com comportamento inconsistente).
- Inverter dependências em excesso, adicionando camadas sem benefício real.

## Relacionadas
- [[Clean-Code]]
- [[Paradigmas]]
- [[Orientacao-a-Objetos]]