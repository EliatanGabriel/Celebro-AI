---
type: concept
area: todas
status: active
created: "2026-08-19"
updated: "2026-08-19"
---

# Guia de Uso

#area/home

**Resumo:** Como o vault Celebro AI está organizado e como criar notas no padrão.

## Estrutura

- [[Home]] é o centro e conecta as áreas principais. Cada área orbita ao redor (como constelações); dentro de Estudos há grupos temáticos orbitando.
- Cada área é um **hub** (`type: hub`): Faculdade, Trabalho, Pessoal, Projetos, Estudos.
- Cada hub lista suas **subáreas** em `## Subáreas`, e as subáreas são **MOCs** (`type: moc`) com `## Notas`.
- Notas de conceito (`type: concept`) têm `## Tópicos` e `## Relacionadas`.

## Criar notas no padrão

1. **Ctrl+P** → *Templates: Insert template* e escolha o modelo (Hub, MOC, Concept ou Daily).
2. Troque `AREA` pelo nome da área (ex.: `estudos`) no back-link.
3. `created` e `updated` são preenchidos automaticamente.
4. Termine a nota com o back-link para a área ou subárea pai (ex.: `Backend`).

## Diário

- **Ctrl+P** → *Open today's daily note* cria a nota do dia em `03-Pessoal/Diario/` com o template Daily.

## Regras do grafo

- Cores por tag `#<area>/<subarea>` (ex.: `#estudos/backend`, `#pessoal/habitos`). O Home fica isolado com o Guia.
- Toda nota pertence a uma única área (uma única `#area/`).

[[Home]]