---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Autorizacao

#area/estudos #estudos/seguranca #conceito

**Resumo:** Processo de definir o que um usuário autenticado pode acessar e executar, respondendo "o que você pode fazer?".

## Conceitos-chave
- **Autenticação ≠ autorização:** primeiro se prova a identidade, depois se verifica a permissão para cada ação.
- **Controle de acesso:** modelos como RBAC (papéis), ABAC (atributos) e ACL (listas por recurso).
- **Menor privilégio:** conceder apenas as permissões mínimas necessárias para a função.
- **Autorização no servidor:** decisões de permissão devem ser verificadas no backend, nunca confiando no cliente.
- **Escopo:** tokens com escopos (OAuth) limitam o que um token pode fazer.
- **Separation of duties:** impedir que uma única pessoa acumule passos críticos (ex.: aprovar e executar pagamento).

## Exemplos
```python
# Exemplo de verificação de permissão no backend (pseudo-código)
if not usuario.tem_permissao("relatorio:exportar"):
    raise PermissionDenied("sem permissao para exportar")
```

## Boas práticas
- Aplicar princípio do menor privilégio desde o design.
- Revisar permissões periodicamente (ver [[Auditoria]]).
- Centralizar a lógica de autorização em middleware ou policy engine.
- Usar escopos e papéis granulares em vez de "admin" global.
- Negar por padrão: o que não estiver explicitamente liberado é bloqueado.

## Armadilhas comuns
- Esconder botões/UI no frontend e achar que isso é autorização — o backend precisa validar.
- IDs enumeráveis em URLs (IDOR): acessar `usuario/3` sem checar posse.
- Dar permissão ampla de "admin" a todos para simplificar.
- Confundir autenticação bem-sucedida com autorização automática para tudo.

## Relacionadas
- [[Autenticacao]]
- [[RBAC]]
- [[Tokens]]
- [[Zero-Trust]]