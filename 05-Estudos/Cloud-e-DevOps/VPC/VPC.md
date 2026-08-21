---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# VPC

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Amazon Virtual Private Cloud: rede privada e logicamente isolada dentro da AWS, onde se definem subnets, roteamento, gateways e regras de segurança.

## Conceitos-chave
- **VPC:** rede virtual com CIDR próprio (ex.: 10.0.0.0/16) associada a uma conta/região.
- **Subnets:** divisões do CIDR por AZ; públicas (com Internet Gateway) e privadas (sem acesso direto à internet).
- **Internet Gateway (IGW):** entrada/saída para a internet; NAT Gateway dá egress a subnets privadas.
- **Route table:** tabela de roteamento por subnet que define para onde vai o tráfego.
- **Security Groups:** firewall stateful no nível de instância/ENI (allow-only).
- **Network ACL:** firewall stateless no nível de subnet (allow + deny), filtro adicional.
- **Peering e Transit Gateway:** conexão entre VPCs e redes on-premises (também via VPN/ExpressRoute-style).
- **Endpoints (VPC Endpoints):** acesso privado a serviços AWS (S3, DynamoDB) sem passar pela internet.

## Exemplos

Layout típico:

```text
VPC 10.0.0.0/16
├── subnet pública  10.0.1.0/24 (AZ a) → IGW
├── subnet privada  10.0.2.0/24 (AZ a) → NAT → egress
├── subnet pública  10.0.3.0/24 (AZ b) → IGW
└── subnet privada  10.0.4.0/24 (AZ b) → NAT
```

Criar VPC e subnet com CLI:

```bash
aws ec2 create-vpc --cidr-block 10.0.0.0/16
aws ec2 create-subnet --vpc-id vpc-0123456789 --cidr-block 10.0.1.0/24 \
  --availability-zone us-east-1a
aws ec2 create-internet-gateway
aws ec2 attach-internet-gateway --vpc-id vpc-0123456789 --internet-gateway-id igw-0123
```

## Boas práticas
- Separar subnets públicas (front) de privadas (banco, worker) com roteamento mínimo.
- Restringir Security Groups ao mínimo (origem por SG/prefixo, não 0.0.0.0/0).
- Usar múltiplas AZs para alta disponibilidade da rede.
- Preferir VPC Endpoints para serviços AWS e evitar tráfego pela internet.
- Planejar CIDRs com folga (peering e crescimento futuro são difíceis de mudar).

## Armadilhas comuns
- Esquecer o Internet Gateway e perguntar por que a instância não tem internet.
- Security Group sem regra de saída ou NACL stateless bloqueando respostas.
- Subnet privada sem NAT tentando baixar pacotes — só funciona se o tráfego tiver rota.
- Usar IP público elástico em instância atrás de load balancer sem necessidade.
- Confundir Security Group (stateful, nível recurso) com Network ACL (stateless, nível subnet).

## Relacionadas
- [[AWS]]
- [[EC2]]
- [[Firewall]]