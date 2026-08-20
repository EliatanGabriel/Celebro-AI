---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# OWASP

#area/estudos #estudos/seguranca #conceito

**Resumo:** Open Worldwide Application Security Project: organização sem fins lucrativos que publica padrões, ferramentas e o famoso Top 10 de riscos de segurança em aplicações web.

## Conceitos-chave
- **OWASP Top 10:** ranking atualizado dos riscos mais críticos em apps web (Injection, Broken Access Control, Cryptographic Failures etc.).
- **ASVS (Application Security Verification Standard):** checklist de requisitos por nível de segurança (1 a 3).
- **Cheat Sheets:** guias práticos para mitigar cada risco (auth, password storage, CSRF, XSS).
- **ZAP:** ferramenta gratuita de teste de segurança (DAST) mantida pelo projeto.
- **SAMM:** modelo para amadurecer o programa de segurança em uma organização.
- **Uso em ciclos:** guia pentests (ver [[Pentest]]) e desenvolvimento seguro desde o design.

## Exemplos
```text
# OWASP Top 10 (2021) — principais
01 Broken Access Control
02 Cryptographic Failures
03 Injection
04 Insecure Design
05 Security Misconfiguration
06 Vulnerable and Outdated Components
07 Identification and Authentication Failures
08 Software and Data Integrity Failures
09 Security Logging and Monitoring Failures
10 Server-Side Request Forgery (SSRF)
```

## Boas práticas
- Usar o Top 10 como checklist de review de código e pentest.
- Adotar o ASVS como critério objetivo de "pronto para produção".
- Aplicar cheatsheets da OWASP no desenvolvimento (senhas, headers, TLS).
- Incluir testes de segurança automatizados no pipeline (SAST/DAST).
- Tratar as falhas de logging/monitoring com a mesma seriedade dos exploits.

## Armadilhas comuns
- Tratar o Top 10 como lista exaustiva — ele é um ranking, não a totalidade de riscos.
- Ignorar riscos "menos técnicos" como configuração incorreta e componentes desatualizados.
- Usar o Top 10 como defesa contra todo ataque (ex.: não cobre engenharia social).
- Confiar só na ferramenta ZAP e esquecer validação humana e revisão de código.

## Relacionadas
- [[SQL-Injection]]
- [[XSS]]
- [[CSRF]]
- [[Pentest]]
- [[Vulnerabilidades]]