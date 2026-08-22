---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Comandos Essenciais em Shell

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Um vocabulário enxuto de comandos de navegação, arquivos, busca, texto, processos e permissões resolve o dia a dia do terminal.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `pwd` / `cd dir` | Mostra caminho atual / navega | `cd ~/projetos` |
| `ls -lah` | Lista detalhado, inclusive ocultos | `ls -lah` |
| `cp -r orig dest` | Copia arquivos/pastas (recursivo) | `cp -r src backup/` |
| `mv antigo novo` | Move ou renomeia | `mv rascunho.txt final.txt` |
| `rm -r dir` | Remove arquivos/pastas (irreversível) | `rm -ri temp/` |
| `mkdir -p a/b/c` | Cria diretórios aninhados | `mkdir -p logs/2026` |
| `touch arq` | Cria vazio / atualiza timestamp | `touch .gitkeep` |
| `cat / less` | Exibe / pagina um arquivo | `less +F app.log` |
| `head -n` / `tail -n -f` | Início / fim do arquivo (acompanhando) | `tail -f access.log` |
| `find . -name "*.sh"` | Busca arquivos por nome/critério | `find . -name "*.log"` |
| `grep -rn "txt" pasta` | Busca texto em arquivos com linha | `grep -rn "TODO" src` |
| `which cmd` | Localiza o executável de um comando | `which python3` |
| `wc -l` / `sort` / `uniq -c` | Conta linhas / ordena / agrupa únicos | `sort n.txt \| uniq -c` |
| `cut -d , -f 1` | Extrai colunas delimitadas | `cut -d: -f1 /etc/passwd` |
| `sed 's/a/b/g'` | Substitui texto em fluxo/arquivo | `sed 's/http:/https:/g' urls.txt` |
| `awk '{print $1}'` | Extrai campos por posição | `awk '{print $1}' access.log` |
| `ps aux` / `kill PID` | Lista processos / encerra processo | `kill -TERM 1234` |
| `jobs` / `bg` / `fg` | Controla tarefas do shell | `fg %1` |
| `Ctrl+C` / `Ctrl+Z` | Interrompe / suspende o processo em foco | Depois: `bg` retoma |
| `chmod` / `chown` | Permissões / dono do arquivo | `chmod 600 chave.pem` |
| `tar -czf / -xzf` | Compacta / extrai `.tar.gz` | `tar -czf b.tar.gz dir/` |
| `df -h` / `du -sh` | Espaço dos discos / tamanho de pastas | `du -sh *` |
| `history` / `man cmd` | Histórico / manual de comandos | `man rsync` |

## Exemplos

```sh
# Top 5 IPs mais frequentes no log de acesso
awk '{print $1}' /var/log/nginx/access.log \
  | sort | uniq -c | sort -rn | head -5

# Backup compactado e checagem de espaço
tar -czf "projetos-$(date +%F).tar.gz" ~/projetos
df -h /
```

```sh
grep -rn "TODO" src/           # onde falta trabalho no código
du -sh */ | sort -rh | head    # pastas que mais ocupam espaço
which node && node --version   # confirma instalação antes de usar
```

## Boas práticas

- Consulte `man comando` ou `comando --help` antes de decorar flags.
- Combine comandos com pipes em vez de criar arquivos temporários.
- Use `rm -i` ou mova para lixeira quando em dúvida.
- Complete com Tab e pesquise o histórico com Ctrl+R.
- Comece comandos destrutivos pelo menor escopo possível e revise o path.

## Armadilhas comuns

- `rm -rf` apaga sem lixeira: revisar o caminho duas vezes nunca é demais.
- `mv`/`cp` sobrescrevem o destino silenciosamente; `-i` pede confirmação.
- `sed -i` edita o arquivo original; faça backup (`sed -i.bak`).
- `kill -9` impede o processo de limpar estados; prefira SIGTERM primeiro.
- `awk` separa campos por espaços por padrão; outros delimitadores exigem `-F`.

## Relacionadas

- [[Entrada-Saida-e-Redirecionamento]]
- [[Loops-e-Case]]
- [[Estrutura-do-Script]]
- [[Shell]]
