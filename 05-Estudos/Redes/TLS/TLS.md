---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# TLS

#area/estudos #estudos/redes #conceito

**Resumo:** Protocolo de segurança (Transport Layer Security) que fornece confidencialidade, integridade e autenticação às comunicações, base do HTTPS, e-mail seguro e VPNs; sucessor do SSL.

## Conceitos-chave
- **Handshake:** negocia algoritmos, autentica o servidor via certificado e troca chaves de sessão.
- **Criptografia simétrica** (AES-GCM, ChaCha20) para os dados; **assimétrica** (ECDHE, RSA) para a troca de chaves.
- **Certificados X.509:** compõem uma cadeia de confiança até a autoridade certificadora (AC) raiz.
- **TLS 1.3:** handshake em 1 RTT (0-RTT com retomada), remove cifras fracas.
- **Perfect Forward Secrecy (PFS):** com ECDHE, comprometer a chave privada não expõe sessões passadas.
- **Integridade:** autenticação de cada mensagem impede adulteração em trânsito.

## Exemplos
```bash
# Inspecionar o handshake TLS e o certificado
openssl s_client -connect example.com:443 -tls1_3

# Verificar cadeia de certificados
openssl verify -CAfile ca.pem cert.pem
```

```text
TLS 1.3 (resumo do handshake)
Cliente  -> ClientHello (suites e chaves efêmeras)
Servidor -> ServerHello, certificado, Finished
Cliente  -> Finished
A partir daqui os dados são criptografados com chaves de sessão
```

## Boas práticas
- Usar TLS 1.3 como padrão e TLS 1.2 como mínimo compatível.
- Emitir certificados de ACs confiáveis e renovar automaticamente.
- Desabilitar SSL, TLS 1.0/1.1 e cipher suites fracas (RC4, CBC antigo).
- Proteger a chave privada: exposição compromete toda a confiança do serviço.

## Armadilhas comuns
- Confundir certificado (autenticação da identidade) com a criptografia dos dados.
- Ignorar o validação da cadeia: certificado sem a AC raiz correta falha no cliente.
- Renovar só na data: certificado expirado derruba o serviço.
- Achar que TLS resolve segurança de aplicação: protege o transporte, não o código.

## Relacionadas
- [[HTTPS]]
- [[Criptografia]]
- [[Handshake]]
- [[TCP]]
- [[VPN]]