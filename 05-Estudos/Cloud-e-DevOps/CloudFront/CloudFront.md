---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# CloudFront

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** CDN (Content Delivery Network) da AWS que distribui conteúdo por edge locations ao redor do mundo, reduzindo latência, custo e carga na origem.

## Conceitos-chave
- **Edge locations:** pontos de presença geograficamente distribuídos que cacheiam e servem conteúdo próximo ao usuário.
- **Distribuição (distribution):** unidade de configuração que associa um domínio a uma origem (S3, EC2, ALB, API Gateway).
- **Origem:** servidor de onde o CloudFront busca o conteúdo quando não há cache (cache miss).
- **Cache e TTL:** objetos ficam em cache por um TTL controlado por headers (Cache-Control) ou defaults.
- **Comportamentos (behaviors):** regras por path que definem origem, cache e políticas de cada rota.
- **TLS/SSL:** certificados gerenciados via ACM, com HTTPS de ponta a ponta e SNI.
- **Integração Route 53:** aponta domínio (ex.: cdn.exemplo.com) para a distribuição.

## Exemplos

Invalidar cache de uma distribuição:

```bash
aws cloudfront create-invalidation \
  --distribution-id E1234567890ABCD \
  --paths "/index.html" "/assets/*"
```

Criar uma distribuição apontando para um bucket S3:

```bash
aws cloudfront create-distribution \
  --origin-domain-name meu-bucket.s3.amazonaws.com \
  --default-root-object index.html \
  --default-cache-behavior '{"TargetOriginId":"S3-meu-bucket","ViewerProtocolPolicy":"redirect-to-https","MinTTL":0}'
```

## Boas práticas
- Configurar `Cache-Control` adequado no bucket/origem para controlar o TTL por objeto.
- Usar Origin Access Control (OAC) para impedir acesso direto ao S3 e forçar o tráfego pela CDN.
- Habilitar HTTPS com certificado ACM e forçar redirecionamento.
- Comprimir conteúdo (gzip/brotli) e usar HTTP/2 para reduzir latência.
- Criar comportamento separado para assets estáticos (TTL longo) e HTML (TTL curto).

## Armadilhas comuns
- Cache de conteúdo dinâmico com TTL longo, servindo dados obsoletos.
- Deixar o bucket público, ignorando o OAC e perdendo o controle de acesso.
- Não planejar invalidações de cache em deploys (custo e inconsistência).
- Confundir CloudFront com WAF: são serviços diferentes (a integração WAF+CloudFront é comum, mas não a mesma coisa).
- Não configurar fallback de erro (custom error responses) para origin down.

## Relacionadas
- [[AWS]]
- [[S3]]
- [[CDN]]