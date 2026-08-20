---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# K-means

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Algoritmo não supervisionado de clusterização que particiona dados em k grupos, atribuindo cada ponto ao centroide mais próximo e iterando até convergir.

## Conceitos-chave
- **Centroides**: pontos representativos de cada cluster, inicializados e atualizados a cada iteração.
- **Atribuição**: cada ponto é associado ao centroide com menor distância (geralmente euclidiana).
- **Atualização**: cada centroide é recalculado como a média dos pontos do seu cluster.
- **Convergência**: o processo repete até os centroides pararem de mudar ou atingir o limite de iterações.
- **Inércia (WCSS)**: soma das distâncias quadradas dos pontos ao seu centroide; métrica de qualidade.
- **Método do cotovelo**: escolhe k no ponto em que a inércia deixa de cair rapidamente.

## Exemplos
```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(pontos)

modelo = KMeans(n_clusters=3, init="k-means++", n_init=10, max_iter=300, random_state=42)
rotulos = modelo.fit_predict(X)

print("Centroides:\n", modelo.cluster_centers_)
print("Inércia:", modelo.inertia_)
```

## Boas práticas
- Padronizar as features antes de calcular distâncias euclidianas.
- Usar `init="k-means++"` e `n_init > 1` para evitar soluções ruins locais.
- Definir k com o método do cotovelo e a silhueta, validando com o contexto de negócio.
- Fixar `random_state` para reprodutibilidade.
- Analisar o perfil de cada cluster para dar significado aos grupos.

## Armadilhas comuns
- Assumir clusters de formato esférico; K-means falha com formatos alongados ou aninhados.
- Sensibilidade a outliers, que puxam os centroides.
- Escolher k arbitrário sem validação.
- Não convergir ou convergir para ótimos locais sem `n_init` adequado.
- Confundir clusters descobertos com classes reais supervisionadas.

## Relacionadas
- [[Clustering]]
- [[Machine-Learning]]
- [[Data-Science]]
- [[Classificacao]]