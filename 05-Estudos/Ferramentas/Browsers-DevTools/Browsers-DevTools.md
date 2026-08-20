---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Browsers-DevTools

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Conjunto de ferramentas de desenvolvimento embutidas nos navegadores (Chrome DevTools, Firefox DevTools) para inspecionar, depurar e otimizar aplicações web em tempo real.

## Conceitos-chave
- **Elements/Inspetor**: inspeciona e edita o DOM e o CSS ao vivo, permitindo testar alterações sem recarregar a página.
- **Console**: executa JavaScript, exibe logs (`console.log`, `console.error`) e inspeciona objetos e erros de runtime.
- **Network**: captura todas as requisições HTTP/HTTPS, com status, tamanho, tempo de resposta e headers; essencial para diagnóstico de APIs e performance.
- **Sources/Debugger**: permite breakpoints, step-through, watch expressions e análise de stack traces do JavaScript.
- **Performance**: grava perfis de CPU/memória (profiling) e árvores de chamadas para identificar gargalos de renderização e execução.
- **Application/Storage**: inspeciona localStorage, sessionStorage, cookies, IndexedDB, service workers e cache.
- **Lighthouse**: auditoria automatizada de performance, acessibilidade, SEO e boas práticas (disponível no Chrome).

## Exemplos
Inspecionar a resposta de uma requisição a partir do painel Network:

```js
// No Console, buscar elementos e interagir programaticamente
document.querySelector('.titulo').innerText
```

Gravar um profile de performance e ler o resultado:

```js
performance.measure('init'); // usado com user timing no painel Performance
```

Testar layout responsivo simulando dispositivos:

```bash
# Atalhos no Chrome DevTools (F12 para abrir)
Ctrl+Shift+C   # inspecionar elemento sob o cursor
Ctrl+Shift+P   # command palette (ex.: "Device Toolbar")
```

## Boas práticas
- Use o painel **Network** com a opção "Disable cache" para simular o primeiro carregamento de um visitante.
- Preserve os logs no Console com "Preserve log" ao navegar entre páginas.
- Combine **Performance** com Lighthouse para ter tanto dados granulares quanto uma pontuação automatizada.
- Aproveite o "Copy as fetch" ou "Copy as cURL" no Network para reproduzir requisições em testes.
- Teste acessibilidade com o painel de "Rendering > Emulate CSS media" e o Lighthouse.

## Armadilhas comuns
- Editar CSS no Elements não persiste após o refresh; use "Overrides" ou o painel Sources para persistir.
- Esquecer de desativar o cache no Network pode gerar tempos de carregamento enganosos em debug.
- Confundir o escopo: código no Console roda no contexto global da página e não enxerga variáveis de closures de módulos.
- Profiling em páginas com muitos Web Workers exige cuidado para não atribuir tempo errado a threads.
- Erros de CORS aparecem no Console mas podem ter origem no backend; verifique a resposta real no Network.

## Relacionadas
- [[Chrome]]
- [[Firefox]]