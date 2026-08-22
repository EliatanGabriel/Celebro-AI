---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Uniões e Narrowing (TypeScript)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Union types permitem valores de múltiplos tipos, e o narrowing usa verificações como typeof, in, instanceof e campos discriminadores para restringir o tipo em cada ramo do código.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `A \| B` | Valor pode ser A ou B | `let id: string \| number` |
| `'a' \| 'b'` | Literal types | `type Tam = 'pequeno' \| 'grande'` |
| `typeof x === "..."` | Narrow por primitivo | `if (typeof x === "string")` |
| `"campo" in obj` | Narrow por propriedade | `if ("voar" in bicho)` |
| `x instanceof Y` | Narrow por classe | `if (e instanceof Error)` |
| `kind === "..."` | Discriminated union | `if (f.kind === "circle")` |
| `never` | Tipo impossível/vazio | `function falha(): never` |

## Exemplos

```ts
type Tamanho = "pequeno" | "grande";
let caixa: Tamanho = "pequeno";

function formatar(valor: string | number): string {
  if (typeof valor === "string") {
    return valor.toUpperCase(); // aqui é string
  }
  return valor.toFixed(2); // aqui é number
}
```

```ts
// Discriminated union: campo kind comum a todos os ramos
type Forma =
  | { kind: "circulo"; raio: number }
  | { kind: "retangulo"; base: number; altura: number };

function area(f: Forma): number {
  switch (f.kind) {
    case "circulo":
      return Math.PI * f.raio ** 2;
    case "retangulo":
      return f.base * f.altura;
    default: {
      const _exaustivo: never = f; // erro se faltar um caso
      return _exaustivo;
    }
  }
}

class Gato { miar() {} }
class Cachorro { latir() {} }

function som(bicho: Gato | Cachorro): string {
  if (bicho instanceof Gato) return bicho.miar();
  return bicho.latir();
}

console.log(area({ kind: "circulo", raio: 2 }));
```

## Boas práticas

- Modele estados alternativos com discriminated unions em vez de flags soltas.
- Use o truque `const _: never = valor` no default para garantir exaustividade.
- Prefira literal types a strings livres quando o domínio é fechado.
- Extraia unions complexas para `type` nomeado e reutilize.
- Use `in` para distinguir objetos sem campo discriminador.

## Armadilhas comuns

- Usar o valor da union antes de estreitar: o TS bloqueia métodos que não existem nos dois lados.
- Confundir `typeof` do TS (runtime) com o operador de tipo em posições erradas.
- Esquecer um ramo na discriminated union e cair no default silenciosamente.
- Achar que `instanceof` funciona com interfaces: só serve para classes.
- Tratar `never` como `void`: never significa "nunca retorna/é impossível".

## Relacionadas

- [[TypeScript]]
- [[Tipos-Basicos]]
- [[Enums-e-Assercoes]]
