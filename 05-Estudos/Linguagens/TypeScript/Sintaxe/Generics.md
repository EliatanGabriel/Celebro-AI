---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Generics (TypeScript)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Generics parametrizam tipos com variáveis como `<T>`, permitindo funções, interfaces e classes reutilizáveis que preservam a informação de tipo entre entrada e saída.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `<T>` | Parâmetro de tipo | `function id<T>(v: T): T` |
| `<T extends U>` | Constraint | `<T extends { id: number }>` |
| `<K, V>` | Múltiplos tipos | `<K extends string, V>` |
| `<T = string>` | Default do generic | `interface Caixa<T = string>` |
| `Caixa<number>` | Uso explícito | `new Caixa<number>()` |
| `keyof T` | Chaves de T | `<T, K extends keyof T>` |
| `class Fila<T>` | Classe genérica | `class Pilha<T> {}` |

## Exemplos

```ts
// T "lembra" o tipo passado: entrada e saída casam
function primeiro<T>(lista: T[]): T | undefined {
  return lista[0];
}

const n = primeiro([10, 20]);      // number | undefined
const s = primeiro(["a", "b"]);    // string | undefined

// Constraint: só aceita tipos que têm id, e devolve o mesmo T
function buscar<T extends { id: number }>(itens: T[], id: number): T | undefined {
  return itens.find((i) => i.id === id);
}

buscar([{ id: 1, nome: "Ana" }], 1); // ok, retorna o objeto completo
```

```ts
// Genérico em interface com dois parâmetros e default
interface Mapa<K, V = V[]> {
  obter(chave: K): V;
}

class Pilha<T> {
  private itens: T[] = [];
  empilhar(item: T): void {
    this.itens.push(item);
  }
  desempilhar(): T | undefined {
    return this.itens.pop();
  }
}

const p = new Pilha<string>();
p.empilhar("a");
console.log(p.desempilhar()); // "a"
```

## Boas práticas

- Nomeie generics com letras curtas significativas: `T`, `K`, `V`, `E`.
- Aplique constraints (`extends`) para acessar campos do tipo sem `any`.
- Deixe o TS inferir o argumento de tipo; seja explícito só quando falhar.
- Use default (`<T = string>`) para facilitar casos mais comuns.
- Prefira generics a overloads quando a lógica é a mesma para todos os tipos.
- Combine com `keyof` para APIs seguras de acesso por propriedade.

## Armadilhas comuns

- Escrever `<any>` achando que é genérico: perde-se toda a ligação de tipos.
- Esquecer a constraint e tentar usar `item.id` sem garantir que existe.
- Confundir constraint no parâmetro de tipo com herança de valor.
- Usar generics onde um union simples resolveria com menos complexidade.
- Anotar `<T>` na chamada com tipo incompatível e estranhar o erro propagado.

## Relacionadas

- [[TypeScript]]
- [[Utility-Types]]
- [[Funcoes-Tipadas]]
