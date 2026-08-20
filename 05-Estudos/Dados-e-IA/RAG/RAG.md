---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# RAG

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Retrieval-Augmented Generation: arquitetura que combina busca em uma base de conhecimento externa com geração de linguagem, fornecendo contexto factual ao LLM para respostas mais precisas e atualizadas.

## Conceitos-chave
- **Indexação**: segmentar os documentos e gerar embeddings para busca por similaridade.
- **Embeddings e vetores**: representações numéricas que permitem encontrar trechos semanticamente próximos.
- **Busca (retrieval)**: recuperar os trechos mais relevantes à consulta (top-k) de um banco vetorial.
- **Geração aumentada**: o LLM recebe os trechos recuperados como contexto e gera a resposta citando-os.
- **Redução de alucinação**: ancorar a resposta em documentos reais diminui invenções.
- **Conhecimento próprio/atualizado**: integrar dados internos sem re-treinar o modelo.

## Exemplos
```python
from sentence_transformers import SentenceTransformer
import chromadb

embedder = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
colecao = chromadb.PersistentClient(path="./db").get_or_create_collection("docs")

# Indexação
for doc in documentos:
    colecao.add(ids=[doc.id], documents=[doc.texto],
                embeddings=[embedder.encode(doc.texto).tolist()])

# Busca e geração
pergunta = "Qual é a política de reembolso?"
resultados = colecao.query(query_embeddings=[embedder.encode(pergunta).tolist()], n_results=3)
contexto = "\n".join(resultados["documents"][0])
resposta = llm(f"Responda com base em:\n{contexto}\n\nPergunta: {pergunta}")
```

## Boas práticas
- Escolher chunking adequado (fragmentação dos documentos) para recuperação relevante.
- Avaliar a qualidade do retrieval separadamente da qualidade da geração.
- Armazenar metadados (fonte, data) para citar e filtrar por escopo.
- Re-embeddar e atualizar a base quando os documentos mudarem.
- Combinar filtros de metadados com busca por similaridade para precisão.

## Armadilhas comuns
- Confundir RAG com fine-tuning: RAG injeta contexto na consulta, fine-tuning altera pesos.
- Contexto irrelevante recuperado pode piorar a resposta, não apenas "não ajudar".
- Usar chunking mal dimensionado, fragmentando informações que deveriam estar juntas.
- Achar que RAG elimina 100% da alucinação; ela reduz, mas não garante.
- Ignorar permissões de acesso: recuperar e expor documentos sensíveis indevidamente.

## Relacionadas
- [[LLM]]
- [[Prompts]]
- [[Agentes-IA]]
- [[NLP]]
- [[Datasets]]