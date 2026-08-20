---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# BI

#area/estudos #estudos/dados-e-ia #conceito

**Resumo:** Business Intelligence: conjunto de processos e ferramentas para coletar, integrar e analisar dados com o objetivo de apoiar decisões de negócio.

## Conceitos-chave
- **Dashboards**: painéis visuais interativos que consolidam indicadores em tempo real ou histórico.
- **KPIs**: métricas-chave de desempenho (receita, churn, conversão) que orientam a gestão.
- **Relatórios**: documentos periódicos com análises estruturadas para públicos específicos.
- **Data warehouse**: repositório centralizado e otimizado para leitura analítica (modelo estrela/snowflake).
- **OLAP vs OLTP**: OLAP (análise, leituras agregadas) versus OLTP (transações, escrita frequente).
- **Camada semântica**: definição de métricas e dimensões padronizadas para consultas consistentes.

## Exemplos
```sql
-- Consulta típica de BI sobre um data warehouse (modelo estrela)
SELECT
    d.mes                         AS mes,
    p.categoria                   AS categoria,
    SUM(f.valor)                  AS receita,
    COUNT(DISTINCT f.cliente_id)  AS clientes_ativos
FROM fato_vendas f
JOIN dim_data     d ON f.data_id = d.data_id
JOIN dim_produto  p ON f.produto_id = p.produto_id
WHERE d.ano = 2025
GROUP BY d.mes, p.categoria
ORDER BY d.mes, receita DESC;
```

## Boas práticas
- Definir KPIs alinhados aos objetivos estratégicos antes de construir dashboards.
- Garantir qualidade e governança dos dados na origem (linhagem, catálogo, versões).
- Usar modelos dimensionais (fato/dimensão) para consultas analíticas rápidas e compreensíveis.
- Documentar métricas e suas definições para evitar interpretações divergentes.
- Automatizar o pipeline de atualização dos dados.

## Armadilhas comuns
- Confundir BI com Machine Learning: BI descreve o passado, ML prevê ou decide.
- Dashboards "espaguete" sem foco em decisões, cheios de gráficos irrelevantes.
- Ignorar a granularidade dos dados ao comparar métricas de fontes diferentes.
- Tratar o data warehouse como banco transacional, degradando performance.
- Manter dados duplicados sem regra de atualização, gerando números conflitantes.

## Relacionadas
- [[Data-Science]]
- [[ETL]]
- [[Estatistica]]
- [[Datasets]]