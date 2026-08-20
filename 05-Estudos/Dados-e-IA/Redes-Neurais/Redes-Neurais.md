---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Redes-Neurais

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Modelos de aprendizado inspirados no cérebro, compostos por camadas de neurônios artificiais interligados por pesos, capazes de aprender representações complexas por otimização.

## Conceitos-chave
- **Neurônio artificial**: unidade que combina entradas ponderadas, soma um bias e aplica uma ativação.
- **Pesos e bias**: parâmetros ajustáveis que o treinamento otimiza.
- **Camadas**: camada de entrada, camadas ocultas e camada de saída.
- **Função de ativação**: não linearidade (ReLU, sigmoid, tanh, softmax) que dá poder expressivo.
- **Forward pass e backpropagation**: propagar entradas para obter saída e propagar o erro para atualizar pesos.
- **Loss e otimizador**: função de perda mede o erro; gradiente descendente (SGD, Adam) minimiza.

## Exemplos
```python
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def forward(X, W1, b1, W2, b2):
    camada1 = sigmoid(X @ W1 + b1)
    saida = sigmoid(camada1 @ W2 + b2)   # para regressão/classificação binária
    return camada1, saida

# Gradiente descendente: ajustar pesos para reduzir a perda
for epoca in range(1000):
    camada1, pred = forward(X, W1, b1, W2, b2)
    erro = pred - y
    # backpropagation: derivadas e atualização de W1, W2 (resumido)
```

## Boas práticas
- Normalizar as features para acelerar a convergência.
- Usar ativações adequadas (ReLU em camadas ocultas, sigmoid/softmax na saída).
- Aplicar regularização (dropout, weight decay) para evitar overfitting.
- Inicializar pesos adequadamente (He, Xavier) e usar otimizadores como Adam.
- Monitorar loss de treino e validação com early stopping.

## Armadilhas comuns
- Acreditar que uma rede resolve tudo sem dados e tuning suficientes.
- Usar sigmoid em camadas ocultas profundas, sofrendo com vanishing gradient.
- Inicializar pesos com zero, impedindo o aprendizado (neurônios simétricos).
- Confundir camadas, batch, épocas e iterações ao dimensionar o treino.
- Ignorar a escala dos dados, causando convergência lenta ou instável.

## Relacionadas
- [[Deep-Learning]]
- [[TensorFlow]]
- [[Machine-Learning]]
- [[PyTorch]]
- [[Modelos]]