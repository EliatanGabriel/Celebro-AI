---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Alerting

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Mecanismo que dispara notificações automáticas quando métricas ou logs atingem limites predefinidos, permitindo reação proativa a incidentes.

## Conceitos-chave
- **Alerta (alert):** evento disparado quando uma condição avaliada sobre uma métrica (ex.: CPU > 80%) se mantém verdadeira por um período de tempo.
- **Condição e limite (threshold):** regra que combina uma métrica, um operador (`>`, `<`, `=`) e um valor de referência.
- **Janela de avaliação:** período sobre o qual a métrica é agregada (ex.: média em 5 minutos) para evitar ruído.
- **Severidade:** classificação do impacto (crítico, warning, info) que define prioridade e rota de notificação.
- **Escalonamento (escalation):** encadeamento automático que promove o alerta a níveis superiores (página, gestor, pager) quando não é reconhecido.
- **Silenciamento/supressão:** regras para pausar alertas durante janelas de manutenção conhecidas.

## Exemplos

Regra de alerta no Prometheus:

```yaml
groups:
  - name: infra
    rules:
      - alert: HighCPUUsage
        expr: avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) < 0.2
        for: 10m
        labels:
          severity: critical
        annotations:
          summary: "CPU alta na instância {{ $labels.instance }}"
```

Alerta com AWS CloudWatch:

```bash
aws cloudwatch put-metric-alarm \
  --alarm-name cpu-high \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 \
  --alarm-actions arn:aws:sns:us-east-1:123456789012:alerts
```

## Boas práticas
- Alertar sobre sintomas de usuário (latência, erro), não apenas sobre métricas internas sem contexto.
- Definir `for` (duração) para evitar alertas por picos transitórios.
- Cada alerta deve ter um runbook associado com ações de resposta.
- Revisar e podar alertas regularmente para evitar fadiga de alertas (alert fatigue).
- Usar escalonamento com horário de plantão e reconhecimento obrigatório.

## Armadilhas comuns
- Alertas "não acionam" por limites mal calibrados ou janela de avaliação grande demais.
- Excesso de alertas ruidosos que levam a equipes a ignorar notificações.
- Alertar por métrica sem unidade ou sem baseline — sempre ancorar em valor real de operação.
- Esquecer de silenciar em janelas de manutenção, gerando páginas falsas.
- Confundir alerta com observação: alerta deve exigir ação, não ser apenas status.

## Relacionadas
- [[Monitoring]]
- [[Observability]]
- [[Logging]]
- [[DevOps]]