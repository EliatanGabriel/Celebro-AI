---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# NumPy

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Biblioteca Python para computação numérica eficiente, com arrays multidimensionais e operações vetorizadas que servem de base para todo o ecossistema de dados.

## Conceitos-chave
- **ndarray**: array N-dimensional homogêneo que permite operações rápidas em elementos.
- **Vetorização**: operações aplicadas a arrays inteiros sem loops explícitos, muito mais rápidas.
- **Broadcasting**: regras para operar arrays de formatos diferentes sem cópias.
- **Indexação e slicing**: acesso e seleção avançada (máscaras booleanas, fancy indexing).
- **Funções matemáticas**: ufuncs para álgebra linear, estatística e trigonometria.
- **Base do ecossistema**: Pandas, Scikit-Learn e PyTorch/TensorFlow dependem de arrays NumPy.

## Exemplos
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

print(a + 10)            # vetorização: [11 12 13]
print(a[a > 1])          # máscara booleana: [2 3]

mat = np.arange(9).reshape(3, 3)
print(mat.T)             # transposta
print(np.linalg.det(b))  # determinante
print(np.dot(a, a))      # produto escalar: 14
```

## Boas práticas
- Preferir operações vetorizadas a loops Python sempre que possível.
- Usar o dtype correto para economizar memória em arrays grandes.
- Criar views com slicing quando for seguro, mas usar `.copy()` quando precisar modificar.
- Utilizar `np.random.default_rng()` para números aleatórios reprodutíveis.
- Combinar com Pandas para manipulação de dados e com bibliotecas de ML para modelagem.

## Armadilhas comuns
- Confundir `np.copy` com views: modificar um slice pode alterar o array original.
- Usar listas Python para dados numéricos grandes, perdendo performance.
- Ignorar broadcasting e criar loops desnecessários.
- Misturar tipos no array, que força coerção para um dtype único.
- Esquecer que `*` entre arrays é multiplicação elemento a elemento, não produto matricial.

## Relacionadas
- [[Pandas]]
- [[Data-Science]]
- [[Machine-Learning]]
- [[PyTorch]]