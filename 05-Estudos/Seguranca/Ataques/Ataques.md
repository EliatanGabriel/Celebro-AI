---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Ataques

#area/estudos #estudos/seguranca #conceito

**Resumo:** Tipos de ameaças cibernéticas que exploram vulnerabilidades técnicas ou humanas para comprometer sistemas, dados e pessoas.

## Conceitos-chave
- **Malware:** software malicioso — vírus, worms, trojans, spyware e ransomware.
- **Phishing e engenharia social:** manipulam o fator humano, a camada mais fraca.
- **DoS/DDoS:** esgotam recursos para indisponibilizar serviços (SYN flood, amplificação UDP).
- **Man-in-the-middle (MITM):** intercepta comunicação entre duas partes (ARP spoofing, DNS spoofing).
- **Injeção:** SQL Injection, XSS e command injection exploram inputs mal validados.
- **Zero-day:** exploração de vulnerabilidade sem patch conhecido.
- **Credential stuffing / brute force:** tentativas de login em massa com listas de senhas vazadas.

## Exemplos
```python
# Simulação conceitual de brute force (educacional)
import itertools, requests

charset = "abcdef"
for length in range(1, 4):
    for guess in itertools.product(charset, repeat=length):
        resp = requests.post("https://exemplo/login", data={"senha": "".join(guess)})
        if resp.status_code == 200:
            print("senha encontrada:", "".join(guess))
            break
```

## Boas práticas
- Aplicar princípio do menor privilégio e defesa em profundidade.
- Atualizar software e aplicar patches (ver [[Patch]]).
- Validar e parametrizar toda entrada de usuário.
- Educar usuários e habilitar [[MFA]] para mitigar phishing e credential stuffing.
- Monitorar e auditar logs para detecção precoce.

## Armadilhas comuns
- Subestimar o fator humano, focando apenas em tecnologia.
- Considerar a rede interna "confiável" por padrão (ver [[Zero-Trust]]).
- Testes de intrusão sem autorização, o que configura crime.
- Tratar todos os ataques igualmente, sem classificar impacto e urgência.

## Relacionadas
- [[OWASP]]
- [[Phishing]]
- [[Ransomware]]
- [[Engenharia-Social]]
- [[SQL-Injection]]
- [[XSS]]
- [[Pentest]]