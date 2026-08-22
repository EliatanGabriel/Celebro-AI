---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# Testing Library

#area/estudos #estudos/testes #ferramenta

**Resumo:** Família de ferramentas (React Testing Library, DOM Testing Library) para testar componentes pelo comportamento do usuário — o que ele vê e faz — em vez de detalhes internos de implementação.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `render()` | Monta o componente no DOM virtual | `render(<Contador />)` |
| `screen.getByRole` | Query prioritária (acessibilidade) | `screen.getByRole("button")` |
| `getByLabelText` | Campo via `<label>` associado | `screen.getByLabelText("Email")` |
| `getByText` | Elemento por texto visível | `screen.getByText("Enviar")` |
| `queryBy*` | Retorna `null` se não achar (negativas) | `expect(screen.queryByRole("alert")).toBeNull()` |
| `findBy*` | Async: espera o elemento aparecer | `await screen.findByText("Carregado")` |
| `userEvent.click` | Simula interação real do usuário | `await userEvent.click(botao)` |
| `waitFor` | Espera condição assíncrona | `await waitFor(() => ...)` |
| `toBeInTheDocument` | Matcher do jest-dom | `expect(msg).toBeInTheDocument()` |

## Prioridade de queries (acessibilidade primeiro)

1. `getByRole` + `name` — todos conseguem localizar (leitores de tela também)
2. `getByLabelText` / `getByPlaceholderText` — formulários
3. `getByText` / `getByAltText` / `getByTitle`
4. `getByTestId` — último recurso, invisível para o usuário

## Exemplos

```jsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import Login from "./Login";

describe("Login", () => {
  it("mostra erro com credenciais invalidas", async () => {
    render(<Login />);

    await userEvent.type(screen.getByLabelText("Email"), "ana@teste.com");
    await userEvent.type(screen.getByLabelText("Senha"), "errada");
    await userEvent.click(screen.getByRole("button", { name: "Entrar" }));

    expect(await screen.findByRole("alert")).toHaveTextContent(/inválid/i);
  });
});
```

## Boas práticas

- Consulte elementos como o usuário os encontra: papel, rótulo, texto.
- Use `getBy*` para síncrono, `findBy*` para assíncrono e `queryBy*` para afirmar ausência.
- Instale `@testing-library/jest-dom` para matchers legíveis.
- Teste estados resultantes de interação, não props internas ou estado privado.

## Armadilhas comuns

- `getByText` com substring sem regex pode falhar por quebra de linha no HTML.
- Usar `data-testid` para tudo: esconde problemas reais de acessibilidade.
- Esquecer `await`: queries síncronas falham antes da Promise resolver.
- Atuar sobre `container.querySelector` volta a acoplar à implementação.

## Relacionadas

- [[Testes]]
- [[Jest]]
- [[Vitest]]
- [[Boas-Praticas-de-Testes]]
