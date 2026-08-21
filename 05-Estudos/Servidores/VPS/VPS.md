---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# VPS

#area/estudos #estudos/servidores #conceito #servidor #virtualizacao #hospedagem

**Resumo:** Servidor virtual privado com recursos dedicados e acesso root, usado para hospedar aplicações com controle total do ambiente.

## Conceitos-chave
- **Virtualização:** uma VPS é uma máquina virtual isolada sobre um hypervisor, com CPU, memória e disco garantidos.
- **Acesso root e SSH:** gerenciamento remoto via SSH, de preferência com chaves em vez de senha.
- **Provedores:** DigitalOcean, AWS Lightsail, Vultr, Hetzner e outros; escolha por região, preço e reputação.
- **Segurança:** atualizações, firewall (UFW) e hardening do sistema são responsabilidade do dono.
- **Backup:** snapshots e backups automáticos protegem contra falhas e perda de dados.
- **Papel na arquitetura:** pode hospedar servidores web (Nginx/Apache), bancos, containers e aplicações de qualquer linguagem.

## Exemplos
```bash
# Conexão via SSH
ssh usuario@1.2.3.4

# Criar usuário com sudo
adduser deploy
usermod -aG sudo deploy

# Firewall básico (UFW)
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

## Boas práticas
- Usar autenticação por chave SSH e desabilitar login por senha.
- Manter o sistema atualizado e aplicar patches de segurança.
- Configurar backups automáticos e testar a restauração.
- Escalar verticalmente (mais recursos) e depois horizontalmente (mais instâncias) conforme a demanda.

## Armadilhas comuns
- Deixar o serviço exposto em portas desnecessárias, ampliando a superfície de ataque.
- Confundir VPS com hospedagem compartilhada: aqui você é responsável pelo SO e pela manutenção.
- Escolher o provedor apenas pelo preço sem considerar a latência da região.
- Esquecer de monitorar disco e memória, causando indisponibilidade inesperada.

## Relacionadas
- [[Nginx]]
- [[Apache]]
- [[Docker]]
- [[DNS]]
- [[Firewall]]