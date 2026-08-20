---
type: concept
area: faculdade
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Internet das Coisas (IoT)

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Internet das Coisas: o que é, arquitetura, dispositivos, comunicação, protocolos e aplicações do IoT.

## 1. O que é IoT

**IoT** (*Internet of Things*) é a interconexão de objetos físicos ("coisas") à internet, permitindo que coletem dados, se comuniquem e sejam controlados remotamente.

```
COISA (sensor/atuador) → REDE → NUVEM → APLICAÇÃO → USUÁRIO
```

## 2. Características dos dispositivos IoT

- **Sensoriamento** — capturam dados do ambiente.
- **Conectividade** — enviam/recebem dados pela rede.
- **Processamento** — processam dados localmente (edge) ou na nuvem.
- **Atuação** — executam ações (ligar, mover, alertar).
- **Baixo consumo** — muitos funcionam com bateria.

## 3. Arquitetura em camadas

```
CAMADA DE APLICAÇÃO       → dashboard, apps, análise
        ↓
CAMADA DE PROCESSAMENTO   → nuvem, edge computing
        ↓
CAMADA DE REDE            → Wi-Fi, LoRa, 4G/5G, MQTT
        ↓
CAMADA DE PERCEPÇÃO       → sensores e atuadores
```

## 4. Exemplos de "coisas"

- Lâmpadas e tomadas inteligentes.
- Sensores de temperatura, umidade e presença.
- Rastreadores GPS.
- Máquinas industriais conectadas (IIoT).
- Wearables (relógios, monitores de saúde).
- Smart cities (iluminação pública, estacionamento).

## 5. Comunicação e protocolos

**Transporte físico:**

- **Wi-Fi** — alcance médio, maior consumo.
- **Bluetooth/BLE** — curto alcance, baixo consumo.
- **LoRa/LoRaWAN** — longo alcance, baixa taxa de dados.
- **Zigbee / Z-Wave** — automação residencial.
- **NB-IoT / 4G / 5G** — cobertura celular.

**Aplicação:**

- **MQTT** — protocolo leve de mensagens (pub/sub), padrão em IoT.
- **HTTP/REST** — APIs web.
- **CoAP** — para dispositivos restritos.

## 6. MQTT — como funciona

Baseado em **publicação/assinatura**:

```
SENSOR (publisher) → BROKER → APLICATIVO (subscriber)
```

- **Broker** — intermediário (Mosquitto).
- **Tópicos** — canais nomeados (ex.: `casa/sala/temperatura`).
- **QoS** — níveis de garantia de entrega (0, 1, 2).

```bash
mosquitto_pub -h broker -t casa/sala/temp -m "25.3"
mosquitto_sub -h broker -t 'casa/#'   # # = todos os tópicos abaixo
```

## 7. Edge × Cloud

- **Edge computing** — processa perto do dispositivo (menos latência, menos dados na nuvem).
- **Cloud computing** — processa em servidores remotos (mais poder de cálculo).

Muitas soluções IoT combinam: sensores fazem a leitura, o edge faz o filtro e a nuvem faz a análise e o histórico.

## 8. Raspberry Pi como hub IoT

O Raspberry Pi pode atuar como:

- **Gateway** — coleta dados de vários sensores e envia à nuvem.
- **Broker MQTT** — roda Mosquitto localmente.
- **Servidor de aplicação** — dashboard local (Node-RED, Grafana).
- **Edge node** — processa dados antes de enviar.

## 9. Aplicações

- **Casa inteligente** — automação e segurança.
- **Agricultura** — monitoramento de solo e clima.
- **Saúde** — monitoramento remoto de pacientes.
- **Indústria 4.0** — manutenção preditiva.
- **Logística** — rastreamento de cargas.
- **Cidades inteligentes** — gestão de tráfego e energia.

## 10. Desafios do IoT

- **Segurança** — muitos dispositivos vulneráveis.
- **Privacidade** — coleta massiva de dados.
- **Interoperabilidade** — muitos padrões.
- **Energia** — baterias e consumo.
- **Escala** — bilhões de dispositivos e dados.

## Tópicos
- 

## Relacionadas

- [[Raspberry-Pi-e-IoT]]
- [[Fundamentos de Raspberry Pi]]
- [[Faculdade]]