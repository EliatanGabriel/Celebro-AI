---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Operadores

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Operadores aritméticos, de comparação, lógicos e de atribuição que formam as expressões do PHP.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `+ - * / % **` | Aritméticos (soma, resto, potência) | `2 ** 10 // 1024` |
| `==` | Compara valor, convertendo tipos | `"1" == 1` é true |
| `===` | Compara valor E tipo (estrito) | `"1" === 1` é false |
| `<=>` | Spaceship: -1, 0 ou 1 | `1 <=> 2` retorna -1 |
| `&&` `\|\|` `!` | E lógico, OU lógico, negação | `$a && $b` |
| `?:` | Ternário curto (elvis) | `$idade ?: 18` |
| `??` | Null coalescing: primeiro não-nulo | `$nome ?? "Anônimo"` |
| `.=` / `+=` | Atribuição composta (concat/ soma) | `$txt .= "!";` |

## Exemplos

```php
<?php
$a = 7; $b = 2;

echo $a % $b;      // 1 (resto da divisão)
echo 2 ** 8;       // 256 (potência)
echo $a <=> $b;    // 1, pois 7 > 2

$nome = $_GET["nome"] ?? "visitante";
echo $nome ?: "vazio";   // se falsy, usa "vazio"

$texto = "Olá";
$texto .= ", mundo";     // concatenação composta
$saldo = 100;
$saldo += 50;            // 150
```

```php
<?php
var_dump("5" == 5);    // true  (converte tipo)
var_dump("5" === 5);   // false (tipos diferentes)
var_dump(true && false);        // false
var_dump(true || false);        // true
var_dump(!true);                // false
```

## Boas práticas

- Prefira `===` e `!==` para evitar bugs por conversão implícita.
- Use `??` para valores padrão de arrays e variáveis possivelmente nulas.
- Use `<=>` principalmente em funções de ordenação como usort.
- Agrupe condições com parênteses quando misturar `&&` e `||`.
- Escolha entre `and/or` e `&&/||` com cuidado: têm precedências diferentes.

## Armadilhas comuns

- `==` faz conversões estranhas: `"abc" == 0` era true em versões antigas.
- Confundir `? :` com `??`: o ternário testa falsy, o coalescing só null.
- Usar `.` em vez de `+` para somar números (ou o contrário).
- Divisão por zero em `/` lança erro; use `fdiv()` se quiser INF.
- Esquecer que `%` converte os operandos para int antes do cálculo.

## Relacionadas

- [[PHP]]
- [[Controle-de-Fluxo]]
- [[Variaveis-e-Tipos]]
