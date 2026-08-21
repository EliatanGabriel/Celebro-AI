---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Conflitos

#area/trabalho #trabalho/code-review #conceito

**Resumo:** Divergências entre revisores ou entre versões do código.

## Conceitos-chave
- Merge conflict: alterações em trechos sobrepostos entre branches.
- Discordância técnica entre revisores sobre a melhor solução.
- Decisão: resolver por dados, critérios e consenso.
- Mediação: envolver mais pessoas para decidir impasses.
- Comunicação aberta para evitar conflitos pessoais.

## Exemplos
```
# Resolver conflito de merge
git checkout main
git pull
git checkout minha-branch
git merge main
# editar os arquivos conflitantes
git add arquivo
git commit -m "merge: resolve conflitos com main"
```

## Boas práticas
- Integrar a main com frequência para reduzir conflitos.
- Dividir mudanças pequenas e focadas.
- Discutir divergências técnicas com base em fatos.
- Resolver conflito entendendo as duas intenções, não só aceitando.
- Escalar impasses para decisão coletiva quando necessário.

## Armadilhas comuns
- Resolver conflito descartando o trabalho do outro.
- Discordância virando disputa pessoal.
- Adiar a integração e gerar conflitos gigantes.
- Force push ou sobrescrita de commits de outros.
- Não documentar a decisão tomada no impasse.

## Relacionadas
- [[Feedback]]
- [[Comunicacao-com-Devs]]