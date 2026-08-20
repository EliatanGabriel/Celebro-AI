---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# MFA

#area/estudos #estudos/seguranca #conceito

**Resumo:** Autenticação multifator: exige duas ou mais provas de identidade de categorias diferentes (saber, ter, ser) para conceder acesso.

## Conceitos-chave
- **Fatores distintos:** algo que você sabe (senha), algo que você tem (token, celular, chave física) e algo que você é (biometria).
- **2FA:** caso específico com dois fatores; MFA pode ter dois ou mais.
- **TOTP:** código que muda a cada 30s, derivado de segredo compartilhado (Google Authenticator, Authy).
- **Notificações push e FIDO2/WebAuthn:** chaves de segurança (hardware) e passkeys, resistentes a phishing.
- **Recovery codes:** códigos de contingência para acesso quando o segundo fator é perdido.
- **Elevação de risco:** MFA pode ser exigido só em situações sensíveis (novo dispositivo, pagamento).

## Exemplos
```python
# Geração de TOTP (conceitual)
import pyotp

segredo = pyotp.random_base32()          # segredo compartilhado na matrícula
totp = pyotp.TOTP(segredo)               # padrão RFC 6238
codigo = totp.now()                      # código válido por 30s
assert totp.verify(codigo, valid_window=1)
```

## Boas práticas
- Exigir MFA para contas administrativas e acessos sensíveis.
- Preferir métodos resistentes a phishing (WebAuthn) sobre SMS quando possível.
- Emitir recovery codes e instruir o usuário a guardá-los com segurança.
- Registrar novos dispositivos com verificação e notificar o titular.
- Não obrigar MFA onde o risco não justifica, equilibrando usabilidade.

## Armadilhas comuns
- Considerar SMS um fator forte — é suscetível a SIM swap e interceptação.
- Usar dois fatores da mesma categoria (ex.: senha + código por e-mail).
- Permitir desabilitar MFA sem reautenticação e sem aviso.
- Compartilhar o segredo TOTP ou códigos de recuperação com terceiros.

## Relacionadas
- [[Biometria]]
- [[Senhas]]
- [[Credenciais]]
- [[Segredos]]
- [[Autenticacao]]
- [[Tokens]]