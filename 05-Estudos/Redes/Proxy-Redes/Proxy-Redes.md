---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Proxy-Redes

#area/estudos #estudos/redes #conceito

**Resumo:** Servidor intermediário que atua entre cliente e destino, provendo cache, filtro de conteúdo, anonimato e controle de acesso — em duas formas principais: forward e reverse proxy.

## Conceitos-chave
- **Forward proxy:** representa os clientes perante a internet (filtro, cache, anonimato).
- **Reverse proxy:** representa os servidores perante os clientes (TLS, load balancing, proteção).
- **Cache:** reduz consumo de banda e latência para conteúdo repetido.
- **Filtragem:** bloqueia sites/categorias por política corporativa ou escolar.
- **Anonimato:** esconde o IP do cliente do destino (e, no reverse, o IP dos servidores).
- **Terminação TLS:** o reverse proxy cuida de certificados e descarrega a criptografia dos backends.

## Exemplos
```bash
# Usar forward proxy
export http_proxy=http://proxy.local:3128
curl -x http://proxy.local:3128 https://example.com
```

```nginx
# nginx como reverse proxy
location /api/ {
    proxy_pass http://backend:3000;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

## Boas práticas
- Usar reverse proxy para terminação TLS, load balancing e mitigação de ataques.
- Configurar caches com TTLs coerentes e limpar conteúdo atualizado.
- Registrar logs de acesso do proxy para auditoria e detecção de anomalias.
- Garantir que o proxy resolva o DNS do destino para não vazar o IP do cliente.

## Armadilhas comuns
- Proxy transparente inspecionando TLS sem certificado próprio gera erros de MITM.
- Confundir proxy com VPN: o proxy não criptografa o tráfego entre cliente e proxy por padrão.
- Vazamento de DNS: se o cliente resolve nomes direto, o anonimato do proxy falha.
- Forward e reverse proxy têm finalidades opostas — não usá-los de forma intercambiável.

## Relacionadas
- [[CDN]]
- [[Firewall]]
- [[HTTPS]]
- [[Latencia]]
- [[VPN]]