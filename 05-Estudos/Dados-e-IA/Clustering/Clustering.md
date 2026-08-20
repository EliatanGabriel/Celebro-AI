---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Clustering

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Técnica de aprendizado não supervisionado que agrupa dados similares entre si e diferentes de outros grupos, sem usar rótulos.

## Conceitos-chave
- **Não supervisionado**: nenhum rótulo é usado; o algoritmo descobre estrutura nos dados.
- **Medida de distância**: função que define similaridade (euclidiana, cosseno, Manhattan).
- **K-means**: algoritmo de centroides que particiona dados em k grupos.
- **Clusters**: grupos de pontos próximos segundo a métrica escolhida.
- **Elbow method**: técnica para escolher k comparando inércia (soma das distâncias ao centroide).
- **Segmentação**: aplicação comum para dividir clientes, documentos ou pixels em grupos homogêneos.

## Exemplos
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(df[["idade", "gasto_mensal", "frequencia"]])

inercias = []
for k in range(1, 10):
    inercias.append(KMeans(n_clusters=k, n_init=10, random_state=42).fit(X).inertia_)

k = 3  # escolhido no gráfico de cotovelo
modelo = KMeans(n_clusters=k, n_init=10, random_state=42)
df["cluster"] = modelo.fit_predict(X)
print(df.groupby("cluster").mean(numeric_only=True))
```

## Boas práticas
- Padronizar/normalizar as features antes de aplicar distâncias euclidianas.
- Avaliar a qualidade dos clusters com métricas como silhueta e inércia.
- Escolher o número de clusters com critérios objetivos (elbow, silhueta, negócio).
- Fixar `random_state` e `n_init` para resultados reprodutíveis.
- Validar se os clusters gerados fazem sentido de negócio com especialistas.

## Armadilhas comuns
- Assumir que clusters são classes reais: clustering encontra padrões, não verdade absoluta.
- Usar k arbitrário sem validação, gerando agrupamentos sem significado.
- Misturar variáveis de escalas muito diferentes sem padronização.
- Esperar clusters convexos do K-means, que falha com formatos não esféricos (usar DBSCAN).
- Confundir clustering com classificação supervisionada, que usa rótulos.

## Relacionadas
- [[Classificacao]]
- [[Machine-Learning]]
- [[Data-Science]]
- [[K-means]]