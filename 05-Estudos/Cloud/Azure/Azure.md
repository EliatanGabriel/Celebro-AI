---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Microsoft Azure

#area/estudos #estudos/cloud #conceito #nuvem #azure #microsoft

**Resumo:** Plataforma de nuvem da Microsoft com serviços gerenciados para computação, armazenamento e integração corporativa.

## Conceitos-chave
- **VMs:** máquinas virtuais equivalentes ao EC2, com diversas famílias e tamanhos.
- **Blob Storage:** armazenamento de objetos para arquivos, mídia e backups, com camadas de acesso.
- **Functions:** execução serverless de funções, cobrada por execução.
- **Entra ID (Azure AD):** diretório e gerenciamento de identidade e acesso corporativo.
- **App Services:** hospedagem gerenciada de aplicações web com escala automática.
- **Azure DevOps:** conjunto de ferramentas para CI/CD, repositórios e gerenciamento de trabalho.

## Exemplos
```bash
# Criar um grupo de recursos
az group create --name meu-grupo --location brazilsouth

# Criar uma VM Linux
az vm create \
  --resource-group meu-grupo \
  --name minha-vm \
  --image Ubuntu2204 \
  --admin-username eliatan \
  --generate-ssh-keys

# Listar containers de blob storage
az storage container list --account-name minha-conta
```

## Boas práticas
- Usar Entra ID com RBAC e privilégios mínimos para acesso aos recursos.
- Definir políticas de custo e limites de gasto por assinatura.
- Preferir serviços gerenciados (App Services, Functions) a VMs quando possível.
- Distribuir cargas entre regiões e zonas de disponibilidade.

## Armadilhas comuns
- Configurar infraestrutura apenas pelo portal, sem versionar a automação.
- Ignorar as camadas de acesso do Blob Storage, pagando caro por dados pouco acessados.
- Confundir a nomenclatura dos serviços entre Azure e AWS, que usam nomes diferentes para conceitos equivalentes.

## Relacionadas
- [[AWS]]
- [[Serverless]]