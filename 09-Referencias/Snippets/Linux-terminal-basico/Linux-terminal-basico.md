---
type: snippet
area: referencias
status: active
created: "2026-08-22"
updated: "2026-08-22"
---

# Linux-terminal-basico

#area/referencias #referencias/snippets

Comandos de terminal que resolvem o cotidiano em servidores e CI. Quando usar: navegar, buscar, processar texto e matar processos sem interface gráfica.

## Navegar e inspecionar

```bash
pwd                        # onde estou
ls -lah                    # listar com tamanhos legíveis e ocultos
du -sh * | sort -h         # tamanho de cada pasta, do menor pro maior
df -h                      # espaço em disco das partições
```

## Buscar dentro de arquivos (grep)

```bash
grep -rn "timeout" src/            # busca recursiva mostrando linha
grep -rn "ERROR" app.log | tail -20   # últimos 20 erros do log
grep -c "200 OK" access.log        # contar ocorrências
```

## Processos

```bash
ps aux | grep node          # achar processo pelo nome
kill -9 12345               # matar PID teimoso
lsof -i :3000               # quem está ocupando a porta 3000
```

## Arquivos e permissões

```bash
find . -name "*.log" -mtime +7 -delete   # apagar logs com mais de 7 dias
chmod +x deploy.sh                       # tornar executável
tail -f app.log                          # seguir log em tempo real (Ctrl+C para)
```

> `-delete` no find não pede confirmação — rode antes sem ele para revisar.
