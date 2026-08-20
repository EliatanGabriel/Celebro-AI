---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# UDP

#area/estudos #estudos/redes #conceito

**Resumo:** Protocolo de transporte sem conexão e sem garantias (User Datagram Protocol), com baixo overhead e alta velocidade; usado em streaming, jogos, DNS, VoIP e DHCP.

## Conceitos-chave
- **Sem conexão:** não há handshake; o datagrama é enviado diretamente.
- **Sem confirmação/retransmissão:** perdas não são recuperadas pelo protocolo.
- **Header mínimo:** 8 bytes (contra 20+ do TCP).
- **Sem ordem garantida:** datagramas podem chegar fora de sequência.
- **Uso ideal:** aplicações tolerantes a perdas e sensíveis à latência (áudio/vídeo, jogos).
- **Multiplexação por portas:** mesma faixa de portas do TCP, em espaço próprio.

## Exemplos
```text
Header UDP
+----------+----------+--------+----------+
| Src Port | Dst Port | Length | Checksum |
| 2 bytes  | 2 bytes  | 2 B    | 2 bytes  |
+----------+----------+--------+----------+
```

```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"oi", ("192.168.1.10", 9000))
dados, addr = s.recvfrom(1024)
```

## Boas práticas
- Usar UDP quando perda leve é aceitável e a latência domina a experiência.
- Adicionar na aplicação o que o UDP não oferece: sequência, checksum, retransmissão (se preciso).
- Considerar QUIC quando precisar de confiabilidade com baixa latência.
- Ajustar buffers de recepção, pois datagramas podem ser descartados em picos.

## Armadilhas comuns
- Usar UDP para transferência confiável sem uma camada própria de controle.
- Achar que UDP "não tem controle": o checksum ainda protege integridade básica.
- Confundir os requisitos com os do TCP (ordem e retransmissão não existem).
- Esquecer que a mesma porta em UDP e TCP são serviços independentes.

## Relacionadas
- [[TCP]]
- [[Streaming]]
- [[Sockets]]
- [[Portas]]
- [[TCP-IP]]