---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# TypeScript

#area/estudos #estudos/linguagens #conceito

**Resumo:** Superset do JavaScript que adiciona tipagem estática opcional, interfaces, generics e ferramentas de desenvolvimento superiores, compilado (transpilado) para JavaScript.

## Conceitos-chave
- Multiparadigma: herda tudo do JavaScript (imperativa, OO por protótipos, funcional) e adiciona um sistema de tipos estáticos.
- Tipagem estática e forte com inferência de tipos; tipos são apagados na compilação (type erasure).
- Não é executado diretamente: o `tsc` transpila TypeScript para JavaScript (target ES5/ES2020, etc.).
- Uso principal em aplicações web de grande porte (React, Angular, Vue) e backend Node.js.
- Interfaces, type aliases, generics, enums, union types e discriminated unions.
- Particularidade: structural typing (duck typing em tempo de compilação) e `strict` mode.

## Exemplos
```typescript
type Usuario = {
  nome: string;
  idade: number;
  ativo?: boolean;  // opcional
};

function adultos(usuarios: Usuario[]): string[] {
  return usuarios
    .filter(u => u.idade >= 18)
    .map(u => u.nome);
}

function identidade<T>(valor: T): T {
  return valor;
}

const lista: Usuario[] = [
  { nome: 'Ana', idade: 30 },
  { nome: 'Bruno', idade: 16 },
];

console.log(adultos(lista));          // ['Ana']
console.log(identidade<string>('ok')); // 'ok'
```

## Boas práticas
- Ative `strict: true` no tsconfig para máxima segurança de tipos.
- Prefira `type`/`interface` explícitos a `any`; use `unknown` quando o tipo é desconhecido.
- Use generics e utility types (`Partial`, `Pick`, `Omit`) em vez de duplicar tipos.
- Configure o target adequado e use esbuild/swc para compilação rápida em produção.
- Adote lint com typescript-eslint e formatação automática (Prettier).

## Armadilhas comuns
- Uso excessivo de `any`, eliminando a segurança de tipos que motivou o TS.
- Confundir `interface` com `type` em union types — interfaces não podem ser unions.
- Assumir que os tipos garantem validação em runtime: `as` é apenas uma afirmação em tempo de compilação.
- Não respeitar `strictNullChecks`, reintroduzindo null em lugares inesperados.
- Atualizar a versão do TypeScript sem revisar breaking changes entre projetos grandes.

## Relacionadas
- [[JavaScript]]
- [[Frontend]]
- [[Componentes]]