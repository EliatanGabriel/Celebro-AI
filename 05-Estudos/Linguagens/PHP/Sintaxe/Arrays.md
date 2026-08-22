---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Arrays

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Arrays em PHP são mapas ordenados: funcionam como lista indexada e dicionário associativo ao mesmo tempo.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `[1, 2, 3]` | Array indexado | `$nums = [1, 2, 3];` |
| `['k' => 'v']` | Array associativo | `['nome' => 'Ana']` |
| `count($arr)` | Conta elementos | `count($nums)` |
| `array_push($a, $x)` / `$a[] = $x` | Adiciona no fim | `$a[] = 4;` |
| `unset($arr[$k])` | Remove elemento/chave | `unset($lista[0]);` |
| `in_array` / `array_search` | Verifica/busca valor | `in_array(3, $nums)` |
| `array_keys` / `array_values` | Chaves ou valores do array | `array_keys($user)` |
| `array_map/filter/reduce` | Transformar/filtrar/agregar | `array_map(fn($n) => $n*2, $a)` |
| `implode` / `explode` | Junta ou separa strings | `explode(",", $csv)` |

## Exemplos

```php
<?php
$frutas = ["uva", "maçã", "pera"];
$precos = ["uva" => 7.5, "maçã" => 4.2];

$frutas[] = "kiwi";              // adiciona
unset($frutas[1]);               // remove índice 1
echo count($frutas);             // 3
var_dump(in_array("pera", $frutas)); // true
print_r(array_values($frutas));  // reindexa: [0]=>"uva"...
```

```php
<?php
$notas = [8, 5, 9, 6];

$dobradas = array_map(fn($n) => $n * 2, $notas);
$aprovados = array_filter($notas, fn($n) => $n >= 6);
$total = array_reduce($notas, fn($acc, $n) => $acc + $n, 0);

sort($notas);                        // ordena por valor
usort($pessoas, fn($a, $b) => $b["idade"] <=> $a["idade"]); // ordem customizada

echo implode(", ", $notas);          // "5, 6, 8, 9"
$partes = explode(":", "10:30");     // ["10", "30"]
```

## Boas práticas

- Prefira a sintaxe curta `[]` (PHP 5.4+) em vez de `array()`.
- Use funções de array (map/filter/reduce) antes de escrever loops manuais.
- Após unset, use array_values se precisar de índices sequenciais.
- Verifique com isset/array_key_exists antes de acessar chaves.
- Escolha nomes no plural para arrays: `$usuarios`, `$itens`.

## Armadilhas comuns

- Índices numéricos não se reorganizam após unset (fica buraco).
- `==` entre dois arrays compara conteúdo, mas `===` exige mesma ordem/tipo.
- array_search retorna 0 na primeira posição: teste com `!== false`.
- sort reindexa e destrói chaves associativas; use asort/ksort nelas.
- Acessar chave inexistente gera warning e retorna null silenciosamente.

## Relacionadas

- [[PHP]]
- [[Loops]]
- [[Funcoes]]
