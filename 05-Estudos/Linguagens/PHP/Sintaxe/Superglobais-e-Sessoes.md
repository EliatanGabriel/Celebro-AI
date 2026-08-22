---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Superglobais e Sessões

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Arrays globais que carregam dados da requisição ($_GET, $_POST, $_FILES...) e o controle de estado com $_SESSION.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `$_GET` | Dados da URL/query string | `$_GET["busca"]` |
| `$_POST` | Dados do corpo do formulário POST | `$_POST["email"]` |
| `$_REQUEST` | GET + POST + COOKIE juntos | `$_REQUEST["id"]` |
| `$_COOKIE` | Cookies enviados pelo navegador | `$_COOKIE["tema"]` |
| `session_start()` | Inicia/retoma a sessão | antes de qualquer saída |
| `$_SESSION` | Dados persistentes por usuário | `$_SESSION["user"] = 7;` |
| `$_FILES` | Uploads enviados | `$_FILES["foto"]["tmp_name"]` |
| `$_SERVER` | Informações do servidor/requisição | `$_SERVER["REQUEST_METHOD"]` |
| `htmlspecialchars()` / `filter_var()` | Sanitiza/valida dados externos | ver exemplos |

## Exemplos

```php
<?php
session_start(); // sempre no topo, antes de echo

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // validar e sanitizar
    $email = filter_var($_POST["email"] ?? "", FILTER_VALIDATE_EMAIL);
    $nome  = htmlspecialchars(trim($_POST["nome"] ?? ""), ENT_QUOTES, "UTF-8");

    if ($email === false) {
        die("E-mail inválido");
    }
    $_SESSION["usuario"] = $nome;
}

echo "Bem-vindo, " . ($_SESSION["usuario"] ?? "visitante");
```

```html
<!-- formulário.html -->
<form method="post" action="processa.php">
  <input name="nome" type="text">
  <input name="email" type="email">
  <button type="submit">Enviar</button>
</form>
```

## Boas práticas

- Use GET para buscas/navegação e POST para ações que alteram dados.
- Sempre chame session_start() no início do script.
- Escape toda saída com htmlspecialchars para evitar XSS.
- Prefira filter_var/FILTER_VALIDATE_* para validar entrada.
- Para logout: unset($_SESSION[...]) e depois session_destroy().

## Armadilhas comuns

- Nunca confie em superglobais: tudo pode ser forjado pelo usuário.
- Usar $_REQUEST quando o método importa deixa a API ambígua.
- Echo direto de $_GET/$_POST sem escape abre brecha de XSS.
- Sessão não persiste se houver saída antes de session_start().
- $_FILES só existe com enctype="multipart/form-data" no form.

## Relacionadas

- [[PHP]]
- [[Sintaxe-Basica]]
- [[Strings-e-Formatacao]]
