# Celebro AI

O cérebro do seu conhecimento — um vault Obsidian pessoal, organizado em áreas, para centralizar faculdade, trabalho, projetos, estudos, vida pessoal e leituras. Cada área é uma constelação independente; nem tudo está conectado.

## Estrutura

```
Celebro AI/
├── 00-Home/          # Home e guia de uso do vault
├── 01-Faculdade/     # Disciplinas, provas, trabalhos e metas
├── 02-Trabalho/      # Anotações, reuniões, QA, CI-CD, APIs e metas
├── 03-Pessoal/       # Diário, reflexões, pensamentos, metas e rotinas
├── 04-Projetos/      # Ideias, ativos, concluídos e roadmaps
├── 05-Estudos/       # Backend, frontend, dados, cloud, linguagens e mais
├── 06-Biblioteca/    # Livros (lidos, lendo, quero ler, abandonei)
├── 07-Soltos/        # Notas flutuantes, sem links
├── 08-Humanidades/   # Filosofia, Teologia, História, Literatura e Sociologia-e-Economia
├── 09-Referencias/   # Glossário, snippets e pesquisas — a busca rápida do vault
├── Templates/        # Modelos para criar notas no padrão
├── Excalidraw/       # Diagramas
└── .obsidian/        # Configuração do Obsidian
```

## Como funciona

O vault funciona como **constelações isoladas** — cada área órbita sozinha:

1. **Hubs** (`type: hub`) — áreas: Faculdade, Trabalho, Pessoal, Projetos, Estudos, Biblioteca, Humanidades e Referencias.
2. **MOCs** (`type: moc`) — subáreas dentro de cada hub, com a lista das notas em `## Notas` e visão automática via Dataview em `## Visão automática`.
3. **Conceitos** (`type: concept`) — notas de conteúdo, com `## Conceitos-chave`, `## Exemplos`, `## Boas práticas`, `## Armadilhas comuns` e `## Relacionadas`.
4. **Livros** (`type: book`) — notas de leitura em `06-Biblioteca`, com lições, notas e motivação de leitura.
5. **Verbetes** (`type: verbete`) — definição curta de termo em `09-Referencias/Glossario`, para consulta rápida.
6. **Snippets** (`type: snippet`) — código/comando pronto em `09-Referencias/Snippets`, para copiar e colar.
7. **Pesquisas** (`type: pesquisa`) — investigação com pergunta → fontes → síntese, via template Pesquisa.

Toda nota pertence a uma única área, identificada pela tag `#area/<subarea>`. As tags também definem as cores do grafo no Obsidian.

## Mapa cerebral

O vault funciona como um cérebro: cada pasta-raiz é uma **constelação** que orbita sozinha.

- **Regiões (hubs)** — as sete áreas. Cada uma lista suas subáreas em `## Subáreas`.
- **Circuitos (MOCs)** — as subáreas dentro de cada hub, listadas no hub.
- **Neurônios (conceitos)** — as notas de conteúdo, criadas livremente; não precisam de links para existir.
- **Flutuantes** — notas de `07-Soltos` e a Home (`00-Home`) ficam sem conexões, órfãs no grafo.

Não existem pontes entre áreas: sem back-links para Home, sem seções `## Conexões` cruzando áreas. Cada área é um bloco isolado, então o grafo mostra constelações separadas em vez de uma bola única.

## Como usar

### Criar notas no padrão

1. **Ctrl+P** → *Templates: Insert template* e escolha o modelo (Hub, MOC, Concept, Book, Projeto, Reuniao, Metas, Daily, Verbete, Snippet ou Pesquisa).
2. Substitua `AREA` pelo nome da área no back-link.
3. `created` e `updated` são preenchidos automaticamente.
4. Em conceitos de estudo, use o campo `progresso` (`estudando`, `dominado`) e ligue ao sistema de revisão em `05-Estudos/Revisao`.
5. Não feche ciclos entre áreas: sem back-link para Home no final das notas e sem `## Conexões` cruzando áreas.

### Diário

**Ctrl+P** → *Open today's daily note* cria a nota do dia em `03-Pessoal/Diario/` com o template Daily.

## Tecnologias

- **Obsidian** — editor principal do vault.
- **Markdown** — formato padrão de todas as notas.
- **Git + GitHub** — versionamento e backup do vault.