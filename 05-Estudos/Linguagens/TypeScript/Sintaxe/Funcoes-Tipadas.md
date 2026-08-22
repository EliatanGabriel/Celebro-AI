---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Funções Tipadas (TypeScript)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** No TypeScript, funções declaram tipos para parâmetros e retorno, aceitam parâmetros opcionais/default e podem ser descritas por function types reutilizáveis.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `(x: number)` | Parâmetro tipado | `function dobro(x: number) {}` |
| `: number` | Retorno tipado | `function dobro(x: number): number` |
| `: void` | Sem retorno utilizável | `function log(): void {}` |
| `?` | Parâmetro opcional | `function oi(nome?: string) {}` |
| `= valor` | Parâmetro default | `function oi(nome = "mundo") {}` |
| `type F = (...) => T` | Function type | `type Cb = (x: number) => void` |
| `(...resto: number[])` | Rest params | `function soma(...n: number[])` |
| `(a: string): number => ...` | Arrow tipada | `const tam = (s: string) => s.length` |

## Exemplos

```ts
function somar(a: number, b: number = 0, c?: number): number {
  return a + b + (c ?? 0);
}

somar(1);            // ok, b usa default e c é undefined
somar(1, 2);
somar(1, 2, 3);

function logar(msg: string): void {
  console.log(msg); // sem return útil
}
```

```ts
// Function type: descreve o formato de uma função
type Callback = (valor: number, indice: number) => void;

function percorrer(lista: number[], cb: Callback): void {
  lista.forEach((v, i) => cb(v, i));
}

percorrer([10, 20], (valor) => console.log(valor));

// Rest params tipados
function juntar(separador: string, ...partes: string[]): string {
  return partes.join(separador);
}

juntar("-", "a", "b", "c"); // "a-b-c"
```

## Boas práticas

- Deixe o retorno ser inferido em funções simples; anote retornos públicos de APIs.
- Prefira parâmetros default a opcionais quando houver um valor padrão natural.
- Extraia assinaturas repetidas para `type` ou `interface`.
- Use arrow tipada em callbacks pequenas; o tipo dos params pode ser inferido pelo contexto.
- Nomeie os parâmetros no function type (`(valor: number) => void`) para legibilidade.
- Coloque parâmetros obrigatórios antes dos opcionais/default.

## Armadilhas comuns

- Achar que `void` retorna `undefined` tipado: você não deve usar o resultado.
- Esquecer que opcional `?` torna o tipo `string | undefined` dentro da função.
- Usar `...args: any[]` e perder toda a checagem.
- Confundir function type com corpo de função: `type F = () => void` não executa nada.
- Passar callback com menos parâmetros sem problema, mas com mais parâmetros gera erro.

## Relacionadas

- [[TypeScript]]
- [[JavaScript]]
- [[Generics]]
- [[Tipos-Basicos]]
