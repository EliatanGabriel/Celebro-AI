---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Auditoria

#area/estudos #estudos/seguranca #conceito

**Resumo:** Revisão sistemática de logs, permissões e controles para verificar conformidade, detectar anomalias e dar suporte a investigações forenses.

## Conceitos-chave
- **Logs como evidência:** registros de autenticação, acesso, alterações e erros formam o trilho de auditoria (audit trail).
- **Imutabilidade:** logs de auditoria não devem ser alteráveis pelo próprio sistema auditado (append-only).
- **Revisão de permissões:** verificar periodicamente se os acessos concedidos ainda são necessários (ver [[RBAC]]).
- **Conformidade:** atender requisitos legais e normativos como [[GDPR]], LGPD e SOC 2.
- **Forense:** reconstrução da linha do tempo de um incidente a partir dos registros.
- **Frameworks:** ISO 27001, NIST, CIS Controls orientam o que e como auditar.

## Exemplos
```bash
# Quem logou e quando (exemplo com auth.log)
grep "Accepted password" /var/log/auth.log | tail -20

# Eventos de sudo
grep "sudo:" /var/log/auth.log | tail -20
```

## Boas práticas
- Centralizar logs em SIEM com retenção definida e backup off-site.
- Sincronizar relógios (NTP) para correlação temporal precisa.
- Realizar auditorias recorrentes, não apenas após incidentes.
- Definir quem tem acesso aos logs e proteger contra adulteração.
- Automatizar alertas para padrões anômalos.

## Armadilhas comuns
- Coletar logs sem retenção ou sem proteção contra alteração, perdendo valor probatório.
- Confundir auditoria com monitoramento em tempo real — são complementares, não sinônimos.
- Revisar permissões só no papel, sem validar contra a realidade dos acessos.
- Não testar se a ferramenta de logging sobrevive a um ataque que a desliga.

## Relacionadas
- [[Logging]]
- [[RBAC]]
- [[GDPR]]
- [[Privacidade]]
- [[Dados]]