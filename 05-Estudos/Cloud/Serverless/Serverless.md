---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Serverless

#area/estudos #estudos/cloud #conceito #nuvem #funcoes #escala

**Resumo:** Modelo de execução em nuvem onde o provedor gerencia servidores, escala automaticamente e cobra apenas pelo uso efetivo.

## Conceitos-chave
- **Funções:** unidades de código disparadas por eventos, sem servidor fixo alocado.
- **Gatilhos (triggers):** HTTP, upload de arquivo, mensagem em fila, mudança no banco e outros.
- **Custo por uso:** pagamento por invocação e duração; ociosidade não gera custo.
- **Escala automática:** o provedor cria instâncias sob demanda conforme a carga.
- **Limites:** tempo máximo de execução, memória e payload definidos pelo provedor (na AWS Lambda, por exemplo, cerca de 15 min e 1 GB).
- **Cold start:** atraso inicial quando uma função é invocada após ficar inativa.

## Exemplos
```python
import json

# Handler da AWS Lambda: chamado a cada evento
def handler(event, context):
    nome = event.get("nome", "mundo")
    return {
        "statusCode": 200,
        "body": json.dumps({"mensagem": f"Olá, {nome}!"})
    }
```

```json
{
  "nome": "Ana"
}
```

## Boas práticas
- Manter funções pequenas e de propósito único.
- Reduzir o tamanho do pacote e das dependências para diminuir cold starts.
- Guardar segredos em serviços gerenciados (SSM/Secrets Manager), nunca no código.
- Monitorar métricas de invocação, erro e duração para ajustar limites.

## Armadilhas comuns
- Assumir que serverless é sempre mais barato: cargas contínuas podem custar mais que uma VM.
- Não prever cold starts em fluxos sensíveis à latência.
- Depender de estado local da função, que pode ser perdido entre execuções.
- Estourar o limite de tempo de execução em jobs longos, exigindo outras soluções.

## Relacionadas
- [[AWS]]
- [[Azure]]
- [[Lambda]]