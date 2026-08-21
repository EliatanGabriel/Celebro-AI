---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Monitoring

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Coleta e visualização contínua de métricas e estado dos sistemas para acompanhar saúde, detectar degradação e basear decisões em dados.

## Conceitos-chave
- **Métricas:** valores numéricos com timestamp e labels (CPU, latência, taxa de erro, throughput).
- **Telemetria:** dados coletados periodicamente dos sistemas (agent/exporters).
- **Dashboards:** visualização agregada de métricas para monitorar saúde em tempo real.
- **Alertas:** regras sobre métricas que geram notificações ([[Alerting]]).
- **Red/Use/RED e golden signals:** latência, tráfego, erros, saturação — métricas-chave de usuário.
- **Níveis de monitoramento:** infraestrutura, aplicação, negócio e experiência do usuário.
- **Push vs pull:** Prometheus puxa (scrape); CloudWatch recebe push de métricas.

## Exemplos

Métricas com Prometheus:

```yaml
scrape_configs:
  - job_name: "app"
    metrics_path: /metrics
    static_configs:
      - targets: ["localhost:8080"]
```

Consulta de SLO de disponibilidade:

```text
sum(rate(http_requests_total{status=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
```

Config de alerta no Prometheus:

```yaml
- alert: HighErrorRate
  expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
  for: 5m
```

## Boas práticas
- Monitorar pelo que importa ao usuário (latência, erros, disponibilidade), não só CPU/disco.
- Basear dashboards em métricas com labels consistentes e unidades claras.
- Definir SLOs e SLIs para ancorar alertas e prioridades.
- Unificar agentes de coleta (ex.: Prometheus stack) para reduzir duplicação.
- Revisar dashboards periodicamente para remover métricas mortas.

## Armadilhas comuns
- Coletar tudo e não saber o que olhar — falta de foco em sinais de usuário.
- Dashboard cheio de gráficos sem contexto que ninguém lê.
- Alertas sem `for` que disparam em picos transitórios ([[Alerting]]).
- Confundir monitoring (saber o estado) com observability (descobrir o porquê).
- Métricas com cardinalidade alta demais explodindo o storage (labels dinâmicos).

## Relacionadas
- [[Observability]]
- [[Logging]]
- [[Alerting]]
- [[DevOps]]