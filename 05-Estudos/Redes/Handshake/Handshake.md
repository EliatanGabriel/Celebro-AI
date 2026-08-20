---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Handshake

#area/estudos #estudos/redes #conceito

**Resumo:** Sequência de mensagens que negocia e estabelece uma conexão, abrangendo o three-way handshake do TCP e a negociação criptográfica do TLS.

## Conceitos-chave
- **TCP 3-way handshake:** SYN → SYN-ACK → ACK; alinha números de sequência e abre a conexão.
- **TCP 4-way teardown:** FIN → ACK → FIN → ACK para encerrar a conexão de forma ordenada.
- **TLS handshake:** negocia criptografia, autentica o servidor (certificado) e troca chaves de sessão.
- **RTT:** cada handshake adiciona latência; TLS 1.3 reduz para 1 RTT (0-RTT com resumption).
- **Half-open connections:** conexões SYN recebidas sem ACK final são alvo de SYN flood.

## Exemplos
```text
TCP 3-way handshake
Cliente  --SYN (seq=x)------------------>  Servidor
Cliente  <--SYN+ACK (seq=y, ack=x+1)---  Servidor
Cliente  --ACK (seq=x+1, ack=y+1)------>  Servidor
Conexão estabelecida
```

```text
TLS 1.3 handshake (1 RTT)
Cliente  -> ClientHello (suites, chaves efêmeras)
Servidor -> ServerHello, certificado, Finished
Cliente  -> Finished (chaves de sessão aplicadas)
```

## Boas práticas
- Usar TLS 1.3 para reduzir o custo de RTTs extras na negociação.
- Configurar timeouts de conexão e limites de conexões half-open (SYN cookies).
- Verificar a cadeia de certificados durante o handshake TLS.
- Monitorar a taxa de handshakes incompletos como possível sinal de ataque.

## Armadilhas comuns
- Confundir TCP handshake com TLS handshake: são camadas e objetivos distintos.
- Achar que handshake lento = rede lenta: pode ser CPU do servidor ou criptografia.
- Tratar SYN flood como falha de aplicação: é ataque à camada de transporte.
- Ignorar que o encerramento (4-way teardown) também pode travar em estados TIME_WAIT/CLOSE_WAIT.

## Relacionadas
- [[TCP]]
- [[TLS]]
- [[HTTPS]]
- [[Sockets]]