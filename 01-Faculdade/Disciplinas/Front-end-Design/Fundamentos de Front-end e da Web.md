---
type: concept
area: faculdade
status: active
created: "2026-08-19"
updated: "2026-08-19"
---

# Fundamentos de Front-end e da Web

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Fundamentos de front-end e da web: papel do front-end, as camadas da interface (HTML, CSS e JavaScript), DOM, CSS3, Flexbox, Grid e design responsivo.

## 1. O que vamos aprender

Nesta aula:

- Como uma aplicação front-end organiza a interface que a pessoa utiliza.
- Como o HTML5 dá significado ao conteúdo e melhora a navegação.
- Como o CSS3 ajuda a criar páginas bonitas, responsivas e acessíveis.

## 2. O papel do Front-end

Quando abrimos um site, a primeira interação acontece por meio da interface. É nela que aparecem:

- Textos
- Botões
- Menus
- Imagens
- Respostas às ações do usuário

O front-end cuida da parte visual e interativa que roda no navegador.

## 3. As 3 camadas da interface

Uma interface web pode ser entendida por três tecnologias principais:

- **HTML** — organiza o conteúdo da página.
- **CSS** — define aparência, espaçamento, cores e layout.
- **JavaScript** — adiciona comportamento, respostas e interação.

```
HTML
↓
Estrutura e conteúdo
```

```
CSS
↓
Aparência e layout
```

```
JavaScript
↓
Comportamento e interação
```

## 4. Como a página ganha estrutura

Antes de adicionar cores, estilos ou interações, a página precisa possuir uma estrutura clara. Essa estrutura define onde ficam elementos como:

- Título
- Conteúdo principal
- Navegação
- Imagens
- Rodapé

```
Página
├── Título
├── Navegação
├── Conteúdo principal
├── Imagens
└── Rodapé
```

## 5. HTML5 e significado

O HTML5 trouxe elementos que indicam qual é a função de cada parte da página. Algumas tags semânticas importantes:

- `<header>`
- `<nav>`
- `<main>`
- `<section>`
- `<article>`
- `<aside>`
- `<footer>`

Esses elementos ajudam o navegador a compreender a estrutura da página.

**Benefícios:** o uso de HTML semântico torna o código mais organizado, mais acessível e mais fácil de manter.

## 6. Por que a semântica importa?

Uma dúvida comum: por que não usar apenas `<div>` para tudo?

Uma página construída somente com `<div>` pode aparecer normalmente na tela, mas comunica menos informações para:

- Navegadores
- Leitores de tela
- Mecanismos de busca

Quando cada parte possui uma função clara, a experiência melhora para mais pessoas.

**Ideia principal:** HTML semântico = estrutura com significado.

## 7. Acessibilidade desde o começo

A acessibilidade deve fazer parte do projeto desde a construção da estrutura da página. Alguns recursos importantes:

- **Texto alternativo em imagens** — ajuda pessoas que utilizam leitores de tela a compreender o conteúdo das imagens.
- **Contraste adequado** — facilita a leitura do conteúdo.
- **Navegação por teclado** — permite utilizar a interface sem depender exclusivamente do mouse.

O objetivo é criar uma interface mais inclusiva, mais clara e mais confiável.

## 8. ARIA com cuidado

Os atributos ARIA podem ajudar leitores de tela a interpretar partes interativas da interface. Porém:

- ARIA não deve substituir elementos HTML semânticos quando eles já resolvem o problema.

A prioridade deve ser:

```
HTML semântico adequado
        ↓
ARIA quando necessário
```

Ou seja: primeiro escolha corretamente a tag HTML; depois utilize ARIA para complementar quando necessário.

## 9. Front-end × Back-end

- **Front-end** — é executado no navegador e trabalha principalmente com interface, apresentação e interação do usuário.
- **Back-end** — é executado no servidor e cuida de regras de negócio, dados, segurança e processamento.

Os dois lados trabalham juntos para que uma ação realizada na interface gere uma resposta útil.

```
USUÁRIO
   ↓
FRONT-END
   ↓
BACK-END
   ↓
DADOS / PROCESSAMENTO
   ↓
RESPOSTA
   ↓
FRONT-END
   ↓
USUÁRIO
```

## 10. Como funciona uma requisição Web

O fluxo apresentado envolve: cliente, navegador, internet, servidor, aplicação e banco de dados. Uma representação simplificada:

```
CLIENTE
   ↓
NAVEGADOR
   ↓
REQUISIÇÃO HTTP
   ↓
INTERNET
   ↓
SERVIDOR
   ↓
APLICAÇÃO
   ↓
BANCO DE DADOS
   ↓
SERVIDOR
   ↓
HTML / RESPOSTA
   ↓
NAVEGADOR
   ↓
EXIBIÇÃO
```

A comunicação entre cliente e servidor acontece por meio de requisições HTTP.

## 11. APIs conectam as partes

Quando o usuário clica em um botão para buscar dados, a interface pode enviar uma solicitação para uma API.

**Fluxo:**

```
USUÁRIO
   ↓
CLICA EM UM BOTÃO
   ↓
FRONT-END
   ↓
SOLICITAÇÃO PARA A API
   ↓
SERVIDOR
   ↓
API CONSULTA / PROCESSA
   ↓
RESPOSTA
   ↓
FRONT-END
   ↓
DADOS EXIBIDOS
```

Uma vantagem desse modelo é permitir a criação de páginas mais dinâmicas sem precisar recarregar a página inteira.

## 12. Ferramentas do dia a dia

