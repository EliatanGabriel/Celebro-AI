---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Hashing

#area/estudos #estudos/seguranca #conceito

**Resumo:** Função de via única que transforma dados em um resumo (digest) de tamanho fixo, usado para verificar integridade e armazenar senhas sem expô-las.

## Conceitos-chave
- **Determinístico e irreversível:** mesma entrada produz mesmo hash; não é possível "desfazer" para a entrada original.
- **Propriedades:** resistência a colisão, pré-imagem e segunda pré-imagem.
- **Hashing vs. criptografia:** hashing não tem chave e não é reversível; criptografia é reversível com chave (ver [[Criptografia]]).
- **Algoritmos gerais:** SHA-256, SHA-3 — para integridade/assinatura, não para senhas.
- **Hashing de senhas:** bcrypt, scrypt, argon2 (lentos, com salt) — resistentes a ataques de força bruta e GPU.
- **Salt:** valor aleatório por senha que impede rainbow tables e equalização de hashes iguais.

## Exemplos
```python
# Integridade de arquivo (SHA-256)
import hashlib

h = hashlib.sha256(b"conteudo do arquivo").hexdigest()
print(h)

# Senha com bcrypt (Python)
import bcrypt
hash_senha = bcrypt.hashpw(b"senha-forte", bcrypt.gensalt(rounds=12))
assert bcrypt.checkpw(b"senha-forte", hash_senha)
```

## Boas práticas
- Para senhas, usar bcrypt/scrypt/argon2 com salt e custo adequado, nunca SHA/MD5 puro.
- Verificar integridade de downloads/backups com hash e fonte confiável do valor esperado.
- Ajustar o custo do hash conforme o hardware atual e revisar periodicamente.
- Para assinaturas e HMAC, usar funções recomendadas (SHA-2/3) e chaves bem guardadas.

## Armadilhas comuns
- Usar MD5/SHA1 para senhas — são rápidos demais para brute force.
- Hashear sem salt: hashes idênticos revelam senhas idênticas e rainbow tables facilitam a quebra.
- Confundir hashing com criptografia: não é possível "decifrar" um hash.
- Usar hash "duplo" (hash do hash) ou variações caseiras — a segurança está no algoritmo testado, não em truques.

## Relacionadas
- [[Senhas]]
- [[Criptografia]]
- [[Segredos]]