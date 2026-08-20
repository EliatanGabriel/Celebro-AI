---
type: concept
area: faculdade
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Engenharia de Requisitos

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Engenharia de requisitos: tipos de requisitos, atividades do processo, documentos de requisitos e boas práticas para levantar e validar necessidades.

## 1. O que é um requisito

Um requisito é uma condição ou capacidade que o software deve atender. É a ponte entre a necessidade do cliente e o que o sistema fará.

**Frase-chave:** um bom requisito responde *"o que o sistema deve fazer"*, não *"como fazer"*.

## 2. Tipos de requisitos

### 2.1. Requisitos funcionais

Descrevem o que o sistema **faz**.

- "O sistema deve permitir login com e-mail e senha."
- "O sistema deve calcular o IMC a partir de peso e altura."

### 2.2. Requisitos não funcionais

Descrevem **qualidades** ou restrições do sistema.

- **Desempenho** — "resposta em menos de 2 segundos".
- **Segurança** — "senhas armazenadas com hash".
- **Usabilidade** — "interface intuitiva".
- **Confiabilidade** — "99,9% de disponibilidade".
- **Compatibilidade** — "funciona em navegadores modernos".

## 3. Atividades do processo

```
Levantamento (elicitação)
    ↓
Análise e negociação
    ↓
Especificação (documentação)
    ↓
Validação
    ↓
Gerenciamento de requisitos
```

### 3.1. Levantamento

Técnicas de coleta de requisitos:

- Entrevistas com stakeholders
- Questionários
- Observação do ambiente de trabalho
- Brainstorming
- Análise de documentos existentes
- Prototipação

### 3.2. Análise e negociação

- Classificar e priorizar requisitos (ex.: MoSCoW — Must, Should, Could, Won't).
- Resolver conflitos entre stakeholders.
- Verificar viabilidade.

### 3.3. Especificação

Documentar os requisitos de forma clara e sem ambiguidades, normalmente em um **Documento de Requisitos** ou no **Product Backlog** (em projetos ágeis).

### 3.4. Validação

Confirmar que os requisitos realmente representam o que o cliente deseja:

- Revisões com stakeholders.
- Protótipos validados.
- Casos de teste derivados dos requisitos.

## 4. Boas características de um requisito

- **Completo** — não falta informação.
- **Consistente** — não contradiz outros requisitos.
- **Sem ambiguidade** — apenas uma interpretação.
- **Verificável** — é possível testar se foi atendido.
- **Rastreável** — é possível saber sua origem.
- **Priorizado** — sabe-se sua importância.

## 5. Requisitos funcionais × não funcionais

| Funcional | Não funcional |
| --- | --- |
| O que o sistema faz | Como o sistema se comporta |
| "Calcular nota final" | "Recalcular em menos de 1s" |
| Testável por funcionalidade | Testável por atributo de qualidade |

## Tópicos
- 

## Relacionadas

- [[Engenharia-de-Software]]
- [[Processos e Modelos de Desenvolvimento]]
- [[Faculdade]]