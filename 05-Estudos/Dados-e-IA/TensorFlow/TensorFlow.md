---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# TensorFlow

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Framework de deep learning de código aberto mantido pelo Google, com foco em produção, escalabilidade e integração com Keras para construção de modelos de forma declarativa.

## Conceitos-chave
- **Tensors**: estrutura de dados fundamental, com suporte a GPU/TPU.
- **Keras**: API de alto nível integrada para definir e treinar modelos rapidamente.
- **Gráficos computacionais**: execução eager (por padrão) ou compilação em grafos para performance.
- **Distribuído**: treino em múltiplas GPUs/TPUs com estratégias de distribuição.
- **Produção**: exportação com TF Serving/TFLite/TensorFlow.js para diferentes plataformas.
- **Ecosystema**: tf.data (pipelines de dados), TFX, TensorBoard (visualização de métricas).

## Exemplos
```python
import tensorflow as tf
from tensorflow import keras

modelo = keras.Sequential([
    keras.layers.Dense(64, activation="relu", input_shape=(10,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(1, activation="sigmoid"),
])

modelo.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"],
)

historico = modelo.fit(X_train, y_train,
                       validation_split=0.2,
                       epochs=20, batch_size=32)
```

## Boas práticas
- Começar com a API Keras `Sequential`/`Functional` para a maioria dos casos.
- Usar `tf.data.Dataset` para pipelines de dados escaláveis.
- Monitorar o treino com TensorBoard e early stopping.
- Controlar sementes (`tf.random.set_seed`) para reprodutibilidade.
- Exportar o modelo no formato SavedModel para servir em produção.

## Armadilhas comuns
- Confundir Keras com TensorFlow: Keras é a API de alto nível que roda sobre o backend TensorFlow.
- Ignorar a diferença de comportamento entre `model.fit` e loops manuais.
- Aplicar camadas de dropout em inferência sem `model.evaluate` adequado (Keras já lida).
- Esquecer de especificar `input_shape` na primeira camada, gerando erros.
- Escolher TensorFlow por inércia; PyTorch e TensorFlow são equivalentes em capacidade, escolha pelo time e pela infraestrutura.

## Relacionadas
- [[PyTorch]]
- [[Deep-Learning]]
- [[Redes-Neurais]]
- [[Machine-Learning]]