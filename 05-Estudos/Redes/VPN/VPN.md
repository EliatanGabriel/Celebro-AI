---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# VPN

#area/estudos #estudos/redes #conceito

**Resumo:** Rede privada virtual (Virtual Private Network) que cria um túnel criptografado e autenticado sobre redes públicas, protegendo dados em trânsito e estendendo a rede corporativa.

## Conceitos-chave
- **Túnel:** encapsulamento do tráfego original dentro de um protocolo de transporte.
- **Criptografia:** confidencialidade dos dados em trânsito (ex.: AES).
- **Protocolos:** OpenVPN, WireGuard, IPsec/IKEv2 e VPNs baseadas em SSL/TLS.
- **Autenticação:** usuário/credenciais e certificados, com autenticação mútua possível.
- **Casos de uso:** acesso remoto, site-to-site e proteção em Wi-Fi público.
- **Limitação:** VPN protege o caminho; não é anonimato nem proteção completa do dispositivo.

## Exemplos
```ini
# WireGuard (resumo de configuração)
[Interface]
Address = 10.0.0.2/24
PrivateKey = <chave_privada_do_cliente>

[Peer]
PublicKey = <chave_publica_do_servidor>
Endpoint = vpn.empresa.com:51820
AllowedIPs = 0.0.0.0/0
```

## Boas práticas
- Usar protocolos auditados e atuais (WireGuard, OpenVPN, IPsec).
- Exigir autenticação forte (senha + MFA ou certificados).
- Manter clientes e servidores atualizados para fechar vulnerabilidades.
- Verificar ausência de vazamentos de DNS e de IPv6 fora do túnel.

## Armadilhas comuns
- Achar que VPN garante anonimato: provedor e destino podem registrar o tráfego.
- Vazamento de DNS/IP (IPv6) quando o túnel não captura todo o tráfego.
- Confiar em "VPN gratuita" que coleta dados ou injeta anúncios.
- Confundir VPN com proxy: o proxy não criptografa o tráfego entre o cliente e o destino.

## Relacionadas
- [[Criptografia]]
- [[Firewall]]
- [[TLS]]
- [[Proxy-Redes]]
- [[IP]]