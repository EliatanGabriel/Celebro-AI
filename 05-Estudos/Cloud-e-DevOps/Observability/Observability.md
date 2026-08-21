---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Observability

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Capacidade de entender e explicar o comportamento de um sistema a partir de telemetria externa, combinando métricas, logs e traces (os "três pilares").

## Conceitos-chave
- **Três pilares:** métricas (estado agregado), logs (eventos) e traces (caminho de uma requisição).
- **Trace:** sequência de spans que rastreia uma requisição entre serviços (tracing distribuído).
- **Span:** unidade de trabalho dentro de um trace (duração, atributos, contexto).
- **Correlação:** `trace_id`/`request_id` propagado entre serviços liga métricas, logs e traces.
- **Contexto (context propagation):** headers (W3C traceparent) que carregam o ID entre serviços.
- **Descobrir o "porquê" (unknown unknowns):** observar permite responder perguntas não previstas antecipadamente.
- **Ferramentas:** Prometheus/Grafana (métricas), Loki/ELK (logs), Jaeger/Tempo/OTel (traces).

## Exemplos

Instrumentação com OpenTelemetry (Python):

```python
from opentelemetry import trace
tracer = trace.get_tracer("api")

with tracer.start_as_current_span("processar_pedido") as span:
    span.set_attribute("pedido.id", pedido_id)
    resp = chamar_servico_pagamentos(pedido_id)
```

Contexto propagado entre serviços:

```text
GET /pedidos/123
├── api-gateway       span 500ms
└── pedidos-service   span 320ms
    └── pagamentos    span 200ms  ← mesmo trace_id
```

## Boas práticas
- Instrumentar com OpenTelemetry padrão aberto para evitar vendor lock-in.
- Propagar `trace_id` em todos os logs e métricas para correlação.
- Criar métricas RED/USE e traces de fluxos críticos (pagamento, login).
- Unificar coletores e pipelines de telemetria para custo e consistência.
- Exercitar incidentes com observability para validar que dá para diagnosticar.

## Armadilhas comuns
- Confundir observability com monitoring: monitoring diz o que está quebrado; observability explica por quê.
- Instrumentar tudo sem correlação (logs, métricas e traces desconectados).
- Coletar sem amostragem (sampling) e explodir o custo de storage.
- Sempre só alertar, sem dashboards de investigação e query paths prontos.
- Depurar produção só por logs sem traces — caminho invisível entre serviços.

## Relacionadas
- [[Monitoring]]
- [[Logging]]
- [[Alerting]]
- [[Microservicos]]
- [[DevOps]]