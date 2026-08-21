---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Latencia

#area/estudos #estudos/redes #conceito

**Resumo:** Tempo de atraso entre o envio e a chegada de um dado na rede, medido em milissegundos (ms); fator crítico para a experiência em aplicações interativas.

## Conceitos-chave
- **Componentes:** propagação, transmissão, processamento nos roteadores e fila (queuing).
- **RTT (round-trip time):** tempo de ida e volta; é o que o usuário sente em cada requisição.
- **Limite físico:** a velocidade da luz na fibra (~200.000 km/s) limita o mínimo teórico.
- **Jitter:** variação da latência entre pacotes; tão relevante quanto a média em áudio/vídeo.
- **Impacto:** jogos, VoIP, RDP e transações financeiras são sensíveis a alta latência.

## Exemplos
```bash
# Medir RTT médio
ping -c 5 8.8.8.8

# Exemplo de saída
round-trip min/avg/max = 12.3/14.1/16.0 ms
```

```text
Aproximação física (fibra)
~5 µs por km de ida => ~1 ms de RTT para ~100 km
Sampa -> N. York ≈ 60-80 ms de RTT (distância + roteadores)
```

## Boas práticas
- Usar CDN/edge para aproximar o servidor do usuário.
- Priorizar a redução de RTTs (handshakes, redirects) sobre otimizar banda.
- Monitorar não apenas a média, mas também jitter e picos de latência.
- Evitar bufferbloat: buffers excessivos nos roteadores aumentam a latência.

## Armadilhas comuns
- Confundir latência com banda: são métricas independentes.
- Ignorar o jitter, que causa cortes em voz/vídeo mesmo com média baixa.
- Medir apenas um salto (localhost/gateway) e concluir que a rede inteira está bem.
- Esquecer que protocolos como o handshake TCP/TLS adicionam múltiplos RTTs.

## Relacionadas
- [[Largura-de-Banda]]
- [[CDN]]
- [[ICMP]]
- [[Streaming]]
- [[Diagnostico]]