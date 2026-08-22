---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# POO

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Programação orientada a objetos no PHP moderno: classes, construtor com property promotion, herança, traits e namespaces.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `class Nome {}` | Declara classe | `class User {}` |
| `public/private/protected` | Visibilidade de propriedade/método | `private string $nome;` |
| `__construct` | Executa ao criar o objeto | `new User("Ana")` |
| promotion (PHP 8) | Propriedade declarada no parâmetro | `function __construct(private int $id)` |
| `$this` | Instância atual dentro da classe | `$this->nome` |
| `extends` / `implements` | Herda classe / implementa interface | `class A extends B` |
| `static` + `self::` | Membros de classe, não de instância | `self::contar()` |
| `trait X {}` + `use X;` | Reuso horizontal de código | `use Logavel;` |
| `namespace` + `use` | Organiza e importa classes | `use App\Models\User;` |

## Exemplos

```php
<?php
namespace App\Models;

interface Identificavel {
    public function id(): int;
}

trait Logavel {
    public function log(string $msg): void {
        echo "[LOG] $msg\n";
    }
}

class Usuario implements Identificavel {
    use Logavel;

    private static int $total = 0; // estático: da classe

    // Property Promotion do PHP 8
    public function __construct(
        private readonly int $id,
        private string $nome = "sem nome",
    ) {
        self::$total++;
    }

    public function id(): int { return $this->id; }
}

$u = new Usuario(1, "Ana");
$u->log("usuário criado");
echo Usuario::$total;
```

```php
<?php
class Admin extends Usuario {
    public function __construct(int $id, private array $permissoes = []) {
        parent::__construct($id, "admin");
    }
}
```

## Boas práticas

- Use property promotion para enxugar construtores.
- Prefira `private` por padrão; abra só o necessário (`protected/public`).
- Uma responsabilidade por classe; extraia comportamentos comuns em traits.
- Autoload com namespaces seguindo PSR-4 em vez de muitos require.
- Declare tipos nas propriedades para pegar erros cedo.

## Armadilhas comuns

- Usar `->` para membros static ou `::` para instância: cada um tem seu caso.
- Traits duplicando nomes de métodos geram conflito na composição.
- Esquecer `parent::__construct()` ao sobrescrever o construtor do pai.
- Namespace precisa refletir as pastas no autoload, senão class not found.
- `$this` fora do contexto de objeto lança erro fatal.

## Relacionadas

- [[PHP]]
- [[Funcoes]]
- [[Sintaxe-Basica]]
