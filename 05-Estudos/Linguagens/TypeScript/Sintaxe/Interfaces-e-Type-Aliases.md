---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Interfaces e Type Aliases (TypeScript)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Interfaces e type aliases descrevem formas de dados; a interface suporta declaration merging e herança, enquanto o type alias cobre unions, tuplas e tipos primitivos nomeados.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `interface X { }` | Contrato estrutural | `interface User { id: number }` |
| `type Y = ...` | Alias para qualquer tipo | `type Id = string \| number` |
| `readonly` | Propriedade só leitura | `readonly criadoEm: Date` |
| `?` | Propriedade opcional | `apelido?: string` |
| `[k: string]: T` | Index signature | `{ [campo: string]: number }` |
| `interface A extends B` | Herança entre interfaces | `extends Base` |
| `A & B` | Interseção (via type) | `type Admin = User & Perms` |

## Exemplos

```ts
interface Usuario {
  readonly id: number;
  nome: string;
  apelido?: string;
  [campoExtra: string]: unknown;
}

const u: Usuario = { id: 1, nome: "Ana" };
// u.id = 2; // erro: readonly

type Id = string | number;   // union só existe em type alias
type Chaves = keyof Usuario; // type também dá nomes a utilidades
```

```ts
interface Animal {
  nome: string;
  emitirSom(): void;
}

interface Pet {
  dono: string;
}

// interface pode estender múltiplas bases
interface Cachorro extends Animal, Pet {
  raca: string;
}

// interseção com &: resultado equivalente a "tem tudo junto"
type Gato = Animal & { miadoFino: boolean };

// Declaration merging: interface se mescla, type alias dá erro de duplicado
interface Janela { titulo: string }
interface Janela { largura: number }
const j: Janela = { titulo: "app", largura: 800 };
```

## Boas práticas

- Use `interface` para objetos públicos que podem ser estendidos ou mesclados.
- Use `type` para unions, tuplas, primitivos nomeados e tipos utilitários.
- Marque com `readonly` tudo que não deve mudar após a criação.
- Prefira propriedades opcionais explícitas (`?`) a aceitar `undefined` solto.
- Evite index signatures amplas quando o formato é conhecido.
- Nomeie interfaces sem prefixo `I`: o TS idiomático não usa húngaro.

## Armadilhas comuns

- Tentar union em `interface`: não existe, use `type`.
- Declarar o mesmo `type` duas vezes: erro; interfaces duplicadas apenas se mesclam.
- Esquecer que index signature exige que todas as props casem com o tipo declarado.
- Achar que `readonly` congela o objeto: ele impede reatribuição da prop, não mutação interna.
- Usar `extends` em type alias de objeto quando o objetivo é combinar: isso é `&`.

## Relacionadas

- [[TypeScript]]
- [[Classes-e-Modificadores]]
- [[Utility-Types]]
