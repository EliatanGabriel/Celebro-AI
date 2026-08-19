---
type: concept
area: faculdade
status: active
created: "2026-08-19"
updated: "2026-08-19"
---

# Aula 01 — Fundamentos de Banco de Dados, Dados, Informação e Sistemas

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Conceitos fundamentais de bancos de dados: dado, conhecimento, processo e informação, além das características de uma boa informação e do princípio ELSL/GIGO.

## 1. O caminho da transformação

A transformação da matéria-prima em algo útil para a tomada de decisão pode ser compreendida por meio de alguns conceitos fundamentais:

- **Dados** → matéria-prima
- **Conhecimento** → regras e métodos utilizados para transformar os dados
- **Processo** → conjunto de tarefas logicamente relacionadas
- **Informação** → resultado organizado e com significado
- **Sistemas de Informação** → utilização desses elementos para apoiar atividades e decisões

## 2. Dados

O ponto de partida. Dados são os fatos em sua forma primária e isolada. Representam eventos físicos, numéricos ou textuais que ainda não contam uma história.

**Exemplos:**
- Nome de um empregado
- Quantidade de horas trabalhadas
- Número de peças no estoque
- Valores individuais de vendas

O dado, isoladamente, possui pouco ou nenhum significado para uma decisão.

## 3. Informação

O valor adicional. Quando os fatos (dados) são organizados e arranjados de maneira significativa, eles adquirem valor adicional. A informação serve a um propósito.

**Exemplo:**
- **Dado:** vendas individuais de cada vendedor.
- **Informação:** total de vendas mensais.

O total de vendas mensais possui maior utilidade para um gerente porque pode auxiliar na tomada de decisões.

## 4. Do dado para a informação

A evolução de dados para informação não acontece de forma automática. Existe um processo, ou seja, uma série de tarefas logicamente relacionadas e executadas para atingir um resultado definido.

```
DADOS
  ↓
Tarefas logicamente relacionadas
  ↓
Resultado definido
  ↓
INFORMAÇÃO
```

## 5. Conhecimento

O motor do processo. Conhecimento é o conjunto de:

- Regras
- Diretrizes
- Procedimentos
- Métodos
- Algoritmos

Utilizados para selecionar, organizar e manipular os dados. É o "saber como" que torna o dado útil para uma tarefa específica.

## 6. Dados + Conhecimento = Informação

Uma forma de visualizar a transformação:

```
DADOS
Matéria-prima
        +
CONHECIMENTO
Ferramentas, regras e métodos
        ↓
PROCESSO
Transformação
        ↓
INFORMAÇÃO
Produto final com significado
```

**Metáfora da marcenaria:**
- **Dados** → matéria-prima
  - Exemplo: troncos de madeira bruta.
- **Conhecimento** → ferramentas e regras
  - Exemplo: pregos, furadeiras, cola e habilidade para utilizar as ferramentas.
- **Informação** → produto final
  - Exemplo: uma cadeira ou mesa acabada, pronta para uso.

## 7. Funil de refinamento

- **Dados** — fatos em sua forma primária e bruta. Exemplos: nome isolado, número de horas. Por si só, possuem pouco valor para uma decisão.
- **Conhecimento** — regras, algoritmos e diretrizes de negócio aplicados para manipular os dados. É o "como fazer".
- **Informação** — dados organizados que adquiriram sentido e geram valor para decisões corporativas. Exemplo: total de vendas.

## 8. Matriz de diferenciação

| Elemento | Característica | Exemplo |
| --- | --- | --- |
| Dado | Bruto, não estruturado | "João", "40 horas" |
| Conhecimento | Regras, métodos e diretrizes | Cálculo matemático da folha |
| Informação | Estruturada e contextualizada | Contracheque de João |

**Outro exemplo:**

```
Madeira
   ↓
Marceneiro + Ferramentas
   ↓
Cadeira
```

A madeira representa o dado, o marceneiro e suas ferramentas representam o conhecimento, e a cadeira representa a informação/resultado do processo.

## 9. Checkpoint — O que é um dado?

No contexto de bancos de dados, a melhor definição para dado é: **fatos em sua forma primária e bruta, como peças em estoque, sem valor adicional.**

**Não confundir com:**
- Planilha com gráficos já formatados para a diretoria → informação
- Regras, diretrizes e procedimentos utilizados para manipular informações → conhecimento
- Resultado final exibido em um relatório de lucros mensais → informação

## 10. Exemplo: sistema de cálculo de imposto

Para entender a diferença entre dado, conhecimento e informação, podemos utilizar um sistema de cálculo de imposto.

- **Dado bruto** — valores de entrada utilizados pelo sistema.
  - Exemplos: salário, renda, despesas, dependentes e outros valores necessários ao cálculo.
- **Conhecimento** — regras utilizadas para transformar os dados.
  - Exemplos: algoritmos, leis, regras tributárias e fórmulas de cálculo.
- **Informação final** — resultado apresentado ao usuário.
  - Exemplo: valor do imposto a pagar.

```
DADO BRUTO
     ↓
ALGORITMOS + LEIS
     ↓
PROCESSAMENTO
     ↓
VALOR DO IMPOSTO
```

## 11. ELSL — Entra Lixo, Sai Lixo

