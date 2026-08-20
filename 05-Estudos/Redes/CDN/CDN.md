---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# CDN

#area/estudos #estudos/redes #conceito

**Resumo:** Rede distribuída de servidores (edges) que entrega conteúdo a partir de pontos geograficamente próximos ao usuário, reduzindo latência, aumentando a disponibilidade e aliviando a carga do servidor de origem.

## Conceitos-chave
- **Edge / POps (Points of Presence):** servidores espalhados pelo mundo que respondem em nome da origem.
- **Cache:** cópias de conteúdo estático (imagens, CSS, JS, vídeo) armazenadas nas edges com TTL.
- **Roteamento de requisições:** via anycast ou DNS, o usuário é direcionado ao edge mais próximo/menos carregado.
- **Offload da origem:** diminui o tráfego e a carga de CPU no servidor principal.
- **Recursos de segurança:** mitigação de DDoS, WAF e terminação de TLS próximas ao usuário.
- **Suporte a HTTP/2 e HTTP/3 (QUIC), compressão e otimização de mídia.**

## Exemplos
```bash
# Invalidar (purgar) um objeto em cache após atualização (AWS CloudFront)
aws cloudfront create-invalidation --distribution-id DISTRIBUTION_ID \
  --paths "/assets/v1/app.js"

# Headers que controlam o cache
Cache-Control: public, max-age=86400
ETag: "abc123"
```

## Boas práticas
- Definir TTLs coerentes: longos para assets imutáveis, curtos para conteúdo mutável.
- Enviar headers de cache corretos (Cache-Control, ETag) para não servir conteúdo obsoleto.
- Purgar a CDN após deploys que alteram arquivos versionados.
- Usar CDN para assets estáticos, mídia e APIs de baixa variabilidade; não cachear dados pessoais.
- Configurar fallback para a origem quando o edge não tiver o objeto.

## Armadilhas comuns
- Cachear conteúdo dinâmico ou personalizado vaza dados de outros usuários.
- TTL muito longo após atualização: usuários continuam recebendo versão antiga.
- Não incluir o query string/versão no cache pode servir respostas erradas.
- Acreditar que CDN só serve para acelerar: também é camada de resiliência e segurança.

## Relacionadas
- [[CloudFront]]
- [[Latencia]]
- [[Largura-de-Banda]]
- [[Proxy-Redes]]
- [[Streaming]]