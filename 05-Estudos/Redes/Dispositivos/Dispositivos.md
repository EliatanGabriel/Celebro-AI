---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Dispositivos

#area/estudos #estudos/redes #conceito

**Resumo:** Equipamentos que compõem e se conectam à rede: hosts (clientes e servidores) e infraestrutura de interconexão (switches, roteadores, access points, firewalls).

## Conceitos-chave
- **Hosts/endpoints:** computadores, celulares, impressoras e IoT — origem e destino do tráfego.
- **Switch (L2):** encaminha frames dentro da LAN com base no endereço MAC.
- **Roteador (L3):** encaminha pacotes entre redes usando IP e tabelas de rota.
- **Access Point (AP):** converte o meio cabeado em sem fio (Wi-Fi).
- **Gateway:** porta de saída padrão da rede local para outras redes.
- **Firewall:** filtra e inspeciona tráfego entre zonas (perímetro e interno).

## Exemplos
```text
| Dispositivo  | Camada | Função principal             |
| Hub          | L1     | Replica sinais (obsoleto)    |
| Switch       | L2     | Encaminha frames por MAC     |
| Roteador     | L3     | Encaminha pacotes por IP     |
| Access Point | L1/L2  | Conectividade Wi-Fi          |
| Firewall     | L3-L7  | Filtro e inspeção de tráfego |
```

## Boas práticas
- Separar plano de dados (encaminhamento) do plano de controle (decisões).
- Segmentar a rede em VLANs para isolar tipos de dispositivos (IoT, staff, DMZ).
- Manter firmware e sistemas atualizados em todos os equipamentos.
- Documentar topologia, endereçamento e responsáveis por cada dispositivo.

## Armadilhas comuns
- Confundir switch com roteador: um é L2 (MAC), o outro L3 (IP).
- Achar que o Access Point faz roteamento: ele apenas conecta o meio sem fio.
- Tratar MAC address como credencial de segurança: endereços podem ser clonados.
- Ignorar dispositivos IoT com credenciais padrão, que viram alvo fácil de botnets.

## Relacionadas
- [[Wi-Fi]]
- [[Ethernet]]
- [[IoT]]
- [[Switching]]
- [[Roteamento]]