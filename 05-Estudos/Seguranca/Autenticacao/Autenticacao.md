---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Autenticacao

#area/estudos #estudos/seguranca #conceito

**Resumo:** Processo de verificar a identidade de um usuário ou sistema — responder "quem é você?" — antes de conceder acesso.

## Conceitos-chave
- **Fatores de autenticação:** algo que você sabe (senha), tem (token, celular), é (biometria) e faz (assinatura, localização).
- **Autenticação vs. autorização:** autenticar prova quem é; autorizar decide o que pode fazer (ver [[Autorizacao]]).
- **Sessões:** após autenticar, o servidor emite uma sessão ou token que evita reautenticação a cada request.
- **MFA:** combinar fatores distintos reduz drasticamente o risco de acesso indevido.
- **Protocolos:** OAuth 2.0, OIDC, SAML e passwordless (WebAuthn/FIDO2) modernizam a autenticação.
- **Account lockout e rate limiting:** mitigam brute force.

## Exemplos
```python
# Verificação de senha com hashing seguro (pseudo-código)
if bcrypt.checkpw(senha_digitada, hash_armazenado):
    sessao = criar_sessao(usuario_id)   # gera cookie/token
else:
    registrar_falha(usuario_id)         # log para auditoria
```

## Boas práticas
- Nunca armazenar senhas em texto puro; usar [[Hashing]] com salt (bcrypt, argon2).
- Exigir [[MFA]] para acessos sensíveis e administrativos.
- Implementar rate limiting, lockout e alertas de login suspeito.
- Expirar e renovar sessões/tokens; invalidar no logout.
- Tratar mensagens de erro genéricas ("credenciais inválidas") para não vazar quais usuários existem.

## Armadilhas comuns
- Confundir autenticação com autorização.
- Armazenar hashes fracos (MD5/SHA1 sem salt) para senhas.
- Depois de redefinir senha, manter sessões antigas ativas.
- Enviar tokens de redefinição por meios não seguros.

## Relacionadas
- [[Autorizacao]]
- [[RBAC]]
- [[Senhas]]
- [[MFA]]
- [[Biometria]]
- [[Tokens]]