---
type: verbete
area: referencias
status: active
created: "2026-08-22"
updated: "2026-08-22"
---

# Container

#area/referencias #referencias/glossario

**Definição:** pacote leve que roda uma aplicação isolada compartilhando o kernel do sistema hospedeiro (diferente da máquina virtual, que carrega um sistema operacional inteiro). A imagem é a receita congelada; o container é ela rodando. Docker popularizou; Kubernetes orquestra containers aos milhares.

**Exemplo:** `docker run -p 8080:80 nginx` sobe um servidor web em segundos — mesmo comportamento no seu PC e no servidor, porque a imagem leva tudo junto (bibliotecas, config).

**Ver também:** [[CI-CD]] · [[API-REST]]
