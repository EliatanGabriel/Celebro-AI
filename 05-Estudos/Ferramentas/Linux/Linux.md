---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Linux

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Sistema operacional open-source baseado no kernel Linux e no padrão POSIX; domina servidores, infraestrutura cloud, containers e o desenvolvimento de software, com distribuições (distros) como Debian, Ubuntu, Fedora e Arch.

## Conceitos-chave
- **Kernel**: núcleo que gerencia processos, memória, filesystems, drivers e syscalls; o restante do SO vem do GNU e de outras ferramentas.
- **Distros**: combinações de kernel + userspace + gerenciador de pacotes (apt/dnf/pacman) + init system (systemd).
- **Permissões**: modelo de usuário/grupo/outros com rwx; `sudo`, `chmod`, `chown`, ACLs e capabilities.
- **Filesystem**: hierarquia FHS — `/etc` (config), `/var` (dados variáveis), `/home`, `/tmp`, `/proc`.
- **Gerenciamento de pacotes**: `apt`, `dnf`, `pacman` instalam/atualizam software; versões diferem entre distros.
- **Shell e scripting**: bash/zsh como interface e linguagem de automação; pipes e redirecionamento.
- **Servidores**: web (Nginx/Apache), bancos, containers — a base de praticamente toda a infraestrutura moderna.

## Exemplos
Comandos essenciais:

```bash
ls -lah /etc
ps aux | grep nginx
systemctl status docker
df -h && free -h
sudo apt update && sudo apt upgrade -y
```

Criar usuário e permissões:

```bash
sudo useradd -m -s /bin/bash novo_usuario
sudo usermod -aG sudo novo_usuario
chmod 750 ~/projeto
```

## Boas práticas
- Prefira distribuições com suporte longo (LTS) em servidores e atualize com segurança.
- Bloqueie acesso SSH com chaves, desative login por senha de root e configure firewall (ufw/firewalld).
- Separe serviços em containers ou unidades systemd para isolamento e reinício automático.
- Monitore recursos (`top`, `htop`, `journalctl`, `ss`) antes de escalar infraestrutura.
- Versionar arquivos de configuração (dotfiles, Ansible) para reproduzir ambientes.

## Armadilhas comuns
- Comandos que só funcionam em uma distro (apt vs. dnf) e quebra ao copiar documentação.
- Falta de permissão em logs ou diretórios de serviço causando falhas silenciosas.
- Deletar `/etc` ou arquivos do sistema com `rm -rf` por engano (sempre duplique o caminho).
- Uso de caminhos absolutos vs. relativos em scripts que rodam de diretórios diferentes.
- Ignorar o umask/ownership fazendo arquivos do serviço rodarem com usuário errado.

## Relacionadas
- [[Terminal]]
- [[Zsh]]
- [[Scripts]]
- [[Cron]]