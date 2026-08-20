---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Node-js

#area/estudos #estudos/backend #conceito

**Resumo:** Runtime JavaScript no servidor baseado no motor V8 do Chrome, assíncrono e orientado a eventos, com um enorme ecossistema via npm.

## Conceitos-chave
- **O que é:** ambiente de execução que permite rodar JavaScript fora do navegador (servidor, CLIs, build tools).
- **Event loop:** modelo single-threaded assíncrono; I/O não bloqueia, callbacks/promises continuam quando terminam.
- **npm:** maior registro de pacotes do mundo; `package.json` gerencia dependências e scripts.
- **Single-thread + workers:** lógica JavaScript roda em uma thread; tarefas CPU-bound usam `worker_threads` ou múltiplos processos.
- **Módulos:** `CommonJS` (`require`) e `ES Modules` (`import`) coexistindo no ecossistema.
- **Uso típico:** APIs REST (Express/Nest), WebSockets, microsserviços, ferramentas CLI e builds (Vite/Webpack).
- **Diferenças-chave:** comparação com Python (GIL/threads) e Java (JVM/threads): modelo de concorrência é dirigido a eventos, ideal para I/O intensivo.

## Exemplos
```javascript
import { createServer } from "node:http";

const server = createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ ok: true }));
});

server.listen(3000, () => console.log("Rodando na porta 3000"));
```

```javascript
// Event loop: I/O assíncrono não bloqueia
import { readFile } from "node:fs/promises";

const dados = await readFile("config.json", "utf-8"); // não bloqueia o servidor
console.log(JSON.parse(dados).porta);
```

## Boas práticas
- Preferir `async/await` e APIs de promises em vez de callbacks aninhados.
- Usar `worker_threads` ou processos separados para CPU-bound.
- Manter o `package.json` com scripts de dev/build/test padronizados.
- Configurar gerenciador de versão do Node (nvm) e `engines` no package.
- Tratar erros em promises (`.catch`/try-catch) para não "morrer silenciosamente".

## Armadilhas comuns
- Bloquear o event loop com loops síncronos pesados, travando todo o servidor.
- Usar `console.log` em produção como observabilidade (usar logging estruturado).
- Ignorar o callback/promise e deixar erros não capturados.
- Subir dependências desatualizadas sem auditoria de segurança.
- Confundir concorrência: single-thread não significa incapaz de paralelismo de I/O, mas sim que CPU intensiva congestiona.

## Relacionadas
- [[JavaScript]]
- [[Express]]
- [[Backend]]
- [[APIs]]
- [[NestJS]]
- [[WebSocket]]
- [[Queue]]