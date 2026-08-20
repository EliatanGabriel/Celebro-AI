---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Terraform

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Ferramenta de IaC declarativa (HashiCorp) que provisiona recursos multi-cloud via providers, com state para planejar e aplicar mudanças de forma segura.

## Conceitos-chave
- **IaC declarativo:** descreve o estado desejado; o Terraform calcula o diff e aplica.
- **Provider:** plugin que conecta a um provedor (aws, azurerm, google, kubernetes, github).
- **Resource e data source:** recursos gerenciados (`aws_instance`) e dados lidos (`data`).
- **State (`.tfstate`):** registro do mapeamento real de recursos; base para `plan`/`apply`.
- **HCL:** linguagem de configuração do Terraform (`.tf`), com módulos, variables e outputs.
- **Módulos:** blocos parametrizados reutilizáveis e versionáveis (registry).
- **Backend:** onde o state é armazenado (local, S3 + DynamoDB lock, Terraform Cloud).
- **Plan/Apply:** `plan` mostra mudanças sem aplicar; `apply` executa (com `--auto-approve` opcional).
- **Drift e imports:** divergência entre state e realidade; `terraform import` reconcilia.

## Exemplos

Recurso EC2 + security group:

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "web" {
  name = "web-sg"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web" {
  ami                    = "ami-0abcdef1234567890"
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.web.id]
  tags = { Name = "web-server" }
}

output "public_ip" {
  value = aws_instance.web.public_ip
}
```

Fluxo de trabalho:

```bash
terraform init
terraform fmt && terraform validate
terraform plan -out=tfplan
terraform apply tfplan
terraform destroy
```

## Boas práticas
- Usar backend remoto com lock (S3 + DynamoDB) para o state; nunca versionar `.tfstate`.
- Revisar `plan` em PR e aplicar apenas com aprovação.
- Estruturar com módulos (network, compute, db) e reusar do registry.
- Pinvar versões do provider e módulos para reprodutibilidade.
- Usar workspaces ou separar diretórios/backends por ambiente.

## Armadilhas comuns
- State local ou no git (perde-se e expõe segredos do plano de infra).
- Dois operadores aplicando ao mesmo tempo sem lock, corrompendo o state.
- Recursos criados à mão que o apply "destrói" por drift — importar antes de gerenciar.
- Secrets em variáveis/função `sensitive` negligenciada ficando visíveis no plan.
- Confundir Terraform (provisiona infra) com Ansible (configura máquinas).

## Relacionadas
- [[IaC]]
- [[AWS]]
- [[GCP]]
- [[Azure]]
- [[DevOps]]