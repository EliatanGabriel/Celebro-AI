---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Notebooks

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Documentos interativos que combinam código, texto (markdown), resultados, visualizações e metadados em células; usados para análise exploratória, ciência de dados, ensino e relatórios reprodutíveis.

## Conceitos-chave
- **Células**: unidades editáveis — código (executável por um kernel) e markdown (documentação/renderização).
- **Estado e ordem de execução**: o kernel mantém o estado entre células; a ordem de execução é parte da semântica do notebook.
- **Saídas**: texto, tabelas, figuras e rich outputs (HTML/JS com interatividade) persistidos no arquivo.
- **Formatos**: `.ipynb` (Jupyter), JupyterLab, Google Colab, Kaggle; ferramentas como nbconvert, papermill, nbdime.
- **Kernel**: processo que executa o código (Python/IPython, R, Julia); reiniciar limpa o estado.
- **Reprodutibilidade**: pinagem de versões, seeds e execução headless para gerar resultados confiáveis.

## Exemplos
Bloco markdown + código:

```markdown
## Análise de vendas
Dados de 2025, limpeza e agregação abaixo.
```

```python
import pandas as pd

df = pd.read_csv("vendas.csv")
df.groupby("regiao").vendas.sum()
```

Execução programática com parametrização:

```bash
papermill analise.ipynb relatorio.ipynb -p regiao SUL
jupyter nbconvert --to html relatorio.ipynb
```

## Boas práticas
- Escreva células curtas e independentes; documente dependências entre elas.
- Pine versões de bibliotecas e defina seeds para garantir reprodutibilidade.
- Versionar notebooks com ferramentas que tornam diffs limpos (`nbdime`) e removem saídas (`nbstripout`).
- Separe exploração (notebook) de código de produção (módulos testados).
- Execute em ordem "kernel > Run All" periodicamente para evitar células viciadas por estado.

## Armadilhas comuns
- Ordem de execução diferente da ordem visual gera resultados inconsistentes.
- Grandes saídas/blobs deixam o arquivo enorme e diffs impossíveis de revisar.
- Dependências instaladas no kernel local não existem no deploy/CI.
- Células que dependem de arquivos de caminho relativo quebram ao mover o notebook.
- Copiar/colar código de notebook com estado implícito para produção introduz bugs silenciosos.

## Relacionadas
- [[Jupyter]]
- [[Python]]