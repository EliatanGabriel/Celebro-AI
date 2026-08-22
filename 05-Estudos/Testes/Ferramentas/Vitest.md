---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# Vitest

#area/estudos #estudos/testes #ferramenta

**Resumo:** Framework de testes moderno compatível com a API do Jest, com integração nativa ao Vite, execução rápida e UI própria.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `describe` / `it` | Estrutura da suíte (API igual ao Jest) | `describe("soma", ...)` |
| `expect().toBe` | Igualdade primitiva | `expect(x).toBe(1)` |
| `vi.fn()` | Cria função mock | `const f = vi.fn()` |
| `vi.mock()` | Mocka módulo inteiro | `vi.mock("./api")` |
| `vi.spyOn` | Espiona método existente | `vi.spyOn(obj, "metodo")` |
| `vi.useFakeTimers` | Congela relógio/timers | Testar debounce sem sleep |
| `workspace`/projects | Múltiplas configs por projeto | Monorepo com apps diferentes |
| `@vitest/coverage-v8` | Cobertura via V8 | `vitest run --coverage` |

## Exemplos

```js
import { describe, it, expect, vi, beforeEach } from "vitest";
import { somar } from "./matematica";

vi.mock("./api", () => ({ buscar: vi.fn().mockResolvedValue([]) }));

describe("matematica", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("soma dois numeros", () => {
    expect(somar(2, 3)).toBe(5);
  });

  it("chama a api uma vez", async () => {
    await carregarDados();
    expect(buscar).toHaveBeenCalledTimes(1);
  });
});
```

```ts
// vitest.config.ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    environment: "jsdom",
    coverage: { provider: "v8", reporter: ["text", "html"] },
  },
});
```

## Comandos úteis

```bash
npx vitest            # watch mode padrao em dev
npx vitest run        # execucao unica para CI
npx vitest --ui       # interface grafica no navegador
npx vitest --coverage # cobertura com v8
```

## Boas práticas

- Migração do Jest costuma ser quase direta: troque imports para `vitest`.
- Use projects/workspace em monorepos para configs por pacote.
- Aproveite o transform do Vite: sem build extra antes do teste.
- Combine com [[Testing-Library]] para componentes React/Vue.

## Armadilhas comuns

- Esquecer que `vi.mock` é hoisted: defina factories com cuidado.
- Misturar fake timers reais sem restaurar (`useRealTimers`).
- Configurar ambiente errado (`node` vs `jsdom`) e falhar em DOM.
- Assumir paridade total com Jest: alguns plugins não são compatíveis.

## Relacionadas

- [[Testes]]
- [[Jest]]
- [[Testing-Library]]
- [[Mocks-Stubs-e-Fakes]]
- [[Cobertura-de-Codigo]]
