---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Lua

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem de script leve, interpretada e embarcável, projetada para ser integrada a aplicações — é o padrão em jogos (WoW, Roblox), Redis e configuração de sistemas.

## Conceitos-chave
- Multiparadigma: imperativa, procedural, com suporte a orientação a objetos via metatables e programação funcional.
- Tipagem dinâmica: tipos são associados a valores, não a variáveis.
- Interpretada: o código é compilado para bytecode de uma VM pequena e rápida na primeira execução.
- Uso principal como linguagem embutida (embedding) em jogos, engines, aplicações (LÖVE, Redis, Nginx, WoW addons) e ferramentas de configuração.
- Tabelas (`table`) são a única estrutura de dados: arrays, dicionários, objetos e módulos.
- Particularidade: implementação mínima (~200 KB) e altamente portável, com GC incremental e threads cooperativas via coroutines.

## Exemplos
```lua
-- Tabela como objeto
local Pessoa = {}
Pessoa.__index = Pessoa

function Pessoa.novo(nome, idade)
  return setmetatable({ nome = nome, idade = idade }, Pessoa)
end

function Pessoa:saudar()
  print("Olá, eu sou " .. self.nome)
end

local p = Pessoa.novo("Ana", 30)
p:saudar()

-- Iteração e concatenação
local valores = { 1, 2, 3 }
local soma = 0
for _, v in ipairs(valores) do
  soma = soma + v
end
print("Soma: " .. soma)
```

## Boas práticas
- Use `local` para todas as variáveis: evita poluir o escopo global e acelera o acesso.
- Prefira `ipairs` para arrays e `pairs` para dicionários; entenda a diferença.
- Aproveite `require` e módulos para organização em vez de globais.
- Use `:`, sugar syntax, apenas quando o método recebe o objeto (`self`) como primeiro argumento.
- Respeite o padrão de retornos múltiplos e a convenção de errors (`error`/`pcall`).

## Armadilhas comuns
- Índices de tabela começam em 1, não em 0 — surpreende quem vem de outras linguagens.
- `pairs` não garante ordem de iteração; use array explícito quando a ordem importa.
- Esquecer `setmetatable`/`__index` ao criar herança, retornando `nil` em métodos.
- Concatenar `nil` com `..`, gerando erro; valide antes.
- Confundir `~=` (diferente) com `!=` — em Lua o operador de diferença é `~=`.

## Relacionadas
- [[C]]
- [[Python]]