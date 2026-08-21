---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Containers

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Unidades leves de software que empacotam código, runtime e dependências em imagens imutáveis, garantindo execução consistente em qualquer ambiente com isolamento por namespace e cgroups.

## Conceitos-chave
- **Imagem:** pacote imutável e versionado com o sistema de arquivos, binários e metadados do container.
- **Container:** processo em execução isolado a partir de uma imagem, via namespaces (isolamento) e cgroups (limite de recursos).
- **Isolamento vs virtualização:** containers compartilham o kernel do host; VMs têm kernel próprio e hypervisor.
- **Portabilidade:** a mesma imagem roda igual em dev, CI e produção, pois empacota tudo que o app precisa.
- **Registries:** repositórios de imagens (Docker Hub, ECR, GCR, GHCR) para distribuição e versionamento.
- **Imutabilidade:** containers são efêmeros; estado persistente vai para volumes ou serviços externos.
- **Orquestração:** gerenciar muitos containers exige ferramentas como [[Kubernetes]] (deploy, escala, redes).

## Exemplos

Conceito de camadas de imagem (Dockerfile):

```dockerfile
FROM node:20-alpine
COPY package*.json ./
RUN npm ci
COPY . .
CMD ["node", "server.js"]
```

Comandos essenciais:

```bash
docker build -t minha-app:1.0 .
docker run -d -p 8080:8080 minha-app:1.0
docker push minha-app:1.0
```

## Boas práticas
- Usar imagens base oficiais, pequenas (Alpine/distroless) e pinadas por digest.
- Manter containers efêmeros: sem estado interno, sem dependência de host.
- Rodar processos como usuário não-root dentro do container.
- Escanear imagens por vulnerabilidades no CI (Trivy, Snyk, Grype).
- Uma responsabilidade por container (um processo principal), mas vários processos quando necessário.

## Armadilhas comuns
- Confundir container com máquina virtual: compatibilidade depende do kernel e da arquitetura.
- Persistir dados dentro do container — perde-se tudo ao recriar.
- Imagens gigantes por falta de multi-stage builds e .dockerignore.
- Tratar container como unidade de segurança completa (há falhas no kernel compartilhado).
- Chamar de "container" o runtime do Docker e "container" o objeto; o padrão OCI padroniza a imagem e o runtime.

## Relacionadas
- [[Docker]]
- [[Kubernetes]]
- [[Microservicos]]
- [[DevOps]]