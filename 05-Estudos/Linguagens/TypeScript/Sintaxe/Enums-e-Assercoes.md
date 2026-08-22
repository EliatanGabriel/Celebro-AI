---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Enums e Asserções (TypeScript)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Enums nomeiam conjuntos fechados de valores (numéricos ou string), enquanto asserções (`as`, `!`, `as const`) informam ao compilador fatos de tipo que ele não consegue deduzir sozinho.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `enum E { }` | Enum numérico autoincremento | `enum Dir { Up, Down }` |
| `enum E { A = "a" }` | Enum string | `Status.Ativo` |
| `const enum` | Inlined, sem objeto em runtime | `const enum Tam { P }` |
| `as const` | Congela como literal readonly | `[1, 2] as const` |
| `x as Tipo` | Type assertion | `resp as Usuario` |
| `<Tipo>x` | Assertion antiga (evite) | `<string>x` |
| `x!` | Non-null assertion | `el!.focus()` |
| `x is T` | Type guard customizado | `function isGato(x): x is Gato` |

## Exemplos

```ts
// Enum string: mais legível em logs do que números
enum Status {
  Ativo = "ATIVO",
  Inativo = "INATIVO",
}

function mostrar(s: Status): void {
  console.log(s); // "ATIVO", não 0
}
mostrar(Status.Ativo);

// as const: array literal vira tupla readonly de literais
const TAMANHOS = ["pequeno", "grande"] as const;
type Tamanho = (typeof TAMANHOS)[number]; // "pequeno" | "grande"
```

```ts
interface Animal { nome: string }
interface Gato extends Animal { miar(): void }

// Type guard customizado: o TS passa a confiar no resultado
function isGato(x: Animal): x is Gato {
  return "miar" in x;
}

function brincar(a: Animal): void {
  if (isGato(a)) {
    a.miar(); // estreitado para Gato
  }
}

// Non-null assertion: garanta que não é null/undefined
const el = document.querySelector<HTMLInputElement>("#busca");
el!.focus();
```

## Boas práticas

- Prefira enums com valores string para rastrear em logs e APIs.
- Considere union de literais + `as const` antes de criar um enum novo.
- Use type guards customizados para centralizar checagens complexas.
- Reserve `!` para casos óbvios e documentados; valide o resto.
- Use `as const` para constantes compartilhadas e derivar tipos delas.

## Armadilhas comuns

- Usar `as` como atalho para calar erro: assertion errada vira bug silencioso.
- Esquecer que `const enum` quebra com `isolatedModules` e transpilação por arquivo.
- Aplicar `!` num elemento que realmente pode ser nulo: crash em runtime.
- Confundir `as const` com `Object.freeze`: só afeta tipagem, não execução.
- Numerar enum manualmente e duplicar valores sem perceber.

## Relacionadas

- [[TypeScript]]
- [[Unioes-e-Narrowing]]
- [[Tipos-Basicos]]
