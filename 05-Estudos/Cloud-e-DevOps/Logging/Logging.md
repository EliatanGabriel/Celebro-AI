---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Logging

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Registro estruturado de eventos, erros e atividades dos sistemas, com níveis de severidade, centralização e análise para diagnóstico e auditoria.

## Conceitos-chave
- **Log:** registro textual/estruturado (JSON) de um evento com timestamp, nível e contexto.
- **Níveis de severidade:** DEBUG, INFO, WARN, ERROR, FATAL — usados para filtrar e alertar.
- **Log estruturado:** campos nomeados (JSON) que facilitam consulta e correlação automática.
- **Centralização:** agregação de logs de várias fontes em um ponto único (ELK, Loki, CloudWatch Logs).
- **Correlação:** identificar uma requisição em todos os serviços via `request_id`/`trace_id`.
- **Retenção e compliance:** políticas de arquivamento e exclusão por requisitos legais/auditoria.
- **Log de acesso vs aplicação:** access logs (servidor) e application logs (negócio/erros) têm propósitos distintos.

## Exemplos

Log estruturado em JSON (Node.js):

```json
{
  "level": "error",
  "timestamp": "2026-08-20T10:00:00Z",
  "service": "api-pagamentos",
  "request_id": "7f3c-9a21",
  "method": "POST",
  "path": "/v1/cobrancas",
  "status": 500,
  "message": "falha ao processar cobrança"
}
```

Centralizar com Docker + Grafana Loki:

```yaml
services:
  loki:
    image: grafana/loki:latest
    ports:
      - "3100:3100"
  promtail:
    image: grafana/promtail:latest
    volumes:
      - /var/lib/docker/containers:/var/lib/docker/containers
      - ./promtail.yml:/etc/promtail/config.yml
    command: -config.file=/etc/promtail/config.yml
```

## Boas práticas
- Estruturar logs como JSON com campos consistentes (timestamp, level, service, trace).
- Nunca logar dados sensíveis (senhas, tokens, CPF) — sanitizar e mascarar.
- Incluir `request_id`/`trace_id` em todas as mensagens para correlação.
- Escolher retenção adequada por tipo de log e custo.
- Centralizar e indexar logs; usar alertas baseados em padrões de erro.

## Armadilhas comuns
- Logging desestruturado (strings soltas) impossível de filtrar/agregar.
- Volume excessivo de DEBUG em produção inflando custo e ruído.
- Logar secrets/tokens acidentalmente, criando vulnerabilidade.
- Confiar em `console.log` como única fonte sem centralização.
- Confundir logging com monitoring: logs explicam eventos; métricas medem estado.

## Relacionadas
- [[Observability]]
- [[Monitoring]]
- [[Alerting]]
- [[DevOps]]