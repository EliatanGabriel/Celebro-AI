---
type: concept
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Docker

#area/estudos #devops #conceito #containers #virtualizacao #devops

**Resumo:** Plataforma de conteinerização que empacota aplicações com suas dependências em imagens, garantindo ambiente consistente entre desenvolvimento e produção.

## Conceitos-chave
- **Imagens:** artefatos imutáveis com sistema, código e dependências, construídos a partir de um `Dockerfile`.
- **Contêineres:** processos isolados executados a partir de imagens, compartilhando o kernel do host.
- **Volumes:** áreas persistentes para dados que sobrevivem ao ciclo de vida do contêiner.
- **Networks:** redes isoladas que conectam contêineres entre si e ao host.
- **Docker Compose:** define múltiplos serviços (banco, app, fila) em um arquivo YAML para orquestração local.
- **Dockerfile:** instruções passo a passo (FROM, COPY, RUN, CMD) para construir uma imagem.

## Exemplos
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - db
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: exemplo
```

```bash
docker build -t minha-app .
docker compose up -d
docker ps
```

## Boas práticas
- Usar imagens base oficiais e fixar versões.
- Manter as imagens pequenas (multi-stage build, `.dockerignore`).
- Rodar contêineres como usuário não root.
- Tratar volumes como persistência e contêineres como descartáveis.

## Armadilhas comuns
- Confundir imagem com contêiner: a imagem é o molde; o contêiner é a execução.
- Esquecer de persistir dados, perdendo-os quando o contêiner é removido.
- Expor credenciais no `Dockerfile` ou em variáveis de ambiente versionadas.
- Acreditar que o Docker oferece o mesmo isolamento que uma VM: ele compartilha o kernel do host.

## Relacionadas
- [[CI-CD]]
- [[Kubernetes]]
- [[Containers]]