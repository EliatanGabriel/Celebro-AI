---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Vulnerabilidades

#area/estudos #estudos/seguranca #conceito

**Resumo:** Falhas em software, hardware ou configuração que podem ser exploradas para comprometer confidencialidade, integridade ou disponibilidade de um sistema.

## Conceitos-chave
- **CVE:** identificador padronizado de vulnerabilidade conhecida (CVE-2024-xxxx).
- **CVSS:** score de severidade (0-10) que orienta priorização de correção.
- **Exploit:** código ou técnica que explora a vulnerabilidade; exploit público reduz a janela de reação.
- **Classificação:** por origem (software, configuração), por vetor (rede, física) e por tipo (injeção, auth, XSS).
- **Vulnerabilidade vs. ameaça vs. risco:** falha (vuln) + agente (ameaça) × probabilidade/impacto = risco.
- **Gestão:** scan, inventário, priorização, patch (ver [[Patch]]) e verificação contínua.

## Exemplos
```text
# Exemplo de estrutura de um CVE
CVE-2021-44228  # Log4Shell
Severidade: 10.0 (CVSS)
Vetor: entrada de dados processada por Log4j
Mitigação: atualizar Log4j ou desativar lookup JNDI

# Caminho de gestão de vulnerabilidade
Descobrir → Classificar (CVSS) → Priorizar → Remediar → Verificar
```

## Boas práticas
- Manter inventário de ativos e software para saber o que está exposto.
- Automatizar scans contínuos (SAST/DAST, scanners de dependências).
- Priorizar por severidade + exposição real + exploit público, não só pelo CVSS.
- Aplicar patches dentro de prazos definidos e testar remediação.
- Reduzir superfície de ataque (menos serviços expostos, menor privilégio).

## Armadilhas comuns
- Confundir vulnerabilidade com risco: a falha existe, o risco depende do contexto.
- Priorizar só pelo CVSS sem considerar se o sistema está exposto.
- Ignorar vulnerabilidades em dependências transitivas e imagens de contêiner.
- Não revalidar após o patch — muitas falhas voltam por configuração indevida.

## Relacionadas
- [[Pentest]]
- [[Patch]]
- [[OWASP]]
- [[Ataques]]
- [[SQL-Injection]]
- [[XSS]]