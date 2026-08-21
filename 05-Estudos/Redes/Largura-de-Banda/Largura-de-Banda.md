---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Largura-de-Banda

#area/estudos #estudos/redes #conceito

**Resumo:** Capacidade máxima teórica de transmissão de um enlace, medida em bits por segundo (bps); é distinta do throughput real e da latência.

## Conceitos-chave
- **bps/Kbps/Mbps/Gbps:** unidades de medida; 8 bits = 1 byte (100 Mbps ≈ 12,5 MB/s).
- **Throughput:** taxa efetiva alcançada, quase sempre menor que a banda nominal.
- **Bottleneck:** enlace de menor capacidade no caminho, que limita o fluxo total.
- **Independência da latência:** um link pode ter alta banda e alta latência (ex.: satélite).
- **Compartilhamento:** banda é recurso compartilhado entre os usuários do enlace.

## Exemplos
```text
100 Mbps / 8 = 12,5 MB/s  (máximo teórico de download)
Download de 1 GB a 12,5 MB/s ≈ 80 segundos
```

```bash
# Medir throughput real entre dois hosts
iperf3 -s          # servidor
iperf3 -c servidor -t 10   # cliente
```

## Boas práticas
- Dimensionar a infraestrutura para o pico de uso, não apenas a média.
- Usar QoS para priorizar tráfego crítico (VoIP, videochamada) sobre o restante.
- Monitorar throughput vs banda nominal para identificar saturação.
- Em nuvem, conhecer os limites de banda por instância/região (ex.: EC2, VPC).

## Armadilhas comuns
- Confundir Mbps com MB/s: fator de 8 vezes (100 Mbps não são 100 MB/s).
- Achar que aumentar a banda resolve toda lentidão — a latência domina em apps interativas.
- Medir "velocidade" em sites de teste que usam múltiplas conexões paralelas.
- Ignorar que a banda percebida é limitada pelo enlace mais fraco do caminho.

## Relacionadas
- [[Latencia]]
- [[CDN]]
- [[Streaming]]
- [[Largura-de-Banda]]