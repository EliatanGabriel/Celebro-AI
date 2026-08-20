---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Bash

#area/estudos #estudos/linguagens #conceito

**Resumo:** Shell mais comum em sistemas Unix/Linux e linguagem de script imperativa, amplamente usada para automação de tarefas, pipelines e operações de DevOps.

## Conceitos-chave
- Paradigma imperativo de script; tudo é texto e variáveis têm tipagem dinâmica fraca.
- Interpretada: o interpretador bash executa o script linha a linha (sem compilação).
- Shebang (`#!/bin/bash`) indica o interpretador no início do arquivo.
- Composição poderosa por pipes (`|`) e redirecionamento (`>`, `>>`, `<`, `2>`).
- Código de saída (`$?`) é a forma padrão de sinalizar sucesso (0) ou erro (≠ 0).
- Estruturas de controle: `if`, `for`, `while`, `case`; funções com `function`/`nome() { }`.
- Amplamente usada em CI/CD, cronjobs, scripts de provisionamento e administração de servidores.

## Exemplos
```bash
#!/bin/bash
set -euo pipefail

# Loop com condicional
for arquivo in *.log; do
    if grep -q "ERROR" "$arquivo"; then
        echo "Erro encontrado em $arquivo"
    fi
done

# Função + verificação de exit code
backup() {
    tar -czf "backup-$(date +%F).tar.gz" /dados || {
        echo "Backup falhou" >&2
        exit 1
    }
}
backup
```

## Boas práticas
- Comece sempre com `set -euo pipefail` para falhar rápido e evitar erros silenciosos.
- Cite variáveis com aspas (`"$var"`) para preservar espaços e evitar globbing indesejado.
- Use `[[ ... ]]` em vez de `[ ... ]` para condicionais mais seguras.
- Faça backup com `local` dentro de funções para não vazar variáveis globais.
- Prefira ferramentas padrão POSIX (grep, awk, find) para máxima portabilidade.

## Armadilhas comuns
- Esquecer o shebang e o `chmod +x`, impedindo a execução direta do script.
- Não citar `"$@"`, o que quebra argumentos com espaços.
- Usar `=` em vez de `==` ou esquecer espaços em `[` — o Bash exige espaços ao redor dos operadores.
- Tratar números sem `(( ))` ou `let`, resultando em comparações lexicográficas erradas.
- Confundir `$()` (substituição de comando) com `$( )` de aritmética, que não existe em Bash (use `$(( ))`).

## Relacionadas
- [[Shell]]