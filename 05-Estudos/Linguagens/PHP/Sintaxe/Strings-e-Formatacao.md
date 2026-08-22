---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Strings e Formatação

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Manipulação de strings em PHP: aspas, heredoc, funções clássicas de texto e as versões mb_* para UTF-8.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `'...'` | Aspas simples: sem interpolação | `'Olá $nome'` literal |
| `"..."` | Aspas duplas: interpola variáveis | `"Olá $nome"` |
| `<<<EOT` | Heredoc: texto longo interpolado | `<<<EOT ... EOT;` |
| `strlen` / `substr` | Tamanho / fatia da string | `substr($s, 0, 3)` |
| `str_replace` | Substitui trechos | `str_replace("a", "e", $s)` |
| `strpos` / `str_contains` | Posição / contém (PHP 8) | `str_contains($s, "@")` |
| `strtoupper` / `strtolower` | Maiúsculas / minúsculas | `strtoupper("php")` |
| `trim` | Remove espaços das bordas | `trim($entrada)` |
| `sprintf` / `printf` | Formata string / imprime | `sprintf("%.2f", 1.5)` |

## Exemplos

```php
<?php
$nome = "Ana";
echo 'Oi, $nome';   // Oi, $nome (literal)
echo "Oi, $nome";   // Oi, Ana

$texto = <<<EOT
Prezado(a) $nome,
Seu pedido #$pedido foi enviado.
EOT;

$s = "  Programação PHP  ";
echo strlen($s);                       // bytes! acentos pesam mais
echo mb_strlen(trim($s));              // 15 caracteres reais
echo str_replace("PHP", "8", $s);
var_dump(str_contains($s, "PHP"));     // true
```

```php
<?php
$preco = 1234.567;
printf("Total: R\$ %.2f\n", $preco);          // Total: R$ 1234.57
$linha = sprintf("%s tem %d anos", "Bia", 25);

$email = "  Usuario@Site.COM ";
$limpo = strtolower(trim($email));
echo strtoupper(substr($limpo, 0, 1));        // U
```

## Boas práticas

- Use aspas simples quando não houver variável nem caractere especial.
- Prefira `mb_*` (mb_strlen, mb_strtolower) para textos com acentos.
- Use `sprintf` para formatar números, datas e alinhamento.
- Valide antes e escape depois: sanitize entrada, formate na saída.
- Em PHP 8+, prefira `str_contains`/`str_starts_with` a strpos !== false.

## Armadilhas comuns

- strlen conta BYTES: "maçã" retorna 6, não 4.
- Interpolar array/objeto direto na string gera erro ou "Array".
- `$arr['chave']` dentro de aspas sem chaves `{$arr['chave']}` falha.
- strpos retorna 0 no início da string: comparar com false exige `===`.
- Esquecer que trim só remove do início/fim, não do meio.

## Relacionadas

- [[PHP]]
- [[Arrays]]
- [[Variaveis-e-Tipos]]
