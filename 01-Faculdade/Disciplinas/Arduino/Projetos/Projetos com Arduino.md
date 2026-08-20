---
type: concept
area: faculdade
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Projetos com Arduino

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Projetos com Arduino: metodologia de projeto, componentes, ideias práticas e exemplos comentados de projetos clássicos.

## 1. Metodologia de um projeto

1. **Definir o problema** — o que o projeto deve resolver?
2. **Escolher os componentes** — sensores, atuadores, placa.
3. **Desenhar o circuito** — esquemático e protoboard.
4. **Escrever o código** — em partes testáveis.
5. **Testar** — validar cada funcionalidade.
6. **Empacotar** — montagem final, fiação organizada.

```
PROBLEMA → COMPONENTES → CIRCUITO → CÓDIGO → TESTES → ENTREGA
```

## 2. Projeto: semáforo

Componentes: 3 LEDs (vermelho, amarelo, verde) e 3 resistores.

```cpp
int red = 13, yellow = 12, green = 11;

void setup() {
    pinMode(red, OUTPUT);
    pinMode(yellow, OUTPUT);
    pinMode(green, OUTPUT);
}

void loop() {
    digitalWrite(red, HIGH);
    delay(3000);
    digitalWrite(red, LOW);
    digitalWrite(green, HIGH);
    delay(3000);
    digitalWrite(green, LOW);
    digitalWrite(yellow, HIGH);
    delay(1000);
    digitalWrite(yellow, LOW);
}
```

## 3. Projeto: estação de temperatura

Componentes: LM35 (ou DHT11) + display LCD.

```cpp
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int sensor = A0;

void setup() {
    lcd.begin(16, 2);
}

void loop() {
    int leitura = analogRead(sensor);
    float tensao = leitura * (5.0 / 1023.0);
    float temp = tensao * 100.0;
    lcd.setCursor(0, 0);
    lcd.print("Temp: ");
    lcd.print(temp);
    lcd.print(" C");
    delay(2000);
}
```

## 4. Projeto: alarme de presença

Componentes: sensor PIR + buzzer.

```cpp
int pirPin = 2;
int buzzer = 8;

void setup() {
    pinMode(pirPin, INPUT);
    pinMode(buzzer, OUTPUT);
}

void loop() {
    if (digitalRead(pirPin) == HIGH) {
        digitalWrite(buzzer, HIGH);
        delay(5000);
        digitalWrite(buzzer, LOW);
    }
    delay(100);
}
```

## 5. Projeto: controle de LED por potenciômetro

Componentes: potenciômetro + LED.

```cpp
int pot = A0;
int led = 9;

void setup() {
    pinMode(led, OUTPUT);
}

void loop() {
    int valor = analogRead(pot);       // 0 a 1023
    int pwm = map(valor, 0, 1023, 0, 255);  // 0 a 255
    analogWrite(led, pwm);
}
```

A função `map()` converte uma faixa de valores em outra.

## 6. Projeto: jogo de reação

Componentes: botão, LED e buzzer. Desafio: medir o tempo de reação do jogador.

```cpp
unsigned long inicio;

void setup() {
    pinMode(2, INPUT_PULLUP);
    pinMode(13, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    digitalWrite(13, HIGH);
    delay(random(1000, 5000));   // espera aleatória
    digitalWrite(13, LOW);
    inicio = millis();
    while (digitalRead(2) == HIGH) {
        if (millis() - inicio > 3000) {
            Serial.println("Tempo esgotado");
            return;
        }
    }
    Serial.print("Tempo de reação: ");
    Serial.print(millis() - inicio);
    Serial.println(" ms");
    delay(2000);
}
```

## 7. Dicas de montagem

- Teste o circuito em partes: primeiro o LED, depois o sensor, depois integra tudo.
- Use jumpers coloridos para identificar alimentação e sinais.
- Fixe componentes com suporte ou fita isolante quando necessário.
- Mantenha o código com comentários e dividido em funções.

## 8. Onde evoluir

- Adicionar comunicação **Bluetooth/Wi-Fi** (ESP32, HC-05).
- Usar **display OLED** para interfaces.
- Integrar com a nuvem (IoT) — ver [[Raspberry-Pi-e-IoT]].
- Criar **alimentação por bateria** para projetos portáteis.

## Tópicos
- 

## Relacionadas

- [[Arduino]]
- [[Programação com Arduino]]
- [[Sensores e Atuadores]]
- [[Faculdade]]