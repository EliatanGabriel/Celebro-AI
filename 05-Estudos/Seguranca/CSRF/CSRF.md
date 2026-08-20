---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# CSRF

#area/estudos #estudos/seguranca #conceito

**Resumo:** Cross-Site Request Forgery: ataque que força o navegador autenticado de uma vítima a executar ações indesejadas em um site em que ela confia.

## Conceitos-chave
- **Mecanismo:** o atacante hospeda um site/script que dispara requests ao site-alvo; cookies de sessão viajam automaticamente.
- **Exemplo clássico:** alterar senha, e-mail ou transferir dinheiro usando a sessão já ativa da vítima.
- **Dependência:** cookies (credenciais implícitas) tornam requests indistinguíveis de ações legítimas sem contramedidas.
- **Token CSRF (anti-CSRF):** valor aleatório por sessão embutido nos forms e validado no servidor.
- **SameSite cookies:** atributo `SameSite=Lax|Strict` impede o envio de cookies em requests cross-site.
- **Verificação de origem:** checar `Origin`/`Referer` como camada adicional.

## Exemplos
```html
<!-- Payload de exemplo: dispara POST em site onde a vítima está logada -->
<img src="http://banco.com.br/transferir?conta=666&valor=1000">
```

```python
# Verificação de token CSRF (pseudo-código)
if request.form.get("csrf_token") != session["csrf_token"]:
    abort(403, "token CSRF invalido")
```

## Boas práticas
- Usar token CSRF (Double Submit ou sincronizado) em todos os requests que mudam estado.
- Configurar cookies com `SameSite=Lax` ou `Strict` e `HttpOnly` + `Secure`.
- Validar `Origin`/`Referer` em operações sensíveis.
- Em APIs, exigir header customizado ou token bearer em vez de depender de cookies.

## Armadilhas comuns
- Confundir CSRF com XSS: CSRF abusa da sessão; XSS injeta código no site (ver [[XSS]]).
- Aplicar tokens apenas em GET e esquecer POST/PUT/DELETE.
- Token CSRF válido por tempo longo ou compartilhado entre sessões.
- Achar que CORS resolve CSRF — são problemas diferentes.

## Relacionadas
- [[OWASP]]
- [[XSS]]
- [[Tokens]]
- [[Autenticacao]]