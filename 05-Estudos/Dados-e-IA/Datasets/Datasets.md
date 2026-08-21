---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Datasets

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Conjuntos de dados estruturados usados para treinar, validar e avaliar modelos, compostos por instâncias (linhas), features (colunas) e, no caso supervisionado, rótulos.

## Conceitos-chave
- **Features (variáveis)**: atributos que descrevem cada exemplo e alimentam o modelo.
- **Labels (rótulos)**: alvo a ser previsto em problemas supervisionados.
- **Split treino/teste/validação**: divisão para treinar, calibrar hiperparâmetros e avaliar de forma imparcial.
- **Qualidade dos dados**: consistência, completude, ausência de duplicatas e de erros de medição.
- **Pré-processamento**: limpeza, tratamento de valores ausentes, encoding e escalonamento.
- **Fontes**: bases públicas (Kaggle, UCI), dados proprietários, APIs e geração sintética.

## Exemplos
```python
from sklearn.model_selection import train_test_split

X = df.drop(columns=["target"])
y = df["target"]

# Separa teste primeiro, depois validação a partir do treino
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42)

X_treino, X_val, y_treino, y_val = train_test_split(
    X_treino, y_treino, test_size=0.25, random_state=42)

print("Treino:", X_treino.shape, "Validação:", X_val.shape, "Teste:", X_teste.shape)
```

## Boas práticas
- Separar os dados de teste antes de qualquer etapa que use as features (encoding, scaling).
- Manter o teste com a distribuição mais próxima do mundo real.
- Documentar origem, licenças e transformações aplicadas em cada dataset.
- Checar desbalanceamento e viés de amostragem antes de treinar.
- Persistir um snapshot do dataset usado em cada experimento.

## Armadilhas comuns
- Data leakage: escalonar ou codificar usando estatísticas do conjunto de teste.
- Avaliar em dados que já participaram do treino, superestimando a performance.
- Usar datasets pequenos demais e concluir que o modelo generaliza.
- Confundir validação com teste: a validação ainda influencia a escolha do modelo.
- Ignorar a qualidade: lixo entra, lixo sai (garbage in, garbage out).

## Relacionadas
- [[Data-Science]]
- [[Feature-Engineering]]
- [[Pandas]]
- [[Machine-Learning]]
- [[Overfitting]]