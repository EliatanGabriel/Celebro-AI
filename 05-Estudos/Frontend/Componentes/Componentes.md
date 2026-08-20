---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Componentes

#area/estudos #estudos/frontend #conceito

**Resumo:** Blocos reutilizáveis de interface que encapsulam estrutura, estilo e comportamento, recebendo dados via props e gerenciando estado próprio.

## Conceitos-chave
- **Encapsulamento:** cada componente isola sua marcação, estilos e lógica, com uma interface pública (props).
- **Props:** entradas imutáveis vindas do pai; **estado:** dados internos mutáveis que mudam conforme a interação.
- **Composição:** componentes são construídos pela união de outros menores (children/slots), em vez de herança.
- **Ciclo de vida:** criação, atualização e destruição controlam quando buscar dados, registrar listeners e limpar recursos.
- **Isolamento e reuso:** o mesmo componente renderiza em contextos diferentes desde que receba props distintas.
- **Modelo mental nos frameworks:** React e Vue usam virtual DOM com re-render declarativo; Svelte compila o componente para JS puro; Angular usa classes com templates.

## Exemplos

```tsx
// componente React reutilizável com props e estado
type ButtonProps = {
  label: string;
  onClick: () => void;
  disabled?: boolean;
};

export function Button({ label, onClick, disabled }: ButtonProps) {
  return (
    <button type="button" onClick={onClick} disabled={disabled}>
      {label}
    </button>
  );
}
```

```tsx
// composição: componente pai que combina filhos
export function Card({ title, children }) {
  return (
    <section className="card">
      <h2>{title}</h2>
      {children}
    </section>
  );
}
```

## Boas práticas
- Manter componentes pequenos e com responsabilidade única.
- Preferir composição a herança e a prop drilling excessivo.
- Tipar props explicitamente (TypeScript) e definir valores padrão.
- Elevar estado só quando necessário (`lifting state up`) e mantê-lo mínimo.
- Nomear componentes pela responsabilidade, não pela aparência (ex.: `UserForm` em vez de `LeftPanel`).

## Armadilhas comuns
- Criar "God components" com centenas de linhas que fazem tudo.
- Duplicar estado em vários componentes em vez de elevá-lo ou usar store.
- Mutar props diretamente (viola o fluxo unidirecional e causa bugs).
- Re-renderizar em cascata por passar objetos/arrays novos a cada render.
- Misturar responsabilidades de apresentação e dados no mesmo componente sem separação clara.

## Relacionadas
- [[React]]
- [[Vue]]
- [[Hooks]]
- [[Frontend]]
- [[Props]]
- [[Svelte]]
- [[Angular]]
- [[TypeScript-Frontend]]