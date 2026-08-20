---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Jupyter

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Projeto open-source (Jupyter Notebook, JupyterLab, JupyterHub) que fornece ambientes interativos baseados em notebooks para ciência de dados, exploração e ensino, executando código em kernels por linguagem.

## Conceitos-chave
- **Kernels**: processos que executam o código (IPython para Python, IRkernel para R, IJulia etc.); o notebook se conecta a eles via protocolo Jupyter.
- **Notebook (.ipynb)**: documento JSON com células de código, markdown, saídas e metadados.
- **JupyterLab**: suíte web moderna que substitui o notebook clássico, com painéis, terminals e extensões.
- **Magics**: comandos especiais do IPython (`%timeit`, `%matplotlib inline`, `%%writefile`, `!comando`).
- **Widgets**: controles interativos (ipywidgets) para explorar parâmetros sem reexecutar tudo.
- **nbconvert/nbformat**: conversão para HTML/PDF/slides e execução programática (ex.: com `jupyter nbconvert --execute`).

## Exemplos
Célula com mágica de tempo e execução de shell:

```python
%timeit sum(range(10_000))
!ls -la
```

Célula de plotagem:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.show()
```

Executar um notebook em pipeline (CI):

```bash
jupyter nbconvert --to notebook --execute notebook.ipynb --output executado.ipynb
jupyter nbconvert --to html executado.ipynb
```

## Boas práticas
- Use kernels (ambientes) isolados por projeto para evitar dependências conflitantes.
- Escreva células atômicas: uma ideia por célula, reexecutável de forma independente.
- Combine markdown para documentar o raciocínio e células para o código.
- Defina seeds e versões de bibliotecas para resultados reproduzíveis.
- Versionar notebooks exige cuidado: prefira executar com `--execute` em CI e revisar diffs com nbconvert/nbdime.

## Armadilhas comuns
- Estado global viciado: variáveis de células executadas em outra ordem corrompem o resultado (kernel restaurado).
- Notebooks com saídas grandes no Git geram diffs ilegíveis; use `nbstripout` ou version CSS/HTML exportado.
- Kernel com versão diferente da produção gera resultados que não reproduzem em deploy.
- `!pip install` dentro do notebook instala no kernel atual, não no ambiente de produção.
- Blobs/gráficos pesados travam o JupyterLab; limpe saídas e use plotagem leve.

## Relacionadas
- [[Notebooks]]
- [[Python]]