---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Rust

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem de sistemas focada em segurança de memória e performance de C, sem garbage collector, usando o sistema de ownership/borrowing para garantir código seguro na compilação.

## Conceitos-chave
- Multiparadigma: imperativa, funcional e orientada a dados; zero-cost abstractions.
- Tipagem estática e forte, com inferência e sistema de traits para polimorfismo.
- Compilada (rustc/LLVM) para código nativo de alta performance, sem runtime pesado.
- Uso principal em sistemas, ferramentas CLI (ripgrep, fd), web assembly (Wasm) e infraestrutura.
- Ownership: cada valor tem um único dono; o recurso é liberado ao sair do escopo (drop).
- Borrowing: referências temporárias (`&`, `&mut`) com regras verificadas pelo borrow checker.
- Particularidade: sem garbage collector, com threads seguras ("fearless concurrency").

## Exemplos
```rust
struct Usuario {
    nome: String,
    idade: u8,
}

fn maiores_de_idade(usuarios: &[Usuario]) -> Vec<&str> {
    usuarios
        .iter()
        .filter(|u| u.idade >= 18)
        .map(|u| u.nome.as_str())
        .collect()
}

fn main() {
    let usuarios = vec![
        Usuario { nome: "Ana".into(), idade: 30 },
        Usuario { nome: "Bruno".into(), idade: 16 },
    ];

    for nome in maiores_de_idade(&usuarios) {
        println!("Maior de idade: {nome}");
    }

    // Option e match
    let talvez: Option<i32> = Some(10);
    match talvez {
        Some(v) => println!("Valor: {v}"),
        None => println!("Nada"),
    }
}
```

## Boas práticas
- Deixe o borrow checker orientar o design: funções tomam `&T` para leitura e `&mut T` para mutação.
- Prefira `Result`/`?` para tratamento de erros em vez de pânico (`panic!`).
- Use `cargo` para build/testes/bench e clippy para lint.
- Modele dados com `enum`/`struct` e traits; evite lógica de herança.
- Aproveite `impl` e derive (`Debug`, `Clone`, `PartialEq`) para código idiomático.

## Armadilhas comuns
- Tentar usar um valor após movê-lo (moved value), erro clássico de ownership.
- Criar referências pendentes (dangling) ao retornar referências a valores locais.
- Contenção no `borrow checker` com empréstimos múltiplos (`&mut` + `&`).
- Usar `clone()` em excesso para contornar o compilador, gerando cópias desnecessárias.
- Tratar `Option` com `unwrap()` sem verificar `None`, causando pânico em runtime.

## Relacionadas
- [[Go]]
- [[C]]