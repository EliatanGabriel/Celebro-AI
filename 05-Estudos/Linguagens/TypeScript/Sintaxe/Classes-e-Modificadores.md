---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Classes e Modificadores (TypeScript)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Classes em TypeScript combinam propriedades tipadas, construtores e modificadores de acesso (public, private, protected, readonly), além de suportar interfaces, herança e classes abstratas.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `class X { campo: T }` | Propriedade tipada | `class P { nome: string }` |
| `constructor(...)` | Inicialização | `constructor(nome: string)` |
| `public` | Acesso livre (padrão) | `public id: number` |
| `private` | Só dentro da classe | `private senha: string` |
| `protected` | Classe e filhas | `protected saldo: number` |
| `readonly` | Não reatribuível | `readonly criadoEm: Date` |
| `implements I` | Cumpre interface | `class A implements Repo` |
| `abstract class` | Base não instanciável | `abstract class Forma` |
| `extends S` + `super()` | Herança | `class B extends A` |

## Exemplos

```ts
interface Repositorio {
  salvar(dado: string): void;
}

abstract class Base {
  protected readonly criadoEm = new Date();
  abstract descricao(): string;
}

class Conta extends Base implements Repositorio {
  public titular: string;
  private saldo = 0;
  readonly agencia: string;

  constructor(titular: string, agencia: string) {
    super(); // chama constructor da base abstrata
    this.titular = titular;
    this.agencia = agencia;
  }

  depositar(valor: number): void {
    if (valor > 0) this.saldo += valor; // ok: dentro da classe
  }

  get extrato(): number {
    return this.saldo;
  }

  descricao(): string {
    return `Conta de ${this.titular}`;
  }
}
// Atalho: parâmetros do constructor declaram e atribuem campos
class Usuario {
  constructor(
    public readonly id: number,
    private nome: string,
  ) {}
}
const u = new Usuario(1, "Ana"); // u.id = 2 -> erro: readonly
```

## Boas práticas
- Use o atalho de parâmetros do constructor para enxugar código.
- Marque campos imutáveis com `readonly` desde o início.
- Prefira `private` a `_underscore` por convenção; o TS bloqueia de verdade.
- Implemente interfaces (`implements`) para garantir contratos públicos.
- Reserve `abstract` para bases que exigem métodos das filhas.
- Chame `super()` antes de usar `this` no constructor da filha.

## Armadilhas comuns

- Esquecer que `private` é apagado no build: não protege em runtime como `#campo`.
- Usar `this` antes de `super()` na classe derivada: erro de compilação.
- Achar que `protected` libera acesso externo: só subclasses têm acesso.
- Declarar propriedade sem inicializar nem anotar `undefined`: erro no strict mode.
- Confundir `implements` com `extends`: um cumpre contrato, outro herda implementação.

## Relacionadas

- [[TypeScript]]
- [[Interfaces-e-Type-Aliases]]
- [[Generics]]
