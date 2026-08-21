---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# IoT

#area/estudos #estudos/redes #conceito

**Resumo:** Internet das Coisas — objetos físicos com sensores e atuadores conectados à rede que coletam, transmitem e executam dados, muitas vezes com recursos computacionais limitados.

## Conceitos-chave
- **Sensores/atuadores:** capturam grandezas (temperatura, movimento, umidade) e agem no ambiente.
- **Conectividade:** Wi-Fi, Bluetooth/BLE, Zigbee, LoRaWAN, NB-IoT e 5G.
- **Protocolos leves:** MQTT e CoAP, desenhados para baixo overhead em dispositivos restritos.
- **Edge computing:** processamento próximo ao dispositivo reduz latência e tráfego para a nuvem.
- **Segurança:** credenciais padrão e firmware desatualizado são as maiores vulnerabilidades.

## Exemplos
```bash
# MQTT: publicar e assinar tópicos (broker local)
mosquitto_pub -h broker.local -t casa/sala/temperatura -m "23.5"
mosquitto_sub -h broker.local -t casa/#   # assina todos os tópicos de "casa"
```

```text
Padrão típico
Sensor -> Gateway/MQTT broker -> Processamento (edge/cloud) -> Atuador
```

## Boas práticas
- Trocar credenciais padrão e desativar serviços não utilizados.
- Segmentar dispositivos IoT em VLAN ou rede própria, isolada dos dados corporativos.
- Atualizar firmware regularmente e monitorar o ciclo de vida do dispositivo.
- Usar TLS/MQTT sobre TLS para transporte e autenticar dispositivos.

## Armadilhas comuns
- Dispositivos com senhas padrão alimentam botnets (ex.: Mirai).
- Dados transmitidos em claro podem ser capturados no Wi-Fi.
- Confundir protocolo de aplicação com transporte: MQTT roda sobre TCP; CoAP sobre UDP.
- Achar que "só tem sensor" é inofensivo: sensores também podem ser vetor de ataque.

## Relacionadas
- [[5G]]
- [[Wi-Fi]]
- [[Dispositivos]]
- [[Firewall]]
- [[Protocolos]]