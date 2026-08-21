---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Seguranca-review

#area/trabalho #trabalho/code-review #conceito

**Resumo:** Revisão do código sob a ótica de vulnerabilidades e riscos.

## Conceitos-chave
- Injeção: SQL, XSS, command injection, template injection.
- Autenticação e autorização: validar identidade e permissões.
- Dados sensíveis: não expor nem logar segredos/PII.
- Headers HTTP de segurança e políticas de CORS.
- Validação de entrada em todas as fronteiras.

## Exemplos
```
// Vulnerável: concatenação em query
db.query(`SELECT * FROM usuarios WHERE email = '${email}'`);

// Correto: parâmetros parametrizados
db.query('SELECT * FROM usuarios WHERE email = ?', [email]);

// Nunca logar credenciais
console.log('senha informada:', senha); // proibido
```

## Boas práticas
- Validar e sanitizar toda entrada (body, query, params, headers).
- Usar consultas parametrizadas e ORM seguro.
- Verificar autorização em cada recurso, não só na rota.
- Não expor dados sensíveis em respostas, logs ou erros.
- Aplicar headers de segurança (CSP, HSTS, X-Content-Type-Options).

## Armadilhas comuns
- Confiar na entrada do usuário sem validação.
- Verificar apenas autenticação, esquecendo autorização por recurso.
- Erros de validação vazando stack traces internos.
- Segredos versionados ou logados em ambientes de teste.
- CORS permissivo demais ou validação feita só no frontend.

## Relacionadas
- [[Checklist]]
- [[Best-practices]]