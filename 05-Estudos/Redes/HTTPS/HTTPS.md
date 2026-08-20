---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# HTTPS

#area/estudos #estudos/redes #conceito

**Resumo:** Protocolo HTTP sobre TLS/SSL, que adiciona criptografia, autenticação do servidor e integridade às comunicações web.

## Conceitos-chave
- **TLS:** camada de segurança sob o HTTP; o HTTP transporta dados em texto puro.
- **Porta padrão:** 443 (HTTPS) vs 80 (HTTP).
- **Certificados:** emitidos por autoridades certificadoras (ACs) e validam a identidade do domínio.
- **Cadeia de confiança:** navegador valida o certificado até uma AC raiz confiável.
- **HSTS:** header que força conexões HTTPS e evita downgrade para HTTP.
- **SEO e privacidade:** HTTPS é fator de ranqueamento e protege dados na transmissão.

## Exemplos
```bash
# Ver handshake TLS, certificado e ciphers
curl -v https://example.com
openssl s_client -connect example.com:443 -servername example.com

# Header de segurança
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

```text
Fluxo HTTPS
Cliente -> [TCP handshake] -> [TLS handshake] -> [HTTP request criptografado]
```

## Boas práticas
- Renovar certificados automaticamente (ex.: Let's Encrypt via certbot).
- Configurar HSTS após garantir que todo o site responde HTTPS.
- Redirecionar HTTP → HTTPS com 301 e desabilitar HTTP se possível.
- Usar cipher suites fortes e desabilitar TLS antigo (1.0/1.1) e SSL.

## Armadilhas comuns
- Certificado expirado ou para outro domínio gera erro de confiança no navegador.
- Conteúdo misto (mixed content): recurso HTTP dentro de página HTTPS é bloqueado.
- Usar HTTPS apenas no front e deixar APIs internas sem TLS vaza dados.
- Achar que HTTPS impede todo tipo de ataque: TLS protege o transporte, não a aplicação.

## Relacionadas
- [[TLS]]
- [[Criptografia]]
- [[Handshake]]
- [[TCP]]
- [[Navegacao]]