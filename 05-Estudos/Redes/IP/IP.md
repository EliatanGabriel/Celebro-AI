---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# IP

#area/estudos #estudos/redes #conceito

**Resumo:** Protocolo da camada de rede (Internet Protocol) que endereça hosts e roteia pacotes entre redes distintas, sendo a base da internet em suas versões IPv4 e IPv6.

## Conceitos-chave
- **IPv4:** 32 bits, ~4,3 bilhões de endereços, representado em decimal pontuado (192.168.1.1).
- **IPv6:** 128 bits, notação hexadecimal (2001:db8::1), espaço praticamente ilimitado.
- **Endereços especiais:** 127.0.0.1 (loopback), 0.0.0.0 (qualquer/desconhecido), broadcast 255.255.255.255 e privados RFC1918.
- **Header IP:** campos de versão, TTL, protocolo, endereços origem/destino e checksum.
- **Fragmentação:** pacotes grandes são divididos conforme o MTU dos enlaces no caminho.
- **Best effort:** sem garantia de entrega; confiabilidade é responsabilidade da camada de transporte (TCP).

## Exemplos
```text
Header IPv4 (campos principais)
+--------+-------+-------+-------------+--------------+
| Versão | TTL   | Proto | Origem (32) | Destino (32) |
+--------+-------+-------+-------------+--------------+
Proto: 6=TCP, 17=UDP, 1=ICMP
```

```text
Faixas privadas RFC1918 (não roteáveis na internet)
10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
```

```bash
ip -4 addr show   # endereços IPv4 configurados
ip -6 addr show   # endereços IPv6
```

## Boas práticas
- Adotar IPv6 em novos projetos, com dual-stack quando necessário.
- Planejar o endereçamento com subnets antes de implantar a infraestrutura.
- Evitar IP estático manual desorganizado: usar DHCP ou IPAM.
- Documentar o plano de endereçamento para evitar conflitos.

## Armadilhas comuns
- Confundir IP privado com público: privado não é acessível diretamente pela internet.
- Esquecer a máscara: o mesmo IP pode pertencer a redes diferentes.
- Fragmentação excessiva degrada performance e pode ser explorada por ataques.
- IPv4 e IPv6 não conversam nativamente: exige tradução (NAT64) ou dual-stack.

## Relacionadas
- [[TCP]]
- [[Subnetting]]
- [[DNS]]
- [[TCP-IP]]
- [[NAT]]