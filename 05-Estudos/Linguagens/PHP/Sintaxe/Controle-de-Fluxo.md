---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Controle de Fluxo

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Estruturas de decisão em PHP: if/elseif, switch (com fall-through) e a match expression do PHP 8.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `if / elseif / else` | Decisão clássica por condição | `if ($a > 0) {}` |
| `switch/case/break` | Compara um valor contra casos | `case 1: ...; break;` |
| fall-through | Sem `break`, executa o próximo case | cuidado! |
| `default` | Caso padrão quando nada casa | `default:` |
| `match($x)` | Expressão PHP 8, comparação `===` | `$r = match(true){...}` |
| ternário `? :` | If compacto que retorna valor | `$maior = $a > $b ? $a : $b;` |

## Exemplos

```php
<?php
$nota = 7;

if ($nota >= 9) {
    echo "Excelente";
} elseif ($nota >= 6) {
    echo "Aprovado";
} else {
    echo "Reprovado";
}

$opcao = "b";
switch ($opcao) {
    case "a":
        echo "Opção A";
        break; // sem isso, cai no caso B!
    case "b":
        echo "Opção B";
        break;
    default:
        echo "Inválida";
}
```

```php
<?php
// match é expressão: retorna valor e usa === sem precisar de break
$codigo = 404;
$texto = match($codigo) {
    200 => "OK",
    404 => "Não encontrado",
    default => "Desconhecido",
};
echo $texto;

// match com condições múltiplas
echo match(true) {
    $codigo >= 200 && $codigo < 300 => "sucesso",
    $codigo >= 400 => "erro",
    default => "outro",
};
```

## Boas práticas

- Prefira `match` no PHP 8+ para mapear valores: mais enxuto e estrito.
- Sempre coloque `break` em cada `case` do switch.
- Use `default` para capturar valores inesperados.
- Em ifs longos, extraia lógica para funções com nomes claros.
- Ternários aninhados dificultam leitura: evite mais de um nível.

## Armadilhas comuns

- Switch compara com `==` solto: `"1"` casa com `1`; match não sofre disso.
- Esquecer o `break` causa fall-through executando cases seguintes.
- No if, atribuir (`=`) em vez de comparar (`==`) passa sempre como true.
- Match precisa cobrir todos os casos ou lança erro sem `default`.
- Misturar `elseif` e `else if` no mesmo projeto deixa o estilo inconsistente.

## Relacionadas

- [[PHP]]
- [[Loops]]
- [[Operadores]]
