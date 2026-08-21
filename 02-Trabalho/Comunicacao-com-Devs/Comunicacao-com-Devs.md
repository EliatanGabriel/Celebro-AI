---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Comunicacao com Devs

#area/trabalho #trabalho/comunicacao-com-devs #conceito

**Resumo:** Habilidades de comunicação eficaz com desenvolvedores.

## Conceitos-chave
- Comunicação clara acelera a triagem e correção de bugs e reduz atrito entre QA e dev.
- Bases: clareza, contexto, empatia e feedback objetivo.
- O bug report e o canal escolhido são a "linguagem" entre QA e dev.

## Exemplos
```
Bom: "Ao salvar o pedido com cupom vencido, a API retorna 422 com
'coupon_expired', mas a UI mostra 'erro genérico'. Esperado: mostrar
'Cupom expirado'. Print e request em anexo. Ambiente: staging, v1.4.0."
Ruim: "Não consegui salvar um pedido, tá bugado."
```

## Boas práticas
- Reportar o que acontece, com dados e evidência, e não julgamentos ("seu código está errado").
- Distinguir bug de mudança de comportamento; quando for dúvida, perguntar antes.
- Priorizar canais assíncronos documentados (Jira/Trello) e confirmar no Slack/1:1.
- Dar contexto de negócio quando ajudar a priorizar.

## Armadilhas comuns
- Comunicação vaga sem passos nem evidências.
- Tratar dev como responsável único; o bug é do produto, não da pessoa.
- Discutir decisões de correção em canal errado e perder o registro.
- Excesso de jargão de QA que o dev não entende, ou o oposto.

## Relacionadas
- [[Feedback]]
- [[Reuniao-Tecnica]]
- [[Code-Review]]
- [[Slack]]