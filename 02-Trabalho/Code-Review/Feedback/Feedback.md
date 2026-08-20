---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Feedback

#area/trabalho #trabalho/code-review #conceito

**Resumo:** Comentários construtivos para melhorar a qualidade da mudança.

## Conceitos-chave
- Construtivo: aponta o problema e sugere como melhorar.
- Específico: referencia trechos e cenários concretos.
- Priorizado: distingue bloqueadores de sugestões.
- Tom respeitoso, focado no código, não na pessoa.
- Fechamento: revisar novamente após as correções.

## Exemplos
```
// Comentário vago
"Melhore esse trecho."

// Comentário construtivo
"Aqui a busca é O(n²) e falha com 10k itens.
Sugiro usar um Set para verificar duplicados:
const vistos = new Set(itens.map(i => i.id));
```

## Boas práticas
- Apontar o problema e oferecer caminho de solução.
- Separar bloqueadores (precisam mudar) de sugestões (opcionais).
- Basear-se em fatos do código, não em preferências pessoais.
- Encorajar o autor a responder e questionar.
- Acompanhar o retorno e revisar a nova versão.

## Armadilhas comuns
- Críticas genéricas sem contexto ou sugestão.
- Mixar opinião pessoal com requisito técnico.
- Comentários em tom negativo focados na pessoa.
- Feedback tardio, após o merge ou longe do contexto.
- Ignorar o autor no fechamento dos comentários.

## Relacionadas
- [[Aprovacao]]
- [[Checklist]]
- [[Comunicacao-com-Devs]]