---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Subnetting

#area/estudos #estudos/redes #conceito

**Resumo:** Técnica de dividir um bloco de endereços IP em sub-redes menores usando máscara/CIDR, otimizando o endereçamento e permitindo segmentação lógica da rede.

## Conceitos-chave
- **Máscara de rede:** indica quantos bits são rede vs host (255.255.255.0 = /24).
- **CIDR:** notação compacta — 192.168.1.0/24.
- **Endereços reservados:** o primeiro (network) e o último (broadcast) de cada subnet não são utilizáveis.
- **Cálculo de hosts:** 2^(32-máscara) - 2.
- **VLSM:** máscaras variáveis conforme a necessidade de cada subnet.
- **Fator de 2:** cada bit a mais na máscara divide o bloco pela metade.

## Exemplos
```text
192.168.1.0/24 -> 256 endereços, 254 utilizáveis
/26 -> 64 endereços, 62 utilizáveis

Dividindo 192.168.1.0/24 em 4 subnets /26
192.168.1.0/26     (0-63)
192.168.1.64/26    (64-127)
192.168.1.128/26   (128-191)
192.168.1.192/26   (192-255)
```

```bash
# Calcular rede/broadcast a partir de um IP
ipcalc 192.168.1.100/26
```

## Boas práticas
- Planejar crescimento: não subdividir demais sem folga de endereços.
- Usar /64 fixo para IPv6, que elimina a preocupação com escassez.
- Separar subnets por função (gestão, servidores, IoT, Wi-Fi) para isolar tráfego.
- Documentar o plano de subnets e as VLANs associadas.

## Armadilhas comuns
- Esquecer os -2 (network e broadcast) ao calcular hosts disponíveis.
- Erros de máscara causam overlap de subnets e roteamento ambíguo.
- Confundir subnetting (L3) com VLAN (L2): segmentação IP ≠ segmentação de broadcast.
- Usar máscara errada no DHCP e "perder" hosts que ficam fora do escopo.

## Relacionadas
- [[IP]]
- [[VPC]]
- [[NAT]]
- [[DHCP]]
- [[Roteamento]]