---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Fine-tuning

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Técnica que reutiliza um modelo pré-treinado e o ajusta com dados específicos de um domínio, aproveitando o conhecimento já aprendido (transfer learning).

## Conceitos-chave
- **Transfer learning**: aproveitar representações aprendidas em uma tarefa grande (ex.: texto geral) para outra tarefa menor.
- **Modelo base**: modelo pré-treinado (BERT, GPT, ResNet) cujos pesos são o ponto de partida.
- **Dados de domínio**: conjunto rotulado e representativo do problema-alvo.
- **Learning rate baixa**: o ajuste fino usa taxas pequenas para não destruir os pesos pré-treinados.
- **PEFT (Parameter-Efficient Fine-Tuning)**: técnicas como LoRA que ajustam um pequeno subconjunto de parâmetros.
- **Custo**: reduz tempo, dados e computação comparado ao treino do zero.

## Exemplos
```python
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments

modelo = AutoModelForSequenceClassification.from_pretrained(
    "neuralmind/bert-base-portuguese-cased", num_labels=2)

args = TrainingArguments(
    output_dir="./ft",
    learning_rate=2e-5,
    num_train_epochs=3,
    per_device_train_batch_size=16,
)

trainer = Trainer(
    model=modelo,
    args=args,
    train_dataset=dataset_treino,
    eval_dataset=dataset_val,
)
trainer.train()
```

## Boas práticas
- Coletar dados de qualidade e em volume suficiente para o domínio-alvo.
- Usar learning rate baixa (1e-5 a 3e-5 para transformers) e poucas épocas.
- Separar validação e testar em dados do domínio, não genéricos.
- Avaliar antes vs depois para confirmar que o fine-tuning agregou valor.
- Preferir LoRA/PEFT para reduzir custo e evitar esquecer o conhecimento geral.

## Armadilhas comuns
- Confundir fine-tuning com RAG: RAG injeta contexto na consulta, fine-tuning altera os pesos.
- Esperar que o fine-tuning adicione conhecimento factual novo; ele ajusta comportamento e formato.
- Ajustar com learning rate alto, destruindo o modelo pré-treinado.
- Overfitting no dataset pequeno do domínio.
- Ignorar o desvio entre o domínio do modelo base e o domínio-alvo.

## Relacionadas
- [[LLM]]
- [[Machine-Learning]]
- [[Datasets]]
- [[IA]]
- [[Modelos]]
- [[Overfitting]]