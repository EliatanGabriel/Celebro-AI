---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Mídia e Incorporação

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** HTML nativo permite reproduzir vídeo e áudio, incorporar páginas externas via iframe e desenhar gráficos com canvas e svg, tudo sem plugins.

## Referência rápida

| Tag/Sintaxe | O que faz | Exemplo |
|---|---|---|
| `<video controls>` | Player de vídeo com controles nativos | `<video src="a.mp4" controls>` |
| `autoplay muted` | Reprodução automática (exige mudo) | `<video autoplay muted loop>` |
| `poster` | Imagem exibida antes de dar play | `poster="capa.jpg"` |
| `<audio controls>` | Player de áudio | `<audio src="som.mp3" controls>` |
| `<iframe src title>` | Incorpora página externa (obrigatório `title`) | `<iframe src="..." title="Vídeo">` |
| `<canvas>` | Área desenhada por JavaScript (pixel a pixel) | `<canvas width="400" height="300">` |
| `<svg>` | Gráficos vetoriais inline, escaláveis | `<svg viewBox="0 0 24 24">` |
| `<source>` | Oferece múltiplos formatos ao player | ver exemplo abaixo |
| `<track>` | Legendas/capítulos para vídeo | `<track kind="subtitles" srclang="pt-BR">` |

## Exemplos

```html
<video controls autoplay muted loop poster="capa.jpg" width="640">
  <source src="promocao.webm" type="video/webm">
  <source src="promocao.mp4" type="video/mp4">
  <track src="legendas-pt.vtt" kind="subtitles" srclang="pt-BR" label="Português">
  Seu navegador não suporta vídeo HTML.
</video>

<iframe
  src="https://www.youtube.com/embed/dQw4w9WgXcQ"
  title="Apresentação do produto"
  allowfullscreen>
</iframe>

<canvas id="grafico" width="400" height="200"></canvas>
<svg viewBox="0 0 24 24" width="24"><circle cx="12" cy="12" r="10"/></svg>
```

## Boas práticas

- Nunca use `autoplay` sem `muted`: navegadores bloqueiam áudio automático.
- Sempre informe `title` no iframe — leitores de tela anunciam esse texto.
- Ofereça o mesmo vídeo em WebM + MP4 com `<source>` múltiplos.
- Prefira `<svg>` para ícones/logos (escala sem perder qualidade) e `<canvas>` para animações dinâmicas em JS.
- Forneça `<track>` de legendas; melhora acessibilidade e SEO.

## Armadilhas comuns

- Esquecer `title` no iframe (falha de acessibilidade).
- Usar URL de visualização do YouTube (`watch?v=`) em vez do embed.
- Definir tamanho do canvas só via CSS — isso distorce o desenho; ajuste os atributos `width`/`height`.
- Colocar conteúdo entre `<video>` e `</video>` sem intenção: ele só aparece se o formato falhar.
- Abrir sites sensíveis em iframe sem saber que muitos enviam `X-Frame-Options` e recusam.

## Relacionadas

- [[Estudos-HTML]]
- [[Links-e-Imagens]]
