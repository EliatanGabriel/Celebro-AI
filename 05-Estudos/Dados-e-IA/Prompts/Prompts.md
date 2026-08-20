---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Prompts

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Instruções e contexto fornecidos a modelos de linguagem para orientar a geração de respostas; a engenharia de prompts é a prática de projetar essas instruções para obter melhores resultados.

## Conceitos-chave
- **Engenharia de prompt**: desenhar instruções, contexto e exemplos para guiar o modelo.
- **Contexto**: informações relevantes injetadas no prompt para ancorar a resposta.
- **Few-shot**: incluir exemplos de entrada-saída no prompt para ensinar o formato desejado.
- **Zero-shot**: pedir a tarefa diretamente, sem exemplos.
- **System prompt**: instrução de papel/comportamento que persiste ao longo da conversa.
- **Iteração**: refinar prompts com base na avaliação das respostas geradas.

## Exemplos
```text
Você é um assistente de suporte especializado em telecom.

Responda apenas com base no contexto abaixo. Se não souber, diga "não sei".

Contexto:
- Plano "Fibra 500" tem franquia ilimitada.
- Atraso de pagamento > 30 dias bloqueia o serviço.

Pergunta: Meu plano Fibra 500 tem limite de dados?

Resposta: Não, o plano Fibra 500 tem franquia de dados ilimitada.
```

## Boas práticas
- Definir claramente o papel, a tarefa, o formato de saída e as restrições.
- Fornecer exemplos do formato desejado (few-shot) para tarefas estruturadas.
- Testar variações de prompt e medir a qualidade com um conjunto de avaliação.
- Manter prompts versionados como parte do código do produto.
- Usar RAG para injetar conhecimento atualizado em vez de depender do prompt estático.

## Armadilhas comuns
- Prompts vagos ou ambíguos, gerando respostas inconsistentes.
- Pedir formato estruturado sem mostrar um exemplo (JSON malformado).
- Acreditar que prompts resolvem conhecimento factual; alucinação persiste.
- Injetar contexto excessivo que estoura a janela ou dilui instruções importantes.
- Ignorar a segurança: usuários podem tentar prompt injection ("ignore as instruções").

## Relacionadas
- [[LLM]]
- [[Agentes-IA]]
- [[IA]]
- [[RAG]]
- [[NLP]]