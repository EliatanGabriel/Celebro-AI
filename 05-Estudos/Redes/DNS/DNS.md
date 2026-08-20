---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# DNS

#area/estudos #estudos/redes #conceito

**Resumo:** Sistema hierárquico e distribuído que traduz nomes de domínio legíveis em endereços IP, permitindo navegar sem decorar números.

## Conceitos-chave
- **Hierarquia:** raiz → TLD (.com, .br) → domínio autoritativo → subdomínios.
- **Registros (records):** A/AAAA (IPv4/IPv6), CNAME (alias), MX (e-mail), NS (autoridade), TXT (SPF/DKIM), PTR (reverso).
- **Resolução:** o resolver recursivo consulta raiz, TLD e servidor autoritativo até obter a resposta.
- **Cache e TTL:** respostas ficam cacheadas conforme o TTL para reduzir latência e carga.
- **Privacidade:** DNS sobre HTTPS (DoH) e DNS sobre TLS (DoT) criptografam as consultas.
- **DNSSEC:** assina as respostas para impedir envenenamento de cache.

## Exemplos
```bash
dig example.com A
nslookup -type=MX gmail.com
dig -x 8.8.8.8            # consulta reversa (PTR)

# Registro TXT (SPF) usado por remetentes de e-mail
v=spf1 include:_spf.google.com ~all
```

```text
Fluxo de resolução de https://example.com
1. Resolver recursivo pergunta à raiz
2. Raiz indica o servidor de .com
3. .com indica o autoritativo de example.com
4. Autoritativo responde o A: 93.184.216.34
5. Resolver devolve ao cliente e faz cache (TTL)
```

## Boas práticas
- Usar DNSSEC para impedir envenenamento de cache.
- Antes de migrar, reduzir o TTL dos registros para acelerar a propagação.
- Manter nameservers redundantes e monitorar a resolução dos domínios.
- Configurar registros PTR para servidores de e-mail (validação reversa).

## Armadilhas comuns
- Achar que a propagação DNS é instantânea: ela depende dos TTLs de cada cache.
- Confundir A com CNAME: CNAME aponta para outro nome, não para um IP.
- Esquecer registros PTR quebra autenticação de e-mail (rDNS).
- Cache envenenado (spoofing) sem DNSSEC redireciona usuários para sites falsos.

## Relacionadas
- [[IP]]
- [[Navegacao]]
- [[Protocolos]]
- [[Portas]]