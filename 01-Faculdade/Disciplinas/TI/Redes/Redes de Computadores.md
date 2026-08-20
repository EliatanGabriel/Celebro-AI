---
type: concept
area: faculdade
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Redes de Computadores

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Redes de computadores: conceitos, modelo OSI, TCP/IP, endereçamento IP, topologias, protocolos e tipos de redes.

## 1. O que é uma rede

Uma rede de computadores conecta dispositivos para compartilhar recursos e informações.

**Exemplos de recursos:** arquivos, impressoras, internet, aplicações.

## 2. Modelo OSI

O modelo OSI divide a comunicação em 7 camadas:

```
7. Aplicação    → HTTP, SMTP, DNS
6. Apresentação → codificação, criptografia
5. Sessão       → sessões entre aplicações
4. Transporte   → TCP / UDP
3. Rede         → IP, roteamento
2. Enlace       → MAC, Ethernet, Wi-Fi
1. Física       → cabos, sinais, rádio
```

**Mnêmônico:** "Física, Enlace, Rede, Transporte, Sessão, Apresentação, Aplicação".

## 3. Modelo TCP/IP (na prática)

Modelo simplificado usado na internet:

```
Aplicação   → HTTP, DNS, SSH, SMTP
Transporte  → TCP, UDP
Rede        → IP
Interface   → Ethernet, Wi-Fi
```

## 4. TCP × UDP

| TCP | UDP |
| --- | --- |
| Confiável (entrega garantida) | Rápido, sem garantia |
| Orientado à conexão | Sem conexão |
| Controle de fluxo | Sem controle |
| HTTP, e-mail, FTP | Vídeo, jogos, DNS |

## 5. Endereçamento IP

- **IPv4** — 32 bits, 4 octetos: `192.168.1.10`.
- **IPv6** — 128 bits, notação hexadecimal.
- **Máscara de rede** — define a porção rede/host: `255.255.255.0` (`/24`).
- **Gateway** — porta de saída para outras redes.
- **DNS** — traduz nomes (`google.com`) em IPs.

## 6. Endereços privados comuns

- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16` — usado em roteadores domésticos.

## 7. Topologias de rede

```
Estrela (Star)          Barramento (Bus)
    ──●──                  ─────────
   / | \                      | | |
  ●  ●  ●                    ● ● ●

Anel (Ring)              Malha (Mesh)
  ┌─●─┐                 ●───●
  │   │                 │\ /│
  ●───●                 ●─●─●
```

- **Estrela** — todos conectados a um hub/switch. Mais comum.
- **Barramento** — todos em um mesmo cabo.
- **Anel** — cada dispositivo conectado ao próximo.
- **Malha** — múltiplas conexões, alta redundância.

## 8. Tipos de rede por abrangência

- **PAN** — pessoal (Bluetooth).
- **LAN** — local (escritório, casa).
- **MAN** — metropolitana.
- **WAN** — ampla (internet).

## 9. Equipamentos de rede

- **Hub** — repete o sinal para todos (obsolescente).
- **Switch** — encaminha para o dispositivo correto.
- **Roteador** — interliga redes e faz NAT.
- **Access Point** — provê Wi-Fi.
- **Firewall** — filtra tráfego por segurança.

## 10. Protocolos comuns

- **HTTP/HTTPS** — web.
- **DNS** — resolução de nomes.
- **SSH** — acesso remoto seguro.
- **FTP/SFTP** — transferência de arquivos.
- **SMTP/IMAP** — e-mail.
- **DHCP** — configuração automática de IP.

## 11. Comandos úteis (teste de rede)

```bash
ip addr          # mostra endereços IP
ip route         # mostra rotas
ping 8.8.8.8     # testa conectividade
traceroute x.com # mostra o caminho até o destino
```

## Tópicos
- 

## Relacionadas

- [[TI]]
- [[Fundamentos de TI]]
- [[Faculdade]]