---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Laravel

#area/estudos #estudos/backend #conceito

**Resumo:** Framework PHP expressivo e opinativo, com Eloquent ORM, Blade (templates), Artisan (CLI) e um ecossistema rico para construir aplicações web e APIs.

## Conceitos-chave
- **O que é:** framework full-stack para PHP que entrega autenticação, ORM, filas, cache, migrations e testes prontos.
- **Quando usar:** aplicações web tradicionais, CRUDs, sistemas administrativos e projetos PHP em equipe que valorizam convenções.
- **Estrutura (MVC):** Models + Controllers + Views (Blade), com rotas em `routes/web.php` e `routes/api.php`.
- **Eloquent ORM:** mapeia tabelas para models com relacionamentos, scopes e `migrations`.
- **Blade:** template engine com herança de layout e diretivas (`@if`, `@foreach`).
- **Artisan:** CLI que gera código, roda migrations, cria controllers e gerencia filas.
- **Diferenças-chave:** comparado a Express/NestJS (JS) ou Django/Flask (Python), é a via principal no ecossistema PHP; traz mais pronto que um micro-framework.

## Exemplos
```php
// routes/web.php
Route::get('/', fn () => view('inicio'));

// routes/api.php
Route::get('/usuarios', [UsuarioController::class, 'index']);
```

```php
// Controller com Eloquent
use App\Models\Usuario;

class UsuarioController extends Controller
{
    public function index()
    {
        return Usuario::where('ativo', true)->paginate(10);
    }

    public function store(Request $request)
    {
        $validado = $request->validate([
            'nome' => 'required|max:120',
            'email' => 'required|email|unique:usuarios',
        ]);
        return Usuario::create($validado);
    }
}
```

```bash
php artisan make:model Usuario -m
php artisan migrate
php artisan serve
```

## Boas práticas
- Seguir as convenções do framework (nomes de tabelas, relacionamentos) para aproveitar o automático.
- Usar validação de formulário (`FormRequest`) e `mass assignment` protegido por `$fillable`.
- Colocar lógica de negócio em services ou actions, não em controllers.
- Usar `php artisan` para gerar código e manter migrations versionadas.
- Configurar filas e cache com drivers de produção (Redis, banco) em vez do driver `sync`.

## Armadilhas comuns
- Esquecer `$fillable`/`$guarded` e permitir mass assignment de campos sensíveis.
- Fazer N+1 sem `with('relacionamento')` no Eloquent.
- Colocar queries em views Blade ou lógica pesada em controllers.
- Usar `env()` fora de arquivos de configuração (cacheado) — preferir `config()`.
- Ignorar o `APP_KEY` (usado para criptografia e sessões) mal configurado.

## Relacionadas
- [[PHP]]
- [[Backend]]
- [[Auth]]
- [[ORM]]
- [[Queue]]