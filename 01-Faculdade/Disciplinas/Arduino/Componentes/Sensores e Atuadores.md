---
type: concept
area: faculdade
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Sensores e Atuadores

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Sensores e atuadores no Arduino: tipos de sensores, como ler sinais, principais sensores e atuadores usados em projetos.

## 1. O que são sensores e atuadores

- **Sensor** — capta informações do ambiente (temperatura, luz, distância, movimento) e converte em sinal elétrico.
- **Atuador** — executa uma ação no ambiente (LED, motor, servo, buzzer, relé).

```
AMBIENTE → SENSOR → ARDUINO → ATUADOR → AMBIENTE
```

## 2. Tipos de sensores quanto ao sinal

**Digitais:**

- Entregam apenas `HIGH` ou `LOW`.
- Ex.: botão, sensor de presença PIR, sensor de linha (IR).

**Analógicos:**

- Entregam valores contínuos (0 a 1023 no `analogRead`).
- Ex.: LDR (luz), potenciômetro, sensor de temperatura LM35.

## 3. Sensores comuns

| Sensor | Grandeza | Tipo de sinal |
| --- | --- | --- |
| LDR | Luz | Analógico |
| LM35 / DHT11 | Temperatura | Analógico / digital |
| HC-SR04 | Distância (ultrassom) | Digital (pulso) |
| PIR | Movimento/presença | Digital |
| Sensor de linha (IR) | Refletância | Digital |
| Potenciômetro | Posição | Analógico |
| Fotorresistor | Intensidade luminosa | Analógico |

## 4. Sensor de temperatura LM35

```cpp
int sensorPin = A0;

void setup() {
    Serial.begin(9600);
}

void loop() {
    int leitura = analogRead(sensorPin);
    float tensao = leitura * (5.0 / 1023.0);
    float celsius = tensao * 100.0;
    Serial.println(celsius);
    delay(1000);
}
```

## 5. Sensor ultrassônico HC-SR04

Mede distância pelo tempo do eco:

```
TRIG envia pulso → ECO recebe o retorno → distância = tempo × velocidade / 2
```

## 6. Atuadores comuns

- **LED** — indicação visual.
- **Buzzer** — som (ativo ou passivo).
- **Servo motor** — posição angular precisa (0° a 180°).
- **Motor DC** — rotação contínua (controlado com PWM e ponte H).
- **Motor de passo** — rotação precisa em passos.
- **Relé** — liga/desliga circuitos de maior potência.
- **Display LCD** — exibição de informações.

## 7. Servo motor

```cpp
#include <Servo.h>

Servo meuServo;

void setup() {
    meuServo.attach(9);
}

void loop() {
    meuServo.write(0);    // 0 graus
    delay(1000);
    meuServo.write(180);  // 180 graus
    delay(1000);
}
```

## 8. Relé

Permite controlar cargas maiores (lâmpadas, motores 220V) de forma segura, isolando o Arduino do circuito de potência.

```
Arduino (5V) → Relé → Carga 220V
```

## 9. Exemplo integrado: sistema de alerta

```cpp
int sensorPin = A0;
int buzzer = 8;

void setup() {
    pinMode(buzzer, OUTPUT);
    pinMode(sensorPin, INPUT);
}

void loop() {
    int luz = analogRead(sensorPin);
    if (luz > 800) {          // muito escuro
        digitalWrite(buzzer, HIGH);
    } else {
        digitalWrite(buzzer, LOW);
    }
}
```

## 10. Boas práticas

- Consulte o datasheet do componente antes de ligar.
- Verifique a tensão de alimentação (3,3V vs 5V).
- Use resistores divisores quando o sensor não for compatível com 5V.
- Proteja motores com diodo flyback (1N4007).

## Tópicos
- 

## Relacionadas

- [[Arduino]]
- [[Programação com Arduino]]
- [[Faculdade]]