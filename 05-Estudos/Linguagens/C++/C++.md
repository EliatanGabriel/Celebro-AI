---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# C++

#area/estudos #estudos/linguagens #conceito

**Resumo:** Extensão do C que adiciona orientação a objetos, templates e programação genérica, usada em jogos, sistemas, bancos de dados e aplicações de alta performance.

## Conceitos-chave
- Multiparadigma: procedural (herança do C), orientado a objetos (classes, herança, polimorfismo) e genérico (templates).
- Tipagem estática e forte, com controle explícito de conversões.
- Compilada para código nativo, com performance próxima ao C e zero-cost abstractions.
- Uso principal em game engines (Unreal), navegadores, compiladores, sistemas de baixa latência e computação gráfica.
- RAII (Resource Acquisition Is Initialization): recursos são liberados automaticamente quando o objeto sai de escopo.
- Memória gerenciada por smart pointers (`unique_ptr`, `shared_ptr`) na biblioteca padrão moderna.
- Particularidade: garbage collector não existe; a destruição determinística ocorre via destrutores.

## Exemplos
```cpp
#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>

class Conta {
public:
    explicit Conta(double saldo) : saldo_(saldo) {}
    double saldo() const { return saldo_; }

private:
    double saldo_;
};

int main() {
    std::vector<Conta> contas{{100.0}, {250.0}, {50.0}};
    auto total = 0.0;
    for (const auto& c : contas) total += c.saldo();

    std::cout << "Total: " << total << '\n';
    auto p = std::make_unique<int>(42);  // RAII + smart pointer
    std::cout << *p << '\n';
}
```

## Boas práticas
- Prefira RAII e smart pointers a `new`/`delete` explícitos.
- Use `const` e referências (`const T&`) em parâmetros para evitar cópias desnecessárias.
- Prefira `std::vector`, `std::string` e algoritmos da STL a arrays e loops manuais.
- Evite herança profunda; prefira composição e interfaces explícitas.
- Compile com sanitizers e ferramentas de análise estática em desenvolvimento.

## Armadilhas comuns
- Vazamento de memória por `new` sem `delete` — sempre use RAII.
- Iteradores inválidos após modificar um container (invalidação de iteradores).
- Referências pendentes (dangling) ao retornar referência a objetos locais.
- Confundir `struct` (padrão público) com `class` (padrão privado).
- Conflitos e problemas de ODR (One Definition Rule) com variáveis globais não-inline.

## Relacionadas
- [[C]]