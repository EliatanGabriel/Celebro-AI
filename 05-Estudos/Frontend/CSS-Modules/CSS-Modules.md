---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# CSS-Modules

#area/estudos #estudos/frontend #conceito

**Resumo:** Técnica de escopo local para classes CSS por componente, evitando colisões de nomes, integrada a bundlers como Webpack e Vite.

## Conceitos-chave
- **Escopo local:** classes escritas em `styles.module.css` são transformadas em nomes únicos (ex.: `titulo_x7k2a`) durante o build.
- **Import como objeto:** o bundler devolve um mapa `{ titulo: "titulo_x7k2a" }`, ligando classe à marcação no JS.
- **Composição:** `composes` reaproveita regras de outra classe local, sem duplicar CSS.
- **Globais:** `:global(.classe)` escapa do escopo local quando a classe precisa ser compartilhada.
- **Integração:** ativado por convenção de nome (`*.module.css`) no Webpack (`css-loader` com `modules`) e Vite.
- **Quando usar:** apps com CSS por componente, sem depender de convenções de nomenclatura como BEM.

## Exemplos

```css
/* Button.module.css */
.button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
}
.primary {
  background: #3182ce;
  color: white;
}
:global(.focus-ring) {
  outline: 2px solid #90cdf4;
}
```

```tsx
// Button.tsx
import styles from './Button.module.css';

type ButtonProps = { primary?: boolean; children: React.ReactNode };

export function Button({ primary, children }: ButtonProps) {
  const className = primary ? styles.primary : '';
  return <button className={`${styles.button} ${className}`}>{children}</button>;
}
```

## Boas práticas
- Nomear arquivos com `.module.css` (ou `.module.scss`) e importar como objeto.
- Usar camelCase nos nomes de classe para acesso direto (`styles.buttonPrimary`).
- Combinar com Sass para nesting, variáveis e mixins.
- Reservar classes utilitárias globais para padrões transversais, mantendo o restante local.
- Lembrar que a classe final é determinada pelo objeto importado, não por string digitada.

## Armadilhas comuns
- Achar que seletores de elemento (`p`, `h1`) são escopados — apenas classes recebem hash.
- Esperar escopo em `id` (não são transformados).
- Construir nomes de classe dinamicamente (`styles["button" + cor]`) com chaves inexistentes, retornando `undefined`.
- Esquecer de importar o módulo no componente — sem o mapa, as classes não são aplicadas.
- Misturar `composes` com classes de outro módulo ou globais, criando dependências frágeis.

## Relacionadas
- [[Frontend]]
- [[Sass]]
- [[Componentes]]
- [[Tailwind]]
- [[Webpack]]
- [[Vite]]