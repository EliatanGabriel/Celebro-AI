---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Ferramentas-CLI

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Conjunto de utilitários de linha de comando (grep, sed, awk, jq, curl, ripgrep, fzf) que aceleram busca, transformação e automação de dados e processos no desenvolvimento do dia a dia.

## Conceitos-chave
- **grep/rg (ripgrep)**: busca textual em arquivos com regex; `rg` é otimizado e respeita `.gitignore`.
- **sed**: edição de stream — substituições, exclusões e transformações linha a linha sem abrir o arquivo.
- **awk**: processamento orientado a colunas/campos, ideal para relatórios e parsing simples de texto tabular.
- **jq**: parser/transformador de JSON, essencial para trabalhar com respostas de APIs.
- **curl/wget**: transferência de dados e testes de API a partir do terminal.
- **xargs/parallel**: executa comandos em lote a partir do stdin; `find ... | xargs` é um padrão clássico.
- **fzf**: filtro interativo por fuzzy search sobre listas, combinado com o shell para navegação rápida.

## Exemplos
Buscar e transformar texto:

```bash
rg -n "TODO|FIXME" src/ --type js
grep -riE "senha|password" config/ | sed 's/^/ATENCAO: /'
awk -F, '{print $2}' dados.csv | sort | uniq -c | sort -rn
```

Processar JSON de uma API:

```bash
curl -s https://api.exemplo.com/v1/usuarios \
  | jq '.[] | select(.ativo == true) | .nome'
```

Executar em lote:

```bash
find . -name "*.log" -size +10M -print0 | xargs -0 gzip
ls ~/.config | fzf --preview 'cat ~/.config/{}/**'
```

## Boas práticas
- Use `rg` em vez de `grep` em repositórios grandes; é mais rápido e respeita ignore files.
- Prefira pipelines pequenos e legíveis; teste cada etapa separadamente antes de encadear.
- Proteja comandos com aspas: regex e globs expandem de forma diferente dependendo do shell.
- Documente pipelines complexos em scripts em vez de comandos de uma linha indecifráveis.
- Conheça o `--` para separar opções de argumentos e o `-print0`/`-0` para nomes com espaços.

## Armadilhas comuns
- Regex incompatível entre grep (BRE/ERE) e ferramentas (PCRE): `grep -E` para estendida, `-P` para PCRE.
- `xargs` sem `-0` quebra com nomes de arquivo contendo espaços ou aspas.
- Sed substitui apenas a primeira ocorrência por linha sem a flag `g`.
- `jq` com aspas duplas no shell interpreta variáveis; use aspas simples para preservar o filtro.
- Achar que `awk -F,` resolve CSV com aspas/escape: ele não entende CSV real (vírgulas dentro de campos).

## Relacionadas
- [[Terminal]]
- [[Curl]]
- [[Scripts]]
- [[Zsh]]