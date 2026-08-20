---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# PHP

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem server-side dominante em sites dinâmicos, embutida em HTML, base de plataformas como WordPress, e com evolução moderna a partir do PHP 7/8.

## Conceitos-chave
- Multiparadigma: procedural inicialmente, com forte suporte a orientação a objetos desde o PHP 5.
- Tipagem dinâmica e fraca, com tipagem gradual opcional (declarações de tipos e strict_types).
- Interpretada no servidor: o PHP gera HTML/JSON que é enviado ao cliente; o código nunca é exposto.
- Uso principal em web dinâmica, CMS (WordPress), e-commerce (WooCommerce, Magento) e APIs.
- Sintaxe embutida em HTML com tags `<?php ... ?>`.
- Particularidade: fácil hospedagem em qualquer servidor (LAMP/LEMP), grande legado e ecossistema Composer + PSRs.
- Principais frameworks: Laravel, Symfony e CodeIgniter.

## Exemplos
```php
<?php

declare(strict_types=1);

function saudacao(string $nome): string {
    return "Olá, $nome!";
}

$usuarios = [
    ['nome' => 'Ana', 'idade' => 30],
    ['nome' => 'Bruno', 'idade' => 22],
];

$adultos = array_filter($usuarios, fn($u) => $u['idade'] >= 18);

foreach ($adultos as $u) {
    echo saudacao($u['nome']) . PHP_EOL;
}
?>
```

## Boas práticas
- Use `declare(strict_types=1);` e declarações de tipo para mais segurança.
- Separe lógica de apresentação (use templates ou frameworks MVC como Laravel).
- Valide e sanitize toda entrada de usuário para evitar SQL Injection e XSS.
- Prefira Composer e autoloading PSR-4 a `require` manual.
- Mantenha dependências atualizadas, pois PHP avança rápido entre versões.

## Armadilhas comuns
- Concatenação com ponto em vez de ponto-e-vírgula — erros de sintaxe comuns.
- Comparações `==` com coerção fraca (`"0" == false`); use `===` e `!==`.
- Escapar com `mysqli`/`PDO` de forma errada; sempre use prepared statements.
- Tags de fechamento `?>` no fim de arquivos, que podem injetar espaços em branco indesejados.
- Depender de funcionalidades obsoletas removidas (ex.: `mysql_*`).

## Relacionadas
- [[JavaScript]]
- [[Backend]]
- [[HTTP]]