---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Env

#area/estudos #estudos/seguranca #conceito

**Resumo:** Variáveis de ambiente que separam configurações e segredos do código-fonte, permitindo comportamentos diferentes por ambiente (dev, staging, produção).

## Conceitos-chave
- **Configuração externa ao código:** valores como URLs, portas, chaves e flags ficam fora dos arquivos versionados.
- **Segredos em env vars:** tokens, chaves de API e senhas podem ser injetados no runtime sem ir para o repositório.
- **Isolamento por ambiente:** dev/test/prod leem conjuntos próprios de variáveis.
- **Gestão:** `.env` no desenvolvimento; secret managers/cofres em produção (ver [[Segredos]]).
- **Precedência:** variáveis de ambiente têm precedência sobre defaults; nenhum segredo deve ter default no código.

## Exemplos
```bash
# .env (NUNCA versionar)
DB_HOST=postgres.internal
DB_USER=app
DB_PASSWORD=supersecreto

# Uso no código
import os
conexao = conectar(host=os.environ["DB_HOST"], senha=os.environ["DB_PASSWORD"])
```

```bash
# Uso em linha de comando
DB_PASSWORD=abc123 npm run start
```

## Boas práticas
- Adicionar `.env` ao `.gitignore` e nunca commitar o arquivo real.
- Fornecer `.env.example` com placeholders para documentar as variáveis necessárias.
- Em produção, preferir cofres de segredos (AWS Secrets Manager, HashiCorp Vault) a env vars estáticas.
- Registrar e auditar quais variáveis cada serviço consome.
- Rotacionar segredos e não logar seus valores em erros e dumps.

## Armadilhas comuns
- Commitar `.env` com segredos reais — o histórico do git preserva o vazamento.
- Logar variáveis de ambiente inteiras em erros de depuração.
- Achar que env var é "segura" porque não está no código — ainda é um segredo a proteger.
- Versionar `.env.example` e depois alguém copiá-lo como `.env` com valores sensíveis.

## Relacionadas
- [[Segredos]]
- [[Credenciais]]
- [[Docker]]