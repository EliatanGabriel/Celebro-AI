---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# TCP-IP

#area/estudos #estudos/redes #conceito

**Resumo:** Modelo de arquitetura em 4 camadas que rege a internet (Acesso à rede, Internet, Transporte e Aplicação), sendo o modelo dominante na prática — equivalente simplificado do OSI.

## Conceitos-chave
- **Acesso à rede:** Ethernet, Wi-Fi — reúne as camadas 1 e 2 do OSI.
- **Internet:** IP, ICMP, ARP — endereçamento e roteamento entre redes.
- **Transporte:** TCP (confiável) e UDP (rápido) — comunicação entre processos via portas.
- **Aplicação:** HTTP, HTTPS, DNS, SMTP, SSH — protocolos que os usuários utilizam.
- **Correspondência OSI:** 4 camadas agrupam as 7 camadas do modelo OSI.
- **Encapsulamento:** cada camada adiciona seu cabeçalho ao dado recebido da camada superior.

## Exemplos
```text
Aplicação   HTTP, DNS, SMTP, SSH
Transporte  TCP | UDP
Internet    IP, ICMP, ARP
Acesso      Ethernet, Wi-Fi, PPP
```

```text
Encapsulamento ao enviar uma requisição web
Dados HTTP
+ TCP header (portas 80/443)
+ IP header (origem/destino)
+ Ethernet frame (MAC origem/destino)
```

## Boas práticas
- Diagnosticar de baixo para cima usando o modelo como referência.
- Escolher TCP para confiabilidade e UDP/QUIC para baixa latência.
- Usar a terminologia do modelo na comunicação com equipes e fornecedores.
- Estudar o fluxo de dados com ferramentas (Wireshark) para fixar o encapsulamento.

## Armadilhas comuns
- Confundir o modelo TCP/IP com o protocolo TCP (um é arquitetura, outro é transporte).
- Achar que o modelo OSI é a arquitetura da internet (a internet segue o TCP/IP).
- Posicionar ARP na camada de internet quando, na prática, ele atua no acesso (L2).
- Esquecer que cada camada adiciona overhead ao dado original.

## Relacionadas
- [[OSI]]
- [[TCP]]
- [[IP]]
- [[UDP]]
- [[Protocolos]]