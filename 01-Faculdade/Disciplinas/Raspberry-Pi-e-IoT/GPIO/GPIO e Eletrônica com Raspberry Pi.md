---
type: concept
area: faculdade
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# GPIO e Eletrônica com Raspberry Pi

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** GPIO no Raspberry Pi: pinos, tensões, entrada/saída, PWM e uso com Python (GPIO Zero e RPi.GPIO).

## 1. O que é GPIO

**GPIO** (*General Purpose Input/Output*) são pinos programáveis para entrada e saída digital. O Raspberry Pi possui um conector de **40 pinos**.

## 2. Mapa dos pinos

```
         3V3  5V
         ┌───┬───┐
      GPIO2 │   │ │
      GPIO3 │   │ │   ... 40 pinos
      ...
```

- **Pinos de alimentação** — 3,3V, 5V e GND.
- **GPIO** — pinos programáveis (numerados por GPIO ou por posição).
- **I2C, SPI, UART** — protocolos de comunicação embutidos.

## 3. Tensões

- **3,3V** — nível lógico dos GPIO (NÃO usar 5V direto na entrada).
- **5V** — alimentação para alguns sensores/módulos.
- **GND** — terra comum.

**Cuidado:** aplicar 5V em um pino GPIO pode danificar a placa.

## 4. Saída digital com Python (GPIO Zero)

```python
from gpiozero import LED
from time import sleep

led = LED(17)        # GPIO 17

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

## 5. Entrada digital com botão

```python
from gpiozero import Button, LED

botao = Button(2)
led = LED(17)

while True:
    if botao.is_pressed:
        led.on()
    else:
        led.off()
```

## 6. PWM (brilho do LED)

```python
from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

for valor in range(0, 101, 5):
    led.value = valor / 100    # 0.0 a 1.0
    sleep(0.1)
```

## 7. Leitura analógica?

O Raspberry Pi **não possui** entradas analógicas nativas (diferente do Arduino). Para ler sensores analógicos, use:

- **ADC externo** (MCP3008) via SPI.
- Sensores **digitais** (DHT22, BMP280, I2C).

```python
from mcp3008 import MCP3008
pot = MCP3008(channel=0)
print(pot.value)   # 0.0 a 1.0
```

## 8. Usando RPi.GPIO (alternativa)

```python
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

GPIO.output(17, GPIO.HIGH)
GPIO.cleanup()
```

**GPIO Zero** é recomendado por ser mais simples; **RPi.GPIO** dá mais controle.

## 9. Exemplo: semáforo

```python
from gpiozero import LED
from time import sleep

vermelho = LED(17)
amarelo = LED(27)
verde = LED(22)

while True:
    verde.on()
    sleep(3)
    verde.off()
    amarelo.on()
    sleep(1)
    amarelo.off()
    vermelho.on()
    sleep(3)
    vermelho.off()
```

## 10. Boas práticas

- Use resistores em série com LEDs (220–330Ω).
- Nunca conecte 5V direto em um GPIO.
- Utilize protoboard e jumpers para prototipar.
- Verifique o mapa de pinos antes de ligar.

## Tópicos
- 

## Relacionadas

- [[Raspberry-Pi-e-IoT]]
- [[Fundamentos de Raspberry Pi]]
- [[Faculdade]]