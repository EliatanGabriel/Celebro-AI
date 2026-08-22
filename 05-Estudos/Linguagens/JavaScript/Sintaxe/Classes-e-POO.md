---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Classes e POO em JavaScript

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Classes em JavaScript organizam objetos com `constructor`, herança via `extends` + `super`, getters/setters, campos privados com `#`, métodos estáticos e `instanceof`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `class Nome {}` | Declara uma classe (não sofre hoisting) | `class Pessoa {}` |
| `constructor(...)` | Inicializa o objeto criado pelo `new` | `constructor(nome) { this.nome = nome; }` |
| `new Nome()` | Cria instância da classe | `const p = new Pessoa("Ana");` |
| `extends` / `super()` | Herança e chamada ao construtor pai | `class Aluno extends Pessoa { super(nome); }` |
| `get x()` / `set x(v)` | Acessor e modificador computados | `get nome() { return this._nome; }` |
| `#campo` | Campo/método privado (só visível na classe) | `#saldo = 0;` |
| `static metodo()` | Pertence à classe, não à instância | `static criarVazio() {}` |
| `obj instanceof Classe` | Verifica se obj vem da classe (ou filha) | `a instanceof Aluno;` |

## Exemplos

```js
// Classe base com campo privado, getter/setter e static
class Conta {
  #saldo = 0;

  constructor(titular) {
    this.titular = titular;
  }

  get saldo() { return this.#saldo; }
  set saldo(valor) {
    if (valor < 0) throw new Error("Saldo negativo");
    this.#saldo = valor;
  }

  static banco = "Banco JS";
  depositar(valor) { this.#saldo += valor; }
}
```

```js
// Herança com extends e super
class ContaVIP extends Conta {
  constructor(titular, limite) {
    super(titular);            // chama o construtor pai
    this.limite = limite;
  }
}

const conta = new ContaVIP("Ana", 1000);
conta.depositar(500);
console.log(conta.saldo);                  // 500
console.log(conta instanceof Conta);       // true
```

## Boas práticas

- Proteja estado interno com campos privados e exponha via getters/setters.
- Chame `super()` antes de usar `this` no construtor filho.
- Use métodos `static` para fábricas e utilitários ligados à classe.
- Prefira composição a herança quando a relação não for "é um".
- Uma classe por arquivo facilita manutenção em projetos grandes.

## Armadilhas comuns

- Acessar `this` antes de `super()` no construtor filho dá erro.
- Classes não sofrem hoisting: usar antes de declarar lança ReferenceError.
- Métodos de classe não ficam enumeráveis nem anexados à instância.
- `#campo` só pode ser acessado dentro do corpo da própria classe.
- Esquecer o `new` faz o código rodar sem criar objeto (erro em modo strict).

## Relacionadas

- [[Objetos-e-Destructuring]]
- [[Funcoes]]
- [[JavaScript]]
