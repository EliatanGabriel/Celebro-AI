---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# PyTorch

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Framework de deep learning de código aberto desenvolvido pela Meta, conhecido por gráficos computacionais dinâmicos e API imperativa, muito usado em pesquisa.

## Conceitos-chave
- **Tensors**: estruturas de dados multidimensionais (semelhantes a ndarray) com aceleração de GPU.
- **Autograd**: sistema automático de diferenciação que calcula gradientes para backpropagation.
- **Gráfico computacional dinâmico**: o grafo é construído em tempo de execução, facilitando experimentação.
- **nn.Module**: base para definir camadas e modelos.
- **DataLoader**: carrega dados em lotes com shuffle, paralelismo e transformações.
- **Ecossistema**: Hugging Face Transformers, TorchVision e Lightning construídos sobre PyTorch.

## Exemplos
```python
import torch
import torch.nn as nn
import torch.optim as optim

torch.manual_seed(42)

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.camadas = nn.Sequential(
            nn.Linear(10, 64), nn.ReLU(), nn.Linear(64, 1))

    def forward(self, x):
        return self.camadas(x)

modelo = MLP()
perda = nn.MSELoss()
otimizador = optim.Adam(modelo.parameters(), lr=0.001)

for xb, yb in dataloader:   # xb, yb: tensors
    otimizador.zero_grad()
    pred = modelo(xb)
    loss = perda(pred, yb)
    loss.backward()
    otimizador.step()
```

## Boas práticas
- Mover dados e modelo para o mesmo device (CPU/GPU) com `.to(device)`.
- Chamar `model.train()` e `model.eval()` nos modos corretos (dropout/batchnorm).
- Usar `torch.no_grad()` durante a avaliação para economizar memória.
- Controlar a semente com `torch.manual_seed` para reprodutibilidade.
- Organizar o código em classes `nn.Module` e loops de treino separados.

## Armadilhas comuns
- Misturar tensors de devices diferentes (CPU e GPU) causa erros de device mismatch.
- Esquecer `optimizer.zero_grad()`, acumulando gradientes entre batches.
- Gradientes desabilitados (`requires_grad=False`) bloqueiam `loss.backward()`.
- Comparar PyTorch e TensorFlow como se fossem incompatíveis; hoje ambos usam eager execution e Keras suporta ambos.
- Ignorar a memória da GPU com batches grandes, estourando VRAM.

## Relacionadas
- [[TensorFlow]]
- [[Deep-Learning]]
- [[Redes-Neurais]]
- [[Machine-Learning]]
- [[NumPy]]