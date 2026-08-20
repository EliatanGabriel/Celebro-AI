---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# R

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem especializada em estatística e análise de dados, com operações vetorizadas, data frames e um ecossistema de pacotes (CRAN) voltado à ciência de dados e visualização.

## Conceitos-chave
- Multiparadigma: funcional com suporte a OO (S3/S4) e programação vetorizada.
- Tipagem dinâmica: vetores, listas, data frames e fatores têm coerção automática de tipos.
- Interpretada: executada via interpretador R (com JIT limitado); foco em análise exploratória.
- Uso principal em estatística, bioinformática, econometria, machine learning e visualização.
- Data frame como estrutura central: tabela retangular com colunas nomeadas e tipos por coluna.
- Pacotes principais: ggplot2 (visualização), dplyr (manipulação), tidyr (limpeza), stats (testes).
- Particularidade: CRAN (Comprehensive R Archive Network) e integração com RStudio/Posit e notebooks.

## Exemplos
```r
library(dplyr)

# Data frame de exemplo
dados <- data.frame(
  nome  = c("Ana", "Bruno", "Carlos"),
  idade = c(30, 22, 41)
)

# Manipulação com dplyr (pipe)
media_maiores <- dados %>%
  filter(idade >= 25) %>%
  summarise(media = mean(idade))

print(media_maiores)  #   media / 35.5

# Função e vetorização
dobro <- function(x) x * 2
print(dobro(c(1, 2, 3)))  # 2 4 6
```

## Boas práticas
- Use `<-` para atribuição (padrão idiomático) e operações vetorizadas em vez de loops.
- Prefira o pipe `%>%` (ou `|>`) e dplyr para fluxos de manipulação legíveis.
- Nomeie colunas sem espaços ou acentos; evite caracteres especiais.
- Documente scripts e mantenha reprodutibilidade com `renv`/`packrat`.
- Use projetos do RStudio e versionamento (Git) desde o início da análise.

## Armadilhas comuns
- Loop explícito em vez de operação vetorizada, tornando o código lento.
- `c(1, "a")` coage tudo para caractere silenciosamente, mudando o tipo.
- Fatores: `as.factor` pode ordenar niveis alfabeticamente e causar resultados inesperados.
- Confundir `=` (em chamadas nomeadas) com `<-` (atribuição real).
- Faltas de NA não tratadas: `mean()` retorna `NA` sem `na.rm = TRUE`.

## Relacionadas
- [[Python]]