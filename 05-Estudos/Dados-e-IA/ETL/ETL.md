---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# ETL

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Extract, Transform, Load: processo de mover e preparar dados de múltiplas fontes para um destino analítico, garantindo consistência e qualidade.

## Conceitos-chave
- **Extração (Extract)**: coleta de dados de fontes heterogêneas (bancos, APIs, arquivos, logs).
- **Transformação (Transform)**: limpeza, padronização, joins, agregações e validações aplicadas aos dados.
- **Carga (Load)**: gravação dos dados transformados no destino (data warehouse, data lake, BI).
- **Pipelines**: fluxos automatizados e agendados que executam ETL de ponta a ponta.
- **ETL vs ELT**: no ELT a transformação acontece depois da carga, no próprio destino.
- **Qualidade de dados**: checagens de integridade, deduplicação e alertas de falha.

## Exemplos
```python
import pandas as pd

# Extração
fonte = pd.read_csv("vendas_bruto.csv")

# Transformação
fonte["data"] = pd.to_datetime(fonte["data"], errors="coerce")
fonte = fonte.dropna(subset=["data", "valor"])
fonte["valor"] = fonte["valor"].astype(float)
fonte = fonte.drop_duplicates(subset=["pedido_id"])

# Carga
fonte.to_sql("fato_vendas", con, if_exists="append", index=False)
```

## Boas práticas
- Projetar pipelines idempotentes para reexecução segura sem duplicar dados.
- Logar cada execução e alertar em caso de falha ou queda de volume.
- Manter a lógica de transformação versionada (código, não scripts perdidos).
- Adicionar etapas de validação antes da carga (totais, nulos, tipos).
- Documentar a linhagem dos dados (origem → transformação → destino).

## Armadilhas comuns
- Rodar transformações em memória com dados que não cabem nela (usar batches ou Spark).
- Ignorar schema drift: mudanças na estrutura da fonte quebram o pipeline silenciosamente.
- Executar ETL em horário que compete com operações produtivas.
- Não tratar timezone e formatos de data inconsistentes entre fontes.
- Confundir ETL (prepara dados para análise) com BI (analisa e exibe os dados).

## Relacionadas
- [[BI]]
- [[Data-Science]]
- [[Datasets]]
- [[Pandas]]