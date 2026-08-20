---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Criptografia

#area/estudos #estudos/seguranca #conceito

**Resumo:** Técnica de transformar dados legíveis em formato cifrado, de modo que apenas quem possui a chave correta possa ler o conteúdo original.

## Conceitos-chave
- **Cifra simétrica (AES):** mesma chave para cifrar e decifrar; rápida, usada para dados em massa.
- **Cifra assimétrica (RSA, ECC):** par de chaves público/privado; usada para troca de chaves e assinaturas.
- **Cifrar vs. hashear:** criptografia é reversível (com chave); hashing é de via única (ver [[Hashing]]).
- **Confidencialidade, integridade e autenticidade:** criptografia protege o sigilo; MACs/assinaturas garantem integridade e origem.
- **Em trânsito vs. em repouso:** TLS/HTTPS protegem o tráfego; criptografia de disco/banco protege dados salvos.
- **Gerenciamento de chaves:** a segurança depende do sigilo da chave, não do algoritmo (princípio de Kerckhoffs).

## Exemplos
```python
# Simétrica (AES via cryptography)
from cryptography.fernet import Fernet

chave = Fernet.generate_key()
cifra = Fernet(chave)
token = cifra.encrypt(b"dado secreto")
# ... decifrar: cifra.decrypt(token)
```

## Boas práticas
- Usar algoritmos modernos e padronizados (AES-256, ChaCha20, ECDHE), nunca cifras próprias.
- Cifrar dados em repouso e em trânsito por padrão.
- Guardar chaves em HSM ou secret manager, separadas dos dados (ver [[Segredos]]).
- Rotacionar chaves e usar AEAD (ex.: AES-GCM) para garantir autenticidade.
- Seguir recomendações atuais (NIST/OWASP) e evitar algoritmos legados (DES, RC4, MD5).

## Armadilhas comuns
- Implementar criptografia própria ou usar modos inseguros (ex.: ECB) — uso incorreto enfraquece tudo.
- Armazenar a chave junto com os dados cifrados, anulando a proteção.
- Confundir criptografia com hashing ou com anonimização de dados.
- Achar que criptografar substitui controle de acesso e monitoramento.

## Relacionadas
- [[TLS]]
- [[HTTPS]]
- [[Hashing]]
- [[Segredos]]
- [[Ransomware]]