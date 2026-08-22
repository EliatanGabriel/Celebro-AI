---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Loops

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Estruturas de repetição do PHP: for, while, do-while, foreach e o uso de break/continue com níveis.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `for (init; cond; inc)` | Repete com contador | `for ($i = 0; $i < 3; $i++)` |
| `while (cond)` | Enquanto a condição for verdadeira | `while ($i < 10)` |
| `do {} while (cond)` | Executa ao menos uma vez | `do {...} while ($x);` |
| `foreach ($arr as $v)` | Percorre valores de um array | `foreach ($frutas as $f)` |
| `foreach ($arr as $k => $v)` | Percorre chave e valor | `foreach ($user as $c => $v)` |
| `break` / `break 2` | Sai do loop (ou de N loops) | `break 2;` |
| `continue` / `continue 2` | Pula para a próxima iteração | `continue 2;` |

## Exemplos

```php
<?php
for ($i = 1; $i <= 3; $i++) {
    echo "Volta $i\n";
}

$i = 0;
while ($i < 3) {
    echo $i++;
}

// foreach com chave e valor em array associativo
$usuario = ["nome" => "Ana", "idade" => 30];
foreach ($usuario as $chave => $valor) {
    echo "$chave: $valor\n";
}
```

```php
<?php
// break e continue com níveis em loops aninhados
foreach ([1, 2, 3] as $linha) {
    foreach ([10, 20] as $coluna) {
        if ($coluna === 20) {
            continue 2; // pula para a próxima $linha
        }
        echo "$linha-$coluna ";
    }
}
// saída: 1-10 2-10 3-10

$n = 5;
do {
    echo "roda mesmo com condição falsa";
    $n++;
} while ($n < 5);
```

## Boas práticas

- Use `foreach` para arrays: é mais simples e evita erros de índice.
- Reserve `for` quando precisar do índice numérico ou percorrer de trás.
- Prefira funções como array_map/array_filter a loops manuais complexos.
- Nomeie contadores curtos (`$i`, `$j`) apenas em loops pequenos.
- Garanta que while tenha uma condição que eventualmente fica falsa.

## Armadilhas comuns

- Loop infinito esquecendo de incrementar dentro do while.
- Modificar o array durante o foreach gera comportamento inesperado.
- Confundir `break` (sai) com `continue` (pula iteração).
- Sem nível explícito, break/continue agem apenas no loop mais interno.
- do-while executa sempre uma vez mesmo com condição falsa inicial.

## Relacionadas

- [[PHP]]
- [[Arrays]]
- [[Controle-de-Fluxo]]
