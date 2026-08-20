---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Cron

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Agendador de tarefas do Unix que executa comandos periodicamente; as regras ficam no `crontab` e cada linha define o momento (minuto, hora, dia, mês, dia da semana) e o comando.

## Conceitos-chave
- **crontab**: arquivo de agendamento por usuário; gerenciado com `crontab -e`, `crontab -l` e `crontab -r`.
- **Campos de tempo**: cinco campos — minuto (0-59), hora (0-23), dia do mês (1-31), mês (1-12) e dia da semana (0-7, onde 0 e 7 são domingo).
- **Especiais**: `*` (todos), `*/n` (a cada n), intervalos `1-5`, listas `1,15` e macros como `@daily`, `@reboot`, `@monthly`.
- **Ambiente**: o cron executa com um PATH mínimo e shell padrão; caminhos absolutos são recomendados.
- **Saída**: stdout/stderr de cada execução é enviado por email ao usuário se não redirecionado; logs ficam em `/var/log/cron` (ou journal).
- **cron.d**: diretório de fragmentos de agendamento com a coluna extra de usuário, comum em pacotes do sistema.

## Exemplos
Editar o agendamento:

```bash
crontab -e
```

Linhas típicas de crontab:

```cron
# backup todo dia às 02:30
30 2 * * * /usr/local/bin/backup.sh

# limpeza a cada 15 minutos
*/15 * * * * /usr/bin/find /tmp -type f -mtime +7 -delete

# relatório mensal no dia 1 às 07:00
0 7 1 * * /home/user/bin/relatorio.py >> /var/log/relatorio.log 2>&1

# executa ao iniciar o sistema (roda como root via cron.d)
@reboot /usr/local/sbin/start-service.sh
```

Criar um fragmento de sistema em `/etc/cron.d/meu-trabalho`:

```
15 3 * * *  root  /opt/app/limpar.sh
```

## Boas práticas
- Sempre redirecionar saída (`>> log 2>&1`) ou usar logging explícito no script para facilitar o diagnóstico.
- Usar caminhos absolutos para binários e arquivos; o PATH do cron não inclui diretórios de usuário.
- Testar o script manualmente antes de agendá-lo, com as mesmas variáveis de ambiente mínimas.
- Adicionar proteção contra execuções sobrepostas (lock com `flock`) para tarefas longas.
- Configurar timezone explicitamente (`CRON_TZ=America/Sao_Paulo`) para evitar deslocamentos.

## Armadilhas comuns
- Confundir o dia da semana com 0=segunda; na verdade 0 e 7 são domingo.
- Achar que `30 2 * * *` roda de hora em hora — ele roda apenas uma vez por dia.
- Cron não executa o script se ele não tiver permissão de execução (`chmod +x`).
- Tarefas perdidas sem aviso: falhas de comando não geram erro visível se a saída não for redirecionada.
- Editar `crontab` do usuário errado (root vs. usuário) e achar que a tarefa vai rodar.

## Relacionadas
- [[Scripts]]
- [[Linux]]
- [[Terminal]]