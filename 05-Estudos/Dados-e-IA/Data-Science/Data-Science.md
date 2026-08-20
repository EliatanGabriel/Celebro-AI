---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Data-Science

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Ciência de extrair conhecimento e insights acionáveis de dados por meio de estatística, programação e aprendizado de máquina, para apoiar decisões.

## Conceitos-chave
- **Ciclo do projeto**: definição do problema, coleta, limpeza, exploração, modelagem, avaliação e comunicação.
- **Coleta**: obtenção de dados de fontes diversas (APIs, bancos, arquivos, scraping).
- **Análise exploratória (EDA)**: entender distribuições, correlações e anomalias antes de modelar.
- **Modelagem**: aplicação de estatística ou ML para descrever, prever ou agrupar.
- **Visualização**: comunicação de achados com gráficos claros e honestos.
- **Comunicação**: entregar insights de forma compreensível para stakeholders não técnicos.

## Exemplos
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendas.csv")
df["data"] = pd.to_datetime(df["data"])

# Análise exploratória rápida
print(df.describe())
print(df.isna().sum())

# Agregação por mês
df["mes"] = df["data"].dt.to_period("M")
vendas_mensais = df.groupby("mes")["receita"].sum()
vendas_mensais.plot(kind="bar")
plt.title("Receita mensal")
plt.show()
```

## Boas práticas
- Começar por uma pergunta de negócio clara e mensurável, não pelos dados.
- Registrar versões de dados, código e experimentos para reprodutibilidade.
- Validar hipóteses com dados de teste fora da amostra.
- Combinar estatística descritiva com inferência antes de partir para ML.
- Apresentar resultados com incerteza e limitações explicitadas.

## Armadilhas comuns
- Confundir correlação com causalidade nas conclusões.
- Saltar direto para modelos complexos sem fazer EDA.
- Data leakage: informações do futuro/do teste vazam no treino e inflam métricas.
- Comunicar resultados sem contexto, induzindo decisões erradas.
- Confundir o escopo: Data Science gera insights, BI reporta indicadores e ML automatiza previsões.

## Relacionadas
- [[Estatistica]]
- [[Machine-Learning]]
- [[BI]]
- [[Datasets]]
- [[Pandas]]
- [[NumPy]]