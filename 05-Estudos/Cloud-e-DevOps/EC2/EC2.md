---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# EC2

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Amazon Elastic Compute Cloud (EC2): serviço de máquinas virtuais sob demanda na AWS, com controle de AMIs, tipos de instância, armazenamento EBS e escala elástica.

## Conceitos-chave
- **Instância:** máquina virtual criada a partir de uma AMI, com tipo definindo CPU/memória/GPU.
- **AMI (Amazon Machine Image):** template do sistema operacional + configurações; pode ser pública, da AWS ou customizada (snapshot).
- **Tipos de instância:** famílias (ex.: t3 de uso geral, m5 memória, c5 compute, r5 RAM, g5 GPU) com opções on-demand, reserved, spot.
- **EBS (Elastic Block Store):** volume de disco persistente anexado à instância; suporta snapshots.
- **Key pair:** par de chaves SSH usado no acesso inicial à instância.
- **Security Group:** firewall virtual no nível da instância (regras de entrada/saída por protocolo/porta/IP).
- **Elastic IP:** IP público estático associável à instância.
- **Auto Scaling:** grupo que adiciona/remove instâncias por métricas (CPU, tráfego) com health checks.

## Exemplos

Conectar e gerenciar com CLI:

```bash
ssh -i minha-chave.pem ec2-user@<ip-publico>
aws ec2 describe-instances --query 'Reservations[].Instances[].InstanceId'
aws ec2 stop-instances --instance-ids i-0123456789abcdef0
```

Criar um volume EBS e anexar:

```bash
aws ec2 create-volume --size 50 --availability-zone us-east-1a --volume-type gp3
aws ec2 attach-volume --volume-id vol-0123456789 --instance-id i-0123456789abcdef0 --device /dev/sdf
```

## Boas práticas
- Usar IAM role na instância em vez de access keys embutidas.
- Distribuir instâncias entre AZs e usar Auto Scaling para resiliência.
- Fazer snapshots regulares dos volumes EBS e usar AMIs versionadas para deploys.
- Escolher instância por demanda real (right-sizing) e considerar Spot/Reserved.
- Restringir Security Groups ao mínimo necessário (princípio do menor privilégio).

## Armadilhas comuns
- Esquecer instâncias ligadas (custo recorrente) — usar tags e autoshutdown.
- Portas 22/3389 abertas para 0.0.0.0/0, expondo a máquina à internet.
- Deletar a instância junto com o volume sem snapshot, perdendo dados.
- Escalar verticalmente por reflexo quando a arquitetura permitir escala horizontal.
- Confundir stop (mantém EBS, cobra storage) com terminate (destrói a instância).

## Relacionadas
- [[AWS]]
- [[VPC]]
- [[Servidores]]