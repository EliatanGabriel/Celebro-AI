---
type: concept
area: faculdade
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Programação com Arduino

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Programação com Arduino: estrutura do sketch, funções setup/loop, pinos, digital/analógico, e a linguagem baseada em C/C++.

## 1. O que é um sketch

Um **sketch** é o programa escrito para o Arduino. Ele é salvo com a extensão `.ino` e escrito na IDE do Arduino.

## 2. Estrutura básica

Todo sketch possui duas funções obrigatórias:

```cpp
void setup() {
    // Executa uma vez no início
    // Configura pinos, velocidade serial, etc.
    pinMode(13, OUTPUT);
}

void loop() {
    // Executa repetidamente enquanto a placa estiver ligada
    digitalWrite(13, HIGH);
    delay(1000);
    digitalWrite(13, LOW);
    delay(1000);
}
```

- **setup()** — roda uma única vez.
- **loop()** — roda em loop infinito.

## 3. Configuração de pinos

```cpp
pinMode(pino, modo);
```

Modos:

- `OUTPUT` — pino envia sinal (LED, motor).
- `INPUT` — pino lê sinal (botão, sensor).
- `INPUT_PULLUP` — entrada com resistor interno de pull-up.

## 4. Saída digital

```cpp
digitalWrite(13, HIGH);   // 5V (ou 3,3V)
digitalWrite(13, LOW);    // 0V
```

## 5. Entrada digital

```cpp
int valor = digitalRead(2);   // HIGH ou LOW
```

Usado com botões e sensores de contato.

## 6. Entrada e saída analógica

- **Analógico de entrada:** `analogRead(pino)` lê valores de **0 a 1023** (10 bits). Pinos A0–A5.
- **Analógico de saída:** `analogWrite(pino, valor)` emite um **PWM** de 0 a 255, controlando brilho do LED ou velocidade do motor. Pinos com `~`.

```cpp
int leitura = analogRead(A0);
analogWrite(9, 128);   // metade do brilho
```

## 7. PWM (Pulse Width Modulation)

O PWM simula uma saída analógica ligando e desligando o pino rapidamente. A "média" da tensão varia com a largura do pulso.

```
Duty 50%:  ████████
Duty 25%:  ██
```

## 8. Comunicação Serial

Usada para depuração e envio de dados ao computador.

```cpp
void setup() {
    Serial.begin(9600);       // inicia na taxa 9600 baud
}

void loop() {
    Serial.println("Olá mundo");
    delay(1000);
}
```

Para ler: `Serial.read()`, `Serial.available()` e `Serial.parseInt()`.

## 9. Tipos e variáveis

- `int` — inteiro.
- `float` — decimal.
- `char` — caractere.
- `String` — texto.
- `bool` — verdadeiro/falso.
- `const` — valor que não muda.

```cpp
int led = 13;
const int buttonPin = 2;
```

## 10. Estruturas de controle

```cpp
if (digitalRead(2) == HIGH) {
    digitalWrite(13, HIGH);
} else {
    digitalWrite(13, LOW);
}

for (int i = 0; i < 5; i++) {
    digitalWrite(13, HIGH);
    delay(200);
    digitalWrite(13, LOW);
    delay(200);
}

while (Serial.available() == 0) {
    // aguarda entrada
}
```

## 11. Boas práticas

- Use constantes para pinos.
- Evite `delay()` em projetos que precisam de reação rápida (prefira `millis()`).
- Trate o "debounce" de botões.
- Documente o sketch com comentários.

## Tópicos
- 

## Relacionadas

- [[Arduino]]
- [[Fundamentos de Eletrônica]]
- [[Faculdade]]