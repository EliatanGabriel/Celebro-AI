---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Overfitting

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Fenômeno em que o modelo memoriza o conjunto de treino em vez de aprender padrões gerais, apresentando ótima performance no treino e desempenho ruim em dados novos.

## Conceitos-chave
- **Variance alta**: modelo muito sensível às particularidades do treino, muda muito com pequenas variações.
- **Generalização**: capacidade de performar bem fora do treino; é o que o overfitting destrói.
- **Regularização**: penalizar a complexidade do modelo (L1/L2, dropout, weight decay).
- **Validação cruzada**: estimar a performance real sem depender de um único split.
- **Curvas de aprendizado**: comparar loss de treino e validação para diagnosticar over/underfitting.
- **Underfitting**: o oposto, modelo simples demais que nem aprende o treino.

## Exemplos
```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, cross_val_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Árvore sem limite: tende a overfitar
arvore_livre = DecisionTreeRegressor(random_state=42).fit(X_train, y_train)
print("Treino:", arvore_livre.score(X_train, y_train))  # ~1.0
print("Teste: ", arvore_livre.score(X_test, y_test))    # bem menor

# Com regularização (limite de profundidade)
arvore_reg = DecisionTreeRegressor(max_depth=3, random_state=42).fit(X_train, y_train)
print("Teste com max_depth=3:", arvore_reg.score(X_test, y_test))
```

## Boas práticas
- Avaliar sempre em dados de teste/validação separados do treino.
- Usar regularização proporcional à complexidade do modelo.
- Aumentar a quantidade e a qualidade dos dados de treino.
- Simplificar o modelo (menos features, menos parâmetros) quando necessário.
- Aplicar early stopping em redes neurais monitorando a validação.

## Armadilhas comuns
- Confundir loss de treino baixo com sucesso; o que importa é a generalização.
- Validar com o mesmo dado usado para escolher hiperparâmetros (vazamento de informação).
- Data leakage: features que contêm o rótulo ou informação futura inflam métricas.
- Acreditar que mais dados sempre resolve; dados duplicados ou enviesados não ajudam.
- Ignorar o trade-off viés-variância ao ajustar a complexidade.

## Relacionadas
- [[Machine-Learning]]
- [[Datasets]]
- [[Feature-Engineering]]
- [[Modelos]]
- [[Regressao]]