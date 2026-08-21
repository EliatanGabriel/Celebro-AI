---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Lambda

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Serviço de computação serverless (FaaS) da AWS que executa funções sob demanda, escalando automaticamente e cobrando apenas pelo tempo de execução.

## Conceitos-chave
- **FaaS (Function as a Service):** você fornece o código; a AWS gerencia runtime, servidores e escala.
- **Eventos:** gatilhos que invocam a função (S3, API Gateway, DynamoDB Streams, SQS, cron via EventBridge).
- **Invocation models:** síncrono (API Gateway), assíncrono (S3/SNS), streaming (Kinesis/DynamoDB).
- **Escala automática:** execuções concorrentes por demanda; limite de concorrência configurável (reserved concurrency).
- **Timeouts e memória:** limite de tempo (máx. 15 min) e memória configurável (128 MB–10 GB).
- **Cold start:** atraso da primeira execução ao provisionar o runtime (relevante para latência).
- **Layers e container images:** empacotar dependências como layers ou rodar a função como imagem de container.
- **Integração AWS:** papel central em arquiteturas event-driven e serverless.

## Exemplos

Função com Node.js acionada por API Gateway:

```javascript
exports.handler = async (event) => {
  const name = event.queryStringParameters?.name ?? "mundo";
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mensagem: `Olá, ${name}!` }),
  };
};
```

Deploy via CLI:

```bash
aws lambda create-function \
  --function-name minha-funcao \
  --runtime nodejs20.x \
  --role arn:aws:iam::123456789012:role/lambda-exec \
  --handler index.handler \
  --zip-file fileb://function.zip
```

## Boas práticas
- Manter funções pequenas e focadas em uma única responsabilidade.
- Definir IAM role com escopo mínimo para a função.
- Configurar timeout e memória adequados (memória maior também melhora CPU).
- Usar variáveis de ambiente para configuração e secrets no Secrets Manager.
- Instrumentar com logs estruturados e traces (X-Ray) para observabilidade.

## Armadilhas comuns
- Função de longa duração (processamento pesado) estourando o timeout.
- Dependências pesadas que inflam o cold start — use layers e otimize o pacote.
- Não considerar cold starts em APIs sensíveis a latência.
- Recursão sem proteção (Lambda invocando a si mesma sem parada) gerando custo infinito.
- Assumir estado persistente: Lambda é stateless; estado vai para S3/DynamoDB.

## Relacionadas
- [[Serverless]]
- [[AWS]]
- [[Microservicos]]