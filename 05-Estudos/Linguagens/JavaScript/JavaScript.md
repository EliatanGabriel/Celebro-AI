---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# JavaScript

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem multiparadigma que roda no navegador e no servidor (Node.js), base do desenvolvimento web moderno, com execução assíncrona e orientada a eventos.

## Conceitos-chave
- Multiparadigma: imperativa, orientada a objetos (por protótipos) e funcional (funções de primeira classe).
- Tipagem dinâmica e fraca: tipos são definidos em runtime e conversões são automáticas (e surpreendentes).
- Interpretada/JIT: o V8 compila o código em tempo de execução; roda no navegador e no servidor via Node.js.
- Event loop e modelo assíncrono não-bloqueante: Promises, `async`/`await` e callbacks.
- Objetos baseados em protótipos; herança via `Object.create` e classes sintáticas (`class`).
- Particularidade: ecossistema gigante no npm e JSON nativo da linguagem.
- Hoisting, closures e escopo por função (com `let`/`const` para escopo de bloco).

## Exemplos
```javascript
const usuarios = [
  { nome: 'Ana', ativo: true },
  { nome: 'Bruno', ativo: false },
];

const ativos = usuarios.filter(u => u.ativo).map(u => u.nome);

async function carregarDados() {
  try {
    const resp = await fetch('https://api.exemplo.com/dados');
    const dados = await resp.json();
    console.log(ativos, dados);
  } catch (erro) {
    console.error('Falha ao carregar:', erro);
  }
}
carregarDados();
```

## Boas práticas
- Prefira `const`/`let` a `var` para evitar hoisting confuso e escopo vazado.
- Use `===` (igualdade estrita) em vez de `==`.
- Trate operações assíncronas com `async`/`await` e `try/catch`.
- Estruture o código em módulos (ES modules) e mantenha funções puras onde possível.
- Teste com frameworks consolidados (Jest, Vitest) e use lint (ESLint).

## Armadilhas comuns
- Comparações `==` com coerção surpreendente (`0 == false` é `true`).
- `NaN !== NaN`, quebrando comparações diretas de números inválidos.
- Callback hell e Promises sem tratamento de rejeição (unhandled rejection).
- Variação de `this` em callbacks; use arrow functions para preservar o contexto.
- Confundir cópia rasa com profunda: objetos aninhados são compartilhados por referência.

## Relacionadas
- [[TypeScript]]
- [[Frontend]]
- [[Node-js]]
- [[DOM]]