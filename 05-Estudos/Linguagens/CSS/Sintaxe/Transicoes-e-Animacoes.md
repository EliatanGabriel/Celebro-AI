---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Transições e Animações

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Transições suavizam mudanças de estado (como hover) e animações com `@keyframes` executam sequências complexas de estilos ao longo do tempo.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `transition-property` | Qual propriedade anima | `background-color` ou `all` |
| `transition-duration` | Duração da transição | `.3s` |
| `transition-timing-function` | Curva de aceleração | `ease`, `linear`, `cubic-bezier` |
| `transition-delay` | Atraso antes de iniciar | `.1s` |
| Atalho `transition` | Tudo junto, na ordem acima | `all .3s ease .1s` |
| `transform` | Move/escala/gira/inclina | `translateX(8px)` |
| `translate()` / `scale()` | Desloca / redimensiona | `scale(1.05)` |
| `rotate()` / `skew()` | Gira / inclina | `rotate(-4deg)` |
| `@keyframes nome` | Define os quadros da animação | ver exemplo abaixo |
| `animation-name/duration` | Liga e dura a animação | `pulse 2s infinite` |
| `iteration-count` | Repetições (`infinite`) | `3` |
| `direction` | Sentido da execução | `alternate` |
| `fill-mode` | Estado antes/depois da animação | `forwards` mantém o fim |
| `prefers-reduced-motion` | Respeita quem evita movimento | media query de acessibilidade |

## Exemplos

```css
/* Botão com hover suave */
.btn {
  transition: background-color 0.25s ease, transform 0.25s ease;
}
.btn:hover {
  background-color: hsl(220 90% 45%);
  transform: translateY(-2px);
}

/* Animação pulsante em loop */
@keyframes pulse {
  from { transform: scale(1); opacity: 1; }
  to   { transform: scale(1.08); opacity: 0.6; }
}
.badge-novo { animation: pulse 1.5s ease-in-out infinite alternate; }

@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

## Boas práticas

- Anime só `transform` e `opacity`: são acelerados por GPU.
- Prefira transições para feedback; keyframes para chamadas de atenção.
- Sempre ofereça o estado final via `fill-mode: forwards`.
- Inclua `prefers-reduced-motion` em qualquer projeto público.
- Use hover como gatilho combinado a `transition` no estado base.

## Armadilhas comuns

- Declarar `transition` só no `:hover` — a volta fica instantânea.
- Animar `height`/`width`/`top`: causa reflow e engasga.
- Esquecer que `transform` sobrescreve o transform anterior inteiro.
- `@keyframes` definido depois de usar — funciona, mas dificulta leitura.
- Loop infinito sem pausa (banner piscando) incomoda e viola WCAG.

## Relacionadas

- [[Estudos-CSS]]
- [[Flexbox]]
