---
type: concept
area: faculdade
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Arquitetura e Padrões de Projeto

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Arquitetura de software e padrões de projeto: estilos arquiteturais, padrões de criação, estruturais e comportamentais, e princípios SOLID.

## 1. O que é arquitetura de software

Arquitetura é a estrutura de alto nível do sistema: seus componentes, relacionamentos e princípios que guiam o design e a evolução.

**Frase-chave:** a arquitetura define a "ossatura" do sistema; os padrões resolvem problemas recorrentes de projeto.

## 2. Estilos arquiteturais

- **Monolítica** — tudo em uma única aplicação.
- **Cliente-servidor** — cliente requisita, servidor responde.
- **Camadas (layered)** — divisão em camadas (apresentação, negócio, dados).
- **Microserviços** — serviços pequenos e independentes que se comunicam por rede.
- **Event-driven** — componentes reagem a eventos.
- **Arquitetura hexagonal / ports and adapters** — isola o núcleo de negócio das tecnologias externas.

## 3. Padrões de projeto (Design Patterns)

Padrões de projeto são soluções reutilizáveis para problemas comuns de design. São classificados em três grupos.

## 4. Padrões de criação

- **Singleton** — garante uma única instância da classe.
- **Factory Method** — delega a criação de objetos a subclasses.
- **Builder** — constrói objetos complexos passo a passo.

## 5. Padrões estruturais

- **Adapter** — adapta uma interface para outra esperada pelo cliente.
- **Facade** — fornece uma interface simplificada para um subsistema.
- **Decorator** — adiciona responsabilidades a um objeto dinamicamente.

## 6. Padrões comportamentais

- **Strategy** — define uma família de algoritmos intercambiáveis.
- **Observer** — notifica vários objetos quando o estado muda.
- **Command** — encapsula uma solicitação como objeto.

## 7. Princípios SOLID

- **S** — *Single Responsibility*: uma classe deve ter um único motivo para mudar.
- **O** — *Open/Closed*: aberta para extensão, fechada para modificação.
- **L** — *Liskov Substitution*: subclasses podem substituir suas classes base.
- **I** — *Interface Segregation*: interfaces específicas em vez de genéricas.
- **D** — *Dependency Inversion*: depender de abstrações, não de implementações.

## 8. Exemplo no dia a dia

Um sistema pode combinar:

```
Camada de apresentação (Front-end)
    ↓
Camada de aplicação (APIs)
    ↓
Camada de domínio (regras de negócio)
    ↓
Camada de infraestrutura (banco, filas, e-mail)
```

Padrões como Repository e Service são comuns nessa organização.

## 9. Quando usar padrões?

- Use quando o problema for recorrente e a solução conhecida.
- Não aplique padrões por "decoração" — cada padrão adiciona complexidade.
- O padrão certo reduz manutenção e melhora comunicação da equipe.

## Tópicos
- 

## Relacionadas

- [[Engenharia-de-Software]]
- [[Modelagem e UML]]
- [[Faculdade]]