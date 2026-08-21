---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Clean Code

#area/estudos #estudos/programacao #conceito #codigo #qualidade #boas-praticas

**Resumo:** Princípios para escrever código legível, simples e de fácil manutenção, priorizando a leitura por humanos sobre truques de otimização.

## Conceitos-chave
- **Nomes claros:** nomes de variáveis, funções e classes devem expressar intenção e evitar abreviações ambíguas.
- **Funções pequenas:** funções com um único propósito, poucas linhas e nomes que descrevem o que fazem.
- **Sem repetição (DRY):** extrair lógica duplicada para evitar divergências futuras.
- **Comentários úteis:** comentar o "porquê", nunca o "o quê"; o código deve se auto-explicar.
- **Regra do escoteiro:** deixar o código um pouco melhor do que se encontrou a cada alteração.

## Exemplos
```python
# Ruim: nome vago e várias responsabilidades
def p(d):
    t = 0
    for i in d:
        t += i.get("v", 0)
    return t / len(d) * 100

# Bom: nome claro e função com um propósito
def percentual_concluido(tarefas):
    total = sum(t.valor for t in tarefas)
    return total / len(tarefas) * 100
```

## Boas práticas
- Nomear funções com verbos e variáveis com substantivos.
- Manter funções pequenas o suficiente para caberem na tela.
- Aplicar a regra do três: na terceira repetição, extraia a lógica.
- Escrever testes que documentam o comportamento esperado.

## Armadilhas comuns
- Confundir "código curto" com "código limpo", usando nomes de uma letra.
- Comentar código morto em vez de removê-lo.
- Otimizar prematuramente com microtruques que sacrificam a legibilidade.
- Criar funções gigantes que misturam várias responsabilidades.

## Relacionadas
- [[SOLID]]
- [[Paradigmas]]
- [[Debug]]