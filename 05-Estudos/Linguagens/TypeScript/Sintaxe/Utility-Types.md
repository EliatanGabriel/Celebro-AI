---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Utility Types (TypeScript)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Utility types transformam tipos existentes em variações úteis (parciais, somente leitura, recortadas), evitando duplicação de declarações no código.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `Partial<T>` | Todas as props opcionais | `Patch: Partial<Usuario>` |
| `Required<T>` | Todas as props obrigatórias | `Completo: Required<Usuario>` |
| `Readonly<T>` | Todas as props readonly | `Congelado: Readonly<Config>` |
| `Pick<T, K>` | Seleciona propriedades | `Pick<Usuario, "id" \| "nome">` |
| `Omit<T, K>` | Remove propriedades | `Omit<Usuario, "senha">` |
| `Record<K, V>` | Mapa de chaves para valores | `Record<string, number>` |
| `ReturnType<F>` | Tipo de retorno da função | `ReturnType<typeof carregar>` |
| `Awaited<T>` | Desembrulha Promise | `Awaited<Promise<string>>` |

## Exemplos

```ts
interface Usuario {
  id: number;
  nome: string;
  email?: string;
}

// PATCH de API: só o que veio precisa ser atualizado
function atualizar(id: number, mudancas: Partial<Usuario>): void {
  console.log(id, mudancas);
}
atualizar(1, { nome: "Novo nome" });

type Publico = Omit<Usuario, "email">;
type Resumo = Pick<Usuario, "id">;

const contagem: Record<"a" | "b", number> = { a: 1, b: 2 };
```

```ts
declare function carregar(): Promise<{ itens: string[]; total: number }>;

// ReturnType pega o tipo que a função devolve (a Promise inteira)
type Resposta = ReturnType<typeof carregar>;

// Awaited desembrulha a Promise e revela os dados
type Dados = Awaited<ReturnType<typeof carregar>>;

async function usar(): Promise<void> {
  const r: Dados = await carregar();
  console.log(r.total);
}

const cfg: Readonly<{ host: string }> = { host: "localhost" };
// cfg.host = "outro"; // erro: readonly
```

## Boas práticas

- Use `Partial` em funções de atualização (PATCH) e formulários.
- Prefira `Omit` a reescrever interfaces quando só esconde campos.
- Combine utilitários (`Readonly<Pick<T, K>>`) em vez de criar tipos paralelos.
- Use `Record` para dicionários tipados em vez de `{ [k: string]: any }`.
- Derive tipos com `typeof fn` + `Awaited` para não duplicar contratos de API.
- Aplique `Required` antes de validar dados obrigatórios.

## Armadilhas comuns

- Esquecer que `Partial` aceita objeto vazio `{}` sem erro.
- Usar `Pick`/`Omit` com chave inexistente: erro silencioso de digitação só no build.
- Achar que `Readonly` congela em runtime: é só checagem estática.
- Confundir `ReturnType<F>` com tipo da função: ele extrai apenas o retorno.
- Aplicar `Awaited` num valor que já foi resolvido e esperar mágica.

## Relacionadas

- [[TypeScript]]
- [[Generics]]
- [[Interfaces-e-Type-Aliases]]
