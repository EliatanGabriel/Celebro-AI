---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Hash

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Função que mapeia dados de tamanho variável para valores de tamanho fixo, formando a base de hash tables, verificação de integridade e criptografia.

## Conceitos-chave
- **Função hash:** transforma uma chave (string, número, objeto) em um índice ou resumo determinístico.
- **Hash table (tabela de dispersão):** estrutura que usa o hash da chave para armazenar e localizar valores em O(1) médio.
- **Colisões:** duas chaves distintas podem gerar o mesmo índice; são tratadas com encadeamento (lista) ou endereçamento aberto (probing).
- **Fator de carga:** relação entre elementos e capacidade; ao crescer, a tabela precisa redimensionar (rehash).
- **Uso em criptografia:** hash criptográfico (SHA-256, MD5) gera resumos usados em integridade e senhas; a segurança depende da resistência a colisões.
- **Uso em cache e deduplicação:** identificar dados já vistos sem comparar conteúdo completo.

## Exemplos
```python
# Simulação simples de hash table com encadeamento
def hash_simples(chave, capacidade):
    return sum(ord(c) for c in str(chave)) % capacidade

tabela = [[] for _ in range(10)]

def inserir(chave, valor):
    indice = hash_simples(chave, len(tabela))
    for i, (k, v) in enumerate(tabela[indice]):
        if k == chave:          # chave já existe: atualiza
            tabela[indice][i] = (chave, valor)
            return
    tabela[indice].append((chave, valor))

def buscar(chave):
    indice = hash_simples(chave, len(tabela))
    for k, v in tabela[indice]:
        if k == chave:
            return v
    return None
```

```text
// Uso de dicionário (hash table) nativo
dic["nome"] = "Ana"     # insere via hash da chave
nome = dic["nome"]      # acesso O(1) médio
"nome" in dic           # verificação de existência O(1)
```

## Boas práticas
- Escolher uma função hash bem distribuída para evitar aglomeração em poucos índices.
- Usar o mecanismo de hash nativo da linguagem (dict em Python, Map em JS) sempre que possível.
- Para senhas, usar hash com salt e função lenta (bcrypt, argon2), nunca MD5 ou SHA-1.
- Controlar o fator de carga e redimensionar a tabela para manter O(1) médio.
- Usar chaves imutáveis e bem definidas (hash de chaves mutáveis muda e quebra a tabela).

## Armadilhas comuns
- Usar hash criptográfico fraco (MD5, SHA-1) para segurança; estão quebrados para colisões.
- Armazenar senhas sem salt ou com salt fixo, permitindo ataques de tabela rainbow.
- Confiar no O(1) do pior caso: com muitas colisões a hash table degrada para O(n).
- Usar objetos mutáveis como chave de hash table.
- Confundir hash para dispersão (rápido, não seguro) com hash criptográfico (lento, seguro).

## Relacionadas
- [[Estruturas-de-Dados]]
- [[Arrays]]
- [[Algoritmos]]
- [[Estudos-Complexidade]]
- [[JSON]]
- [[Performance]]