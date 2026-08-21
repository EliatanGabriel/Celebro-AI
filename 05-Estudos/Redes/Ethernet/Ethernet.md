---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Ethernet

#area/estudos #estudos/redes #conceito

**Resumo:** Família de tecnologias de rede local com fio definida pelo padrão IEEE 802.3, que padroniza o meio físico, os quadros e o acesso ao meio em LANs.

## Conceitos-chave
- **IEEE 802.3:** define quadros, cabos (UTP Cat5e/6, fibra óptica) e velocidades (10/100/1G/10G/40G).
- **Frame Ethernet:** campos de MAC destino/origem, EtherType, payload e FCS (checksum de integridade).
- **CSMA/CD (legado):** acesso ao meio com detecção de colisão; em full-duplex não há colisões.
- **Full-duplex:** transmissão e recepção simultâneas em par dedicado.
- **Auto-negotiation:** negociação automática de velocidade e duplex entre os equipamentos.
- **MTU:** tamanho máximo do payload (padrão 1500 bytes), relevante para fragmentação IP.

## Exemplos
```text
Frame Ethernet (IEEE 802.3)
+--------+--------+-----------+--------+------+
| Dest   | Src    | EtherType | Payload| FCS  |
| 6 B    | 6 B    | 2 B       |46-1500B| 4 B  |
+--------+--------+-----------+--------+------+
EtherType 0x0800 = IPv4 | 0x86DD = IPv6 | 0x0806 = ARP
```

```bash
# Verificar velocidade e duplex do enlace
ethtool eth0
# Exemplo de saída: Speed: 1000Mb/s, Duplex: Full
```

## Boas práticas
- Usar cabos compatíveis com a velocidade desejada (Cat6/Cat6a para 1G+).
- Habilitar STP/RSTP nos switches para evitar loops com links redundantes.
- Preferir fibra óptica para distâncias superiores a 100 m.
- Padronizar comprimento e organização de cabos para facilitar manutenção.

## Armadilhas comuns
- Cabo crossover vs direto: a maioria dos equipamentos modernos já negocia automaticamente.
- Colisões só ocorrem em hubs e half-duplex; em full-duplex o problema não existe.
- Confundir quadro Ethernet (L2) com pacote IP (L3).
- MTU incoerente (jumbo frames) causa perdas silenciosas em caminhos mistos.

## Relacionadas
- [[Switching]]
- [[Wi-Fi]]
- [[Protocolos]]
- [[OSI]]
- [[ARP]]