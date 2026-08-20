---
type: concept
area: faculdade
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Fundamentos de Eletrônica

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Fundamentos de eletrônica para projetos com Arduino: tensão, corrente, resistência, lei de Ohm, protoboard e circuitos básicos.

## 1. Conceitos básicos

- **Tensão (V)** — medida em volts (V). É a "pressão" que empurra os elétrons.
- **Corrente (I)** — medida em amperes (A). É o fluxo de elétrons.
- **Resistência (R)** — medida em ohms (Ω). Dificulta a passagem da corrente.
- **Potência (P)** — medida em watts (W). É a energia consumida. `P = V × I`

## 2. Lei de Ohm

A relação entre tensão, corrente e resistência:

```
V = R × I
I = V / R
R = V / I
```

**Exemplo:** um LED de 2V alimentado com 5V precisa de um resistor. Com `R = (5 - 2) / 0,02A = 150Ω`, a corrente é limitada em 20mA.

## 3. Grandezas e unidades

| Grandeza | Símbolo | Unidade |
| --- | --- | --- |
| Tensão | V | Volt (V) |
| Corrente | I | Ampère (A) |
| Resistência | R | Ohm (Ω) |
| Potência | P | Watt (W) |
| Capacitância | C | Farad (F) |

## 4. Circuito elétrico

Um circuito é composto por:

```
FONTE (bateria/alimentação)
    ↓
CONDUTOR (fio/cobre)
    ↓
CARGA (LED, motor, resistor)
    ↓
retorno à fonte (GND)
```

Um circuito fechado permite o fluxo de corrente; um aberto interrompe o fluxo.

## 5. Série e paralelo

**Circuito em série:**

- A corrente é a mesma em todos os elementos.
- A tensão se divide.
- Resistência total = soma das resistências.

**Circuito em paralelo:**

- A tensão é a mesma em todos os ramos.
- A corrente se divide.
- Resistência total é menor que cada resistência individual.

## 6. Protoboard (matriz de contato)

A protoboard permite montar circuitos sem solda.

- As linhas centrais (A–E e F–J) são conectadas verticalmente em colunas.
- As trilhas laterais (vermelha e azul) são os barramentos de alimentação e GND.

```
   +VCC      GND
┌─────────┬─────────┐
│ ─ ─ ─ ─ │ ─ ─ ─ ─ │   trilhas de alimentação
├─┬─┬─┬─┬─┼─┬─┬─┬─┬─┤
│o│o│o│o│o│ │o│o│o│o│o│   colunas conectadas
└─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘
```

## 7. Componentes comuns

- **LED** — diodo que emite luz. Tem polaridade (ânodo +, cátodo −).
- **Resistor** — limita corrente. Código de cores indica o valor.
- **Botão (push button)** — fecha ou abre o circuito.
- **Potenciômetro** — resistor ajustável.
- **Capacitor** — armazena carga elétrica.
- **Diodo** — permite corrente em um único sentido.
- **Transistor** — funciona como chave ou amplificador.

## 8. Tensões típicas no Arduino

- **5V** — alimentação dos pinos lógicos.
- **3,3V** — alimentação alternativa (menor consumo).
- **GND** — terra comum.
- **Vin** — entrada de alimentação externa.

## 9. Segurança

- Confira sempre a polaridade (GND × VCC).
- Calcule o resistor antes de ligar um LED direto.
- Não conecte 220V AC diretamente nos pinos.
- Use resistores de pull-up/pull-down quando necessário.

## Tópicos
- 

## Relacionadas

- [[Arduino]]
- [[Faculdade]]