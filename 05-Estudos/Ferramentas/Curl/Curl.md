---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Curl

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Ferramenta de linha de comando (e biblioteca libcurl) para transferir dados via protocolos como HTTP/HTTPS, FTP e SMTP; essencial para testar APIs, baixar arquivos e automatizar requisições.

## Conceitos-chave
- **Métodos HTTP**: `-X` define o método (GET, POST, PUT, DELETE, PATCH), embora curl infira POST a partir de `-d`.
- **Headers**: `-H` adiciona headers personalizados (ex.: `Authorization`, `Content-Type`).
- **Dados**: `-d`/`--data` envia corpo como `application/x-www-form-urlencoded`; `--data-raw`, `--json` e `-F` (multipart) cobrem outros formatos.
- **Saída**: `-o arquivo` grava em disco, `-O` mantém o nome remoto, `-s` silencia progresso e `-i` inclui os headers da resposta.
- **Certificados**: `-k`/`--insecure` ignora validação TLS (usar apenas em testes); `--cacert` aponta para CA customizada.
- **Verbose**: `-v` mostra a troca completa (headers, TLS, redirecionamentos); `--trace` grava tudo em arquivo.

## Exemplos
Testar uma API REST:

```bash
# GET com header de autenticação
curl -H "Authorization: Bearer TOKEN" https://api.exemplo.com/v1/usuarios

# POST JSON
curl -X POST https://api.exemplo.com/v1/usuarios \
  -H "Content-Type: application/json" \
  -d '{"nome": "Ana", "email": "ana@exemplo.com"}'

# upload de arquivo (multipart)
curl -F "arquivo=@./foto.png" https://api.exemplo.com/v1/upload
```

Baixar e acompanhar progresso:

```bash
curl -L -o instalar.sh https://exemplo.com/instalar.sh
```

Debug de uma requisição:

```bash
curl -sv https://api.exemplo.com 2>&1 | head -50
```

## Boas práticas
- Prefira `--json '{"chave": "valor"}'` para JSON e deixe o curl ajustar Content-Type e escape.
- Use `-f`/`--fail` em scripts para retornar erro quando o servidor responder 4xx/5xx.
- Trate redirecionamentos com `-L` (seguir) ou inspecione o Location antes de decidir.
- Sempre valide o certificado TLS em produção; `-k` só em ambientes controlados.
- Combine com `jq` para processar respostas JSON em pipelines de automação.

## Armadilhas comuns
- Confundir `-d` (form-urlencoded) com envio de JSON: falta de `Content-Type: application/json` gera respostas inesperadas.
- `-X POST` junto com `-I` (HEAD) ou com outros métodos pode sobrescrever o comportamento esperado.
- Esquecer `-L`: downloads de arquivos que redirecionam (ex.: GitHub release) baixam a página HTML.
- Achar que `-s` suprime apenas o progresso: ele também suprime erros — combine com `-S` para ver erros.
- Variáveis de ambiente (proxy) podem interferir; use `--noproxy` ou desative com `-x ""` quando necessário.

## Relacionadas
- [[Terminal]]
- [[Ferramentas-CLI]]
- [[Wget]]
- [[Postman]]