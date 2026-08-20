---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Protocol-Buffers

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Mecanismo de serialização binária de dados criado pelo Google; define um schema `.proto` tipado e gera código em múltiplas linguagens, sendo a base do gRPC e mais compacto que JSON/XML.

## Conceitos-chave
- **.proto**: definição de mensagens com campos tipados, números de campo e regras de cardinalidade.
- **Números de campo**: identificadores usados na codificação; campos 1-15 usam 1 byte no wire, o restante 2+ bytes.
- **Wire format (varint)**: codificação compacta; tipos escalares como int32, string, bytes, bool, enums e repeated (listas).
- **Compatibilidade**: regras de evolução — renomear campos, adicionar campos com novos números, `reserved` para evitar reuso.
- **Code generation**: `protoc` (ou plugins como `buf`) gera classes/estruturas em Go, Java, Python, Rust, TS etc.
- **gRPC**: framework RPC baseado em protobuf para contratos de serviço (`service` + `rpc`) com streaming e HTTP/2.
- **Oneof e map**: `oneof` limita a mensagem a um dos campos; `map<K,V>` para dicionários.

## Exemplos
Definição de contrato (`person.proto`):

```proto
syntax = "proto3";

package exemplo;

message Person {
  string name = 1;
  int32 id = 2;
  string email = 3;
  repeated string phones = 4;
  reserved 5, 6;          // campos removidos não podem ser reutilizados
  reserved "old_field";
}
```

Gerar código e usar:

```bash
protoc --go_out=. --go_opt=paths=source_relative person.proto
```

```go
p := &exemplo.Person{Name: "Ana", Id: 42, Phones: []string{"11 99999-0000"}}
data, _ := proto.Marshal(p)
```

Serviço gRPC:

```proto
service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply);
}
```

## Boas práticas
- Comece numerando campos do 1 em diante e reserve números/campos ao remover, nunca reutilize.
- Prefira `int64`/`string` para estabilidade; use `uint32`/`sfixed32` conforme o domínio (valores negativos, grandes).
- Mantenha os arquivos `.proto` como fonte da verdade e gere artefatos no CI.
- Use `buf lint`/`buf breaking` para validar mudanças de schema sem quebrar consumidores.
- Evite `required` (não existe em proto3) e trate default values como ausentes quando necessário.

## Armadilhas comuns
- Reutilizar número de campo removido corrompe dados de consumidores antigos.
- `int32` com valor negativo é codificado como 10 bytes (varint); prefira `sint32`/`sint64`.
- Mensagens são imutáveis após publicação: mudar tipo de campo quebra compatibilidade.
- Esquecer de regenerar os stubs após mudar o schema gera erros de import/timeout.
- Dados default (0, "", false) não são serializados — não confunda com ausência do campo.

## Relacionadas
- [[Ferramentas]]
- [[Postman]]