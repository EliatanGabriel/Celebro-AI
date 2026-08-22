---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Links e Imagens

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Links conectam páginas, seções e contatos; imagens ilustram o conteúdo e precisam de alternativas textuais para acessibilidade e SEO.

## Referência rápida

| Tag/Sintaxe | O que faz | Exemplo |
|---|---|---|
| `<a href>` | Link para outro recurso | `<a href="/sobre">Sobre</a>` |
| `target="_blank"` | Abre em nova aba | `<a href="..." target="_blank">` |
| `rel="noopener"` | Segurança com `_blank` (evita tabnabbing) | `rel="noopener noreferrer"` |
| `href="#id"` | Âncora interna para elemento com id | `<a href="#contato">` |
| `mailto:` | Abrir cliente de e-mail | `<a href="mailto:a@b.com">` |
| `tel:` | Iniciar chamada telefônica | `<a href="tel:+5511999999999">` |
| `<img src alt>` | Imagem + texto alternativo obrigatório | `<img src="foto.jpg" alt="Praia ao amanhecer">` |
| `width` / `height` | Dimensões que evitam layout shift | `<img ... width="600" height="400">` |
| `loading="lazy"` | Carregamento adiado fora da tela | `<img ... loading="lazy">` |
| `<picture>` | Art direction / formatos modernos | ver exemplo abaixo |
| `<figure>` | Agrupa conteúdo autocontido | `<figure>...</figure>` |
| `<figcaption>` | Legenda da figura | `<figcaption>Fig. 1</figcaption>` |

## Exemplos

```html
<a href="https://exemplo.com" target="_blank" rel="noopener noreferrer">
  Site externo
</a>
<a href="#contato">Ir para contato</a>
<a href="mailto:oi@site.com">Enviar e-mail</a>

<figure>
  <picture>
    <source srcset="paisagem.webp" type="image/webp">
    <img src="paisagem.jpg" alt="Vale com montanhas ao entardecer"
         width="800" height="450" loading="lazy">
  </picture>
  <figcaption>Vale visto do mirante, outono de 2025</figcaption>
</figure>
```

## Boas práticas

- Todo `<img>` precisa de `alt`: descritivo se informativo, vazio (`alt=""`) se decorativo.
- Sempre declare `width`/`height` para reservar espaço e evitar "pulos" no layout.
- Use `rel="noopener noreferrer"` junto de `target="_blank"`.
- Prefira formatos modernos (WebP/AVIF) via `<picture>` ou `srcset`.
- Texto do link deve fazer sentido sozinho ("ver preço", não "clique aqui").

## Armadilhas comuns

- Usar imagem como botão sem `alt` — leitores de tela leem o caminho do arquivo.
- Esquecer `noopener`, permitindo que a página aberta manipule a sua.
- Caminho relativo errado (`/img/foto.jpg` quando o arquivo está em subpasta).
- `alt="imagem"` ou `alt="foto"` — descreva o conteúdo real.
- Colocar elementos de bloco dentro de `<a>` sem necessidade (embora seja válido em HTML5).

## Relacionadas

- [[Estudos-HTML]]
- [[Midia-e-Incorporacao]]
