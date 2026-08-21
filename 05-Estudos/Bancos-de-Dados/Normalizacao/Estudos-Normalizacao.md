---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Normalizacao

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Processo de organizar tabelas em formas normais para reduzir redundância, evitar anomalias de inserção, atualização e exclusão, e garantir integridade dos dados.

## Conceitos-chave
- **Dependência funcional:** diz-se que X → Y quando o valor de Y é determinado pelo valor de X.
- **1FN:** valores atômicos, sem grupos repetidos ou múltiplos valores em uma coluna.
- **2FN:** estar em 1FN e não ter dependência parcial — colunas não-chave não dependem de parte da chave composta.
- **3FN:** estar em 2FN e não ter dependência transitiva — colunas não-chave não dependem de outras colunas não-chave.
- **BCNF:** refinamento da 3FN em que toda determinante é uma superchave.
- **Anomalias:** inconsistências de inserção, atualização e exclusão causadas por redundância.
- **Integridade:** o esquema normalizado preserva consistência com menos risco de conflito.

## Exemplos

```sql
-- Antes: redundância e dependência transitiva (viola 3FN)
CREATE TABLE pedidos (
  pedido_id INT PRIMARY KEY,
  cliente   VARCHAR(100),
  cidade    VARCHAR(100)  -- depende do cliente, não do pedido
);

-- 3FN: cidade movida para a tabela clientes
CREATE TABLE clientes (
  id     INT PRIMARY KEY,
  nome   VARCHAR(100),
  cidade VARCHAR(100)
);

CREATE TABLE pedidos (
  pedido_id  INT PRIMARY KEY,
  cliente_id INT REFERENCES clientes(id)
);
```

## Boas práticas
- Normalizar até a 3FN como regra geral de modelagem.
- Identificar dependências funcionais antes de criar o esquema.
- Usar chaves estrangeiras para manter a integridade referencial.
- Somente denormalizar com critério, medindo ganho de performance.

## Armadilhas comuns
- Achar que "mais normalizado é sempre melhor" — leituras com muitos JOINs podem piorar.
- Parar na 1FN achando que a modelagem está resolvida.
- Normalizar em excesso (4FN/5FN) sem necessidade prática.
- Confundir 2FN (dependência parcial) com 3FN (dependência transitiva).

## Relacionadas
- [[Bancos-de-Dados]]
- [[Denormalizacao]]
- [[Indexes]]