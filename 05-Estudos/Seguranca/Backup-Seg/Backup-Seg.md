---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Backup-Seg

#area/estudos #estudos/seguranca #conceito

**Resumo:** Estratégia de cópias redundantes e recuperáveis dos dados, essencial para resiliência contra perda acidental, desastres e ransomware.

## Conceitos-chave
- **Regra 3-2-1:** 3 cópias, em 2 mídias diferentes, 1 off-site.
- **Off-site / off-line:** cópias fora do ambiente e fora da rede reduzem exposição a ransomware.
- **RPO e RTO:** quanto dado se pode perder (Recovery Point) e quanto tempo até recuperar (Recovery Time).
- **Backup criptografado:** protege dados em repouso; a chave precisa estar acessível na recuperação.
- **Teste de restore:** backup que nunca é restaurado não tem valor garantido.
- **Imutabilidade:** repositórios append-only/imutáveis impedem que malware apague ou criptografe os backups.

## Exemplos
```bash
# Cópia incremental com rsync (exemplo conceitual)
rsync -a --delete /dados /backup/remoto/

# Restore de um snapshot
restic restore latest --target /restauracao
```

## Boas práticas
- Automatizar backups e monitorar falhas com alertas.
- Testar restauração periodicamente (mensal, ao menos).
- Manter uma cópia imutável ou desconectada para cenários de ransomware.
- Definir retenção alinhada a requisitos legais e de auditoria.
- Proteger as credenciais de acesso ao backup com o mesmo rigor dos demais segredos.

## Armadilhas comuns
- Backups na mesma rede/infra que o sistema original, eliminados junto no incidente.
- Nunca testar restores e descobrir dados corrompidos na hora da crise.
- Criptografar sem documentar/guardar a chave de recuperação.
- Confundir replicação (espelho, propaga corrupção) com backup (versões recuperáveis).

## Relacionadas
- [[Ransomware]]
- [[Dados]]
- [[Criptografia]]