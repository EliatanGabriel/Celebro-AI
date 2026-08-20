---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# LLM

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Large Language Models: modelos de linguagem de grande escala baseados em transformers que preveem e geram texto coerente, como GPT e LLaMA.

## Conceitos-chave
- **Tokens**: unidades básicas de texto (palavras, subpalavras) que o modelo processa.
- **Transformers**: arquitetura baseada em atenção que processa sequências em paralelo.
- **Autoregressão**: o modelo gera o próximo token dado o contexto anterior, token a token.
- **Pré-treinamento**: treino em corpus gigante (texto da web) para aprender linguagem e conhecimento geral.
- **Contexto (janela)**: número máximo de tokens que o modelo considera ao gerar.
- **Alinhamento**: ajuste por instruções e preferências humanas para respostas úteis e seguras.

## Exemplos
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B-Instruct")
modelo = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B-Instruct")

mensagens = [{"role": "user", "content": "Explique tokens em uma frase."}]
entrada = tokenizer.apply_chat_template(mensagens, return_tensors="pt")
saida = modelo.generate(entrada, max_new_tokens=80, do_sample=True)
print(tokenizer.decode(saida[0], skip_special_tokens=True))
```

## Boas práticas
- Escolher o modelo pelo tamanho, qualidade e licença adequados à tarefa.
- Usar o template de chat correto do modelo para evitar respostas degradadas.
- Controlar parâmetros de geração (temperature, top_p, max_new_tokens).
- Combinar com RAG para conhecimento atualizado e reduzir alucinação.
- Avaliar respostas com métricas e testes de domínio, não só qualitativamente.

## Armadilhas comuns
- Confundir LLM com uma base de conhecimento confiável; eles podem alucinar.
- Ignorar os limites de contexto e truncar informações importantes.
- Esperar raciocínio garantido em tarefas numéricas ou lógicas complexas.
- Esquecer que a saída é probabilística: mesma pergunta, respostas diferentes.
- Aplicar custos e latência sem otimização (cache, prompts mais curtos, modelos menores).

## Relacionadas
- [[NLP]]
- [[Prompts]]
- [[IA]]
- [[Fine-tuning]]
- [[RAG]]
- [[Agentes-IA]]