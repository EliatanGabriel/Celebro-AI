---
type: concept
area: faculdade
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Modelagem e UML

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Modelagem de software com UML: o que é, diagramas estruturais e comportamentais, casos de uso e boas práticas de modelagem.

## 1. O que é modelagem

Modelagem é criar representações simplificadas de um sistema antes de construí-lo. Um modelo ajuda a:

- Entender o problema.
- Comunicar ideias entre a equipe.
- Encontrar erros cedo.
- Documentar decisões.

**Frase-chave:** modelos são "plantas" do software, assim como plantas arquiteturais para a construção civil.

## 2. O que é UML

UML (*Unified Modeling Language*) é uma linguagem padrão para visualizar, especificar, construir e documentar sistemas de software. É composta por **diagramas**.

## 3. Diagramas estruturais

Mostram a **estrutura estática** do sistema (o que existe).

- **Diagrama de classes** — classes, atributos, métodos e relacionamentos.
- **Diagrama de objetos** — instâncias em um momento específico.
- **Diagrama de componentes** — componentes de software e dependências.
- **Diagrama de implantação** — hardware e software físico.

## 4. Diagramas comportamentais

Mostram o **comportamento dinâmico** (o que acontece ao longo do tempo).

- **Diagrama de casos de uso** — interações entre atores e sistema.
- **Diagrama de sequência** — sequência de mensagens entre objetos.
- **Diagrama de atividades** — fluxo de atividades e decisões.
- **Diagrama de estados** — estados pelos quais um objeto passa.

## 5. Diagrama de casos de uso

Mostra **quem** (ator) interage com o sistema e **para quê** (caso de uso).

**Elementos:**

- **Ator** — papel externo (usuário, sistema, cliente).
- **Caso de uso** — funcionalidade oferecida.
- **Relacionamentos** — include (sempre inclui) e extend (opcionalmente estende).

**Exemplo de caixa eletrônico:**

- Ator: Cliente
- Casos de uso: Sacar dinheiro, Consultar saldo, Depositar
- `Sacar dinheiro` **include** `Autenticar`

## 6. Diagrama de classes

É o diagrama mais utilizado. Uma classe é representada por um retângulo dividido em três partes:

```
+------------------+
|     Cliente      |   ← Nome
+------------------+
| nome: str        |   ← Atributos
| saldo: float     |
+------------------+
| + depositar()    |   ← Métodos
| + sacar()        |
+------------------+
```

**Relacionamentos:**

- **Associação** — linha simples.
- **Composição** — losango preenchido (parte pertence ao todo).
- **Agregação** — losango vazio (parte pode existir sozinha).
- **Herança** — seta com triângulo.

## 7. Diagrama de sequência

Descreve a ordem das mensagens entre objetos ao longo do tempo.

```
Cliente → CaixaEletronico: inserir cartão
Cliente → CaixaEletronico: senha
CaixaEletronico → Banco: verificar senha
Banco → CaixaEletronico: ok
```

## 8. Boas práticas de modelagem

- Modelar apenas o que agrega valor — não "diagramas por diagramas".
- Manter os diagramas simples e atualizados.
- Utilizar ferramentas (draw.io, Lucidchart, PlantUML).
- Em projetos ágeis, preferir diagramas enxutos e código como documentação.

## Tópicos
- 

## Relacionadas

- [[Engenharia-de-Software]]
- [[Engenharia de Requisitos]]
- [[Faculdade]]