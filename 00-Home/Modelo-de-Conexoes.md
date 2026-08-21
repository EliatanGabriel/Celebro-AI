---
type: concept
area: todas
status: active
tags:
  - modelo
created: "2026-08-20"
updated: "2026-08-20"
---

# Modelo de Conexões

#area/home #modelo

**Resumo:** O padrão de conexões que deixa o grafo com constelações isoladas — modelo aprovado e congelado. Sem pontes entre áreas.

## Ideia central

O vault funciona como um cérebro: cada pasta-raiz é uma **constelação** que orbita sozinha. Nenhuma área se conecta a outra; o grafo mostra blocos separados em vez de uma bola única.

## Tipos de nota e como se conectam

| Tipo | `type:` | Papel | Conexões |
|------|---------|-------|----------|
| **Hub** | `hub` | Área (constelação) | Aponta para suas subáreas em `## Subáreas` |
| **MOC** | `moc` | Subárea dentro do hub | Aponta para as notas de conteúdo em `## Notas` |
| **Concept** | `concept` | Nota de conteúdo | Aponta para relacionadas em `## Relacionadas` |
| **Daily** | — | Nota do dia | Fica na área, sem links |

## Regras das conexões

1. **Uma única área por nota** — cada nota tem uma única tag `#area/<subarea>` e pertence a uma só constelação.
2. **Sem back-links para Home** — nenhuma nota de área linka `[[Home]]` ou o Guia; o Home fica isolado.
3. **Sem `## Conexões` cruzando áreas** — conceitos só linkam dentro da própria área.
4. **Notas soltas flutuam** — notas de `07-Soltos` não têm `[[links]]`, então não orbitam constelação alguma.
5. **MOCs listam, não linkam** — o MOC tem `## Notas` com os links; o hub tem `## Subáreas`.
6. **Conceitos linkam entre si** — `## Relacionadas` conecta conceitos dentro da mesma área, criando o "circuito".

## Como o grafo fica

- Cada área aparece como uma **constelação isolada** no grafo.
- `00-Home` (Home + Guia + Modelo) fica **isolada** no centro.
- Notas soltas ficam **órfãs/flutuantes**, fora de qualquer constelação.
- As cores do grafo vêm das tags `#area/<subarea>`.

## Mantendo o modelo

Ao criar notas novas, siga os templates (Hub, MOC, Concept). Nunca feche ciclos entre áreas: sem back-link para Home e sem `## Conexões` cruzando áreas.