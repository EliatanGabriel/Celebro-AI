---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Feature-Engineering

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Processo de criar, selecionar e transformar variáveis para melhorar a performance e a interpretabilidade dos modelos de aprendizado de máquina.

## Conceitos-chave
- **Criação de features**: derivar novas variáveis a partir das existentes (datas, composições, interações).
- **Transformação**: aplicar escalonamento (StandardScaler), logaritmo, binning ou codificação.
- **Encoding**: converter categóricas em numéricas (one-hot, ordinal, target encoding).
- **Normalização/padronização**: ajustar escalas para algoritmos sensíveis à magnitude (KNN, SVM, gradiente).
- **Seleção de features**: escolher as variáveis mais relevantes e reduzir dimensionalidade (correlação, importância).
- **Impacto no modelo**: bons features podem valer mais que o algoritmo escolhido.

## Exemplos
```python
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd

df["dias_desde_cadastro"] = (df["data_ref"] - df["data_cadastro"]).dt.days
df["receita_por_cliente"] = df["receita_total"] / df["qtd_clientes"].clip(lower=1)

# Categóricas -> one-hot
df = pd.get_dummies(df, columns=["regiao"], drop_first=True)

# Padronização de numéricas
num = df[["idade", "receita_por_cliente"]]
df[["idade", "receita_por_cliente"]] = StandardScaler().fit_transform(num)
```

## Boas práticas
- Ajustar transformações apenas no conjunto de treino para evitar data leakage.
- Manter features interpretáveis quando o negócio exige explicação.
- Validar o ganho de cada feature com validação cruzada antes de mantê-la.
- Evitar cardinalidade alta no one-hot, preferindo encoding com alvo ou embeddings.
- Documentar cada feature criada e sua justificativa.

## Armadilhas comuns
- Data leakage ao usar estatísticas globais (média do teste) na transformação.
- Criar features derivadas do rótulo (leakage) ou com informação futura.
- One-hot com categorias raras gerando esparsidade excessiva.
- Aplicar transformações sensíveis à escala sem padronizar, degradando KNN/SVM.
- Acumular features sem validação, aumentando overfitting e custo de treino.

## Relacionadas
- [[Datasets]]
- [[Machine-Learning]]
- [[Overfitting]]
- [[Data-Science]]
- [[Classificacao]]