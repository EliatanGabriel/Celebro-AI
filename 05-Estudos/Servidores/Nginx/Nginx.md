---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Nginx

#area/estudos #estudos/servidores #conceito #servidor #web #proxy

**Resumo:** Servidor web e proxy reverso de alto desempenho, com arquitetura assíncrona e baixo consumo de memória.

## Conceitos-chave
- **Arquitetura event-driven:** um pequeno número de processos trata milhares de conexões concorrentes com pouco overhead.
- **Proxy reverso:** recebe requisições e as repassa a aplicações de backend (Node, Django, etc.).
- **Load balancing:** distribui o tráfego entre vários servidores de aplicação.
- **SSL/TLS:** terminação HTTPS com gerenciamento de certificados e suporte a HTTP/2.
- **Configuração:** blocos `http`, `server` e `location` definem o comportamento em níveis distintos.
- **Estáticos:** eficiente para servir arquivos estáticos, cache e compressão gzip.

## Exemplos
```nginx
server {
    listen 80;
    server_name meu-dominio.com.br;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /var/www/meu-site/static/;
        expires 30d;
    }
}
```

```bash
sudo nginx -t              # valida a configuração
sudo systemctl reload nginx
```

## Boas práticas
- Usar `nginx -t` antes de recarregar para não derrubar o serviço com erro de sintaxe.
- Servir estáticos direto pelo Nginx e delegar conteúdo dinâmico ao backend.
- Aplicar limites de requisição e tempo para proteção contra abusos.

## Armadilhas comuns
- Esquecer `proxy_set_header Host`, quebrando aplicações que dependem do domínio.
- Confundir os blocos `server` e `location`, aplicando regras no nível errado.
- Fazer offload de TLS e repassar em HTTP ao backend sem isolar a rede interna.
- Não recarregar após mudanças de configuração, mantendo versões antigas em memória.

## Relacionadas
- [[VPS]]
- [[Apache]]
- [[Proxy-Redes]]
- [[CDN]]
- [[HTTPS]]