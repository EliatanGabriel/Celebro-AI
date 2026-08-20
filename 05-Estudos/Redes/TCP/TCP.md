---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# TCP

#area/estudos #estudos/redes #conceito

**Resumo:** Protocolo de transporte orientado a conexão e confiável (Transmission Control Protocol), com entrega ordenada, controle de fluxo e congestionamento; base de HTTP, e-mail, SSH e FTP.

## Conceitos-chave
- **Conexão:** three-way handshake (SYN → SYN-ACK → ACK) antes dos dados.
- **Segmento:** dados + cabeçalho com portas, sequence number, ACK, flags e janela.
- **Confiabilidade:** ACKs e retransmissão de segmentos perdidos.
- **Ordenação:** números de sequência reordenam segmentos que chegam fora de ordem.
- **Controle de fluxo:** janela do receptor limita o envio à capacidade de consumo.
- **Congestionamento:** controle de janela do emissor (slow start, congestion avoidance, retransmissão).
- **Flags:** SYN, ACK, FIN, RST, PSH, URG controlam estados e comportamento.

## Exemplos
```text
Sequência de segmentos
Emissor envia 1-1000, 1001-2000, 2001-3000
Receptor responde ACK 1000 -> 2000 (perdeu 2001-3000)
Emissor retransmite 2001-3000 e reduz a janela de congestionamento
```

```text
HTTP/1.1 e HTTPS usam TCP
Porta 80 (HTTP) e 443 (HTTPS)
```

## Boas práticas
- Usar TCP quando a entrega completa e ordenada é obrigatória (transações, arquivos).
- Aplicar TLS sobre TCP para proteger os dados transportados.
- Ajustar buffers do sistema operacional e timeouts quando o desempenho exigir.
- Monitorar retransmissões e RTT para detectar degradação do enlace.

## Armadilhas comuns
- Em redes com alta perda, o TCP reduz drasticamente o throughput (banda sobra, mas nada flui).
- Head-of-line blocking: um segmento perdido segura os seguintes, mesmo entregues.
- O handshake adiciona RTTs extras antes do primeiro dado útil.
- Confundir controle de fluxo (receptor) com controle de congestionamento (rede).

## Relacionadas
- [[UDP]]
- [[IP]]
- [[Handshake]]
- [[TCP-IP]]
- [[HTTPS]]
- [[Sockets]]