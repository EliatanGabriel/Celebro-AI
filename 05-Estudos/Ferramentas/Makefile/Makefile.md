---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Makefile

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Arquivo de automação de builds e tarefas processado pela ferramenta `make`; define targets com dependências e receitas de shell, amplamente usado para compilar C/C++ e também como runner de tarefas em projetos de qualquer linguagem.

## Conceitos-chave
- **Targets**: alvos que uma regra constrói; podem representar arquivos ou ações (phony).
- **Dependências**: arquivos/outros targets que devem estar prontos antes do alvo; o make só reexecuta se algo mudou.
- **Variáveis**: definidas com `=` (recursiva), `:=` (imediata), `?=` (default) e `+=` (append); úteis para flags e listas de fontes.
- **Automatic variables**: `$@` (target), `$<` (primeira dependência), `$^` (todas as dependências).
- **Pattern rules**: `%.o: %.c` define regras genéricas; o compilador infere ações para sufixos conhecidos.
- **Phony targets**: alvos sem arquivo físico (`clean`, `install`) declarados em `.PHONY` para não conflitarem com arquivos de mesmo nome.
- **Shell**: cada linha da receita roda em um subshell próprio; use `;`/`\` para encadear no mesmo shell.

## Exemplos
Makefile clássico para C:

```makefile
CC    := gcc
CFLAGS := -Wall -O2
SRC   := main.c utils.c
OBJ   := $(SRC:.c=.o)
BIN   := app

all: $(BIN)

$(BIN): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(BIN)

.PHONY: all clean
```

Makefile como runner de tarefas:

```makefile
setup:
	python -m venv .venv && .venv/bin/pip install -r requirements.txt

test:
	.venv/bin/pytest

lint:
	.venv/bin/ruff check .

.PHONY: setup test lint
```

Executar:

```bash
make -j4          # compila em paralelo
make clean test   # encadeia targets
```

## Boas práticas
- Declare `.PHONY` para targets que não criam arquivos e evite conflitos de nome.
- Use variáveis para flags e listas, permitindo sobrescrever da linha de comando (`make CFLAGS="-O0"`).
- Mantenha receitas simples e herméticas; cada target deve ser reprodutível.
- Aproveite `-j` para builds paralelos e escreva dependências corretas para não quebrar com concorrência.
- Prefixe receitas com `@` para suprimir eco quando a saída for ruído.

## Armadilhas comuns
- Recuo com espaços em vez de TAB: o make exige TAB literal no início de cada receita.
- Target de mesmo nome de um arquivo existente é ignorado (usar `.PHONY`).
- Variáveis com `=` avaliadas no uso causam comportamento surpreendente; use `:=` para valores imediatos.
- Dependências ausentes fazem o make rodar receitas sem necessidade ou nunca (arquivo "mais novo").
- Receitas longas quebram ao mudar de shell; encadeie com `\` ou escreva em scripts.

## Relacionadas
- [[Terminal]]
- [[Scripts]]
- [[Cron]]
- [[Ferramentas-CLI]]