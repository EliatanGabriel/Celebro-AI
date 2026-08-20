---
type: concept
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# AWS

#area/estudos #cloud #conceito #nuvem #aws #infraestrutura

**Resumo:** Serviços da Amazon Web Services para computação, armazenamento e escala sob demanda, com faturamento por uso e alcance global.

## Conceitos-chave
- **EC2:** máquinas virtuais (instâncias) com SO e hardware definidos por tipo de instância.
- **S3:** armazenamento de objetos com alta durabilidade, usado para arquivos, backups e estáticos de sites.
- **Lambda:** execução de funções sem servidor, cobrada por invocação e tempo de execução.
- **RDS:** banco de dados relacional gerenciado (PostgreSQL, MySQL e outros) com backups automáticos.
- **VPC:** rede virtual privada que isola os recursos e controla o tráfego da conta.
- **Regiões e zonas de disponibilidade:** distribuição geográfica dos datacenters para latência e alta disponibilidade.

## Exemplos
```bash
# Criar uma instância EC2 via CLI
aws ec2 run-instances \
  --image-id ami-0abcdef1234567890 \
  --instance-type t3.micro \
  --key-name minha-chave

# Listar objetos de um bucket S3
aws s3 ls s3://meu-bucket/

# Invocar uma função Lambda
aws lambda invoke --function-name minha-funcao saida.json
```

## Boas práticas
- Usar IAM com privilégios mínimos em vez de credenciais de acesso raiz.
- Configurar alertas de orçamento (budgets) para evitar surpresas na fatura.
- Aproveitar instâncias reservadas ou spot para cargas previsíveis.
- Distribuir instâncias entre múltiplas zonas de disponibilidade para resiliência.

## Armadilhas comuns
- Versionar credenciais de acesso em código ou repositórios.
- Escolher uma região distante dos usuários, aumentando a latência.
- Usar VMs quando um serviço gerenciado (Lambda, RDS) atenderia com menos operação.
- Esquecer de terminar instâncias não utilizadas, gerando cobrança contínua.

## Relacionadas
- [[Serverless]]
- [[Azure]]
- [[EC2]]
- [[S3]]
- [[Lambda]]
- [[RDS]]