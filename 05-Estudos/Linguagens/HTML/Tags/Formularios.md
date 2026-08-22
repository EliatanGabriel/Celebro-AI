---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Formulários

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Formulários coletam dados do usuário através de inputs tipados, validação nativa e controles como select, textarea e botões.

## Referência rápida

| Tag/Sintaxe | O que faz | Exemplo |
|---|---|---|
| `<form action method>` | Onde envia e o verbo HTTP | `<form action="/login" method="post">` |
| `<label for>` | Rótulo associado ao campo (pelo `id`) | `<label for="email">E-mail</label>` |
| `<input type="text">` | Campo de texto simples | ver exemplo abaixo |
| `type="email"` | Valida formato de e-mail | `<input type="email">` |
| `type="password"` | Oculta os caracteres digitados | `<input type="password">` |
| `type="number"` | Aceita só números (com min/max) | `<input type="number" min="1" max="10">` |
| `type="date"` | Seletor de data nativo | `<input type="date">` |
| `type="checkbox"` | Múltipla escolha independente | `<input type="checkbox">` |
| `type="radio"` | Escolha única no mesmo `name` | `<input type="radio" name="plano">` |
| `type="file"` | Upload de arquivos | `<input type="file" accept=".pdf">` |
| `type="hidden"` | Valor invisível enviado junto | `<input type="hidden" name="id">` |
| `required / pattern` | Validadores nativos | `pattern="[0-9]{5}-?[0-9]{3}"` |
| `placeholder / value` | Dica visual / valor inicial | `placeholder="Seu nome"` |
| `<textarea>` | Texto multilinha | `<textarea rows="4"></textarea>` |
| `<select>/<option>` | Lista suspensa | `<select><option>...</option></select>` |
| `<datalist>` | Sugestões para um input de texto | `list="cidades"` |
| `<button type="submit">` | Envia o formulário | `<button type="submit">Enviar</button>` |
| `<fieldset>/<legend>` | Agrupa campos com título | `<fieldset><legend>Endereço</legend>` |

## Exemplos

```html
<form action="/cadastro" method="post">
  <fieldset>
    <legend>Dados pessoais</legend>

    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome" required placeholder="Maria Silva">

    <label for="email">E-mail:</label>
    <input type="email" id="email" name="email" required>

    <input type="radio" id="pf" name="tipo" value="pf" checked>
    <label for="pf">Pessoa física</label>

    <button type="submit">Cadastrar</button>
    <button type="reset">Limpar</button>
  </fieldset>
</form>
```

## Boas práticas

- Todo input tem um `<label>` com `for` apontando para seu `id`.
- Radio buttons do mesmo grupo compartilham o mesmo `name`.
- Use validação nativa (`required`, `min`, `max`, `pattern`) antes da validação em JS/servidor.
- `method="get"` para buscas/filtros; `post` para dados que alteram o servidor.
- Botão fora de formulário precisa de `form="id-do-form"` ou JS.

## Armadilhas comuns

- Usar `<div>` clicável em vez de `<button type="button">` — perde teclado e leitor de tela.
- Esquecer `name` nos campos: sem ele, o valor não é enviado ao servidor.
- Radios sem `name` igual ficam independentes (permite marcar vários).
- Placeholder usado como label — some quando o usuário digita.
- Confundir `value` inicial com `placeholder` (o primeiro é enviado se não mexerem).

## Relacionadas

- [[Estudos-HTML]]
- [[Listas-e-Tabelas]]
