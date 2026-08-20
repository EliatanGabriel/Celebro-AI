---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Replication

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Cópia contínua de dados entre servidores (réplicas) para garantir alta disponibilidade, failover automático e escalar leituras.

## Conceitos-chave
- **Master-slave / primary-replica:** o nó primário recebe escritas; as réplicas copiam as mudanças.
- **Read replicas:** consultas distribuídas entre réplicas para escalar leituras.
- **Failover:** promoção de uma réplica quando o primário falha.
- **Consistência eventual:** replicação assíncrona — réplicas podem estar levemente atrasadas.
- **Síncrono vs assíncrono:** assíncrono tem menor latência, mas pode perder dados recentes; síncrono prioriza durabilidade.
- **Replicação lógica vs física:** lógica replica mudanças a nível de dados; física replica os arquivos (streaming).
- **Lag de replicação:** atraso entre o primário e a réplica, monitorado para detectar problemas.

## Exemplos

```bash
# Primário — postgresql.conf
wal_level = replica
max_wal_senders = 10

# Réplica — via pg_basebackup com -R
pg_basebackup -h primario -U replicador -D /var/lib/postgresql/data -R
# standby.signal presente inicia como réplica; primary_conninfo aponta para o primário
```

## Boas práticas
- Definir RPO: replicação assíncrona pode perder escritas recentes; síncrona protege mais.
- Testar failover regularmente, não apenas no momento da falha.
- Direcionar leituras às réplicas; nunca escrever nelas.
- Monitorar o lag de replicação como alerta proativo.

## Armadilhas comuns
- Assumir consistência imediata em réplicas assíncronas.
- Escrever diretamente em uma réplica, quebrando a consistência.
- Não testar o failover até precisar dele em produção.
- Confundir replicação com backup — a réplica não substitui um ponto de restauração.

## Relacionadas
- [[Sharding]]
- [[Bancos-de-Dados]]
- [[Backup-DB]]