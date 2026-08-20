---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Segredos

#area/estudos #estudos/seguranca #conceito

**Resumo:** Chaves, senhas, tokens e certificados que devem ser protegidos, rotacionados e nunca versionados em repositórios ou espalhados no código.

## Conceitos-chave
- **Tipos:** chaves de API, chaves privadas, senhas de banco, tokens de serviço, certificados.
- **Vazamento:** commits em git, logs, imagens de contêiner, arquivos `.env` e mensagens são vias comuns de exposição.
- **Secret managers:** AWS Secrets Manager, Vault, GCP Secret Manager centralizam acesso com criptografia e auditoria.
- **Rotação:** trocar segredos periodicamente e após suspeita de vazamento.
- **Menor privilégio:** cada serviço acessa apenas os segredos de que precisa.
- **Detecção:** scanners (gitleaks, trufflehog) varrem o repositório e o histórico do git.

## Exemplos
```bash
# Varredura de segredos no repositório
gitleaks detect --source . --verbose

# Uso de cofre via CLI (HashiCorp Vault)
vault kv put secret/db user=app password=$(openssl rand -base64 32)
```

## Boas práticas
- Usar secret manager ou env vars injetadas no runtime, nunca segredos hardcoded.
- Adicionar scanners de segredos ao CI e ao pre-commit.
- Rotacionar segredos e remover do histórico quando vazarem (o commit continua no git).
- Aplicar menor privilégio e auditar acessos ao cofre.
- Distinguir ambientes: dev/staging/prod com segredos diferentes.

## Armadilhas comuns
- Commitar `.env` ou chaves "só de teste" — vazamento é vazamento.
- Remover o segredo do arquivo mas deixá-lo no histórico do git.
- Achar que `gitignore` protege segredos que já foram commitados.
- Compartilhar segredos por chat ou e-mail "uma única vez".
- Usar um único segredo para todos os serviços, ampliando o impacto de um vazamento.

## Relacionadas
- [[DevOps]]
- [[Env]]
- [[Credenciais]]
- [[Senhas]]
- [[Criptografia]]