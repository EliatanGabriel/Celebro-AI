---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Tipos Básicos (TypeScript)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Anotações de tipo no TypeScript descrevem o formato de variáveis, arrays e tuplas, com inferência automática quando a anotação é omitida.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `: string` | Texto | `let nome: string = "Ana"` |
| `: number` | Número (int ou float) | `let idade: number = 30` |
| `: boolean` | Verdadeiro/falso | `let ativo: boolean = true` |
| `string[]` | Array de strings | `let tags: string[] = ["a"]` |
| `Array<number>` | Array alternativo | `let nums: Array<number> = [1]` |
| `[string, number]` | Tupla fixa | `let par: [string, number] = ["id", 1]` |
| `any` | Desliga a checagem | `let x: any = "qualquer"` |
| `unknown` | Qualquer tipo, mas seguro | `let y: unknown = 42` |
| `void` | Ausência de retorno | `function log(): void {}` |
| `null` / `undefined` | Tipos próprios | `let n: null = null` |
| `string \| number` | Union type | `let id: string \| number = 1` |

## Exemplos

```ts
let nome: string = "Eliatan";
let idade: number = 25;
let hobbies: string[] = ["ler", "correr"];
let pessoa: [string, number] = ["Eliatan", 25];

// Inferência: o TS já sabe que é string, sem anotação
let saudacao = "Olá"; // tipo inferido: string
saudacao.toUpperCase(); // ok
```

```ts
function processar(dado: unknown): void {
  if (typeof dado === "string") {
    console.log(dado.length); // unknown exige verificação antes de usar
  }
}

let vazio: void = undefined;
let nada: null = null;
```

## Boas práticas

- Deixe a inferência trabalhar em variáveis inicializadas na declaração.
- Prefira `unknown` a `any`: força checagem antes do uso.
- Use tupla só para posições fixas e conhecidas; caso contrário, crie um tipo.
- Ative `strictNullChecks` para tratar `null`/`undefined` de verdade.
- Nomeie union types complexos com `type` para reutilizar.
- Evite anotar duas vezes (inferência + anotação idêntica) sem necessidade.

## Armadilhas comuns

- Usar `any` "para resolver rápido" e perder toda a segurança de tipos.
- Esquecer que `number` cobre inteiros e decimais; não existe `int` separado.
- Achar que `[string, number]` valida conteúdo dinâmico: tupla confia na posição.
- Comparar `null == undefined` sem entender que são tipos distintos.
- Anotar como `string[]` um array que recebe números em runtime.

## Relacionadas

- [[TypeScript]]
- [[JavaScript]]
- [[Funcoes-Tipadas]]
- [[Unioes-e-Narrowing]]
