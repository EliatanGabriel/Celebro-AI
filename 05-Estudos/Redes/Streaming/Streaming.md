---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Streaming

#area/estudos #estudos/redes #conceito

**Resumo:** Entrega contínua de mídia (vídeo e áudio) pela rede com reprodução enquanto os dados chegam, tolerante a perdas e fortemente dependente de banda, latência e jitter estáveis.

## Conceitos-chave
- **Buffer:** acumula dados para compensar variações da rede (jitter).
- **Adaptive Bitrate (ABR):** o cliente escolhe a qualidade conforme a banda disponível (HLS, DASH).
- **Protocolos:** HLS/DASH sobre HTTP (TCP), RTP/RTSP (tempo real) e WebRTC.
- **TCP vs UDP:** HTTP streaming usa TCP (confiável); mídia ao vivo de baixa latência usa UDP/QUIC.
- **CDN:** aproxima o conteúdo e reduz latência e rebuffering.
- **Segmentação:** o vídeo é dividido em segmentos curtos (2-6 s) para troca de qualidade.

## Exemplos
```text
Playlist HLS (.m3u8) com múltiplas qualidades
#EXTM3U
#EXT-X-STREAM-INF:BANDWIDTH=800000,RESOLUTION=640x360
media-800k.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=2400000,RESOLUTION=1280x720
media-2400k.m3u8
```

## Boas práticas
- Oferecer múltiplas bitrates para que o ABR adapte à banda do usuário.
- Usar CDN para distribuir segmentos e reduzir carga na origem.
- Manter segmentos curtos (2-6 s) para troca rápida de qualidade e menor atraso.
- Monitorar métricas como rebuffer rate, startup time e bitrate média.

## Armadilhas comuns
- Buffer muito grande aumenta o atraso ao vivo (live), mesmo com boa experiência de imagem.
- Ignorar o jitter: flutuação constante causa rebuffering mesmo com banda nominal alta.
- Usar TCP para ao vivo em rede com perda: head-of-line blocking trava a reprodução.
- Confundir bitrate do vídeo com banda necessária (é preciso folga para overhead).

## Relacionadas
- [[UDP]]
- [[CDN]]
- [[Latencia]]
- [[Largura-de-Banda]]
- [[TCP]]