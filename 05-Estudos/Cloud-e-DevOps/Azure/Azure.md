---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Azure

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Nuvem pública da Microsoft, com forte integração com ecossistema Windows e soluções enterprise, incluindo Active Directory e Azure DevOps.

## Conceitos-chave
- **Azure Resource Manager (ARM):** camada de gerenciamento que organiza recursos em grupos e aplica modelos declarativos (ARM templates).
- **Entra ID (antigo Azure AD):** serviço de identidade e acesso usado por apps enterprise e SSO.
- **Compute:** Virtual Machines, Azure App Service (PaaS), Azure Functions (serverless), AKS (Kubernetes).
- **Armazenamento:** Blob Storage (objetos), Azure SQL Database, Cosmos DB (NoSQL).
- **Modelo híbrido:** conecta datacenter on-premises à nuvem via ExpressRoute ou VPN, com Azure Arc para governança.
- **Regiões e Availability Zones:** redundância geográfica e zonas isoladas dentro da região.
- **Azure DevOps:** suíte de CI/CD com Azure Pipelines, Repos, Boards e Artifacts.

## Exemplos

Criar um grupo de recursos e uma Storage Account com a CLI:

```bash
az group create --name rg-prod --location eastus
az storage account create \
  --name minhaestore123 \
  --resource-group rg-prod \
  --sku Standard_LRS \
  --kind StorageV2
```

Pipeline YAML no Azure DevOps:

```yaml
trigger:
  - main

pool:
  vmImage: ubuntu-latest

steps:
  - task: UseDotNet@2
    inputs:
      packageType: 'sdk'
      version: '8.x'

  - script: dotnet build --configuration Release
    displayName: 'Build'
```

## Boas práticas
- Usar RBAC (role-based access control) com o princípio do menor privilégio.
- Padronizar criação de recursos com ARM/Bicep/Terraform para reprodutibilidade.
- Separar assinaturas por ambiente (dev, staging, prod) para isolamento de custo e acesso.
- Aproveitar Azure Policy para impor compliance e governança.
- Integrar identidades via Entra ID em vez de credenciais espalhadas.

## Armadilhas comuns
- Assumir que tudo no Azure é Windows; a maioria dos serviços roda Linux normalmente.
- Misturar conceitos de Azure AD (antigo) com o novo Entra ID em documentação e scripts.
- Deixar Storage Accounts com acesso público ou sem network rules.
- Escalar Vertical VMs por reflexo, esquecendo PaaS/serverless como alternativa.
- Custos surpresa por recursos provisionados em regiões caras ou sem autoshutdown.

## Relacionadas
- [[AWS]]
- [[GCP]]
- [[IaC]]
- [[CI-CD-Conceito]]