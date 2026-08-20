---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Ransomware

#area/estudos #estudos/seguranca #conceito

**Resumo:** Malware que criptografa os dados da vítima e exige resgate para liberar o acesso, frequentemente distribuído via phishing e RDP exposto.

## Conceitos-chave
- **Criptografia de dados:** dados e backups acessíveis são cifrados, tornando-os inúteis sem a chave.
- **Cadeia de infecção:** phishing → execução → movimentação lateral → exfiltração → criptografia.
- **Dupla extorsão:** além de cifrar, vazam dados e ameaçam publicá-los.
- **Exfiltração antes do ransomware:** muitos grupos roubam dados antes de ativar a criptografia.
- **Resgate (ransom):** pagar não garante a chave e financia o crime; decisão legal/política complexa.
- **Mitigação principal:** backups imutáveis/off-line e resposta a incidentes testada.

## Exemplos
```
# Vetores de entrada comuns
- E-mail de phishing com macro/URL maliciosa
- RDP com credenciais fracas exposto à internet
- Downloads "piratas" e engenharia social
- Vulnerabilidades em aplicações expostas
```

## Boas práticas
- Manter backups imutáveis e testados (regra 3-2-1, ver [[Backup-Seg]]).
- Aplicar patches e limitar superfície de exposição (RDP não deve ficar público).
- Usar [[MFA]], antivírus/EDR e segmentação de rede.
- Treinar usuários contra [[Phishing]] e limitar privilégios administrativos.
- Ter plano de resposta e simulações (tabletop) de incidente.

## Armadilhas comuns
- Achar que só grandes empresas são alvo — SMBs são as principais vítimas.
- Manter backups no mesmo host/rede, criptografados junto com os dados.
- Pagar resgate rápido por desespero, sem avaliar alternativas e sem base legal.
- Confiar em "decriptadores" gratuitos de casos comuns como solução garantida.

## Relacionadas
- [[Antivirus]]
- [[Phishing]]
- [[Backup-Seg]]
- [[Ataques]]
- [[Criptografia]]