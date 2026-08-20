---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Props

#area/estudos #estudos/frontend #conceito

**Resumo:** Dados imutáveis passados de um componente pai para um filho, formando o fluxo unidirecional de dados nos frameworks modernos.

## Conceitos-chave
- **Fluxo unidirecional:** os dados descem do pai para o filho; mudanças sobem via callbacks, nunca por alteração direta da prop.
- **Imutabilidade:** props não devem ser modificadas pelo componente receptor — ele apenas as lê.
- **Composição:** `children`/slots permitem passar conteúdo e componentes como prop, viabilizando composição.
- **Props vs estado:** props vêm de fora e são imutáveis; estado é interno e mutável pelo próprio componente.
- **Tipagem:** TypeScript (`interface Props`) ou PropTypes documentam e validam a interface do componente.
- **Modelo mental:** o componente é uma função pura — `f(props) -> UI` — o que torna previsível e testável.

## Exemplos

```tsx
// React: props tipadas, imutáveis
type UserCardProps = {
  name: string;
  email: string;
  onSelect?: (id: string) => void;
};

export function UserCard({ name, email, onSelect }: UserCardProps) {
  return (
    <div onClick={() => onSelect?.(email)}>
      <h3>{name}</h3>
      <p>{email}</p>
    </div>
  );
}
```

```vue
<!-- Vue: props com validação -->
<script setup lang="ts">
defineProps<{ title: string; done?: boolean }>();
</script>

<template>
  <p :class="{ done }">{{ title }}</p>
</template>
```

## Boas práticas
- Manter as props mínimas e com nomes claros sobre o que representam.
- Tipar todas as props (TypeScript) e definir valores padrão para opcionais.
- Usar callbacks (`onChange`, `onSubmit`) para o filho comunicar eventos ao pai.
- Preferir `children`/slots para composição em vez de passar muitos dados fragmentados.
- Derivar estado interno de props com cuidado — prefira calcular durante a renderização quando possível.

## Armadilhas comuns
- Mutar props no filho (viola o fluxo unidirecional e gera bugs de renderização).
- Passar objetos/arrays novos a cada render do pai, causando re-render desnecessário nos filhos.
- Prop drilling excessivo (passar props por muitos níveis) — considere contexto ou store.
- Duplicar props em estado local (`useState(props.x)`), criando duas fontes de verdade.
- Renomear cada prop sem ganho semântico, dificultando a leitura do componente.

## Relacionadas
- [[Componentes]]
- [[React]]
- [[Hooks]]
- [[TypeScript-Frontend]]
- [[Vue]]
- [[Svelte]]