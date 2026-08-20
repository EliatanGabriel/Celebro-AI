---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-16"
updated: "2026-08-20"
---

# Navegação

#area/estudos #estudos/redes #conceito

**Resumo:** Processo de carregar uma página web: o navegador resolve o domínio via DNS, abre conexão TCP/TLS e requisita os recursos via HTTP até renderizar a página.

## Conceitos-chave
- **URL:** estrutura esquema://host/caminho — ex.: https://example.com/pagina.
- **Fluxo completo:** DNS → TCP handshake → TLS handshake → HTTP request → resposta → render.
- **Cache do navegador:** reduz requisições repetidas usando TTL e validação (ETag).
- **Versões HTTP:** HTTP/1.1 (conexões paralelas), HTTP/2 (multiplexação), HTTP/3 (QUIC/UDP).
- **Recursos bloqueantes:** CSS/JS bloqueiam a renderização; carregamento async melhora a experiência.

## Exemplos
```text
1. Digita https://example.com
2. DNS resolve example.com -> 93.184.216.34
3. TCP handshake (SYN/SYN-ACK/ACK)
4. TLS handshake (1 RTT no TLS 1.3)
5. GET / HTTP/1.1  ->  200 OK (HTML)
6. Navegador baixa CSS, JS e imagens e renderiza
```

```bash
# Medir as fases do carregamento
curl -w "DNS: %{time_namelookup}s\nTCP: %{time_connect}s\n\
TLS: %{time_appconnect}s\nTotal: %{time_total}s\n" \
  -o /dev/null -s https://example.com
```

## Boas práticas
- Usar HTTPS com HSTS e evitar redirects extras (cada redirect adiciona RTT).
- Minificar e versionar assets; usar CDN e HTTP/2+ para reduzir latência percebida.
- Testar em dispositivos e conexões reais, não apenas em rede local.
- Monitorar métricas como LCP e FCP (Core Web Vitals).

## Armadilhas comuns
- Medir apenas o tempo de "load" sem separar DNS/TCP/TLS/HTTP.
- Tratar o DNS como "instantâneo": resolução lenta atrasa toda a navegação.
- Cache indevido de conteúdo dinâmico serve dados obsoletos ou errados.
- Ignorar o custo de múltiplos handshakes TLS em páginas com muitos domínios.

## Relacionadas
- [[DNS]]
- [[HTTPS]]
- [[TCP]]
- [[HTTP]]