---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Scikit-Learn

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Biblioteca Python de Machine Learning com algoritmos prontos para classificação, regressão e clustering, API uniforme e ferramentas de pré-processamento e avaliação.

## Conceitos-chave
- **API uniforme**: todos os estimadores seguem `fit(X, y)`, `predict(X)`, `score(X, y)`.
- **Pré-processamento**: transformadores (StandardScaler, OneHotEncoder) no módulo `preprocessing`.
- **Pipelines**: encadeiam transformações e estimadores em um único objeto.
- **Seleção de modelo**: `train_test_split`, `GridSearchCV` e `cross_val_score`.
- **Métricas**: acurácia, precisão, recall, F1, R², MAE no módulo `metrics`.
- **Algoritmos**: regressão linear/logística, árvores, florestas, SVM, KMeans, Naive Bayes.

## Exemplos
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

preprocessador = ColumnTransformer([
    ("num", StandardScaler(), ["idade", "saldo"]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["regiao"]),
])

pipeline = Pipeline([
    ("prep", preprocessador),
    ("modelo", RandomForestClassifier(random_state=42)),
])

parametros = {"modelo__n_estimators": [100, 200]}
busca = GridSearchCV(pipeline, parametros, cv=5, scoring="f1")
busca.fit(X_train, y_train)
print(busca.best_params_, busca.best_score_)
```

## Boas práticas
- Sempre usar Pipelines para evitar data leakage entre treino e teste.
- Tunar hiperparâmetros com validação cruzada, nunca no conjunto de teste.
- Escolher métricas de avaliação alinhadas ao problema de negócio.
- Combinar com Pandas e NumPy para preparação dos dados.
- Persistir o modelo treinado com `joblib` para uso em produção.

## Armadilhas comuns
- Ajustar transformadores no conjunto inteiro antes do split (data leakage).
- Tunar hiperparâmetros no teste, viciando a avaliação final.
- Aplicar StandardScaler a dados esparsos, quebrando a esparsidade.
- Confundir `transform` com `fit_transform` em novos dados.
- Esperar que Scikit-Learn sirva para deep learning em larga escala; para isso use PyTorch/TensorFlow.

## Relacionadas
- [[Machine-Learning]]
- [[Regressao]]
- [[Classificacao]]
- [[Clustering]]
- [[Feature-Engineering]]