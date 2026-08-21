---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Steps-to-reproduce

#area/trabalho #trabalho/bug-report #conceito

**Resumo:** Sequência numerada de passos que levam à ocorrência do bug.

## Conceitos-chave
- Cada passo é uma ação concreta e observável, não uma intenção.
- A sequência precisa ser suficiente para outro QA ou dev reproduzir sem adivinhação.
- Steps bem escritos economizam tempo de investigação e evitam idas e vindas.

## Estrutura de um bom bug report
- **Pré-condições:** estado inicial (login, dados, ambiente, versão).
- **Passos numerados** (1., 2., 3.) escritos no imperativo: "Clique em...", "Preencha...".
- **Entradas exatas:** valores usados em formulários, filtros e pesquisas.
- **Resultado de cada passo** quando relevante para identificar onde o fluxo quebra.
- **Passo final:** a ação que dispara o comportamento incorreto.

## Boas práticas
- Validar os passos em um ambiente limpo antes de reportar.
- Usar dados fictícios ou de teste que o dev consiga reproduzir.
- Indicar frequência de ocorrência (sempre/intermitente).
- Anexar evidências correspondentes aos passos.

## Armadilhas comuns
- Passos dependentes de ações anteriores não documentadas.
- Misturar passos de reprodução com passos de verificação de correção.
- Omitir o passo que realmente causa o bug (tempo de espera, cache, refresh).
- Escrever passos longos demais sem isolar o mínimo necessário.

## Relacionadas
- [[Ambiente]]
- [[Reproducao]]
- [[Expected-vs-actual]]
- [[Evidencias]]