---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Firewall

#area/estudos #estudos/redes #conceito

**Resumo:** Sistema (hardware ou software) que filtra o tráfego de rede conforme regras e políticas, protegendo o perímetro, hosts e serviços.

## Conceitos-chave
- **Regras/ACL:** decisões baseadas em IP, porta, protocolo e interface.
- **Stateful vs stateless:** o firewall stateful acompanha o estado das conexões e permite apenas respostas de conexões estabelecidas.
- **NGFW (Next-Generation Firewall):** inspeção na camada de aplicação (IPS, malware, identidade).
- **Default-deny:** política que bloqueia tudo e libera apenas o necessário.
- **Zonas:** LAN, DMZ e WAN com políticas de tráfego diferentes entre si.
- **Logs e alertas:** registro de tentativas bloqueadas e aprovadas para auditoria.

## Exemplos
```bash
# nftables: política default drop, libera SSH e tráfego estabelecido
table inet filter {
  chain input {
    type filter hook input priority filter; policy drop;
    tcp dport 22 accept
    ct state established,related accept
  }
}
```

```text
Zonas típicas
LAN   -> WAN  : liberado (navegação)
WAN   -> LAN  : bloqueado (exceto regras específicas)
WAN   -> DMZ  : liberado apenas para serviços públicos
LAN   -> DMZ  : liberado quando necessário
```

## Boas práticas
- Aplicar o princípio do menor privilégio: liberar só o que é necessário.
- Revisar e auditar regras periodicamente; regras antigas acumulam risco.
- Testar mudanças em ambiente controlado antes de aplicar em produção.
- Monitorar logs e criar alertas para tentativas de acesso indevido.

## Armadilhas comuns
- Esquecer de cobrir IPv6: tráfego pode contornar regras que só tratam IPv4.
- Ordem das regras importa: a primeira que casa decide o destino do pacote.
- Regras duplicadas ou contraditórias tornam o comportamento imprevisível.
- Achar que firewall resolve tudo: sem endpoint security e atualizações, o perímetro é insuficiente.

## Relacionadas
- [[VPN]]
- [[Zero-Trust]]
- [[Portas]]
- [[NAT]]
- [[Proxy-Redes]]