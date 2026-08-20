---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# DHCP

#area/estudos #estudos/redes #conceito

**Resumo:** Protocolo (Dynamic Host Configuration Protocol) que distribui automaticamente endereços IP, máscara, gateway e DNS para hosts em uma rede local, usando o fluxo DORA (Discover, Offer, Request, Ack).

## Conceitos-chave
- **DORA:** sequência de mensagens do processo de concessão de IP.
- **Lease (concessão):** IP válido por um período (ex.: 24h), renovado antes do vencimento.
- **Escopo (scope):** faixa de endereços e opções que o servidor oferece a uma rede.
- **Reservas:** IP fixo vinculado a um MAC específico (impressoras, servidores).
- **Options:** campos extras como máscara (1), gateway (3), DNS (6) e boot PXE (66/67).
- **Transporte:** usa UDP nas portas 67 (servidor) e 68 (cliente).

## Exemplos
```text
DHCP Discover  -> broadcast: "Procurando servidor DHCP"
DHCP Offer     -> servidor propõe IP 192.168.1.50
DHCP Request   -> cliente aceita e formaliza o pedido
DHCP Ack       -> servidor confirma a concessão (lease)
```

```bash
# Exemplo de escopo (ISC dhcpd.conf)
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.200;
  option routers 192.168.1.1;
  option domain-name-servers 8.8.8.8;
  default-lease-time 86400;
  host impressora { hardware ethernet AA:BB:CC:00:00:11; fixed-address 192.168.1.10; }
}
```

## Boas práticas
- Reservar IPs para servidores, impressoras e roteadores (evitar mudança).
- Dimensionar leases coerentes: curtos para redes muito dinâmicas (Wi-Fi), longos para fixos.
- Manter um único servidor DHCP por escopo, com failover, para evitar conflito de endereços.
- Em acesso corporativo, habilitar DHCP snooping no switch para bloquear servidores rogue.

## Armadilhas comuns
- Dois servidores DHCP na mesma rede causam disputa e IPs errados.
- Confundir lease com IP fixo: após o vencimento sem renovação o IP muda.
- Esquecer de atualizar as options ao migrar de gateway ou DNS.
- Cliente sem escopo adequado cai em IP da faixa errada ou 169.254.x.x (APIPA).

## Relacionadas
- [[IP]]
- [[NAT]]
- [[Subnetting]]
- [[Wi-Fi]]