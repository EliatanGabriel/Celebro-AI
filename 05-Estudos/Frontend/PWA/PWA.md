---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# PWA

#area/estudos #estudos/frontend #conceito

**Resumo:** Progressive Web App: aplicações web com capacidades de apps nativos — instaláveis, funcionais offline e com notificações push — via service workers e manifest.

## Conceitos-chave
- **Service worker:** script que roda em segundo plano, intercepta requisições (`fetch`) e controla cache e offline.
- **Web App Manifest:** arquivo JSON com nome, ícones, cores e exibição, habilitando a instalação no dispositivo.
- **Estratégias de cache:** `cache-first` (servir do cache, ideal para assets estáticos) e `network-first` (atualizar via rede com fallback offline, ideal para conteúdo).
- **Notificações push:** mensagens enviadas ao dispositivo mesmo com o app fechado, via Push API e notificações.
- **Instalável:** critérios como HTTPS, manifest válido e service worker com handler de fetch.
- **HTTPS obrigatório:** service workers e push exigem contexto seguro (exceto localhost).

## Exemplos

```json
// manifest.webmanifest
{
  "name": "Minha App",
  "short_name": "App",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#3182ce",
  "icons": [{ "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" }]
}
```

```js
// registro e estratégia cache-first para assets
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}

// sw.js
const CACHE = 'v1';
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then((cached) => {
      return (
        cached ||
        fetch(event.request).then((response) => {
          const copy = response.clone();
          caches.open(CACHE).then((cache) => cache.put(event.request, copy));
          return response;
        })
      );
    })
  );
});
```

## Boas práticas
- Servir sempre por HTTPS e registrar o service worker no escopo correto.
- Escolher a estratégia de cache por tipo de recurso (assets: cache-first; páginas: network-first).
- Versionar o cache (`caches.open('v1')`) e limpar versões antigas na ativação do SW.
- Fornecer um fallback offline (ex.: página "sem conexão") para requisições de navegação.
- Testar em Lighthouse (auditoria PWA) e no modo offline do DevTools.

## Armadilhas comuns
- Ficar preso a versões antigas de assets por usar `cache-first` com URLs sem hash de build.
- Aplicar `cache-first` em HTML dinâmico, servindo páginas desatualizadas.
- Não limpar caches antigos após atualizar o service worker (crescimento sem fim).
- Fazer `fetch` sem `catch`, deixando requisições quebrando quando offline.
- Esperar push funcionar sem manifest válido, permissão do usuário ou HTTPS.

## Relacionadas
- [[Frontend]]
- [[JavaScript]]
- [[Performance-Frontend]]