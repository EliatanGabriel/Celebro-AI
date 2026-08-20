---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Design

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Disciplina de concepção visual e de experiência (UI/UX) de interfaces e produtos digitais; abrange pesquisa, prototipagem, design systems e validação de usabilidade.

## Conceitos-chave
- **UI (User Interface)**: elementos visuais e interativos — layout, cores, tipografia, ícones, componentes.
- **UX (User Experience)**: jornada do usuário, arquitetura da informação, fluxos e facilidade de uso como um todo.
- **Design system**: conjunto de princípios, tokens (cores, espaçamento, tipografia), componentes e padrões reutilizáveis que garantem consistência.
- **Prototipagem**: de wireframes (baixa fidelidade) a protótipos interativos (alta fidelidade) para validar fluxos antes do código.
- **Tokens de design**: variáveis que centralizam decisões visuais e permitem temas (dark mode, acessibilidade) sem retrabalho.
- **Heurísticas de usabilidade**: critérios (ex.: de Nielsen) para avaliar interfaces — visibilidade do estado, feedback, prevenção de erros.

## Exemplos
Tokens de design em CSS (independência de framework):

```css
:root {
  --cor-primaria: #2563eb;
  --espaco-1: 0.25rem;
  --raio-card: 8px;
  --fonte-corpo: 16px;
}
```

Documentação de um padrão de componente em markdown:

```md
## Button
- Primary: fundo `--cor-primaria`, texto branco, raio `--raio-card`
- Estados: default, hover, disabled
- Uso: ações principais; nunca mais de um por viewport
```

## Boas práticas
- Projete pensando em estados: loading, vazio, erro, sucesso — não apenas o happy path.
- Valide com usuários reais desde wireframes; protótipos não substituem testes de usabilidade.
- Garanta contraste AA/AAA e navegação por teclado para acessibilidade.
- Separe tokens de componentes: mudanças de tema nunca devem exigir alterar componentes.
- Documente decisões de design para facilitar o trabalho com o time de desenvolvimento.

## Armadilhas comuns
- Confundir UI com UX: estética bonita não garante usabilidade.
- Criar design systems antes de entender o produto gera padrões artificiais e pouco adotados.
- Ignorar responsividade e estados de erro até a implementação, causando retrabalho no código.
- Redimensionar imagens sem contexto: cores e contrastes são alterados em ambientes diferentes.
- Tratar design como "acabamento": mudanças tardias têm custo muito maior.

## Relacionadas
- [[Figma]]
- [[Mobile]]