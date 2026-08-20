---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Swift

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem da Apple para iOS, macOS, watchOS e tvOS, moderna, segura e de alto desempenho, com optionals, protocol-oriented programming e gerenciamento de memória por ARC.

## Conceitos-chave
- Multiparadigma: orientada a objetos (classes), protocol-oriented (protocols e extensions) e funcional (map/filter).
- Tipagem estática e forte, com inferência de tipos.
- Compilada via LLVM para código nativo das plataformas Apple (Swift Playgrounds para experimentação).
- Uso principal no desenvolvimento de apps para o ecossistema Apple e servidores (Vapor).
- Optionals (`Int?`) e unwrapping seguro (`if let`, `guard let`, `??`) eliminam referências nulas.
- ARC (Automatic Reference Counting) gerencia memória por contagem de referências, sem GC.
- Particularidade: structs são amplamente preferidas a classes por valor e cópia eficiente.

## Exemplos
```swift
struct Pessoa {
    let nome: String
    var idade: Int

    func saudacao() -> String {
        "Olá, eu sou \(nome)!"
    }
}

func classificar(_ pessoa: Pessoa) -> String {
    guard pessoa.idade >= 18 else {
        return "\(pessoa.nome) é menor de idade"
    }
    return "\(pessoa.nome) é adulto"
}

let ana = Pessoa(nome: "Ana", idade: 30)
let bruno = Pessoa(nome: "Bruno", idade: 16)

print(ana.saudacao())
print(classificar(ana))    // Ana é adulto
print(classificar(bruno))  // Bruno é menor de idade

let nomes = [ana, bruno].map { $0.nome }  // funcional
```

## Boas práticas
- Prefira `let` (constante) a `var` e structs a classes para tipos de valor simples.
- Use `guard let`/`guard` no início de funções para sair cedo de condições inválidas.
- Aproveite protocols + extensions para composição em vez de herança de classe.
- Trate optionals com unwrapping seguro e `??` para valores padrão.
- Siga as convenções da Apple: `camelCase` para funções, nomes descritivos e frameworks com tipagem forte.

## Armadilhas comuns
- Forçar unwrap com `!` em optional nulo, gerando crash (fatal error).
- Ciclos de retenção com closures: `[weak self]` é necessário para evitar memory leak no ARC.
- Mutabilidade de structs: propriedades `var` só podem ser alteradas se o próprio struct for `var`.
- Confundir `let`/`var` com constância de referência vs. valor.
- APIs de Objective-C retornam optionals implícitos (IUO), que podem causar crashes inesperados.

## Relacionadas
- [[Kotlin]]
- [[Frontend]]