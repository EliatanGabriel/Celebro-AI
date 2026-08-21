---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Proxy

#area/estudos #estudos/backend #conceito

**Resumo:** Servidor intermediário entre cliente e destino que encaminha, filtra e modifica o tráfego; no backend o papel mais comum é o reverse proxy.

## Conceitos-chave
- **Forward proxy:** atua em nome do cliente (ex.: acesso corporativo, anonimato, filtros).
- **Reverse proxy:** atua em nome do servidor (ex.: Nginx); recebe o tráfego público e distribui para os serviços internos.
- **Funções:** balanceamento de carga, SSL termination, cache, compressão, roteamento por host/path e proteção.
- **SSL termination:** o proxy encerra o TLS e repassa o tráfego em HTTP para a rede interna.
- **Isolamento:** oculta os servidores de aplicação e suas portas da internet.
- **Diferenças-chave:** o load balancer se especializa em distribuir tráfego; um reverse proxy faz isso e muito mais (cache, segurança, roteamento).

## Exemplos
```nginx
# Nginx como reverse proxy
server {
  listen 443 ssl;
  server_name app.exemplo.com;

  ssl_certificate /etc/ssl/cert.pem;
  ssl_certificate_key /etc/ssl/key.pem;

  location /api/ {
    proxy_pass http://backend_interno:3000;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $remote_addr;
  }

  location / {
    proxy_pass http://frontend_interno:8080;
  }
}
```

```bash
# Docker: proxy na frente do app
docker run -p 80:80 -v ./nginx.conf:/etc/nginx/nginx.conf nginx
```

## Boas práticas
- Terminar TLS no proxy e encaminhar o tráfego interno em rede privada.
- Repassar headers `X-Forwarded-*` para o app saber o IP/cliente real.
- Configurar timeouts e limites de body para proteção contra abuso.
- Manter o proxy redundante (HA) para não virar ponto único de falha.
- Logar e monitorar o tráfego que passa pelo proxy.

## Armadilhas comuns
- Usar o proxy como o próprio servidor de aplicação (confundir papéis).
- Não repassar `X-Forwarded-For`, quebrando logs e rate limiting por IP.
- Esquecer que o app deve confiar apenas em proxies controlados ao ler esses headers.
- Cachear respostas dinâmicas/personalizadas no proxy sem cabeçalhos adequados.
- Subdimensionar o proxy e criar um gargalo de rede para todos os serviços.

## Relacionadas
- [[Load-Balancer]]
- [[Nginx]]
- [[Caching]]
- [[Kubernetes]]
- [[HTTPS]]