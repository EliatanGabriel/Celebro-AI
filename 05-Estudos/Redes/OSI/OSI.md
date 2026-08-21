---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# OSI

#area/estudos #estudos/redes #conceito

**Resumo:** Modelo de referência da ISO com 7 camadas que descreve a comunicação em redes, servindo como linguagem comum, base de ensino e guia para diagnóstico.

## Conceitos-chave
- **Camada 1 — Física:** bits, sinais, cabos, conectores e radiofrequência.
- **Camada 2 — Enlace:** frames, endereços MAC, switches (Ethernet, Wi-Fi).
- **Camada 3 — Rede:** pacotes, endereços IP e roteamento.
- **Camada 4 — Transporte:** segmentos, TCP/UDP e portas.
- **Camadas 5-7 — Sessão, Apresentação, Aplicação:** sessões, codificação/formatação e protocolos de aplicação.
- **Modelo conceitual:** na prática, a internet segue o modelo TCP/IP (4 camadas), que agrupa as 7 do OSI.

## Exemplos
```text
7 Aplicação    HTTP, DNS, SMTP, SSH
6 Apresentação codificação, criptografia, compressão
5 Sessão       estabelecimento e controle de sessões
4 Transporte   TCP/UDP, portas
3 Rede         IP, roteamento
2 Enlace       Ethernet, MAC, switches
1 Física       cabos, rádio, bits
```

## Boas práticas
- Usar o modelo como referência para diagnosticar de baixo para cima.
- Usar a terminologia do OSI para comunicação clara entre times e fornecedores.
- Mapear cada protocolo real (IP, TCP, HTTP) à sua camada ao estudar tráfego.
- Relembrar que as camadas são abstrações: na implementação os protocolos dialogam diretamente.

## Armadilhas comuns
- Achar que as camadas 5 e 6 têm protocolos concretos equivalentes às demais na prática.
- Confundir a ordem das camadas ao descrever o fluxo de dados.
- Aplicar o OSI como se fosse a arquitetura real da internet (que usa TCP/IP).
- Tratar encapsulamento como se cada camada adicionasse "envelope" idêntico ao outro modelo.

## Relacionadas
- [[TCP-IP]]
- [[Protocolos]]
- [[IP]]
- [[Ethernet]]
- [[Switching]]