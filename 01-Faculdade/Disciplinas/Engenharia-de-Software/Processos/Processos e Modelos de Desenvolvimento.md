---
type: concept
area: faculdade
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Processos e Modelos de Desenvolvimento

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Processos e modelos de desenvolvimento de software: cascata, iterativo, incremental, espiral, ágil, Scrum e Kanban.

## 1. Modelo Cascata

O modelo cascata segue um fluxo linear e sequencial. Cada fase só começa quando a anterior termina.

```
Requisitos
    ↓
Projeto
    ↓
Implementação
    ↓
Testes
    ↓
Implantação
    ↓
Manutenção
```

**Vantagens:** simples de entender, documentação completa.

**Desvantagens:** pouco flexível, erros descobertos tarde, retrabalho caro.

## 2. Modelo Iterativo e Incremental

Em vez de entregar tudo de uma vez, o software é desenvolvido em ciclos. Cada **iteração** repete as atividades do processo e entrega um **incremento** do produto.

```
Incremento 1 → requisitos + projeto + código + testes
Incremento 2 → requisitos + projeto + código + testes
Incremento 3 → ...
```

**Vantagens:** feedback mais cedo, riscos reduzidos, partes funcionais são entregues antes.

## 3. Modelo Espiral

Combina o cascata com prototipação e análise de risco. Cada loop da espiral passa por:

1. Determinar objetivos
2. Analisar riscos
3. Desenvolver e testar
4. Planejar a próxima iteração

Indicado para projetos grandes, complexos e de alto risco.

## 4. Desenvolvimento Ágil

O Manifesto Ágil (2001) valoriza:

- **Indivíduos e interações** mais que processos e ferramentas.
- **Software funcionando** mais que documentação extensa.
- **Colaboração com o cliente** mais que negociação de contratos.
- **Responder a mudanças** mais que seguir um plano.

## 5. Scrum

Scrum é o framework ágil mais usado. Elementos principais:

- **Sprint** — ciclo de trabalho de 1 a 4 semanas.
- **Product Backlog** — lista priorizada de funcionalidades.
- **Sprint Backlog** — tarefas selecionadas para a sprint.
- **Incremento** — resultado entregue ao final de cada sprint.

**Papéis:**

- **Product Owner** — define prioridades e representa o cliente.
- **Scrum Master** — facilita o processo e remove impedimentos.
- **Time de desenvolvimento** — constrói o incremento.

**Eventos:** Sprint Planning, Daily Scrum, Sprint Review e Sprint Retrospective.

## 6. Kanban

Kanban é um método visual de gerenciamento de fluxo de trabalho, baseado em um quadro de colunas (To Do, Doing, Done).

Princípios:

- Visualizar o trabalho.
- Limitar o trabalho em progresso (WIP).
- Gerenciar o fluxo.
- Melhoria contínua.

## 7. Cascata × Ágil

| Cascata | Ágil |
| --- | --- |
| Sequencial | Iterativo |
| Documentação extensa | Software funcionando |
| Cliente no início e no fim | Cliente participa o tempo todo |
| Mudanças caras | Mudanças bem-vindas |
| Entregas no final | Entregas frequentes |

## 8. Qual modelo escolher?

- **Cascata** — requisitos estáveis, projetos simples, escopo fixo.
- **Iterativo/Incremental** — quando se quer feedback cedo.
- **Espiral** — projetos grandes e arriscados.
- **Ágil** — requisitos que mudam, times pequenos e colaborativos.

## Tópicos
- 

## Relacionadas

- [[Engenharia-de-Software]]
- [[Faculdade]]