---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Sockets

#area/estudos #estudos/redes #conceito

**Resumo:** Endpoint de comunicação bidirecional entre processos (endereço IP + porta + protocolo), base da programação de rede via TCP/UDP e de protocolos como WebSocket.

## Conceitos-chave
- **Definição:** socket = IP + porta + protocolo (TCP ou UDP), identificando unicamente um ponto de conexão.
- **Fluxo TCP (servidor):** socket() → bind() → listen() → accept().
- **Fluxo TCP (cliente):** socket() → connect().
- **Full-duplex:** dados trafegam nas duas direções simultaneamente.
- **Stream vs datagram:** SOCK_STREAM (TCP, ordem garantida) vs SOCK_DGRAM (UDP, sem conexão).
- **WebSocket:** protocolo de aplicação que mantém canal bidirecional sobre TCP (ws://, wss://).

## Exemplos
```python
import socket

# Servidor TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 8080))
s.listen(5)
conn, addr = s.accept()
data = conn.recv(1024)
conn.sendall(b"ok")
conn.close()
```

```python
# Cliente UDP
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"oi", ("192.168.1.10", 9000))
dados, addr = s.recvfrom(1024)
```

## Boas práticas
- Fechar sockets sempre (context manager ou finally) para não vazar file descriptors.
- Tratar erros não bloqueantes (EAGAIN/EWOULDBLOCK) em servidores concorrentes.
- Definir timeouts para evitar conexões penduradas.
- Escalar com event loop/async (asyncio, epoll, kqueue) em vez de thread por conexão.

## Armadilhas comuns
- Não fechar a conexão vaza descritores e esgota os recursos do processo.
- Confundir socket do sistema operacional com WebSocket (camadas diferentes).
- Bloquear o thread principal com recv() síncrono trava a aplicação.
- Ignorar o tamanho do buffer e fazer recv() incompleto por mensagem.

## Relacionadas
- [[TCP]]
- [[UDP]]
- [[Portas]]
- [[Handshake]]
- [[IP]]