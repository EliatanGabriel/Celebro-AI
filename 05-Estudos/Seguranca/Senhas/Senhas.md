---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Senhas

#area/estudos #estudos/seguranca #conceito

**Resumo:** Credenciais secretas usadas para autenticação; devem ser fortes, únicas por serviço e armazenadas apenas como hash com salt.

## Conceitos-chave
- **Força da senha:** comprimento importa mais que complexidade; senhas longas (passphrases) resistem melhor a brute force.
- **Armazenamento seguro:** hash com salt e algoritmo lento (bcrypt, scrypt, argon2 — ver [[Hashing]]).
- **Reuso:** a mesma senha em vários serviços amplifica qualquer vazamento (credential stuffing).
- **Gerenciadores:** guardam senhas únicas e fortes, reduzindo a memória e o reuso.
- **Políticas:** MFA preferível a forçar expiração frequente; bloquear reuso e listas vazadas.
- **Vazamento:** nunca enviar senhas por e-mail/chat; redefinição por link seguro, nunca devolver a senha.

## Exemplos
```python
# Gerar passphrase forte (exemplo)
import secrets
palavras = ["sol", "lua", "mar", "porta", "tigre"]
senha = "-".join(secrets.choice(palavras) for _ in range(5))
print(senha)
```

```
# Critérios práticos de uma boa senha
- Mínimo 12-16 caracteres (passphrase).
- Única por serviço.
- Preferir aleatoriedade gerada por gerenciador.
- Habilitar MFA como segunda camada.
```

## Boas práticas
- Usar gerenciador de senhas com master password forte e MFA.
- Adotar passphrases (frases longas) em vez de trocas de símbolos.
- Nunca reutilizar senhas entre serviços importantes.
- Verificar se a senha aparece em vazamentos (HaveIBeenPwned).
- Armazenar apenas hash + salt, com custo alto, no servidor.

## Armadilhas comuns
- Exigir expiração frequente de senha — estudos mostram que incentiva senhas fracas e reuso.
- Usar padrões previsíveis: datas, nomes, "senha123", sequências.
- Guardar senhas em planilhas, notas do celular ou post-its.
- Achar que trocar símbolos (P@ssw0rd) é forte — crackers já cobrem essas variações.

## Relacionadas
- [[MFA]]
- [[Credenciais]]
- [[Segredos]]
- [[Hashing]]
- [[Autenticacao]]