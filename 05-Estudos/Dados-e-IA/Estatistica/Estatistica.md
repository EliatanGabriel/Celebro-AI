---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Estatistica

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Ciência de coletar, organizar, analisar e interpretar dados, oferecendo a base matemática para a Data Science e o Machine Learning.

## Conceitos-chave
- **Estatística descritiva**: resume dados com medidas de tendência central (média, mediana, moda) e dispersão (desvio padrão, quartis).
- **Inferência estatística**: generalizar conclusões de uma amostra para a população com margem de incerteza.
- **Probabilidade**: modela a incerteza e fundamenta distribuições e testes.
- **População vs amostra**: população é o todo; amostra é um subconjunto representativo usado na prática.
- **Testes de hipótese**: decidem se uma diferença observada é estatisticamente significativa (p-valor, t-test).
- **Correlação**: mede associação entre variáveis, mas não implica causalidade.

## Exemplos
```python
import numpy as np
from scipy import stats

dados = np.array([12, 15, 14, 16, 13, 18, 20, 14])

media = dados.mean()
desvio = dados.std(ddof=1)  # ddof=1 -> amostral

# Teste t de uma amostra: H0: média = 15
t, p_valor = stats.ttest_1samp(dados, 15)
print(f"Média: {media:.2f}, Desvio: {desvio:.2f}, p-valor: {p_valor:.3f}")
```

## Boas práticas
- Analisar a distribuição antes de aplicar testes que assumem normalidade.
- Distinguir desvio padrão populacional e amostral (n-1 no denominador).
- Relatar intervalo de confiança junto com a estimativa pontual.
- Definir a hipótese e o nível de significância antes do teste.
- Usar métodos robustos (mediana, IQR) quando houver outliers fortes.

## Armadilhas comuns
- Confundir correlação com causalidade.
- P-hacking: testar muitas hipóteses até alguma ficar "significativa".
- Aplicar testes paramétricos em dados claramente não normais.
- Confundir significância estatística com importância prática.
- Interpretar p-valor como probabilidade de a hipótese nula ser verdadeira.

## Relacionadas
- [[Data-Science]]
- [[Regressao]]
- [[Datasets]]
- [[Machine-Learning]]