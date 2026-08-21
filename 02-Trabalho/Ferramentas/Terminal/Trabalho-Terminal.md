---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Terminal

#area/trabalho #trabalho/ferramentas #conceito

**Resumo:** Interface de linha de comando para executar comandos e scripts.

## Conceitos-chave
- Interface de linha de comando para executar comandos e scripts.
- Shell (bash, zsh) interpreta e encadeia comandos.
- Comandos essenciais: ls, cd, grep, find, ps, curl, chmod.
- Pipes e redirecionamento combinam ferramentas.
- Scripts e aliases automatizam tarefas repetitivas.

## Exemplos
```
# Buscar erros nos logs
grep -i "error" logs/app.log | tail -20

# Rodar testes e salvar a saída
npm test > reports/resultado.txt 2>&1

# Encontrar arquivos grandes
find . -type f -size +50M
```

## Boas práticas
- Aprender atalhos (Tab, Ctrl+R, Ctrl+E) para ganhar velocidade.
- Escrever scripts reprodutíveis e documentados.
- Conferir o comando antes de executar ações destrutivas.
- Usar permissões mínimas necessárias (evitar sudo à toa).
- Versionar scripts úteis de automação.

## Armadilhas comuns
- Executar comandos destrutivos (rm, mv) sem verificar o caminho.
- Quoting errado em caminhos com espaços.
- Esquecer de escapar variáveis em scripts.
- Uso excessivo de sudo, criando risco de danos.
- Comandos longos não documentados que ninguém entende.

## Relacionadas
- [[Trabalho-Git]]
- [[Git-Branch-Strategy]]