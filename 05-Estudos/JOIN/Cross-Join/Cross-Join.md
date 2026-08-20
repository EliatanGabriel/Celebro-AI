---
type: concept
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# CROSS JOIN

#area/estudos #join #conceito #sql #join #produto-cartesiano

**Resumo:** Combina cada linha de uma tabela com todas as linhas da outra, produzindo o produto cartesiano sem condição de junção.

## Conceitos-chave
- **Produto cartesiano:** com m e n linhas, o resultado tem m × n linhas.
- **Sem condição ON:** não existe chave de junção; todas as combinações possíveis são geradas.
- **Uso raro:** útil para gerar combinações, matrizes de parâmetros ou preencher séries de datas.
- **Cuidado com volume:** tabelas grandes tornam o resultado gigante e o custo alto.
- **Sintaxe alternativa:** `FROM a, b` sem cláusula `WHERE` gera o mesmo efeito.

## Exemplos
```sql
-- Todas as combinações de cores e tamanhos
SELECT cores.nome, tamanhos.nome
FROM cores
CROSS JOIN tamanhos;

-- Séries de datas × produtos
SELECT d.data, p.produto
FROM (SELECT generate_series('2026-08-01'::date, '2026-08-02'::date, '1 day') AS data) d
CROSS JOIN produtos p;
```

## Boas práticas
- Garantir que o produto cartesiano seja intencional e que o tamanho do resultado seja aceitável.
- Preferir `CROSS JOIN` explícito a `FROM a, b` para deixar a intenção clara.
- Aplicar filtros ou limites em resultados grandes.

## Armadilhas comuns
- Produzir produto cartesiano acidental ao esquecer a condição de junção em um JOIN normal.
- Usar CROSS JOIN em tabelas grandes, gerando bilhões de linhas e travando o banco.
- Assumir que o resultado mantém ordem ou correspondência lógica, quando é apenas combinação.

## Relacionadas
- [[Inner-Join]]
- [[Left-Join]]
- [[Estudos-SQL]]