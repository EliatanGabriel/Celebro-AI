---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Inteligencia-Artificial

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Área da computação que busca criar sistemas com capacidades cognitivas, como aprendizado, percepção, linguagem e raciocínio, simulando comportamentos inteligentes.

## Conceitos-chave
- **ML (Machine Learning)**: aprendizado de padrões a partir de dados, subárea central da IA.
- **NLP**: processamento e geração de linguagem natural.
- **Visão computacional**: interpretação de imagens e vídeos.
- **LLMs**: modelos de linguagem em larga escala baseados em transformers.
- **Agentes**: sistemas autônomos que percebem, decidem e agem.
- **IA forte vs fraca**: a IA atual é "fraca" (estreita), especializada em tarefas específicas.

## Exemplos
```python
# Visão computacional com um modelo pré-treinado
from torchvision import models, transforms
from PIL import Image

modelo = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
modelo.eval()

transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
])
img = transform(Image.open("gato.jpg")).unsqueeze(0)
pred = modelo(img)
# argmax(pred) -> índice da classe prevista no ImageNet
```

## Boas práticas
- Compreender o histórico e os limites do campo para escolher abordagens adequadas.
- Combinar representação de conhecimento com aprendizado estatístico quando apropriado.
- Avaliar robustez: testar com dados fora da distribuição e cenários adversários.
- Considerar impacto ético e social antes de automatizar decisões.
- Manter-se atualizado, pois o campo evolui rapidamente.

## Armadilhas comuns
- Usar os termos IA, ML, Deep Learning e LLM como sinônimos.
- Acreditar em "inteligência artificial geral" iminente sem evidência.
- Ignorar que modelos de IA não raciocinam de verdade; eles generalizam padrões.
- Aplicar IA onde uma solução simples e determinística resolve melhor.
- Desconsiderar viés de dados, causando decisões discriminatórias.

## Relacionadas
- [[Machine-Learning]]
- [[LLM]]
- [[Deep-Learning]]
- [[Agentes-IA]]
- [[IA]]
- [[NLP]]