---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Deep-Learning

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Subcampo do Machine Learning que usa redes neurais com múltiplas camadas (profundas) para aprender representações complexas diretamente dos dados.

## Conceitos-chave
- **Redes profundas**: empilhamento de camadas que aprendem níveis crescentes de abstração.
- **Backpropagation**: algoritmo que propaga o erro para trás e atualiza os pesos via gradiente.
- **Funções de ativação**: não linearidades (ReLU, sigmoid, softmax) que permitem representar funções complexas.
- **GPU**: acelera a multiplicação de matrizes, essencial no treinamento de redes grandes.
- **Dados volumosos**: deep learning brilha com grandes volumes de dados e alta capacidade computacional.
- **Arquiteturas**: CNN (imagens), RNN/transformers (sequências), MLP (tabelas).

## Exemplos
```python
import torch
import torch.nn as nn

modelo = nn.Sequential(
    nn.Linear(20, 64),
    nn.ReLU(),
    nn.Linear(64, 32),
    nn.ReLU(),
    nn.Linear(32, 1),
)
perda = nn.MSELoss()
otimizador = torch.optim.Adam(modelo.parameters(), lr=0.001)

# Loop de treinamento (batches de X, y)
for xb, yb in dataloader:
    otimizador.zero_grad()
    pred = modelo(xb)
    loss = perda(pred, yb)
    loss.backward()
    otimizador.step()
```

## Boas práticas
- Começar com uma baseline simples (ML clássico) antes de partir para redes profundas.
- Usar regularização (dropout, weight decay) para combater overfitting.
- Normalizar as entradas e usar learning rate com scheduler.
- Controlar a semente aleatória para reprodutibilidade.
- Monitorar loss de treino e validação para decidir quando parar (early stopping).

## Armadilhas comuns
- Usar deep learning sem dados suficientes, resultando em overfitting severo.
- Ignorar a GPU e treinar redes grandes em CPU, inviabilizando experimentos.
- Confundir loss de treino baixa com boa generalização.
- Deep learning não é sempre melhor que ML clássico em dados tabulares pequenos.
- Esquecer que `loss.backward()` precisa de gradientes habilitados e do optimizer resetado.

## Relacionadas
- [[Redes-Neurais]]
- [[TensorFlow]]
- [[PyTorch]]
- [[Machine-Learning]]
- [[Overfitting]]