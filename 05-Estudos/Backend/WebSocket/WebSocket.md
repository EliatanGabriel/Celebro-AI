---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# WebSocket

#area/estudos #estudos/backend #conceito

**Resumo:** Protocolo que mantém uma conexão bidirecional e persistente entre cliente e servidor, permitindo comunicação em tempo real com baixa latência.

## Conceitos-chave
- **O que é:** upgrade a partir de um handshake HTTP (`101 Switching Protocols`); depois disso, ambos os lados enviam mensagens livremente.
- **Full-duplex:** o servidor pode empurrar dados sem que o cliente peça, ao contrário do HTTP requisição/resposta.
- **Quando usar:** chats, notificações, dashboards ao vivo, jogos multiplayer, colaboração e streaming.
- **Conexão persistente:** um socket fica aberto, com overhead menor por mensagem após o handshake.
- **Framing:** mensagens em frames binários ou texto, sem headers HTTP a cada envio.
- **Infra:** requer cuidados com load balancers (sticky/keepalive), proxies e firewall para conexões longas.
- **Alternativas:** SSE (Server-Sent Events) é unidirecional (servidor→cliente) e mais simples para notificações.

## Exemplos
```javascript
// Cliente
const socket = new WebSocket("wss://api.exemplo.com/chat");

socket.onopen = () => socket.send(JSON.stringify({ tipo: "msg", texto: "Oi" }));
socket.onmessage = (evento) => console.log("Recebido:", evento.data);
socket.onclose = () => console.log("Conexão encerrada");
```

```javascript
// Servidor com Socket.IO (Node.js)
import { Server } from "socket.io";

const io = new Server(3000, { cors: { origin: "*" } });

io.on("connection", (socket) => {
  console.log("Cliente conectado:", socket.id);

  socket.on("msg", (dados) => {
    io.emit("msg", { de: socket.id, texto: dados.texto });
  });

  socket.on("disconnect", () => console.log("Desconectado"));
});
```

## Boas práticas
- Validar e autenticar na conexão (handshake) e revalidar em mensagens sensíveis.
- Implementar heartbeat/ping-pong para detectar conexões mortas.
- Usar backpressure e limitar taxa para não sobrecarregar o servidor.
- Reenviar/recuperar estado no reconexão (o cliente precisa tolerar quedas).
- Escalar com camada de pub/sub (Redis) para broadcast entre múltiplas instâncias.

## Armadilhas comuns
- Usar WebSocket quando uma chamada HTTP simples resolveria (comunicação pontual).
- Não tratar reconexão, deixando o cliente "preso" em estado quebrado.
- Enviar dados sensíveis sem criptografia (sempre `wss://`/TLS).
- Ignorar limites de conexões: cada socket ocupa memória e conexão de rede.
- Assumir entrega garantida: mensagens podem se perder; adicionar confirmação/replay quando necessário.

## Relacionadas
- [[HTTP]]
- [[Node-js]]
- [[Frontend]]
- [[Sockets]]
- [[gRPC]]
- [[Redis]]