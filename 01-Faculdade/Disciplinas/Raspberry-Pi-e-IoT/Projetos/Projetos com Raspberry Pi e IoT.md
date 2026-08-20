---
type: concept
area: faculdade
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Projetos com Raspberry Pi e IoT

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Projetos práticos com Raspberry Pi e IoT: monitoramento de temperatura, servidor web, automação residencial e publicação de dados com MQTT.

## 1. Metodologia de projeto

1. **Definir o objetivo** — o que medir/controlar?
2. **Escolher sensores e atuadores**.
3. **Montar o circuito** na protoboard.
4. **Desenvolver o código** em Python.
5. **Conectar à rede** (Wi-Fi, MQTT, web).
6. **Testar e iterar**.

## 2. Projeto: monitoramento de temperatura com sensor digital

Usando um sensor DHT22 (temperatura e umidade) com GPIO Zero.

```python
from gpiozero import DHT22
from time import sleep

sensor = DHT22(17)

while True:
    print(f"Temperatura: {sensor.temperature} °C")
    print(f"Umidade: {sensor.humidity} %")
    sleep(5)
```

## 3. Projeto: publicar dados com MQTT (Paho)

```python
import paho.mqtt.client as mqtt
from gpiozero import DHT22
from time import sleep

broker = "192.168.1.10"      # IP do broker Mosquitto
client = mqtt.Client("pi-temp")
client.connect(broker)

sensor = DHT22(17)

while True:
    msg = f"{sensor.temperature:.1f}"
    client.publish("casa/sala/temperatura", msg)
    sleep(10)
```

No computador, assine para ver os dados:

```bash
mosquitto_sub -h 192.168.1.10 -t 'casa/#'
```

## 4. Projeto: servidor web com Flask

Cria uma página que mostra a temperatura ao acessar pelo navegador.

```python
from flask import Flask, jsonify
from gpiozero import DHT22

app = Flask(__name__)
sensor = DHT22(17)

@app.route("/")
def index():
    return {"temperatura": sensor.temperature,
            "umidade": sensor.humidity}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

Acesso: `http://IP-DO-PI:5000`.

## 5. Projeto: automação residencial (Node-RED + Mosquitto)

Fluxo típico:

```
SENSOR → MQTT (broker) → Node-RED → atuação/notificação
```

- **Mosquitto** — broker MQTT local.
- **Node-RED** — fluxos visuais para tratar mensagens.
- **Home Assistant** — automação completa.

Instalação:

```bash
sudo apt install mosquitto mosquitto-clients
sudo apt install node-red
```

## 6. Projeto: câmera de vigilância

```python
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (640, 480)

camera.start_preview()
sleep(2)
camera.capture("/home/pi/foto.jpg")
camera.stop_preview()
```

Com detecção de movimento (OpenCV), pode capturar fotos quando há presença.

## 7. Projeto: ligar/desligar LED remotamente via MQTT

```python
import paho.mqtt.client as mqtt
from gpiozero import LED

led = LED(17)

def on_message(client, userdata, msg):
    if msg.payload.decode() == "on":
        led.on()
    elif msg.payload.decode() == "off":
        led.off()

client = mqtt.Client("pi-led")
client.on_message = on_message
client.connect("192.168.1.10")
client.subscribe("casa/luz")
client.loop_forever()
```

Controle pelo terminal:

```bash
mosquitto_pub -h 192.168.1.10 -t casa/luz -m on
```

## 8. Boas práticas em projetos IoT

- **Segurança:** troque senhas padrão, use TLS quando possível.
- **Confirme entregas:** use QoS 1+ no MQTT para dados críticos.
- **Trate erros:** sensores podem falhar; use `try/except`.
- **Documente** o circuito e o fluxo dos dados.
- **Estruture** o código em funções e módulos.

## 9. Onde evoluir

- Adicionar **banco de dados** (SQLite/InfluxDB) para histórico.
- Criar **dashboards** com Grafana.
- Integrar **notificações** (Telegram, e-mail).
- Rodar tudo com **Docker** no Raspberry Pi.
- Explorar **câmera + IA** (YOLO, TensorFlow Lite).

## Tópicos
- 

## Relacionadas

- [[Raspberry-Pi-e-IoT]]
- [[GPIO e Eletrônica com Raspberry Pi]]
- [[Internet das Coisas (IoT)]]
- [[Faculdade]]