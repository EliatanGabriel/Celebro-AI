---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Wi-Fi

#area/estudos #estudos/redes #conceito

**Resumo:** Tecnologia de rede sem fio baseada no padrão IEEE 802.11, que conecta dispositivos via rádio dentro de uma área de cobertura, permitindo mobilidade e facilidade de implantação.

## Conceitos-chave
- **Padrões:** 802.11n (Wi-Fi 4), 802.11ac (Wi-Fi 5), 802.11ax (Wi-Fi 6), 802.11be (Wi-Fi 7).
- **Bandas:** 2,4 GHz (maior alcance, mais interferência) e 5 GHz (mais rápida, menor alcance); Wi-Fi 6E/7 usam 6 GHz.
- **SSID:** nome da rede usado para identificação e seleção.
- **Segurança:** WPA2/WPA3 (nunca WEP ou WPA1, considerados quebrados).
- **Access Points e roaming:** pontos de acesso que permitem transição entre células.
- **Meio compartilhado:** o espectro de rádio é compartilhado; interferência e congestionamento afetam a taxa.

## Exemplos
```text
Família 802.11 (nomenclatura Wi-Fi Alliance)
Wi-Fi 4  802.11n   2,4/5 GHz
Wi-Fi 5  802.11ac  5 GHz
Wi-Fi 6  802.11ax  2,4/5 GHz, OFDMA, maior eficiência
Wi-Fi 7  802.11be  2,4/5/6 GHz, maior throughput
```

```bash
# Listar redes Wi-Fi e intensidade do sinal (Linux)
nmcli dev wifi list
iw dev wlan0 scan | grep -E "SSID|signal"
```

## Boas práticas
- Usar WPA3 (ou WPA2-Enterprise em corporativo); nunca WEP/WPA1.
- Escolher canais 1, 6 ou 11 na banda de 2,4 GHz para reduzir interferência.
- Planejar a cobertura com APs suficientes, evitando sobreposição excessiva.
- Manter firmware dos APs e drivers atualizados.

## Armadilhas comuns
- Confundir Wi-Fi com internet: o Wi-Fi é só o acesso; a conexão vem do provedor.
- SSID oculto não é segurança: qualquer scanner o detecta.
- Interferência de vizinhos, micro-ondas e paredes degradam a taxa real.
- Range extender reduz pela metade a banda efetiva por repetir o sinal no mesmo canal.

## Relacionadas
- [[DHCP]]
- [[Dispositivos]]
- [[Ethernet]]
- [[IoT]]
- [[5G]]