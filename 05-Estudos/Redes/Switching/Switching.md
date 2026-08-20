---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Switching

#area/estudos #estudos/redes #conceito

**Resumo:** Encaminhamento de frames na camada de enlace (L2) dentro de uma rede local, feito por switches com base na tabela de endereços MAC.

## Conceitos-chave
- **Tabela MAC (forwarding table):** mapeia porta ↔ MAC para encaminhamento seletivo.
- **Learning:** o switch aprende os MACs lendo o endereço de origem dos frames.
- **Flooding:** quando o destino é desconhecido ou broadcast, o frame vai para todas as portas (exceto a origem).
- **Full-duplex:** elimina colisões; o switch divide os domínios de colisão por porta.
- **VLAN:** segmentação lógica de uma LAN em redes L2 isoladas (802.1Q).
- **STP/RSTP:** evita loops de rede quando há links redundantes.

## Exemplos
```text
Tabela MAC de um switch
| Porta | MAC               |
| 1     | AA:BB:CC:00:11:22 |
| 2     | AA:BB:CC:00:11:33 |

Frame para AA:BB:CC:00:11:33 -> encaminhado à porta 2
Frame para MAC desconhecido  -> flooding em todas as portas
```

```bash
# Exibir a tabela MAC em um switch (ex.: Cisco)
show mac address-table
```

## Boas práticas
- Habilitar STP/RSTP para proteger a rede contra loops.
- Usar VLANs para segmentar por função e reduzir o domínio de broadcast.
- Monitorar a tabela MAC e detectar MACs desconhecidos (spoofing).
- Preferir switches gerenciáveis para controle e diagnóstico.

## Armadilhas comuns
- Confundir switch (L2, MAC) com roteador (L3, IP).
- Loop sem STP causa broadcast storm e derruba a rede inteira.
- Flooding excessivo ocorre quando a tabela MAC está cheia ou o tráfego é desconhecido.
- Ignorar que broadcast ainda se propaga por todas as portas da mesma VLAN.

## Relacionadas
- [[Roteamento]]
- [[OSI]]
- [[Ethernet]]
- [[ARP]]
- [[Dispositivos]]