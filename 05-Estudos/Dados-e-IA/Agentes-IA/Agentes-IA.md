---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Agentes-IA

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Sistemas autônomos que planejam e executam tarefas combinando um modelo de linguagem com ferramentas, memória e ciclos de feedback.

## Conceitos-chave
- **Autonomia**: o agente decide os passos seguintes a partir de um objetivo, em vez de seguir um script fixo.
- **Ferramentas (tools)**: funções expostas ao modelo (busca, API, execução de código) que ampliam o que a IA consegue fazer.
- **Planejamento**: decomposição do objetivo em sub-tarefas, com reavaliação após cada passo.
- **Memória**: memória de curto prazo (contexto da conversa) e de longo prazo (vetores, bases de conhecimento) para decisões consistentes.
- **Loop agente-ferramenta**: o ciclo observação → decisão → ação → resultado é repetido até concluir o objetivo.
- **Multi-agente**: vários agentes com papéis distintos (orquestrador, executor, revisor) cooperam para tarefas complexas.

## Exemplos
```python
# Pseudocódigo de um agente com ferramentas (ex.: via function calling)
ferramentas = {"buscar_documento": buscar_documento, "executar_sql": executar_sql}

def executar_agente(objetivo, max_passos=5):
    mensagens = [{"role": "system", "content": "Assistente que usa ferramentas."},
                 {"role": "user", "content": objetivo}]
    for _ in range(max_passos):
        resposta = modelo.chat(mensagens, tools=ferramentas)
        if resposta["tool_calls"]:
            for chamada in resposta["tool_calls"]:
                resultado = ferramentas[chamada["name"]](**chamada["args"])
                mensagens.append({"role": "tool", "content": resultado})
        else:
            return resposta["content"]
```

## Boas práticas
- Validar e limitar os passos do agente para evitar loops infinitos e custos altos.
- Sanitizar as saídas das ferramentas antes de alimentar o modelo.
- Definir objetivos claros e critérios de parada mensuráveis.
- Registrar cada ação executada para auditoria e depuração.
- Restringir permissões das ferramentas ao mínimo necessário.

## Armadilhas comuns
- Confundir agente com um simples chatbot com instruções; agente pressupõe ação e loop de feedback.
- Dar ferramentas com efeitos destrutivos sem supervisão (apagar arquivo, apagar tabela).
- Esperar planejamento perfeito: agentes erram e precisam de correção por feedback humano ou validação automatizada.
- Não lidar com falhas de ferramenta (timeout, erro de API), deixando o agente preso em retry infinito.
- Ignorar o custo acumulado de múltiplas chamadas por tarefa.

## Relacionadas
- [[LLM]]
- [[Prompts]]
- [[IA]]
- [[RAG]]
- [[Fine-tuning]]