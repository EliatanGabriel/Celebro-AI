---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Ruby

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem dinâmica e expressiva, orientada a objetos "pura" (tudo é objeto), famosa pelo framework web Ruby on Rails e pelo lema "Convenção sobre Configuração".

## Conceitos-chave
- Orientação a objetos pura: classes, módulos e até números são objetos.
- Tipagem dinâmica e forte, com duck typing e metaprogramação poderosa.
- Interpretada: executada via interpreter Ruby (MRI) com garbage collector.
- Uso principal em desenvolvimento web rápido (Ruby on Rails), automação e ferramentas (Chef, Homebrew).
- Blocos, procs e lambdas dão expressividade funcional ao código.
- Gems (bibliotecas) gerenciadas pelo RubyGems/Bundler.
- Particularidade: filosofia "matz" prioriza a felicidade do desenvolvedor e a leitura do código.

## Exemplos
```ruby
class Pessoa
  attr_reader :nome, :idade

  def initialize(nome, idade)
    @nome = nome
    @idade = idade
  end

  def adulto?
    idade >= 18
  end
end

pessoas = [Pessoa.new("Ana", 30), Pessoa.new("Bruno", 16)]
adultos = pessoas.select(&:adulto?).map(&:nome)
puts adultos  # ["Ana"]

5.times { |i| puts i }  # bloco
```

## Boas práticas
- Siga a convenção de estilo (Ruby Style Guide): `snake_case`, `?` para predicados, `!` para versões perigosas.
- Prefira blocos e iteradores (`each`, `map`, `select`) a loops imperativos.
- Mantenha métodos curtos e com responsabilidade única (princípio do Rails).
- Use `attr_reader`/`attr_accessor` em vez de getters/setters manuais.
- Fixe versões de gems no Gemfile.lock e mantenha dependências atualizadas.

## Armadilhas comuns
- Confundir `=` (atribuição) com `==` (comparação) — em Ruby `if x = 1` sempre é verdadeiro.
- Mutação acidental de parâmetros: arrays passados por referência são alterados dentro de métodos.
- `symbol` vs `string`: `:nome` é símbolo e `"nome"` é string; não são intercambiáveis como chaves.
- Métodos com `!` modificam o receptor; sem `!`, geralmente retornam cópia — comportamento confuso.
- Interpolação: usar aspas simples `'...'` impede `#{...}`.

## Relacionadas
- [[Python]]
- [[PHP]]
- [[Backend]]