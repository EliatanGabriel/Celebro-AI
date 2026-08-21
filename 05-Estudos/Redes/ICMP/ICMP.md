---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# ICMP

#area/estudos #estudos/redes #conceito

**Resumo:** Protocolo da camada de rede (Internet Control Message Protocol) usado para controle, diagnóstico e reporte de erros — base do ping e do traceroute.

## Conceitos-chave
- **Echo request/reply:** mensagens do ping que medem round-trip time e perda.
- **Destination unreachable:** informa que o destino, porta ou fragmento não é alcançável.
- **Time exceeded:** usado no traceroute, quando o TTL do pacote chega a zero.
- **TTL:** campo do IP que limita o número de hops e evita loops infinitos.
- **Sem portas:** ICMP não usa portas TCP/UDP; usa type e code.
- **Path MTU Discovery:** usa "fragmentation needed" para descobrir o MTU do caminho.

## Exemplos
```bash
ping -c 4 google.com
traceroute -n 8.8.8.8
# Exemplo de tipo/código
# 0 = echo reply | 8 = echo request
# 3 = destination unreachable | 11 = time exceeded
```

```text
Fluxo do traceroute
1. Envia pacote UDP com TTL=1 -> primeiro roteador responde "time exceeded"
2. TTL=2 -> segundo roteador responde
3. Repete até o destino responder
```

## Boas práticas
- Permitir ICMP de forma limitada (echo) para manter diagnóstico da rede.
- Não bloquear "fragmentation needed", pois isso quebra a descoberta de MTU.
- Monitorar RTT e perda de pacotes como métricas de saúde do enlace.
- Combinar ping e traceroute para localizar onde o problema ocorre.

## Armadilhas comuns
- Bloquear todo ICMP no firewall derruba o path MTU discovery e causa perdas.
- "time exceeded" de um hop não significa falha: alguns roteadores não respondem.
- Confundir ICMP com TCP/UDP na análise de tráfego.
- Achar que ping baixo garante boa experiência: não mede banda nem jitter.

## Relacionadas
- [[IP]]
- [[Latencia]]
- [[Diagnostico]]
- [[Protocolos]]