---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Variáveis e Tipos

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** PHP é dinamicamente tipado: variáveis não declaram tipo, mas você pode exigir rigor com `strict_types`.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `$var = valor` | Cria variável sem declarar tipo | `$idade = 30;` |
| `int` / `float` | Números inteiros e decimais | `$preco = 19.90;` |
| `string` / `bool` / `null` | Texto, verdadeiro/falso, vazio | `$ativo = true;` |
| `array` | Lista ou mapa de valores | `$lista = [1, 2];` |
| `gettype($x)` | Retorna o nome do tipo | `gettype($idade);` |
| `var_dump($x)` | Mostra tipo e valor (debug) | `var_dump($preco);` |
| `declare(strict_types=1);` | Exige tipos exatos nas funções | primeira linha do arquivo |
| `const NOME` / `define()` | Constantes imutáveis | `const PI = 3.14;` |
| `"$var"` | Interpolação em aspas duplas | `"Olá, $nome"` |

## Exemplos

```php
<?php
declare(strict_types=1);

$nome = "Ana";          // string
$idade = 30;            // int
$altura = 1.65;         // float
$ativo = true;          // bool
$nada = null;           // null
$frutas = ["maçã", "uva"]; // array

var_dump($altura);              // float(1.65)
echo gettype($idade);           // integer

const LIMITE = 100;
define("VERSAO", "1.0");
echo LIMITE . " / " . VERSAO;
```

```php
<?php
$produto = "café";
$preco = 12.5;

// interpolação só funciona em aspas duplas
echo "O $produto custa R\$ $preco";
echo 'O $produto custa R\$ $preco'; // imprime literal, sem interpolar
```

## Boas práticas

- Coloque `declare(strict_types=1);` no topo dos arquivos para pegar erros cedo.
- Use `var_dump()` em desenvolvimento para inspecionar tipos e valores.
- Prefira `const` a `define()` dentro de classes e arquivos modernos.
- Nomeie constantes em MAIÚSCULAS_COM_UNDERSCORE.
- Inicialize variáveis antes de usar para evitar warnings.

## Armadilhas comuns

- Interpolar variável em aspas simples não funciona: sai o texto literal.
- Comparar `0`, `"0"` e `null` com `==` gera surpresas; prefira `===`.
- `strict_types` é por arquivo: precisa estar em todos que quiser proteger.
- Somar string numérica com int converte silenciosamente (`"5" + 1 == 6`).
- Constantes não usam `$`: escrever `$PI` dá erro de variável inexistente.

## Relacionadas

- [[PHP]]
- [[Sintaxe-Basica]]
- [[Operadores]]
