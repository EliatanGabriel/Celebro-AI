---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Diagnostico

#area/estudos #estudos/redes #conceito

**Resumo:** Conjunto de técnicas e ferramentas para identificar falhas e medir desempenho de rede, cobrindo latência, perda de pacotes, rotas, portas e tráfego.

## Conceitos-chave
- **ping:** mede round-trip time (RTT) e perda de pacotes via ICMP.
- **traceroute/tracert:** mostra os hops percorridos até o destino e onde há atraso/perda.
- **nslookup/dig:** consultam registros DNS e testam resolução de nomes.
- **ss/netstat:** listam conexões ativas e portas em escuta no host.
- **tcpdump/Wireshark:** capturam e analisam pacotes (packet sniffing).
- **iperf3:** mede o throughput real e a banda efetiva entre dois pontos.
- **Teste em camadas:** validar do físico (L1) até a aplicação (L7) para isolar o problema.

## Exemplos
```bash
ping -c 5 8.8.8.8                    # latência e perda
traceroute -n example.com            # hops até o destino
dig +short example.com A             # resolução DNS
ss -tulnp                            # portas em escuta
tcpdump -i eth0 port 443 -n -c 20    # captura de tráfego HTTPS
iperf3 -c servidor -t 10             # teste de throughput
```

```text
Sequência de isolamento
1. L1 físico: cabo/conector, link up?
2. L2 enlace: ARP resolve? VLAN correta?
3. L3 rota: ping no gateway e no destino
4. L4 porta: conexão TCP/UDP aceita?
5. L7 aplicação: serviço responde corretamente?
```

## Boas práticas
- Testar sempre em camadas, de baixo para cima, para não tratar sintoma.
- Isolar variáveis: teste local, depois rede, depois destino.
- Estabelecer um baseline de latência/perda para comparar quando algo falhar.
- Documentar comandos e resultados para reprodução e post-mortem.

## Armadilhas comuns
- Firewall bloqueando ICMP faz o ping falhar mesmo com a rede saudável.
- Confundir perda de pacote com alta latência (são sintomas distintos).
- Usar ping para medir banda: ping não mede throughput.
- Interpretar "time exceeded" do traceroute como falha: um hop pode simplesmente não responder.

## Relacionadas
- [[ICMP]]
- [[TCP]]
- [[Latencia]]
- [[IP]]
- [[Portas]]