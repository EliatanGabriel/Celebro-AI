---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# NLP

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Processamento de linguagem natural: área da IA que capacita máquinas a entender, interpretar e gerar texto e fala humana.

## Conceitos-chave
- **Tokenização**: divisão do texto em tokens (palavras/subpalavras) para o modelo processar.
- **Embeddings**: representações vetoriais densas que capturam significado e semelhança semântica.
- **Análise de sentimento**: classificar a polaridade de um texto (positivo, negativo, neutro).
- **NER (Named Entity Recognition)**: extração de entidades (pessoas, organizações, datas).
- **Tradução automática**: converter texto entre idiomas com modelos sequência-a-sequência.
- **Chatbots e LLMs**: aplicações que usam modelos de linguagem para conversação e geração.

## Exemplos
```python
import spacy

nlp = spacy.load("pt_core_news_lg")
doc = nlp("A Apple lançou o novo iPhone em São Paulo no dia 12 de março.")

# NER: reconhecer entidades
for ent in doc.ents:
    print(ent.text, ent.label_)
# Apple ORG | São Paulo LOC | 12 de março DATE

# Tokenização e lematização
print([tok.lemma_ for tok in doc][:8])
```

## Boas práticas
- Escolher o tokenizador/modelo adequado ao idioma (português tem modelos próprios).
- Normalizar o texto com cuidado (minúsculas, acentos) segundo o problema.
- Avaliar com métricas específicas de NLP (F1 por entidade, BLEU para tradução).
- Combinar regras de domínio com modelos neurais para tarefas de alto risco.
- Considerar o custo de embeddings e contexto ao escalar para grandes volumes.

## Armadilhas comuns
- Aplicar modelos treinados em inglês diretamente em português com resultados ruins.
- Confundir tokenização com lematização ou stemming.
- Acreditar que o modelo "entende" significado como um humano; ele modela padrões.
- Ignorar ambiguidade e contexto, gerando erros de interpretação.
- Tratar LLM e NLP como sinônimos: NLP é a área; LLM é uma técnica/arquitetura.

## Relacionadas
- [[LLM]]
- [[IA]]
- [[Data-Science]]
- [[Prompts]]
- [[RAG]]