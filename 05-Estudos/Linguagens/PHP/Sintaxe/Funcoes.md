---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Funções

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Como declarar funções em PHP com parâmetros tipados, valores padrão, arrow functions e argumentos variáveis.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `function nome() {}` | Declara função | `function ola() { return "oi"; }` |
| `= valor` | Parâmetro com valor padrão | `function f($x = 10)` |
| `: tipo` | Tipo de retorno declarado | `function f(): string` |
| `?int` | Parâmetro/retorno anulável | `function f(?int $x)` |
| `int\|string` | Union types (PHP 8) | `function f(int\|string $x)` |
| `&$var` | Passagem por referência | `function f(&$total)` |
| `fn() =>` | Arrow function (uma expressão) | `$dobro = fn($n) => $n * 2;` |
| `...$args` | Função variádica (n argumentos) | `function soma(...$nums)` |

## Exemplos

```php
<?php
declare(strict_types=1);

function somar(int $a, int $b = 0): int {
    return $a + $b;
}

function buscar(?string $nome): ?array {
    if ($nome === null) return null;
    return ["nome" => $nome];
}

echo somar(2);        // 2
print_r(buscar("Ana")); // Array ( [nome] => Ana )
```

```php
<?php
// Union types e variádica
function formatar(int|string $valor): string {
    return is_int($valor) ? number_format($valor, 0, ",", ".") : $valor;
}

function media(float ...$notas): float {
    return array_sum($notas) / count($notas);
}

echo media(7.5, 8.0, 6.0); // 7.166...

// Arrow function captura $fator automaticamente
$fator = 3;
$triplo = fn(int $n): int => $n * $fator;
echo $triplo(5); // 15
```

## Boas práticas

- Sempre declare tipos de parâmetros e retorno; ative strict_types.
- Coloque parâmetros com valor padrão por último na assinatura.
- Prefira funções puras e curtas, com uma responsabilidade só.
- Use arrow functions para callbacks simples de uma linha.
- Nomeie funções como verbos: `calcularTotal`, `validarCpf`.

## Armadilhas comuns

- Chamar função antes de defini-la funciona no PHP, mas confunde a leitura.
- Parâmetro default seguido de obrigatório gera erro ao chamar.
- Arrow functions não têm escopo próprio para múltiplas linhas.
- Usar referência `&` sem necessidade torna o código difícil de rastrear.
- Esquecer do return: função sem return devolve null silenciosamente.

## Relacionadas

- [[PHP]]
- [[Arrays]]
- [[Variaveis-e-Tipos]]
