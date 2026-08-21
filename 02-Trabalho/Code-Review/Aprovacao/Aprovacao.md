---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Aprovacao

#area/trabalho #trabalho/code-review #conceito

**Resumo:** Consenso da equipe de que a mudança está pronta para integrar.

## Conceitos-chave
- Aprovar: mudança atende aos critérios e pode integrar.
- Comentar: observações sem impedir o merge.
- Solicitar mudanças: apontar bloqueadores que precisam ser corrigidos.
- Gate de qualidade: padrão mínimo acordado pelo time.
- Autonomia responsável: não aprovar sem entender a mudança.

## Exemplos
```
# Decisões típicas de review
- Aprovar quando atende aos critérios de aceite.
- Solicitar mudanças para bugs, falhas de segurança ou código sem testes.
- Comentar (não bloquear) para melhorias opcionais de estilo/leitura.
```

## Boas práticas
- Definir regras claras: quem aprova, quantas aprovações, prazos.
- Aprovar apenas o que se entendeu por completo.
- Comunicar os critérios de aprovação ao time.
- Registrar o motivo ao solicitar mudanças.
- Revisar novamente após as correções antes de aprovar.

## Armadilhas comuns
- Aprovar por pressão ou sem ler o código.
- Bloquear o merge por preferências pessoais.
- Critérios de aprovação inconsistentes entre revisores.
- Solicitar mudanças e não acompanhar o retorno.
- Bypass do processo (merge direto) sem justificativa.

## Relacionadas
- [[Checklist]]
- [[Feedback]]
- [[Best-practices]]
- [[Padroes]]