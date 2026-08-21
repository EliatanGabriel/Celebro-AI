---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# gRPC

#area/estudos #estudos/backend #conceito

**Resumo:** Framework de RPC do Google baseado em HTTP/2 e Protocol Buffers, voltado para comunicação interna entre serviços com alta performance e contratos fortes.

## Conceitos-chave
- **O que é:** define serviços e mensagens em arquivos `.proto` e gera clientes/servidores em várias linguagens.
- **Quando usar:** comunicação entre microserviços, sistemas internos, streaming e cenários com alta demanda de performance.
- **Protocol Buffers:** serialização binária compacta e rápida, mais eficiente que JSON.
- **HTTP/2:** multiplexação de requisições, streaming bidirecional e compressão de headers.
- **Padrões de chamada:** unary (1 req / 1 res), server streaming, client streaming e bidirecional.
- **Contratos fortes:** o `.proto` versiona o contrato com compatibilidade de campos.
- **Diferenças-chave:** REST/GraphQL são ótimos para APIs públicas/browser; gRPC brilha no backend interno e streaming.

## Exemplos
```protobuf
// proto/usuarios.proto
syntax = "proto3";

service UsuarioService {
  rpc GetUsuario (UsuarioRequest) returns (Usuario);
  rpc ListarUsuarios (Vazio) returns (stream Usuario);
}

message UsuarioRequest {
  int32 id = 1;
}

message Usuario {
  int32 id = 1;
  string nome = 2;
}
```

```python
# Cliente gRPC gerado
import grpc
import usuarios_pb2, usuarios_pb2_grpc

canal = grpc.insecure_channel("localhost:50051")
stub = usuarios_pb2_grpc.UsuarioServiceStub(canal)
resposta = stub.GetUsuario(usuarios_pb2.UsuarioRequest(id=42))
print(resposta.nome)
```

## Boas práticas
- Manter o `.proto` como fonte única do contrato e versioná-lo no repositório.
- Usar gRPC para tráfego interno; expor REST/GraphQL (via gateway) para fora.
- Configurar timeouts, retries e deadlines nas chamadas.
- Proteger com TLS e autenticação (mTLS/Token) nas comunicações.
- Evoluir o schema adicionando campos com numeração compatível.

## Armadilhas comuns
- Usar gRPC em APIs públicas de navegador (exige proxy gRPC-Web).
- Quebrar compatibilidade ao reutilizar números de campos no `.proto`.
- Esquecer de tratar streams interrompidos e erros de rede.
- Assumir que gRPC é "REST binário": o modelo de contratos e chamadas é diferente.
- Ignorar que payloads binários são menos legíveis/difíceis de depurar sem ferramentas.

## Relacionadas
- [[APIs]]
- [[HTTP]]
- [[Protocol-Buffers]]
- [[WebSocket]]
- [[Microservicos]]