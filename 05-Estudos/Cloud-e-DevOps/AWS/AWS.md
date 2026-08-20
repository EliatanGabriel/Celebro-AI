---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# AWS

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Amazon Web Services, a maior nuvem pública do mercado, com dezenas de serviços de computação, armazenamento, banco de dados e redes, cobrados por uso.

## Conceitos-chave
- **Compute:** EC2 (VMs), Lambda (serverless/FaaS), ECS e EKS (containers), Lightsail (simples).
- **Storage:** S3 (objetos), EBS (volumes de bloco), EFS (arquivos), Glacier (arquivamento).
- **Banco de dados:** RDS (relacional gerenciado), DynamoDB (NoSQL), Aurora, ElastiCache.
- **Redes e entrega:** VPC, CloudFront (CDN), Route 53 (DNS), Elastic Load Balancing.
- **Regiões e Availability Zones (AZ):** regiões são áreas geográficas; cada uma tem múltiplas AZs isoladas para alta disponibilidade.
- **Modelo pay-as-you-go:** cobrança por segundo/hora de uso, com escala elástica.
- **IAM (Identity and Access Management):** controle de acesso via roles, policies e users.

## Exemplos

Criar uma instância EC2:

```bash
aws ec2 run-instances \
  --image-id ami-0abcdef1234567890 \
  --instance-type t3.micro \
  --key-name minha-chave \
  --security-group-ids sg-0123456789 \
  --subnet-id subnet-0123456789
```

Upload de objeto ao S3:

```bash
aws s3 cp app.zip s3://meu-bucket/app.zip
aws s3 ls s3://meu-bucket --recursive
```

## Boas práticas
- Usar IAM roles em instâncias/Lambda em vez de guardar access keys.
- Distribuir workloads entre múltiplas AZs para tolerância a falhas.
- Usar tags em todos os recursos para organização e controle de custo.
- Habilitar versionamento e encryption nos buckets S3.
- Preferir serviços gerenciados (RDS, Lambda) para reduzir operação manual.

## Armadilhas comuns
- Deixar recursos sem uso rodando e acumular custos (VMs esquecidas, IPs elásticos).
- Buckets S3 públicos por engano, causando vazamento de dados.
- Colocar tudo na mesma AZ, anulando a alta disponibilidade.
- Confundir serviço regional com global (IAM, CloudFront e Route 53 são globais).
- Ignorar limites de conta (service quotas) que causam falhas de provisionamento.

## Relacionadas
- [[EC2]]
- [[S3]]
- [[RDS]]
- [[Lambda]]
- [[VPC]]
- [[CloudFront]]