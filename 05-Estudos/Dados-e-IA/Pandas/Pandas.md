---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Pandas

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Biblioteca Python para manipulação e análise de dados tabulares, oferecendo estruturas como Series e DataFrame com operações de filtro, agregação e limpeza.

## Conceitos-chave
- **DataFrame**: tabela bidimensional com linhas e colunas rotuladas, estrutura central do Pandas.
- **Series**: coluna unidimensional com rótulos (index).
- **Filtros**: seleção de linhas por condições booleanas.
- **Agregações**: `groupby` + `agg` para sumarizar dados por categoria.
- **Limpeza**: tratamento de valores nulos, duplicatas e conversão de tipos.
- **Merge/join**: combinação de DataFrames por chaves, similar a SQL.

## Exemplos
```python
import pandas as pd

df = pd.read_csv("clientes.csv")

print(df.head())
print(df.dtypes)
print(df["idade"].describe())

# Limpeza
df = df.drop_duplicates(subset=["cliente_id"])
df["data"] = pd.to_datetime(df["data"], errors="coerce")
df = df.dropna(subset=["cliente_id"])

# Filtro e agregação
ativos = df[df["status"] == "ativo"]
gasto_por_cidade = df.groupby("cidade")["gasto"].agg(["sum", "mean", "count"])
print(gasto_por_cidade.sort_values("sum", ascending=False))
```

## Boas práticas
- Usar `df.info()` e `df.describe()` no início para conhecer os dados.
- Preferir operações vetorizadas a `iterrows()` para performance.
- Utilizar `copy()` antes de modificar slices para evitar warnings e efeitos colaterais.
- Encadear transformações em pipelines claros e versionados.
- Combinar com NumPy e Scikit-Learn para modelagem após a preparação.

## Armadilhas comuns
- Confundir `df[df["col"] == x]` (boolean mask) com `df["col"] == x` (Series booleana).
- `SettingWithCopyWarning`: modificar um DataFrame derivado sem saber se é view ou cópia.
- `inplace=True` gerando confusão; preferir atribuição explícita.
- Usar loops para operações que deveriam ser vetorizadas, deixando o código lento.
- Ignorar o `dtype` de datas (ficar com `object` em vez de `datetime64`).

## Relacionadas
- [[Data-Science]]
- [[NumPy]]
- [[Datasets]]
- [[Feature-Engineering]]
- [[ETL]]