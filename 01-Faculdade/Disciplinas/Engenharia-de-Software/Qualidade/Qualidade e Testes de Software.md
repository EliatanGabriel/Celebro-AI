---
type: concept
area: faculdade
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Qualidade e Testes de Software

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Qualidade e testes de software: níveis de teste, tipos de teste, caixa preta e branca, TDD e métricas de qualidade.

## 1. O que é qualidade de software

Qualidade é o grau em que o software atende aos requisitos e às expectativas do usuário. Testar é uma das principais atividades para garantir qualidade.

**Frase-chave:** teste é um processo de verificação de que o software faz o que deveria, e de validação de que é o que o cliente quer.

## 2. Níveis de teste

```
Testes de unidade
    ↓
Testes de integração
    ↓
Testes de sistema
    ↓
Testes de aceitação
```

- **Teste de unidade** — testa a menor parte do código (função/método) isoladamente.
- **Teste de integração** — verifica a interação entre módulos.
- **Teste de sistema** — testa o sistema completo, como um todo.
- **Teste de aceitação** — validado pelo cliente; confirma se atende às necessidades.

## 3. Tipos de teste

- **Funcional** — verifica se a funcionalidade atende aos requisitos.
- **Regressão** — garante que mudanças não quebraram o que já funcionava.
- **Desempenho** — mede velocidade, uso de recursos e escalabilidade.
- **Segurança** — procura vulnerabilidades.
- **Usabilidade** — avalia a experiência do usuário.
- **Carga/Estresse** — testa o sistema sob condições extremas.

## 4. Caixa preta × Caixa branca

| Caixa preta | Caixa branca |
| --- | --- |
| Não conhece o código interno | Conhece e analisa o código |
| Foco na entrada e saída | Foco nas estruturas internas |
| Baseado em requisitos | Baseado na implementação |
| Ex.: teste funcional | Ex.: teste de cobertura de branches |

## 5. Test-driven Development (TDD)

No TDD, os testes são escritos **antes** do código.

```
RED (escrever teste que falha)
    ↓
GREEN (escrever código mínimo para passar)
    ↓
REFACTOR (melhorar o código mantendo os testes verdes)
```

**Benefícios:** código mais testado, design mais simples e menos bugs.

## 6. Métricas de qualidade

- **Cobertura de código** — % do código exercitado pelos testes.
- **Densidade de defeitos** — defeitos por mil linhas de código.
- **MTBF** (*Mean Time Between Failures*) — tempo médio entre falhas.
- **Índice de defeitos em produção** — defeitos que chegam ao usuário.

## 7. Qualidade de código

- **Legibilidade** — código claro e fácil de entender.
- **Manutenibilidade** — fácil de modificar e estender.
- **Padrões de codificação** — convenções consistentes (ex.: PEP 8).
- **Revisão de código (code review)** — análise por pares antes de integrar.
- **Análise estática** — ferramentas como ESLint, Pylint, SonarQube.

## 8. Benefícios de testar cedo

- Bugs são mais baratos de corrigir no início.
- Reduz o retrabalho.
- Aumenta a confiança da equipe.
- Documenta o comportamento esperado.

## Tópicos
- 

## Relacionadas

- [[Engenharia-de-Software]]
- [[Engenharia de Requisitos]]
- [[Faculdade]]