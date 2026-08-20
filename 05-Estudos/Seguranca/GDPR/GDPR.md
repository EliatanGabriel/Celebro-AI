---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# GDPR

#area/estudos #estudos/seguranca #conceito

**Resumo:** General Data Protection Regulation: regulamento europeu de proteção de dados pessoais que define direitos, obrigações e sanções para quem processa dados de cidadãos da UE.

## Conceitos-chave
- **Dados pessoais:** qualquer informação relativa a pessoa identificada ou identificável (inclusive IP, cookies).
- **Base legal para processamento:** consentimento, contrato, obrigação legal, interesse legítimo etc.
- **Direitos do titular:** acesso, retificação, apagamento ("direito ao esquecimento"), portabilidade e oposição.
- **Princípios:** licitude, minimização, limitação de finalidade, exatidão e segurança.
- **Privacidade por design e por padrão:** proteção embutida desde a concepção do sistema.
- **Notificação de violação:** vazamentos devem ser reportados à autoridade (e, em certos casos, aos titulares) em até 72h.

## Exemplos
```text
# Decisões-chave do GDPR em 1 linha cada
- Consentimento: livre, específico, informado e revogável.
- DPIA: avaliação de impacto exigida para processamento de alto risco.
- Transferência internacional: exige cláusulas contratuais ou adequação.
- Multas: até 20 milhões EUR ou 4% do faturamento global.
```

## Boas práticas
- Mapear e documentar todos os processamentos de dados (registro de atividades).
- Aplicar minimização: coletar só o necessário para a finalidade declarada.
- Implementar segurança técnica (criptografia, acesso) e procedimental.
- Definir canais para exercício de direitos dos titulares.
- No Brasil, alinhar também com a LGPD, que tem estrutura semelhante.

## Armadilhas comuns
- Confundir consentimento com única base legal — há bases adequadas a cada operação.
- Achar que anonimizar corretamente remove do escopo; pseudonimização não anonimiza.
- Tratar GDPR como "problema europeu": se atende cidadãos da UE, aplica-se.
- Somente responder a violações de dados quando a mídia descobre — o prazo de 72h exige preparo.

## Relacionadas
- [[Privacidade]]
- [[Auditoria]]
- [[Dados]]