---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Sintaxe Básica

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Fundamentos da estrutura de um script PHP: tags, instruções, comentários e variáveis.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `<?php ?>` | Abre/fecha bloco PHP | `<?php echo "oi"; ?>` |
| `<?php` sem fechamento | Padrão em arquivos só de PHP | `<?php` no topo do arquivo |
| `;` | Encerra cada instrução (obrigatório) | `$x = 1;` |
| `echo` | Imprime texto na saída | `echo "Olá";` |
| `print` | Como echo, retorna 1 | `print "Olá";` |
| `//` e `#` | Comentário de uma linha | `// nota` |
| `/* */` | Comentário de múltiplas linhas | `/* bloco */` |
| `$var` | Variável sempre com $, sensível a maiúsculas | `$nome = "Ana";` |

## Exemplos

```php
<?php
// Comentário de uma linha
# Também é comentário de uma linha

/*
 * Comentário em bloco,
 * útil para explicações longas.
 */
$mensagem = "Olá, PHP!";
echo $mensagem; // imprime Olá, PHP!
?>
<p>HTML normal aqui: <?php echo date("Y"); ?></p>
```

```php
<?php
$Nome = "Ana";   // começa com maiúscula
$nome = "Bruno"; // variável diferente! PHP diferencia caixa
echo $Nome . " - " . $nome;
```

## Boas práticas

- Em arquivos apenas com código PHP, omita o `?>` final para evitar espaços indesejados.
- Sempre termine instruções com ponto e vírgula.
- Use nomes de variáveis descritivos em minúsculas com camelCase.
- Comente trechos complexos, não o óbvio.
- Para testar rápido, rode `php -S localhost:8000` na pasta do projeto.

## Armadilhas comuns

- Esquecer o `;` gera erro fatal de parse na linha seguinte.
- `$nome` e `$Nome` são variáveis diferentes (case-sensitive).
- Esquecer de fechar aspas quebra tudo com mensagem confusa.
- Misturar muito PHP dentro de HTML deixa o código ilegível.
- Usar `<?` sem configurar `short_open_tag` não funciona em todo servidor.

## Relacionadas

- [[PHP]]
- [[Variaveis-e-Tipos]]
- [[Controle-de-Fluxo]]
