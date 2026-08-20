---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Classificacao

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Tarefa supervisionada em que o modelo atribui uma categoria discreta a cada exemplo, como classificar um e-mail como spam ou não-spam.

## Conceitos-chave
- **Rótulos (labels)**: classes-alvo discretas (binárias ou multiclasse) presentes no treino supervisionado.
- **Matriz de confusão**: tabela de VP/VN/FP/FN que resume acertos e erros por classe.
- **Precisão (precision)**: proporção de positivos previstos que realmente são positivos.
- **Recall (sensibilidade)**: proporção de positivos reais que o modelo conseguiu capturar.
- **F1-score**: média harmônica entre precisão e recall, útil em classes desbalanceadas.
- **Fronteira de decisão**: região do espaço de features onde o modelo muda a classe prevista.

## Exemplos
```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

X = df[["frequencia_compra", "valor_medio", "idade"]]
y = df["churn"]  # 0 = ficou, 1 = saiu

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

modelo = RandomForestClassifier(n_estimators=200, random_state=42)
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
```

## Boas práticas
- Usar `stratify` no split para preservar a proporção das classes.
- Escolher a métrica certa conforme o custo dos erros (ex.: recall para detecção de fraude).
- Avaliar por classe, não apenas pela acurácia, em dados desbalanceados.
- Tratar desbalanceamento com class weights, resampling ou técnicas específicas.
- Validar com k-fold cruzada para estimativas estáveis.

## Armadilhas comuns
- Acurácia alta em classes desbalanceadas pode esconder um modelo inútil (prever sempre a classe majoritária).
- Confundir precisão e recall ao interpretar resultados.
- Vazar dados do teste no treinamento ao escalar features antes do split.
- Tratar problemas multiclasse como binários sem adaptar métricas e rótulos.
- Confundir classificação com regressão: a saída é categórica, não um valor contínuo.

## Relacionadas
- [[Regressao]]
- [[Scikit-Learn]]
- [[Machine-Learning]]
- [[Clustering]]
- [[Modelos]]