ELSL = **Entra Lixo, Sai Lixo**. Em inglês: **GIGO** = *Garbage In, Garbage Out*.

O princípio afirma que, se os dados de entrada estiverem incorretos, o processo de transformação poderá gerar uma informação inútil ou perigosa, mesmo que o processo ou software seja sofisticado.

**Ideia principal:**

```
Dados corretos
     ↓
Processamento
     ↓
Informação confiável
```

Enquanto:

```
Dados incorretos
     ↓
Processamento
     ↓
Informação incorreta
```

## 12. Consequência do ELSL

Inserir dados de entrada errôneos pode destruir a integridade sistêmica, independentemente do nível de sofisticação do software.

O ELSL está diretamente relacionado à característica de **precisão** da informação, ou seja, à ausência de erros sistêmicos.

**Exemplo:** se um sistema de cálculo de imposto recebe um salário incorreto, o resultado do cálculo também poderá estar incorreto.

## 13. Características de uma boa informação

Uma boa informação possui diversas características importantes.

- **1. Precisa** — deve ser livre de erros; evita o efeito ELSL.
  - Exemplo: cálculo de imposto exato.
- **2. Completa** — deve conter todos os dados importantes, sem omissões relevantes.
  - Exemplo: relatório de custos que não oculta taxas.
- **3. Confiável** — a veracidade da informação depende da segurança e confiabilidade da fonte de coleta.
  - Exemplo: utilizar uma fonte oficial e segura em vez de uma planilha sem procedência.
- **4. Econômica** — o benefício obtido pela informação deve ser superior ao custo de sua produção.
  - Exemplo: evitar consultas repetitivas e desnecessárias na nuvem.
- **5. Relevante** — a informação precisa ser importante para a decisão que está sendo tomada.
  - Exemplo: alertas focados em falhas críticas.
- **6. Simples** — deve evitar a sobrecarga de informações; a informação precisa ser apresentada de forma que o usuário consiga identificar aquilo que realmente importa.
  - Exemplo: uma interface contendo apenas os KPIs vitais.
- **7. Verificável** — a informação deve poder ser rastreada e conferida.
  - Exemplo: utilização de logs e auditoria cruzada.
- **8. Flexível** — pode ser utilizada para diferentes finalidades.
  - Exemplo: um dashboard utilizado pelos setores de Marketing, Finanças e outras áreas.
- **9. Em tempo** — a informação deve estar disponível no momento adequado para sua utilização.
  - Exemplo: sistema antifraude de cartão que precisa identificar uma transação rapidamente.

## 14. As 9 características da boa informação

As características podem ser organizadas em três grupos:

- **Qualidade — foco na fonte:** Precisa, Completa, Confiável
- **Eficiência — foco no recurso:** Econômica
- **Utilidade — foco no uso:** Relevante, Simples, Verificável, Flexível, Em tempo

## 15. Checkpoint — ELSL

A frase "**Entra Lixo, Sai Lixo**" está diretamente relacionada à característica **Precisa**, pois dados incorretos podem gerar informações incorretas.

## 16. Checkpoint — Sobrecarga de informações

Para evitar a sobrecarga de informações, na qual o tomador de decisões perde o foco, a informação precisa ser **Simples**.

## 17. Impacto do ELSL no mundo real

Um sistema afetado pelo fenômeno ELSL pode causar prejuízos reais para uma organização.

**Exemplo no setor de vendas:**

```
Preço digitado errado
        ↓
Previsões falsas de lucro
        ↓
Decisões desastrosas
```

Dados incorretos podem afetar:
- Relatórios gerados
- Previsões de lucro
- Decisões gerenciais
- Fluxo de caixa
- Resultados das vendas

Portanto, a qualidade dos dados de entrada é fundamental para que o sistema produza informações confiáveis.

## 18. Resumo para revisão

- **Dados** — fatos brutos, primários e isolados.
- **Conhecimento** — regras, métodos, diretrizes e procedimentos usados para manipular os dados.
- **Processo** — conjunto de tarefas logicamente relacionadas que transforma dados em um resultado.
- **Informação** — dados organizados e contextualizados que possuem significado e valor para uma finalidade ou decisão.
- **ELSL / GIGO** — entra lixo, sai lixo. Dados incorretos podem produzir informações incorretas.
- **Boa informação** — deve ser: Precisa, Completa, Confiável, Econômica, Relevante, Simples, Verificável, Flexível, Em tempo.

## 19. Mapa mental

```
                DADOS
                   │
                   ↓
          Matéria-prima bruta
                   │
                   ↓
             CONHECIMENTO
                   │
          Regras + métodos
          + algoritmos
                   │
                   ↓
               PROCESSO
                   │
                   ↓
             INFORMAÇÃO
                   │
          ┌────────┴────────┐
          ↓                 ↓
      Significado       Valor para
                       decisões
```

**Regra fundamental:**

```
Dados ruins
    ↓
ELSL / GIGO
    ↓
Informação ruim
    ↓
Decisões ruins
```

**Regra de qualidade:**

```
Dados precisos
    ↓
Processamento adequado
    ↓
Informação de qualidade
    ↓
Melhores decisões
```

## Tópicos
- 

## Relacionadas

- [[Banco-de-Dados]]
- [[Faculdade]]
