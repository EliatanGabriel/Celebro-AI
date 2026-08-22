---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Módulos e Tipos Externos (TypeScript)

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** O sistema de módulos do TypeScript organiza o código com import/export, consome tipos de bibliotecas via @types e é configurado pelo tsconfig.json, compilado com tsc ou executado com ts-node.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `export ...` | Exporta membro nomeado | `export function somar() {}` |
| `import { x } from "m"` | Importa nomeado | `import { somar } from "./math"` |
| `export default` | Exportação única principal | `export default class App {}` |
| `export { a } from "m"` | Re-export | `export * from "./tipos"` |
| `@types/pacote` | Tipos da comunidade | `npm i -D @types/express` |
| `.d.ts` | Declaração sem implementação | `declare module "x" {}` |
| `"target"` | JS gerado (ES2017 etc.) | `"target": "ES2020"` |
| `"strict": true` | Checagens rígidas | no tsconfig.json |
| `"outDir"` | Pasta de saída | `"outDir": "dist"` |

## Exemplos

```ts
// src/matematica.ts
export function somar(a: number, b: number): number {
  return a + b;
}

const PI = 3.14;
export default PI;

// src/app.ts
import PI from "./matematica";
import { somar } from "./matematica";
export { somar }; // re-exporta para quem importa de app
```

```jsonc
// tsconfig.json essencial
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "outDir": "dist",
    "rootDir": "src"
  },
  "include": ["src"]
}
```

```bash
npx tsc                 # compila para dist/
npx ts-node src/app.ts  # executa TS direto (dev)
npm i -D @types/node    # tipos do Node.js
```

## Boas práticas

- Prefira exports nomeados; use `default` só para o "assunto principal" do arquivo.
- Instale `@types/*` como devDependency junto à lib que precisa.
- Mantenha um único `tsconfig.json` por projeto e versione-o.
- Habilite `"strict": true` desde o início do projeto.
- Use re-export (`index.ts`) para simplificar imports profundos.

## Armadilhas comuns

- Esquecer extensão/alias e receber erro de módulo não encontrado.
- Misturar `export default` e nomeados no mesmo módulo sem critério.
- Rodar `tsc` sem tsconfig na raiz e compilar arquivos soltos errados.
- Achar que `import type` é opcional sempre: evita imports fantasma no build.
- Editar `.d.ts` de `node_modules`: as mudanças somem ao reinstalar.

## Relacionadas

- [[TypeScript]]
- [[JavaScript]]
- [[TS-no-Dia-a-Dia]]
