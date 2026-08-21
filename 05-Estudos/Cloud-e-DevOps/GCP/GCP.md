---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# GCP

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Google Cloud Platform: nuvem pública do Google, com Kubernetes nativo (GKE), forte em dados/análise (BigQuery) e ferramentas de AI/ML.

## Conceitos-chave
- **Projetos:** unidade organizacional que agrupa recursos, IAM e faturamento.
- **Compute Engine:** VMs (com MIGs para autoscaling), semelhantes ao EC2.
- **GKE (Google Kubernetes Engine):** Kubernetes gerenciado e nativo da plataforma.
- **Cloud Run:** container serverless (executa containers escalando para zero).
- **Cloud Functions:** FaaS equivalente ao Lambda.
- **BigQuery:** data warehouse serverless de análise massiva com SQL.
- **Cloud Storage:** armazenamento de objetos (buckets) com classes e lifecycle.
- **Regiões e zonas:** distribuição global com permissão de infraestrutura única e redes globais.

## Exemplos

Criar um bucket e uma VM:

```bash
gcloud storage buckets create gs://meu-bucket --location=us-central1
gcloud compute instances create minha-vm \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud
```

Deploy simples no Cloud Run:

```bash
gcloud run deploy minha-api \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```

## Boas práticas
- Organizar por projetos por ambiente (dev/prod) com IAM restrito por projeto.
- Preferir GKE Autopilot ou Cloud Run quando possível para reduzir operação.
- Usar labels e orçamentos (budgets) para controle de custo.
- Aproveitar o BigQuery para analytics e integrar com Dataflow/Dataform.
- Usar Service Accounts dedicados com escopos mínimos.

## Armadilhas comuns
- Deixar buckets públicos sem policy correta (acesso público por engano).
- Provisionar VMs quando Cloud Run/GKE seria suficiente e mais barato.
- Confundir projeto com pasta/organização na hierarquia do GCP.
- Não definir budget/alerts, gerando fatura inesperada.
- Ignorar a cobrança por egress (tráfego de saída), que pode ser significativa.

## Relacionadas
- [[AWS]]
- [[Azure]]
- [[Kubernetes]]
- [[Serverless]]