---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Credenciais

#area/estudos #estudos/seguranca #conceito

**Resumo:** Conjunto de identificadores e provas de identidade — usuário/senha, chaves, tokens — que um sujeito apresenta para autenticar em um sistema.

## Conceitos-chave
- **Composição:** identificador (ex.: e-mail, username) + segredo (senha, chave, token).
- **Ciclo de vida:** emissão, uso, expiração, rotação e revogação de credenciais.
- **Armazenamento:** segredos de autenticação devem usar [[Hashing]] com salt (senhas) ou criptografia/cofres (chaves e tokens).
- **Gerenciamento:** gerenciadores de senha, secret managers e cofres (vault) centralizam e protegem.
- **Exfiltração:** phishing, keyloggers, credenciais em repositórios e reuso são as vias comuns de roubo.
- **Credential stuffing:** ataque automatizado que usa credenciais vazadas em diversos serviços.

## Exemplos
```python
# Nunca commitar credenciais em código (pseudo-código)
usuario = os.environ["DB_USER"]        # ler de variável de ambiente / cofre
senha   = os.environ["DB_PASSWORD"]
conexao = conectar(usuario, senha)
```

## Boas práticas
- Usar credenciais únicas por serviço e expirar periodicamente.
- Preferir [[MFA]] e tokens de curta duração a segredos estáticos.
- Armazenar credenciais em secret managers com acesso auditado (ver [[Segredos]]).
- Rotacionar credenciais imediatamente após suspeita de vazamento.
- Remover credenciais órfãs e contas de ex-funcionários.

## Armadilhas comuns
- Reutilizar a mesma senha em vários sistemas — amplifica qualquer vazamento.
- Escrever credenciais em `.env` versionado ou código fonte (ver [[Env]]).
- Dar credenciais permanentes a serviços que poderiam usar credenciais efêmeras.
- Desativar [[MFA]] para "facilitar" — trade-off falso de segurança por conveniência.

## Relacionadas
- [[Segredos]]
- [[MFA]]
- [[Senhas]]
- [[Env]]
- [[Autenticacao]]
- [[Phishing]]