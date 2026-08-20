---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Patch

#area/estudos #estudos/seguranca #conceito

**Resumo:** Correção de software que elimina vulnerabilidades conhecidas e bugs; aplicar patches em tempo hábil é a principal defesa contra exploração.

## Conceitos-chave
- **Tipos de patch:** correção de segurança, bugfix, feature e atualização de dependências.
- **CVE e severidade:** CVEs identificam vulnerabilidades; CVSS pontua severidade para priorizar.
- **Patch management:** processo de identificar, testar, aplicar e verificar correções.
- **Janela de exposição:** tempo entre o anúncio da vulnerabilidade e a aplicação do patch — período crítico de exploração.
- **Zero-day:** vulnerabilidade sem patch disponível; mitigação é limitada.
- **Rollback:** plano para reverter um patch que quebra compatibilidade ou estabilidade.

## Exemplos
```bash
# Debian/Ubuntu
apt update && apt upgrade -y

# RHEL/CentOS
dnf update --security

# Dependências de projeto (exemplo)
npm audit fix
```

## Boas práticas
- Automatizar detecção de vulnerabilidades (scan de dependências, SBOM).
- Priorizar por severidade e exposição real, não aplicar tudo sem critério.
- Testar patches em staging antes da produção, especialmente os que mudam comportamento.
- Manter um inventário de ativos para saber o que atualizar.
- Estabelecer SLA de aplicação: crítico em dias, alto em semanas.

## Armadilhas comuns
- Adiar patches "para não quebrar nada" e ser explorado em uma vuln conhecida.
- Aplicar patch sem testar e quebrar a aplicação em produção.
- Esquecer componentes legados, bibliotecas transitivas e imagens de contêiner.
- Achar que "patch aplicado" é "seguro": configurações erradas seguem expondo.

## Relacionadas
- [[Vulnerabilidades]]
- [[DevOps]]
- [[CI-CD-Conceito]]
- [[Antivirus]]
- [[Pentest]]