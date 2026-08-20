---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Docker-Desktop

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Aplicativo desktop (macOS/Windows) que empacota o Docker Engine, CLI, Docker Compose e uma interface gráfica, facilitando o desenvolvimento com containers locais sem configurar uma VM manualmente.

## Conceitos-chave
- **Docker Engine + CLI**: mesmo `docker`/`docker compose` do Linux, fornecidos em um pacote com atualizações gerenciadas.
- **VM Linux integrada**: no macOS/Windows o runtime roda em uma VM (ex.: HyperKit/Apple Virtualization, WSL2) — o desempenho de montagens de volumes depende dessa integração.
- **Interface gráfica**: dashboard de containers, imagens, volumes e redes; recursos como Dev Environments e Extensions.
- **WSL2 (Windows)**: recomenda-se executar a integração com WSL2 para volume de I/O e uso da CLI a partir das distros Linux.
- **Settings**: configuração de recursos (CPU, memória, swap), registries, proxy, "Virtual disk limit" e comportamento ao iniciar.
- **Compose**: o Docker Desktop já traz o plugin `docker compose` (v2) para orquestração multi-serviço local.

## Exemplos
Subir um stack com Compose e ver no dashboard:

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: senha
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

```bash
docker compose up -d
docker compose ps
docker logs -f db
```

Limpar ambiente local:

```bash
docker system prune -a -f      # remove imagens/containers não usados
docker image prune -f
```

## Boas práticas
- Ajuste o limite de memória/CPU nas Settings conforme o peso das imagens que você usa (ex.: builds do Android exigem mais).
- Use WSL2 no Windows e mantenha os arquivos do projeto dentro do filesystem Linux para montagens rápidas.
- Combine com Dev Containers/VS-Code para ambientes reproduzíveis por todo o time.
- Faça `docker system prune` periodicamente para não encher o disco (o virtual disk cresce, mas nem sempre encolhe).
- Reserve o Dashboard para inspeção; automatize o fluxo comum com scripts e `docker compose`.

## Armadilhas comuns
- Confiar no clock de arquivos entre host e container: no macOS, arquivos montados podem ter timestamps diferentes.
- Esquecer que as Settings (CPU/memória) são da VM: alterar o limite não afeta containers individuais sem restart.
- Achar que remover containers libera disco: imagens, volumes e build cache continuam ocupando espaço.
- Problemas de DNS/proxy corporativo afetam `docker pull`; configure proxies nas Settings e `buildx` no projeto.
- Docker Desktop desatualizado pode quebrar `docker compose` v2 ou integrações com o Kubernetes integrado.

## Relacionadas
- [[Ferramentas]]
- [[Terminal]]
- [[Kubernetes-CLI]]