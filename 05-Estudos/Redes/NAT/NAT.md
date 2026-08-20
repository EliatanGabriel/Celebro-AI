---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# NAT

#area/estudos #estudos/redes #conceito

**Resumo:** Técnica (Network Address Translation) que traduz endereços IP privados para públicos, permitindo que vários dispositivos compartilhem um único endereço IP público.

## Conceitos-chave
- **RFC1918:** endereços privados não roteáveis na internet, usados internamente.
- **SNAT/Masquerade:** traduz o endereço de origem (saída para a internet).
- **DNAT/Port forwarding:** traduz o endereço de destino (entrada a partir da internet).
- **PAT (NAT overload):** múltiplos hosts atrás de um único IP, diferenciados por portas.
- **Tabela de conexões:** mantém o mapeamento IP:porta interno ↔ externo.
- **Limitação:** NAT não é segurança; é tradução, complementa o firewall.

## Exemplos
```text
Host interno 192.168.1.10:5000
Roteador traduz para 200.200.200.1:60000
Tabela: 192.168.1.10:5000 <-> 200.200.200.1:60000
```

```bash
# Port forwarding com iptables
iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT \
  --to-destination 192.168.1.50:80
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

## Boas práticas
- Usar port forwarding apenas quando realmente necessário (expor serviços).
- Manter a tabela de conexões dimensionada para o volume de usuários.
- Considerar IPv6 para eliminar a necessidade de NAT na nova geração.
- Registrar e revisar as regras de encaminhamento periodicamente.

## Armadilhas comuns
- NAT quebra conexões P2P e VoIP (requer STUN/UPnP ou relay).
- Confundir NAT com firewall: traduz endereços, não decide segurança por política.
- Esquecer que UDP também usa portas para multiplexar no PAT.
- Port forwarding mal configurado expõe serviços internos indevidamente.

## Relacionadas
- [[IP]]
- [[Firewall]]
- [[Subnetting]]
- [[DHCP]]