---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Machine-Learning

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Campo da IA em que modelos aprendem padrões a partir de dados, sem regras programadas explicitamente, e generalizam para novos exemplos.

## Conceitos-chave
- **Aprendizado supervisionado**: treino com pares (features, rótulo); classificação e regressão.
- **Aprendizado não supervisionado**: apenas features, o modelo descobre estrutura (clustering).
- **Aprendizado por reforço**: o agente aprende por recompensas a partir de ações.
- **Features e rótulos**: entradas do modelo e alvo a prever.
- **Treino/teste/validação**: divisão de dados para ajustar e avaliar com imparcialidade.
- **Generalização**: capacidade de performar bem em dados nunca vistos, objetivo central do ML.

## Exemplos
```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = df[["idade", "saldo", "transacoes"]]
y = df["inadimplente"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
print("Acurácia:", accuracy_score(y_test, y_pred))
```

## Boas práticas
- Começar com modelos simples e interpretáveis antes de modelos complexos.
- Avaliar sempre em dados fora da amostra com validação cruzada.
- Prevenir data leakage em qualquer etapa de pré-processamento.
- Documentar hiperparâmetros, métricas e versões de dados dos experimentos.
- Monitorar drift de dados em produção.

## Armadilhas comuns
- Sobreajustar ao treino e falhar na generalização (overfitting).
- Acreditar que mais features é sempre melhor.
- Avaliar apenas com acurácia em dados desbalanceados.
- Vazar dados do teste durante o treinamento.
- Esperar que ML resolva problemas sem dados de qualidade e suficientes.

## Relacionadas
- [[Deep-Learning]]
- [[Data-Science]]
- [[IA]]
- [[Scikit-Learn]]
- [[Overfitting]]
- [[Modelos]]