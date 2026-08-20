---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Angular

#area/estudos #estudos/frontend #conceito

**Resumo:** Framework completo da Google, TypeScript-first, para aplicações corporativas, com módulos, injeção de dependência, two-way binding e roteamento próprios.

## Conceitos-chave
- **Modelo mental:** aplicação composta por componentes (classe + template + estilos), organizados em módulos ou standalone, com estado e fluxo de dados controlados.
- **TypeScript-first:** tipos, decorators (`@Component`, `@Input`, `@Output`) e compilação via ngc esbarram em timepos de build mais lentos, mas com segurança de tipos nativa.
- **Two-way data binding:** `[(ngModel)]` sincroniza estado do componente e template, com fluxo de cima para baixo.
- **Injeção de dependência (DI):** serviços são fornecidos e injetados pelo framework, facilitando testes e reuso.
- **Módulos e standalone:** desde Angular 14+, componentes standalone reduzem a necessidade de `NgModule`.
- **Change detection:** o framework detecta mudanças e re-renderiza via zone.js; `OnPush` otimiza quando o estado é imutável.
- **RxJS:** reatividade orientada a streams (Observables) no coração de HTTP, forms e estado.
- **Quando usar:** aplicações grandes e corporativas com equipe estruturada, onde consistência e escala pesam mais que leveza.

## Exemplos

```typescript
// app.component.ts
import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-counter',
  standalone: true,
  template: `
    <p>Contagem: {{ count() }}</p>
    <button (click)="increment()">+1</button>
  `,
})
export class CounterComponent {
  count = signal(0);
  increment() {
    this.count.update((n) => n + 1);
  }
}
```

```typescript
// servico com DI injetado no componente
import { Injectable, inject } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class UsersService {
  getUsers() {
    return fetch('/api/users').then((r) => r.json());
  }
}
```

## Boas práticas
- Preferir componentes standalone e lazy loading de rotas para reduzir bundle inicial.
- Usar `ChangeDetectionStrategy.OnPush` com dados imutáveis.
- Aplicar Reactive Forms para validação complexa, em vez de template-driven.
- Gerar código com o CLI (`ng generate component`) para seguir convenções.
- Manter lógica de negócio em serviços testáveis, não nos componentes.

## Armadilhas comuns
- Confundir `NgModule` (agrupador Angular) com módulos ES (`import`/`export`).
- Abusar de two-way binding, criando fluxo de dados difícil de rastrear.
- Depender do change detection padrão em telas grandes — mutações diretas causam re-renders desnecessários.
- Esquecer de cancelar subscriptions RxJS (vazamento de memória) em componentes.
- Carregar a aplicação inteira sem lazy loading, com bundle inicial pesado.

## Relacionadas
- [[TypeScript]]
- [[Frontend]]
- [[Componentes]]
- [[NestJS]]
- [[TypeScript-Frontend]]
- [[Performance-Frontend]]