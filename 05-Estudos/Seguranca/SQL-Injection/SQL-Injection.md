---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# SQL-Injection

#area/estudos #estudos/seguranca #conceito

**Resumo:** SQL Injection: ataque que injeta comandos SQL maliciosos em queries, explorando input de usuário não tratado para ler, alterar ou deletar dados.

## Conceitos-chave
- **Causa raiz:** concatenação de input do usuário diretamente em strings de SQL.
- **Impacto:** fuga de dados, autenticação burlada, alteração/remoção de dados e, em alguns casos, execução de comandos.
- **Tipos:** in-band (union, error-based), blind (boolean-based, time-based) e out-of-band.
- **Prevenção principal:** prepared statements / parametrização — o SQL e os dados são enviados separadamente.
- **Defesa adicional:** validação/whitelist de input, menor privilégio do usuário de banco, escape quando parametrização não é possível.
- **Posição no Top 10 OWASP:** historicamente o risco nº 1; hoje "Injection" engloba SQLi, NoSQLi, LDAP, OS command.

## Exemplos
```sql
-- Vulnerável: concatenação direta
SELECT * FROM produtos WHERE id = " + request.form["id"] + "

-- Payload de ataque (in-band)
' OR '1'='1' -- 
' UNION SELECT usuario, senha FROM users -- 

-- Correto: prepared statement (exemplo conceitual)
SELECT * FROM produtos WHERE id = ?
```

```python
# Python/psycopg: parâmetros, nunca f-string
cursor.execute("SELECT * FROM produtos WHERE id = %s", (produto_id,))
```

## Boas práticas
- Usar sempre prepared statements/parameterized queries no acesso a dados.
- Validar tipos e formatos de input no servidor (whitelist quando possível).
- Aplicar menor privilégio à conta de banco usada pela aplicação.
- Usar ORM seguro e evitar `raw()`/`query()` com concatenação.
- Testar com scanners e payloads específicos (ver [[Pentest]]).

## Armadilhas comuns
- Achar que sanitizar/escapar strings resolve — parametrização é a solução robusta.
- Fazer "validação" só no frontend, ignorando requests diretos à API.
- Confiar em ORM como garantia: métodos de query bruta continuam vulneráveis.
- Usar conta de banco com privilégios de DBA para a aplicação.

## Relacionadas
- [[OWASP]]
- [[XSS]]
- [[Ataques]]
- [[Pentest]]
- [[Vulnerabilidades]]