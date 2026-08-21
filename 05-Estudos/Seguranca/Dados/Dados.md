---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Dados

#area/estudos #estudos/seguranca #conceito

**Resumo:** Informações processadas e armazenadas por sistemas, cuja confidencialidade, integridade e disponibilidade são protegidas por criptografia, acesso controlado e backups.

## Conceitos-chave
- **Tríade CIA:** Confidencialidade (quem lê), Integridade (não alterado) e Disponibilidade (acessível quando preciso).
- **Classificação de dados:** público, interno, confidencial, restrito — define o nível de proteção.
- **Dados pessoais:** dados identificáveis de pessoas físicas são regulados ([[GDPR]], LGPD).
- **Ciclo de vida:** coleta, armazenamento, uso, compartilhamento, retenção e descarte seguro.
- **Criptografia em repouso/trânsito:** protege contra acesso não autorizado em disco e na rede (ver [[Criptografia]]).
- **Governança de dados:** políticas de acesso, retenção, responsabilidade e conformidade.

## Exemplos
```yaml
# Metadados de classificação (exemplo conceitual)
dados:
  nome: relatorio-clientes
  classificacao: confidencial
  criptografia: AES-256
  retencao: 5 anos
  acessos: ["time-dados", "auditoria"]
```

## Boas práticas
- Classificar dados antes de definir controles de proteção.
- Aplicar controle de acesso baseado em papel (ver [[RBAC]]) e menor privilégio.
- Cifrar dados sensíveis e definir retenção e descarte com segurança.
- Fazer backups testados (ver [[Backup-Seg]]) para garantir disponibilidade.
- Logar e auditar acessos a dados sensíveis.

## Armadilhas comuns
- Tratar todos os dados igualmente: superproteger o trivial e expor o crítico.
- Acumular dados pessoais sem necessidade — minimização é um requisito de privacidade.
- Confundir pseudonimização com anonimização: a primeira ainda é dado pessoal.
- Vazamentos por cópias não controladas (exports, planilhas, backups de dev).

## Relacionadas
- [[GDPR]]
- [[Privacidade]]
- [[Backup-Seg]]
- [[Criptografia]]