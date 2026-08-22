---
type: concept
area: todas
status: active
created: "2026-08-19"
updated: "2026-08-20"
---

# Guia de Uso

#area/home

**Resumo:** Como o vault Celebro AI está organizado e como criar notas no padrão.

## Estrutura

- O vault é organizado como **constelações isoladas**: cada área orbita sozinha, sem pontes entre si.
- Cada área é um **hub** (`type: hub`): Faculdade, Trabalho, Pessoal, Projetos, Estudos, Biblioteca, Humanidades e Referencias.
- Cada hub lista suas **subáreas** em `## Subáreas`, e as subáreas são **MOCs** (`type: moc`) com `## Notas` e visão automática (Dataview) em `## Visão automática`.
- Notas de conceito (`type: concept`) têm `## Conceitos-chave`, `## Exemplos`, `## Boas práticas`, `## Armadilhas comuns` e `## Relacionadas`.
- Notas de livro (`type: book`) ficam em `06-Biblioteca`, com `## Lições principais` (lidos/lendo), `## Por que quero ler` (quero ler) ou `## Por que abandonei` (abandonei).
- `00-Home` (Home + Guia) fica isolada; notas de `07-Soltos` flutuam sem nenhum link.

## Criar notas no padrão

1. **Ctrl+P** → *Templates: Insert template* e escolha o modelo (Hub, MOC, Concept, Book, Projeto, Reuniao, Metas, Daily, Verbete, Snippet ou Pesquisa).
2. Troque `AREA` pelo nome da área (ex.: `estudos`) no back-link.
3. `created` e `updated` são preenchidos automaticamente.

## Revisão e progresso (Estudos)

- Conceitos de estudo usam o campo `progresso` (`estudando` → `dominado`).
- O sistema de revisão espaçada (1-3-7-14-30 dias) está em `05-Estudos/Revisao/Metodo-de-Revisao.md`; a fila de revisão é gerada por Dataview em `05-Estudos/Revisao/Revisao.md`.

## Referências (consulta rápida)

- `09-Referencias` é a **busca do vault**: use `Ctrl+O` e digite o termo.
- **Verbete** (`type: verbete`): definição curta de termo em `Glossario/` — não substitui conceito completo, só responde "o que é X?".
- **Snippet** (`type: snippet`): código/comando testado em `Snippets/`, com "quando usar" e gotchas.
- **Pesquisa** (`type: pesquisa`): investigação com método — pergunta → hipótese → fontes → síntese. Crie pelo template Pesquisa; o hub lista as em aberto.

## Dataview

- MOCs têm uma seção `## Visão automática` com consultas `dataview` que listam as notas da subárea pela tag.
- O hub `06-Biblioteca/Biblioteca.md` usa Dataview para agrupar livros por status.

## Diário

- **Ctrl+P** → *Open today's daily note* cria a nota do dia em `03-Pessoal/Diario/` com o template Daily.

## Regras do grafo

- Não conecte áreas entre si: sem back-links para `[[Home]]`, sem seção `## Conexões` cruzando áreas. Cada área é uma constelação independente.
- Cores por tag `#<area>/<subarea>` (ex.: `#estudos/backend`, `#pessoal/habitos`). O Home fica isolado com o Guia.
- Toda nota pertence a uma única área (uma única `#area/`).
- Notas soltas vão em `07-Soltos` sem `[[links]]` para não orbitar nenhuma constelação.