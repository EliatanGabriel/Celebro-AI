---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Checklist

#area/trabalho #trabalho/code-review #conceito

**Resumo:** Lista de verificação antes de aprovar uma mudança.

## Conceitos-chave
- Funcionalidade: o código faz o que deveria?
- Estilo: segue as convenções e boas práticas?
- Testes: há cobertura dos novos cenários?
- Segurança: sem dados sensíveis, validação e autorização corretas?
- Documentação: o que mudou está atualizado?

## Exemplos
```
# Checklist de review do time de QA
- [ ] Entendi o objetivo da mudança e os critérios de aceite
- [ ] Código legível, consistente com as convenções
- [ ] Testes automatizados para os novos fluxos
- [ ] Sem regressões em fluxos existentes
- [ ] Sem segredos, dados sensíveis ou logs indevidos
- [ ] Documentação (API, changelog) atualizada
```

## Boas práticas
- Adaptar o checklist à realidade e riscos do projeto.
- Verificar testes, segurança e performance além do funcional.
- Aplicar o checklist de forma consistente em todo review.
- Focar nos itens de maior risco primeiro.
- Evoluir o checklist com os aprendizados do time.

## Armadilhas comuns
- Checklist genérico demais que vira burocracia.
- Marcar itens sem de fato verificar o código.
- Esquecer itens de segurança e performance.
- Checklist longo demais, ignorado pelos revisores.
- Não atualizar o checklist com novos padrões.

## Relacionadas
- [[Aprovacao]]
- [[Best-practices]]
- [[Seguranca-review]]