---
type: concept
area: faculdade
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Fundamentos de Raspberry Pi

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Fundamentos do Raspberry Pi: o que é, modelos, componentes, sistemas operacionais e primeiros passos de uso.

## 1. O que é o Raspberry Pi

O Raspberry Pi é um **computador de placa única** (SBC — *Single Board Computer*), do tamanho de um cartão de crédito, desenvolvido pela Raspberry Pi Foundation. Executa um sistema operacional completo, como um PC, mas de baixo custo e consumo.

## 2. Para que serve

- Servidor doméstico (NAS, media center).
- Aprendizado de programação e eletrônica.
- Automação residencial e IoT.
- Retrogaming.
- Cluster de baixo custo.
- Prototipagem de sistemas embarcados.

## 3. Componentes principais

```
┌─────────────────────────────────┐
│   USB ×4          HDMI       GPIO│
│  ┌──┐ ┌──┐   ┌────┐  ┌───────┐ │
│  │  │ │  │   │    │  │ o o o │ │
│  └──┘ └──┘   └────┘  └───────┘ │
│  Ethernet   Micro-SD   USB-C    │
└─────────────────────────────────┘
```

- **CPU/GPU** — processador ARM.
- **Memória RAM** — 1 a 16 GB conforme o modelo.
- **GPIO** — pinos de entrada/saída de propósito geral (40 pinos).
- **USB** — conexão de periféricos.
- **HDMI** — saída de vídeo.
- **Micro-SD** — armazenamento do sistema.
- **Ethernet / Wi-Fi / Bluetooth** — conectividade.

## 4. Modelos

| Modelo | Características |
| --- | --- |
| Raspberry Pi 5 | O mais recente, muito mais rápido, PCIe |
| Raspberry Pi 4 Model B | 1–8 GB RAM, USB 3.0, dois HDMI |
| Raspberry Pi Zero 2 W | Minúsculo, baixo custo, Wi-Fi |
| Raspberry Pi Pico | Microcontrolador (RP2040), estilo Arduino |

- **Raspberry Pi 4/5** — computador completo (Linux).
- **Pico** — microcontrolador para projetos embarcados (Python/C).

## 5. Sistemas operacionais

- **Raspberry Pi OS** — sistema oficial baseado em Debian Linux.
- **Ubuntu** — para uso geral/servidor.
- **RetroPie** — emulador de consoles.
- **Home Assistant OS** — automação residencial.
- **Headless** — sem tela, acessado via SSH.

## 6. Primeiros passos

1. **Gravar o sistema** — usar o Raspberry Pi Imager para gravar o SO no Micro-SD.
2. **Conectar** — teclado, mouse, monitor (ou cabeamento via SSH).
3. **Inicializar** — ligar na energia e configurar usuário.
4. **Atualizar** — `sudo apt update && sudo apt upgrade`.
5. **Acessar remotamente** — `ssh usuario@ip`.

## 7. Raspberry Pi × Arduino

| Raspberry Pi | Arduino |
| --- | --- |
| Computador com Linux | Microcontrolador |
| Executa SO completo | Executa um programa por vez |
| Alto processamento | Baixo processamento |
| Ideal para IoT, servidores, mídia | Ideal para sensores e atuadores simples |
| Consome mais energia | Consome pouquíssima energia |

## 8. Boas práticas

- Use **fonte de alimentação adequada** (5V com amperagem suficiente).
- Faça **backup do cartão SD**.
- Desligue com `sudo shutdown now` antes de cortar energia.
- Instale com **Raspberry Pi Imager** (configura SSH/Wi-Fi de forma fácil).

## Tópicos
- 

## Relacionadas

- [[Raspberry-Pi-e-IoT]]
- [[Faculdade]]