---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Monitoramento

#area/trabalho #trabalho/ci-cd #conceito

**Resumo:** Observação de builds, deploys e aplicações em produção.

## Conceitos-chave
- Monitoramento cobre o pipeline (falhas de build/deploy) e a aplicação (disponibilidade, erros, performance).
- Métricas, logs e alertas permitem detectar problemas antes que afetem usuários.
- SLO/SLI definem metas de disponibilidade e performance acordadas.

## Exemplos
```yaml
# Prometheus: alerta de alta taxa de erro
groups:
  - name: app
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
        for: 5m
```
```bash
# CLI (kubectl)
kubectl get pods -w
kubectl logs deploy/app -f
```

## Boas práticas
- Definir alertas acionáveis, com runbook, sem ruído excessivo.
- Correlacionar métricas de aplicação com o histórico de deploys.
- Monitorar o próprio pipeline (duração, falhas, taxa de sucesso).
- Ter dashboards por camada: infra, aplicação, negócio.

## Armadilhas comuns
- Alertas em volume alto demais que ninguém acompanha (alert fatigue).
- Monitorar sem ter a linha de base, impossibilitando detectar anomalias.
- Não correlacionar erro em produção com o release que o introduziu.
- SLO definido sem processo de acompanhamento e revisão.

## Relacionadas
- [[Producao]]
- [[Rollback]]
- [[Deploy]]