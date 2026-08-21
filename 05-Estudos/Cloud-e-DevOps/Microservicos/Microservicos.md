---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Microservicos

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Arquitetura que divide a aplicação em serviços pequenos, independentes e fracamente acoplados, cada um com seu ciclo de vida, escala e deploy próprios, comunicando-se via APIs.

## Conceitos-chave
- **Serviço independente:** cada microserviço tem seu próprio banco de dados, código e equipe.
- **Comunicação via API:** integração por HTTP/REST, gRPC ou mensageria (SQS, Kafka).
- **Escala isolada:** escalar apenas o serviço com demanda, sem escalar o monólito inteiro.
- **Failover e resiliência:** falha em um serviço não derruba o todo (com circuit breakers e retries).
- **Deploy independente:** releases frequentes e menores por serviço.
- **Observabilidade distribuída:** necessário tracing e logging com correlação entre serviços.
- **Descoberta de serviço e load balancing:** registros dinâmicos (Kubernetes Services, Consul).
- **Complexidade de rede e dados:** consistência eventual, transações distribuídas, latência de rede.

## Exemplos

Comunicação síncrona entre serviços (REST):

```text
Cliente → API Gateway → Serviço Pedidos (POST /pedidos)
                             └→ Serviço Pagamentos (POST /pagamentos)
                             └→ Serviço Estoque (PATCH /estoque)
```

Padrão assíncrono com fila:

```yaml
Pedidos -> [SQS fila-de-pedidos] -> Worker de Envio (consome e processa)
```

## Boas práticas
- Definir limites de domínio claros (Domain-Driven Design) antes de fragmentar.
- Cada serviço com banco próprio (database per service) — sem tabela compartilhada.
- Tornar a comunicação tolerante a falhas (timeouts, retries, circuit breaker, idempotência).
- Manter contratos de API versionados e estáveis.
- Investir em observabilidade e deploys contínuos desde o início.

## Armadilhas comuns
- Microserviços precoces sem necessidade: monólito modular costuma ser melhor primeiro.
- Serviços "distributed monolith": banco compartilhado e acoplamento forte disfarçado.
- Ignorar consistência eventual e tratar tudo como transação síncrona.
- Comunicar serviços em cadeia síncrona longa (chatty), amplificando latência e falhas.
- Subestimar custo operacional (K8s, observabilidade, redes, múltiplos deploys).

## Relacionadas
- [[Monolitos]]
- [[Kubernetes]]
- [[Serverless]]
- [[Observability]]