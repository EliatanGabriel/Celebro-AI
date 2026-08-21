---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Queue

#area/estudos #estudos/backend #conceito

**Resumo:** Sistema de filas de mensagens que desacopla produtores e consumidores, permitindo processamento assíncrono de tarefas em background.

## Conceitos-chave
- **Modelo:** produtor enfileira mensagens; consumidores (workers) processam em paralelo; mensagens ficam em espera até serem consumidas.
- **Desacoplamento:** o request HTTP responde rápido e a tarefa pesada (email, imagem, PDF) roda depois, sem bloquear o usuário.
- **Propriedades:** FIFO (ordem), at-least-once (retry/duplicidade), at-most-once (perda) e exactly-once (difícil).
- **Dead letter queue (DLQ):** mensagens que falharam repetidamente vão para uma fila de inspeção manual.
- **Retry e backoff:** tentativas com espera crescente para lidar com falhas transitórias.
- **Ferramentas:** RabbitMQ, Apache Kafka, AWS SQS, BullMQ (Redis) e Celery (Python).
- **Quando usar:** envio de email/SMS, processamento de arquivos, jobs agendados, ingestão de eventos.

## Exemplos
```javascript
// BullMQ (Redis) em Node.js
import { Queue, Worker } from "bullmq";

const fila = new Queue("emails", { connection: { host: "localhost" } });

await fila.add("enviar-boas-vindas", { email: "ana@exemplo.com" });

const worker = new Worker("emails", async (job) => {
  await enviarEmail(job.data.email);
}, { connection: { host: "localhost" } });
```

```python
# Celery em Python (com Redis)
from celery import Celery

app = Celery("tarefas", broker="redis://localhost:6379/0")

@app.task
def redimensionar_imagem(path):
    # processamento pesado em background
    return processar(path)
```

## Boas práticas
- Fazer as mensagens idempotentes: reprocessar não pode duplicar efeitos colaterais.
- Definir retry com backoff e DLQ para falhas persistentes.
- Manter as mensagens pequenas; dados grandes vão em referência (ID) ao armazenamento.
- Monitorar tamanho das filas, idade das mensagens e taxa de falha.
- Escalar workers independentemente do número de instâncias da API.

## Armadilhas comuns
- Processar tarefas pesadas de forma síncrona no request.
- Assumir entrega exatamente-uma-vez (a maioria entrega pelo menos uma vez).
- Não tornar as tarefas idempotentes e duplicar envios/cobranças.
- Mensagens gigantes no broker, estourando limites de memória.
- Sem DLQ/monitoramento, tarefas falhas desaparecem silenciosamente.

## Relacionadas
- [[Redis]]
- [[Backend]]
- [[Caching]]
- [[Microservicos]]