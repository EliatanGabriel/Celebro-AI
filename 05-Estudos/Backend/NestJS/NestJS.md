---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# NestJS

#area/estudos #estudos/backend #conceito

**Resumo:** Framework Node.js progressivo e opinionativo, escrito em TypeScript, com arquitetura modular, injeção de dependência e inspiração no Angular.

## Conceitos-chave
- **O que é:** estrutura completa para backend Node/TypeScript; roda sobre Express (ou Fastify) por baixo.
- **Quando usar:** aplicações corporativas e APIs que precisam de arquitetura sólida, testabilidade e escala em equipe.
- **Módulos:** cada funcionalidade vive em um `@Module` que agrupa controllers, providers e imports.
- **Injeção de dependência:** containers resolvem dependências automaticamente; facilita testes com mocks.
- **Decorators:** `@Controller`, `@Get`, `@Injectable`, `@Inject` organizam o código declarativamente.
- **Extras:** guardas (auth), interceptors, pipes (validação/transformação), filters (erros) e WebSockets.
- **Diferenças-chave:** Express é minimalista e flexível; NestJS impõe estrutura, DI e TypeScript, com mais curvas de aprendizado.

## Exemplos
```typescript
// usuarios.module.ts
import { Module } from "@nestjs/common";
import { UsuariosController } from "./usuarios.controller";
import { UsuariosService } from "./usuarios.service";

@Module({
  controllers: [UsuariosController],
  providers: [UsuariosService],
})
export class UsuariosModule {}
```

```typescript
// usuarios.controller.ts
import { Controller, Get, Post, Body, Param } from "@nestjs/common";

@Controller("usuarios")
export class UsuariosController {
  constructor(private readonly service: UsuariosService) {}

  @Get(":id")
  getUm(@Param("id") id: string) {
    return this.service.buscar(id);
  }

  @Post()
  criar(@Body() dados: CriarUsuarioDto) {
    return this.service.criar(dados);
  }
}
```

```bash
nest new app && nest g module usuarios && nest g controller usuarios
```

## Boas práticas
- Organizar por módulos de domínio e manter providers pequenos e testáveis.
- Usar pipes com class-validator para validar DTOs no `@Body()`.
- Aproveitar guards para autenticação/autorização centralizadas.
- Testar controllers e services com o TestModule do Nest.
- Configurar openapi (Swagger) com o módulo `@nestjs/swagger`.

## Armadilhas comuns
- Tratar NestJS como um "Express com classes", ignorando o container de DI.
- Criar um único módulo gigante em vez de dividir por domínio.
- Misturar decorators de forma inconsistente (ex.: providers sem `@Injectable`).
- Assumir que `NestFactory` em modo `nest build` continua com hot reload automático.
- Comparar a NestJS com Express sem considerar que a estrutura e a DI têm custo de aprendizado.

## Relacionadas
- [[TypeScript]]
- [[Node-js]]
- [[Backend]]
- [[Express]]
- [[Middleware]]
- [[GraphQL]]