- **VS Code** — ajuda na escrita e na organização do código.
- **Git** — é utilizado para registrar versões, controlar alterações e facilitar o trabalho com diferentes versões do projeto.
- **Navegadores** — permitem testar a interface, inspecionar elementos, identificar problemas e ajustar a interface durante o desenvolvimento.

## 13. DOM — Document Object Model

O DOM representa a página como uma árvore de elementos. Cada tag HTML se transforma em um nó dessa árvore. Esses elementos podem ser encontrados, lidos e alterados pelo JavaScript. Isso permite que a interface responda às ações do usuário sem precisar carregar a página novamente.

**Representação:**

```
DOCUMENT
│
├── HTML
│   │
│   ├── HEAD
│   │
│   └── BODY
│       │
│       ├── HEADER
│       ├── MAIN
│       │   ├── SECTION
│       │   └── ARTICLE
│       └── FOOTER
```

## 14. XPath no DOM

O XPath ajuda a localizar elementos dentro da estrutura da página. Ele pode ser útil quando a seleção precisa considerar:

- Posição
- Atributos
- Relações entre elementos

Em testes automatizados, o XPath pode ser utilizado para encontrar partes específicas de interfaces mais complexas.

## 15. CSS3 e aparência da página

O CSS3 define como os elementos aparecem na tela. Ele controla:

- Cores
- Fontes
- Espaçamentos
- Alinhamentos
- Bordas
- Comportamento visual

Sem CSS, a página pode continuar funcionando, mas perde identidade visual, organização visual e qualidade de leitura.

## 16. Seletores no CSS

Os seletores indicam quais elementos receberão uma determinada regra de estilo. Eles podem identificar:

- Uma tag
- Uma classe
- Um identificador
- Um atributo
- Um estado do elemento

**Exemplos:**

```css
p {
    /* seletor de tag */
}

.texto {
    /* seletor de classe */
}

#intro {
    /* seletor de ID */
}
```

Quanto melhor for o seletor, mais previsível será a estilização.

## 17. Herança no CSS

A herança permite que determinadas propriedades passem de um elemento pai para seus elementos internos.

**Exemplo conceitual:**

```
Elemento Pai
    │
    ├── Filho 1
    ├── Filho 2
    └── Filho 3
```

Algumas propriedades definidas no pai podem ser herdadas pelos filhos.

## 18. Especificidade no CSS

A especificidade determina qual regra deve vencer quando existem várias regras tentando estilizar o mesmo elemento. Quanto mais específico o seletor, maior sua prioridade.

A ordem apresentada é:

1. Seletor de tag
2. Seletor de classe
3. Seletor de ID
4. Estilo inline

**Exemplos:**

```css
p {
    color: blue;
}

.texto {
    color: green;
}

#intro {
    color: red;
}
```

Nesse caso, o seletor `#intro` é mais específico que `.texto` e `p`.

## 19. Conflito entre duas classes

Quando duas regras de classe entram em conflito, a regra que aparece por último no arquivo CSS vence.

**Exemplo:**

```css
.texto {
    color: blue;
}

.texto {
    color: red;
}
```

O resultado será `color: red;`, porque essa regra aparece depois.

## 20. Evite !important

O material recomenda evitar o uso de `!important` sempre que possível, pois ele pode:

- Quebrar a cascata
- Criar conflitos
- Dificultar a manutenção do CSS

Prefira organizar corretamente os seletores e a especificidade.

## 21. Flexbox

O Flexbox organiza elementos em uma direção principal. É especialmente útil para:

- Menus
- Barras
- Cards em linha
- Centralização de conteúdo

Duas propriedades importantes:

- `justify-content`
- `align-items`

Elas facilitam o alinhamento dos elementos de maneira flexível.

**Ideia:**

```
Flex container
─────────────────────────
│  Item  │  Item  │ Item │
─────────────────────────
```

## 22. Grid Layout

O CSS Grid Layout organiza elementos em linhas e colunas. É especialmente útil quando a página possui áreas bem definidas.

**Exemplos:** galerias, painéis e layouts com várias seções.

```
┌─────────┬─────────┐
│         │         │
│  Item   │  Item   │
│         │         │
├─────────┼─────────┤
│         │         │
│  Item   │  Item   │
│         │         │
└─────────┴─────────┘
```

O Grid permite controlar melhor o desenho da página sem depender excessivamente de ajustes manuais.

## 23. Flexbox × Grid

| Flexbox | Grid |
| --- | --- |
| Trabalha principalmente em uma direção | Trabalha com linhas e colunas |
| Ótimo para alinhamento | Ótimo para estruturas |
| Menus | Galerias |
| Barras | Painéis |
| Cards em linha | Layouts com várias áreas |
| Centralização | Estruturas bidimensionais |

**Regra prática:**

- **Flexbox** → alinhamento em uma direção
- **Grid** → estrutura em linhas e colunas

## 24. Design Responsivo

O design responsivo adapta a interface para diferentes tamanhos de tela. A página deve funcionar adequadamente em:

- Celular
- Tablet
- Computador

### Media Queries

As Media Queries permitem aplicar estilos de acordo com características do dispositivo. Podem considerar, por exemplo: largura, orientação e outras características do dispositivo.

**Exemplo:**

```css
@media (max-width: 768px) {
    /* estilos para telas menores */
}
```

### Unidades e imagens flexíveis

O design responsivo também utiliza unidades flexíveis e imagens ajustáveis. O objetivo é tornar a página mais confortável em diferentes dispositivos.

## Tópicos
- 

## Relacionadas

- [[Front-end-Design]]
- [[Faculdade]]