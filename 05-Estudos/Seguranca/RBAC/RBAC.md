---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# RBAC

#area/estudos #estudos/seguranca #conceito

**Resumo:** Role-Based Access Control: modelo de autorização que concede permissões por meio de papéis (roles), simplificando a gestão de acesso em larga escala.

## Conceitos-chave
- **Papéis (roles):** agrupam permissões relacionadas a uma função (ex.: "analista", "admin", "auditor").
- **Atribuição:** usuário → papel → permissões; o acesso vem do papel, não do usuário individual.
- **Menor privilégio:** papéis devem conter apenas o necessário para a função.
- **Separation of duties:** papéis incompatíveis não podem ser acumulados pelo mesmo usuário.
- **ABAC como alternativa:** controle por atributos (contexto, recurso, ambiente) mais dinâmico e fino.
- **Revisão periódica:** papéis inflam com permissões acumuladas ao longo do tempo.

## Exemplos
```sql
-- Exemplo conceitual de RBAC em banco
CREATE TABLE papeis (id INT PRIMARY KEY, nome TEXT NOT NULL);
CREATE TABLE permissoes (id INT PRIMARY KEY, nome TEXT NOT NULL);
CREATE TABLE papel_permissao (papel_id INT, permissao_id INT);
CREATE TABLE usuario_papel (usuario_id INT, papel_id INT);
```

```python
# Verificação em middleware (pseudo-código)
def requer_papel(*roles):
    def deco(fn):
        def wrapper(req):
            if req.usuario.papel not in roles:
                abort(403)
            return fn(req)
        return wrapper
    return deco
```

## Boas práticas
- Modelar papéis por função de negócio, não por usuário.
- Começar com o menor privilégio e ampliar sob demanda.
- Revisar e remover papéis/permissões órfãos periodicamente (ver [[Auditoria]]).
- Registrar quem atribuiu e alterou papéis (trilha de auditoria).
- Evitar papéis "superadmin" genéricos sempre que possível.

## Armadilhas comuns
- Confundir RBAC com autenticação: RBAC define o que fazer após autenticar (ver [[Autorizacao]]).
- Criar centenas de papéis quase idênticos, recriando o problema de gestão individual.
- Atribuir papéis amplos "por segurança" sem revisão.
- Não considerar conflito de funções (ex.: quem aprova também executa).

## Relacionadas
- [[Autorizacao]]
- [[Zero-Trust]]
- [[Auditoria]]
- [[Autenticacao]]