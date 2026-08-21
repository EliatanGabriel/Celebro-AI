---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# RDS

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Amazon Relational Database Service: serviço gerenciado de banco de dados relacional da AWS que automatiza backup, patch, replicação e failover.

## Conceitos-chave
- **Multi-engine:** suporta PostgreSQL, MySQL, MariaDB, SQL Server e Oracle; Aurora é o engine proprietário da AWS.
- **Gerenciado:** AWS cuida de instalação, patches, backups automáticos e storage; você gerencia schema e consultas.
- **Backup automático e snapshots:** retenção configurável, point-in-time recovery e restauração sob demanda.
- **Multi-AZ:** réplica síncrona em outra AZ para failover automático (alta disponibilidade).
- **Read replicas:** réplicas assíncronas para escala de leitura e offload de tráfego.
- **Segurança:** VPC, Security Groups, criptografia (KMS), SSL/TLS e IAM auth.
- **Escala:** alterar classe de instância (vertical) e storage com pouco downtime.

## Exemplos

Criar uma instância RDS PostgreSQL:

```bash
aws rds create-db-instance \
  --db-instance-identifier app-db \
  --db-instance-class db.t3.medium \
  --engine postgres \
  --engine-version 16.3 \
  --allocated-storage 100 \
  --master-username admin \
  --master-user-password 'SenhaForte!' \
  --multi-az \
  --backup-retention-period 7
```

Conectar:

```bash
psql -h app-db.c7abc123.us-east-1.rds.amazonaws.com -U admin -d postgres
```

## Boas práticas
- Habilitar Multi-AZ para produção e read replicas para tráfego de leitura.
- Configurar retenção de backup alinhada ao RPO desejado e testar restores.
- Usar Security Group restrito ao app (porta 5432) e SSL obrigatório.
- Monitorar conexões e storage com CloudWatch para planejar escala.
- Gerenciar schema com migrations versionadas ([[Migrations]]).

## Armadilhas comuns
- Acessar RDS com credenciais mestre embutidas no código — usar IAM auth/secrets.
- Esquecer de testar failover e point-in-time restore (só acredita no que testou).
- Confundir Multi-AZ (HA) com read replicas (escala de leitura).
- Custo de instância grande parada sem uso; pausar apenas em dev (serverless).
- Ignorar o limite de conexões e estourar `max_connections`.

## Relacionadas
- [[AWS]]
- [[VPC]]
- [[Monitoring]]