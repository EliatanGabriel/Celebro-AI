---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Listas e Tabelas

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Listas organizam itens em sequência ou associação, e tabelas exibem dados tabulares com cabeçalhos e mesclagem de células.

## Referência rápida

| Tag/Sintaxe | O que faz | Exemplo |
|---|---|---|
| `<ul>` | Lista não ordenada (marcadores) | `<ul><li>Item</li></ul>` |
| `<ol>` | Lista ordenada (numerada) | `<ol><li>Passo</li></ol>` |
| `<ol type start>` | Tipo de marcador e número inicial | `<ol type="a" start="3">` |
| `<li>` | Item da lista | `<li>Café</li>` |
| Listas aninhadas | `<ul>` dentro de `<li>` (sublista) | ver exemplo abaixo |
| `<dl>` | Lista de descrição (termo + definição) | `<dl>...</dl>` |
| `<dt>` / `<dd>` | Termo / descrição do termo | `<dt>API</dt><dd>Interface...</dd>` |
| `<table>` | Tabela de dados | `<table>...</table>` |
| `<thead>` | Cabeçalho da tabela | `<thead><tr>...` |
| `<tbody>` | Corpo com as linhas de dados | `<tbody><tr>...` |
| `<tfoot>` | Rodapé (totais) | `<tfoot><tr>...` |
| `<th scope>` | Célula de cabeçalho com escopo | `<th scope="col">Nome</th>` |
| `colspan` / `rowspan` | Mescla colunas / linhas | `<td colspan="2">` |
| `<caption>` | Legenda/título da tabela | `<caption>Vendas 2026</caption>` |

## Exemplos

```html
<ol>
  <li>Instalar o Node.js
    <ul>
      <li>Windows: instalador .msi</li>
      <li>Linux: via nvm</li>
    </ul>
  </li>
  <li>Criar o projeto</li>
</ol>

<table>
  <caption>Vendas por trimestre</caption>
  <thead>
    <tr><th scope="col">Produto</th><th scope="col" colspan="2">1º Semestre</th></tr>
  </thead>
  <tbody>
    <tr><td>Notebook</td><td>120</td><td rowspan="2">150</td></tr>
    <tr><td>Mouse</td><td>80</td></tr>
  </tbody>
</table>
```

## Boas práticas

- Use `<table>` só para dados tabulares — nunca para montar layout.
- `scope="col"` ou `scope="row"` em todo `<th>` ajuda leitores de tela.
- Sempre inclua `<caption>` descrevendo o propósito da tabela.
- Use `<dl>` para glossários, FAQ e pares termo/descrição.
- Em listas aninhadas, a sublista fica **dentro** do `<li>` pai.

## Armadilhas comuns

- Colocar texto solto direto em `<table>` fora de `<td>`/`<th>`.
- Esquecer de fechar `<li>` antes de abrir a sublista.
- Usar `colspan` sem conferir se o total de células bate em cada linha.
- Trocar `<ul>` por `<ol>` quando a ordem não importa (ou vice-versa).
- Estilizar tabela sem considerar responsividade — tabelas largas estouram no celular.

## Relacionadas

- [[Estudos-HTML]]
- [[Formularios]]
