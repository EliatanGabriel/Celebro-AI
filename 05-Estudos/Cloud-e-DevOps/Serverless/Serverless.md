---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Serverless

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Modelo de computação em nuvem onde o provedor gerencia servidores e escala automaticamente, cobrando apenas por execução/recurso usado, permitindo foco total no código.

## Conceitos-chave
- **Sem gerenciamento de servidor:** o provedor provisiona, escala e cuida da infraestrutura.
- **Pay-per-use:** cobrança por invocações, tempo de execução e recursos consumidos (não por capacidade ociosa).
- **FaaS:** funções sob demanda ([[Lambda]], Cloud Functions, Azure Functions).
- **BaaS (Backend as a Service):** serviços gerenciados (Auth, DB, storage) usados diretamente do front.
- **Escala automática:** de zero a milhões de requisições sem intervenção manual.
- **Event-driven:** arquitetura reativa a eventos (API, fila, storage, schedule).
- **Limites:** timeouts, concorrência, cold start e estado efêmero definem o design.
- **Custo de cold starts:** latência da primeira execução após período de inatividade.

## Exemplos

Arquitetura serverless na AWS:

```text
S3 (upload) → Lambda (processa) → DynamoDB (persiste)
SQS (fila)  → Lambda (worker)   → SNS (notifica)
```

Função acionada por upload no S3:

```python
import boto3

def handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]
    print(f"processando {key} de {bucket}")
```

## Boas práticas
- Projetar funções stateless e idempotentes (eventos podem se repetir).
- Usar filas (SQS/SNS) para desacoplar e tolerar picos.
- Configurar timeouts, memória e concurrency conforme a carga real.
- Separar processamento pesado em funções dedicadas com limites claros.
- Monitorar invocações, erros, latência e custo por função.

## Armadilhas comuns
- Assumir que serverless = sem limites: há timeouts, cold starts e quotas de concorrência.
- Lógica de longa duração dentro da função (estourar o timeout).
- Recursão sem proteção que gera custo infinito.
- Manter estado local (temperatura, cache em memória) que some entre invocações.
- Migrar tudo para serverless sem avaliar custo de cold start e egress.

## Relacionadas
- [[Lambda]]
- [[AWS]]
- [[Microservicos]]
- [[GCP]]