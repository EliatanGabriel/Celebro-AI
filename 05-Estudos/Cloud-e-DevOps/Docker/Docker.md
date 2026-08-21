---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Docker

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Plataforma de containers que empacota aplicações e dependências em imagens OCI, com runtime para executá-las de forma isolada e portátil em qualquer host.

## Conceitos-chave
- **Dockerfile:** arquivo declarativo com instruções (FROM, RUN, COPY, EXPOSE, CMD) para construir a imagem.
- **Imagem:** camadas empilhadas e imutáveis; build cache por camada acelera reconstruções.
- **Container:** instância em execução da imagem, com rede, storage e processos próprios.
- **Docker Engine:** daemon (dockerd) que gerencia imagens, containers e redes + CLI (`docker`).
- **Compose:** orquestração local multi-container declarada em YAML (docker-compose.yml).
- **Volumes:** storage persistente montado no container, independente do ciclo de vida do container.
- **Networking:** bridge padrão, host e overlay; portas expostas com `-p`.
- **OCI (Open Container Initiative):** padrão aberto de imagens e runtimes seguido pelo Docker.

## Exemplos

Dockerfile multi-stage para reduzir tamanho da imagem:

```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
```

Docker Compose:

```yaml
services:
  web:
    build: .
    ports:
      - "8080:80"
    depends_on:
      - db
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: segredo
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

## Boas práticas
- Manter o container o mais enxuto possível: base small, multi-stage e .dockerignore.
- Ordenar camadas estáveis primeiro (dependências) para aproveitar o cache.
- Rodar como usuário não-root e definir `HEALTHCHECK`.
- Versionar e assinar imagens, puxando por digest em produção.
- Configurar recursos com `--memory`/`--cpus` e limits no Compose.

## Armadilhas comuns
- Usar `latest` em produção — quebra reprodutibilidade.
- Colocar segredos em ENV no Dockerfile (ficam gravados na imagem).
- Não usar .dockerignore, enviando node_modules/.git para o build.
- Compor imagem por container sem orquestração: Docker não escala por padrão.
- Confundir `CMD` com `ENTRYPOINT`: um define default, outro fixa o executável principal.

## Relacionadas
- [[Containers]]
- [[Kubernetes]]
- [[CI-CD-Conceito]]
- [[DevOps]]