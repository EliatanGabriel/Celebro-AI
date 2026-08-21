---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Sistemas

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Ambientes computacionais — sistema operacional, processos, serviços e infraestrutura — que gerenciam hardware e executam as aplicações.

## Conceitos-chave
- **Sistema operacional:** camada entre hardware e aplicações; gerencia CPU, memória, processos e dispositivos (Linux, Windows, macOS).
- **Processos e threads:** unidades de execução; o SO faz escalonamento, aloca recursos e isola processos entre si.
- **Memória virtual:** abstração que dá a cada processo um espaço de endereçamento próprio, com paginação.
- **Sistemas de arquivos:** organização de dados em disco (NTFS, ext4, APFS), com permissões e hierarquia de diretórios.
- **Serviços e daemons:** processos em segundo plano que fornecem funcionalidades contínuas (web server, banco de dados, logging).
- **Infraestrutura:** hardware, redes e camadas de virtualização/containers sobre os quais os sistemas rodam.
- **Monitoramento e logs:** observabilidade de processos, recursos e erros em produção.

## Exemplos
```text
// Ciclo de vida de um processo
criado → pronto → executando → bloqueado → encerrado
              ↕            ↕
          (escalonador)   (aguarda I/O)

// Comandos típicos de observação
ps aux          // lista processos
top / htop      // uso de CPU e memória em tempo real
df -h           // espaço em disco
free -h         // uso de RAM
```

```text
// Camadas de um sistema
Aplicações (navegador, servidor, serviços)
↑
Sistema operacional (processos, memória, arquivos, drivers)
↑
Hardware (CPU, RAM, disco, rede)

// Exemplo: requisição web
Requisição → SO recebe pela rede → entrega ao processo do servidor
          → servidor processa → responde → SO envia resposta
```

## Boas práticas
- Conhecer os comandos e métricas essenciais do SO para diagnosticar problemas.
- Entender a relação entre processo, thread e concorrência antes de escalar.
- Monitorar CPU, memória, disco e rede para detectar gargalos cedo.
- Tratar falhas de processos (restart, health checks) em ambientes de produção.

## Armadilhas comuns
- Confundir processo com thread; threads compartilham memória do processo.
- Ignorar a memória virtual e achar que RAM física é o único limite.
- Não considerar que o SO também consome recursos (overhead).
- Achar que "o sistema está lento" sem medir onde está o gargalo (CPU, I/O, rede).
- Esquecer permissões e usuários ao lidar com arquivos e serviços.

## Relacionadas
- [[Windows]]
- [[Memoria]]
- [[Performance]]
- [[Stack-Heap]]
- [[Debug]]
- [[Computacao]]
- [[Filas]]
- [[Programacao]]