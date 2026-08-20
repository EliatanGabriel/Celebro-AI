---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# IaC

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Infraestrutura como Código: prática de definir e gerenciar infraestrutura por código versionável e revisável, garantindo reprodutibilidade e consistência.

## Conceitos-chave
- **Declarativo vs imperativo:** declarativo (Terraform, CloudFormation) descreve o estado desejado; imperativo (scripts) descreve passos.
- **Provisionamento vs configuração:** Terraform cria recursos; Ansible/Chef configuram máquinas existentes.
- **Versionável e revisável:** infra fica no git, com PRs, review e histórico (auditoria).
- **Reprodutível:** o mesmo código gera o mesmo ambiente (dev = staging = prod).
- **State:** registro do estado real dos recursos (Terraform state) para planejar mudanças.
- **Módulos e reuso:** blocos parametrizados para padronizar e evitar duplicação.
- **Drift:** diferença entre o código e o estado real causada por mudanças manuais.

## Exemplos

Terraform declarativo criando um bucket S3:

```hcl
resource "aws_s3_bucket" "app" {
  bucket = "app-prod-bucket"
  tags = { Environment = "prod" }
}

resource "aws_s3_bucket_versioning" "app" {
  bucket = aws_s3_bucket.app.id
  versioning_configuration {
    status = "Enabled"
  }
}
```

Ciclo de trabalho:

```bash
terraform init
terraform plan   # mostra o que vai mudar
terraform apply  # aplica
terraform destroy
```

## Boas práticas
- Nunca aplicar mudanças sem revisão em PR e sem `plan` validado.
- Armazenar o state em backend remoto (S3 + lock/DynamoDB) e versioná-lo com segurança.
- Usar módulos para padrões reutilizáveis e pinar versões dos providers.
- Tratar infra como parte do repositório da aplicação ou em repo dedicado com review.
- Executar IaC dentro da pipeline (plan + apply automático) com gates.

## Armadilhas comuns
- Confundir Terraform (provisiona) com Ansible (configura) — papéis complementares, não intercambiáveis.
- Manter state local ou em git (corrompe/expõe segredos).
- Mudanças manuais no console que causam drift e sobrescritas pelo apply.
- Secrets no código/state em texto puro — usar var e backend cifrado.
- `apply` automático sem `plan` revisado em ambientes críticos.

## Relacionadas
- [[Terraform]]
- [[Ansible]]
- [[DevOps]]
- [[Pipeline]]