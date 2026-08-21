---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Zero-Trust

#area/estudos #estudos/seguranca #conceito

**Resumo:** Modelo de segurança que nunca confia implicitamente, exigindo verificação contínua de identidade e dispositivo a cada acesso, independentemente da localização da rede.

## Conceitos-chave
- **"Never trust, always verify":** cada request é autenticado e autorizado, mesmo dentro da rede.
- **Fim do modelo de perímetro:** a rede interna não é tratada como zona confiável (cisco do castelo).
- **Microsegmentação:** dividir a rede em zonas pequenas para limitar movimentação lateral.
- **Verificação contínua:** reavaliar confiança por contexto (identidade, dispositivo, localização, risco).
- **Acesso com menor privilégio:** permissões mínimas, dinâmicas e temporárias.
- **Pilares:** identidade, dispositivos, rede, dados, aplicações e automação de políticas.

## Exemplos
```
# Princípios de uma arquitetura Zero Trust
- Autenticar e autorizar todo request (não apenas o primeiro acesso).
- Validar o dispositivo antes de liberar acessos.
- Aplicar microsegmentação e políticas por workload.
- Monitorar e coletar telemetria de todos os acessos.
- Usar MFA e privilégio mínimo em toda interação.
```

## Boas práticas
- Começar por identidade forte: [[MFA]] e ciclo de vida de credenciais.
- Aplicar princípio do menor privilégio em papel e rede (ver [[RBAC]]).
- Segmentar a rede e restringir tráfego lateral.
- Monitorar continuamente acessos e comportamentos anômalos.
- Implementar de forma incremental, priorizando dados e sistemas críticos.

## Armadilhas comuns
- Achar que Zero Trust é um produto a comprar — é um modelo de arquitetura e processos.
- Tratar apenas o acesso remoto como caso, esquecendo acessos internos e entre serviços.
- Manter contas privilegiadas amplas e permanentes, anulando a verificação contínua.
- Implementar sem telemetria/monitoramento, perdendo a capacidade de resposta.

## Relacionadas
- [[RBAC]]
- [[Firewall]]
- [[Autenticacao]]
- [[MFA]]
- [[Autorizacao]]