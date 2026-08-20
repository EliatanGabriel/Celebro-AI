# Celebro AI

O cérebro do seu conhecimento — um vault Obsidian pessoal, organizado em áreas, para centralizar faculdade, trabalho, projetos, estudos, vida pessoal e leituras em um único lugar conectado.

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
├── Templates/        # Modelos para criar notas no padrão
├── Excalidraw/       # Diagramas
└── .obsidian/        # Configuração do Obsidian
```

## Como funciona

O vault segue uma organização em camadas:

1. **Home** — centro do vault, conecta as seis áreas principais.
2. **Hubs** (`type: hub`) — áreas: Faculdade, Trabalho, Pessoal, Projetos, Estudos e Biblioteca.
3. **MOCs** (`type: moc`) — subáreas dentro de cada hub, com a lista das notas em `## Notas`.
4. **Conceitos** (`type: concept`) — notas de conteúdo, com `## Tópicos` e `## Relacionadas`.

Toda nota pertence a uma única área, identificada pela tag `#area/<subarea>`. As tags também definem as cores do grafo no Obsidian.

## Como usar

### Criar notas no padrão

1. **Ctrl+P** → *Templates: Insert template* e escolha o modelo (Hub, MOC, Concept ou Daily).
2. Substitua `AREA` pelo nome da área no back-link.
3. `created` e `updated` são preenchidos automaticamente.
4. Termine a nota com o back-link para a área ou subárea pai.

### Diário

**Ctrl+P** → *Open today's daily note* cria a nota do dia em `03-Pessoal/Diario/` com o template Daily.

## Tecnologias

- **Obsidian** — editor principal do vault.
- **Markdown** — formato padrão de todas as notas.
- **Git + GitHub** — versionamento e backup do vault.