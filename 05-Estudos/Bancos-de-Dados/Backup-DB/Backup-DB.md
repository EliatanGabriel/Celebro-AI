---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Backup-DB

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Estratégias para proteger dados contra perda, corrupção ou erro humano e garantir recuperação (restore) em caso de falha.

## Conceitos-chave
- **Backup full:** cópia completa de todos os dados; é a base para os demais tipos e o mais demorado.
- **Backup incremental:** copia apenas as mudanças desde o último backup (full ou incremental); é rápido e pequeno, mas o restore depende de toda a cadeia.
- **Backup diferencial:** copia as mudanças desde o último full; meio-termo entre full e incremental.
- **PITR (Point-in-Time Recovery):** permite restaurar até um instante específico usando logs de transação (ex.: WAL no PostgreSQL), limitando a perda a minutos/segundos.
- **RPO e RTO:** RPO define quanto dado se pode perder e RTO o tempo máximo de indisponibilidade; ambos orientam a frequência e o tipo de backup.
- **Regra 3-2-1:** ter 3 cópias, em 2 mídias diferentes, com 1 cópia off-site.
- **Restore testado:** um backup sem restore validado não é backup de verdade.

## Exemplos

```bash
# Backup lógico (PostgreSQL)
pg_dump -U postgres -h localhost mydb > mydb.sql
psql -U postgres -h localhost mydb < mydb.sql

# Backup físico base para PITR (PostgreSQL)
pg_basebackup -U replicator -D /backup/base -X stream
```

```bash
# MySQL
mysqldump -u root -p mydb > mydb.sql
mysql -u root -p mydb < mydb.sql
```

## Boas práticas
- Automatizar os backups e monitorar o resultado de cada execução.
- Testar o restore periodicamente em um ambiente separado.
- Definir RPO/RTO antes de escolher frequência, tipo e local dos backups.
- Criptografar backups e proteger credenciais usadas no processo.
- Guardar cópias off-site (nuvem ou outro datacenter).

## Armadilhas comuns
- Fazer apenas backup incremental sem um full anterior válido.
- Assumir que gerar backup é o mesmo que conseguir restaurar.
- Armazenar backups no mesmo disco/servidor do banco de dados.
- Ignorar logs/WAL e perder a capacidade de PITR.
- Não monitorar falhas silenciosas de backup.

## Relacionadas
- [[Bancos-de-Dados]]
- [[Replication]]