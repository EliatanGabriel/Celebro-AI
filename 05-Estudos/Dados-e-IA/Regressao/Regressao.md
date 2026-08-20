---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Regressao

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Tarefa de aprendizado supervisionado que prevê um valor numérico contínuo a partir de variáveis de entrada, como prever preço de imóvel ou temperatura.

## Conceitos-chave
- **Variável alvo contínua**: a saída é um número real, não uma categoria.
- **Regressão linear**: modela a relação como combinação linear das features mais um termo de erro.
- **R² (coeficiente de determinação)**: proporção da variância explicada pelo modelo (quanto mais próximo de 1, melhor).
- **Métricas de erro**: MAE, MSE e RMSE medem a magnitude dos erros de previsão.
- **Resíduos**: diferenças entre valores reais e previstos; devem ser aleatórios e pequenos.
- **Regularização**: Ridge (L2) e Lasso (L1) controlam complexidade e overfitting.

## Exemplos
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

X = df[["area_m2", "quartos", "idade_imovel"]]
y = df["preco"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

pred = modelo.predict(X_test)
print("R²:", r2_score(y_test, pred))
print("MAE:", mean_absolute_error(y_test, pred))
print("Coeficientes:", modelo.coef_, "Intercepto:", modelo.intercept_)
```

## Boas práticas
- Explorar a relação entre features e alvo antes de modelar (scatter plots, correlação).
- Padronizar features quando usar regularização ou algoritmos baseados em distância.
- Analisar resíduos para detectar não linearidades e heterocedasticidade.
- Evitar multicolinearidade entre features na regressão linear clássica.
- Reportar intervalos de confiança das previsões quando possível.

## Armadilhas comuns
- Confundir regressão (valor contínuo) com classificação (categoria discreta).
- Interpretar R² como acerto percentual; ele mede proporção de variância explicada.
- Assumir linearidade onde a relação é não linear, produzindo previsões ruins.
- Extrapolar previsões muito além do intervalo dos dados de treino.
- Deixar outliers dominarem a minimização de MSE, distorcendo o ajuste.

## Relacionadas
- [[Classificacao]]
- [[Scikit-Learn]]
- [[Estatistica]]
- [[Machine-Learning]]
- [[Overfitting]]