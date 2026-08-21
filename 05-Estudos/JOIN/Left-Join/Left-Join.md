---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# LEFT JOIN

#area/estudos #estudos/join #conceito #sql #estudos/join #consultas

**Resumo:** Retorna todas as linhas da tabela esquerda e apenas as correspondentes da direita, preenchendo com NULL quando não há correspondência.

## Conceitos-chave
- **Tabela preservada:** todas as linhas da tabela à esquerda permanecem no resultado.
- **Valores nulos:** para linhas sem correspondência, as colunas da tabela direita vêm como NULL.
- **Sintaxe:** `SELECT ... FROM a LEFT JOIN b ON a.id = b.fk`.
- **Uso prático:** encontrar registros órfãos (`WHERE b.id IS NULL`), como pedidos sem pagamento.
- **Diferença para INNER:** o INNER remove sem correspondência; o LEFT mantém todas as linhas da esquerda.

## Exemplos
```sql
SELECT clientes.nome, pedidos.id
FROM clientes
LEFT JOIN pedidos ON pedidos.cliente_id = clientes.id;

-- Clientes que nunca fizeram pedido
SELECT clientes.nome
FROM clientes
LEFT JOIN pedidos ON pedidos.cliente_id = clientes.id
WHERE pedidos.id IS NULL;
```

## Boas práticas
- Colocar filtros das colunas da tabela direita no `WHERE` apenas quando quiser forçar correspondência (mas então prefira INNER JOIN).
- Usar `IS NULL` (nunca `= NULL`) ao filtrar ausências.
- Documentar quando o LEFT JOIN é intencional para não confundir a cardinalidade esperada.

## Armadilhas comuns
- Filtrar a tabela direita no `WHERE` (ex.: `WHERE pedidos.valor > 100`) e transformar o LEFT em INNER sem perceber.
- Assumir que a tabela esquerda é sempre a listada primeiro no `FROM`, o que vale na sintaxe padrão.
- Tratar NULLs como valores de negócio reais, contaminando agregações.

## Relacionadas
- [[Inner-Join]]
- [[Cross-Join]]
- [[Estudos-SQL]]
- [[Indexes]]