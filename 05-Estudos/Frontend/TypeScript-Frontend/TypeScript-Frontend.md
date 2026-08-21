---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# TypeScript-Frontend

#area/estudos #estudos/frontend #conceito

**Resumo:** Aplicação de TypeScript no frontend para tipar props, estado, eventos e componentes, reduzindo bugs e melhorando a manutenibilidade de grandes bases de código.

## Conceitos-chave
- **Tipagem de props:** interfaces descrevem a API do componente — obrigatórias, opcionais e callbacks — com autocompletar e validação em tempo de compilação.
- **Tipos de estado:** modelos tipados para `useState`, stores e respostas de API evitam estados inválidos.
- **Discriminated unions:** união de tipos com um campo discriminador modelam estados de request (loading/success/error) de forma segura.
- **Generic components:** componentes e hooks tipados por parâmetro (`useList<T>`, `Table<T>`) reutilizam lógica com tipos corretos.
- **Utility types:** `Partial`, `Pick`, `Omit` e `Record` derivam tipos sem reescrevê-los.
- **Eventos e DOM:** tipos específicos (`MouseEvent`, `KeyboardEvent`, `FormEvent`) evitam erros de handler.
- **tsconfig:** `strict: true` e alias de imports (`@/components`) padronizam o projeto.

## Exemplos

```tsx
import { useState } from 'react';

type Status = 'loading' | 'success' | 'error';

type User = { id: string; name: string; email: string };

type UserCardProps = {
  user: User;
  onSelect: (user: User) => void;
  disabled?: boolean;
};

export function UserCard({ user, onSelect, disabled }: UserCardProps) {
  const [status, setStatus] = useState<Status>('loading');

  return (
    <button type="button" onClick={() => onSelect(user)} disabled={disabled}>
      {user.name} — {user.email}
    </button>
  );
}
```

```ts
// estado de requisição modelado com union discriminada
type FetchState<T> =
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; message: string };

function handle<T>(state: FetchState<T>) {
  switch (state.status) {
    case 'loading':
      return 'Carregando...';
    case 'success':
      return state.data;
    case 'error':
      return state.message;
  }
}
```

## Boas práticas
- Habilitar `strict: true` e deixar o compilador apontar problemas (nunca silenciar com `any`).
- Tipar props explicitamente e inferir o que é derivável (estado, retornos).
- Modelar estados com unions em vez de booleanos soltos (`isLoading`, `hasError`).
- Preferir `type` para uniões e `interface` para objetos extensíveis, com critério consistente.
- Extrair tipos compartilhados para módulos próprios (ex.: `types.ts`) e reutilizar em props e API.

## Armadilhas comuns
- Usar `any` para "resolver rápido", perdendo a segurança que motivou o TypeScript.
- Escolher `interface` vs `type` sem regra, gerando inconsistência no código.
- Tipar eventos com o tipo errado (`ChangeEvent` no lugar de `FormEvent`), criando bugs sutis.
- Preferir `enum` quando `const` objects + unions resolveriam com menos surpresas.
- Ignorar `strictNullChecks` e tratar valores possivelmente `null`/`undefined` como presentes.

## Relacionadas
- [[TypeScript]]
- [[React]]
- [[Frontend]]
- [[Props]]
- [[Angular]]
- [[Vue]]