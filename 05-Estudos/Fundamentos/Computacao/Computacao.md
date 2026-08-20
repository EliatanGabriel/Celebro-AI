---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Computacao

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Ciência que estuda o processamento de informação por meios automáticos, dos modelos teóricos de cálculo às máquinas e softwares que os realizam.

## Conceitos-chave
- **Máquina de Turing:** modelo abstrato de cálculo que define formalmente o que é computável; base da teoria da computação.
- **Computabilidade e limites:** alguns problemas são indecidíveis (ex.: problema da parada) — não existe algoritmo que os resolva.
- **Modelos de computação:** Turing machine, autômatos finitos, lambda-cálculo; todos equivalentes em poder expressivo.
- **Abstração:** a computação é organizada em camadas (hardware, sistema operacional, linguagem, aplicação), cada uma ocultando a complexidade da anterior.
- **Informação:** a computação manipula dados que são codificados e interpretados; a representação binária é a base.
- **Complexidade:** o estudo do custo de computação levou à classificação de problemas em classes como P e NP.

## Exemplos
```text
// Problema da parada (indecidível)
- Entrada: um programa P e um dado d
- Pergunta: P termina ao processar d?
- Resposta: não existe algoritmo que responda para todos os casos (Turing, 1936)

// Equivalência de modelos
Máquina de Turing  ≡  Lambda-cálculo  ≡  Funções recursivas
(qualquer coisa computável por um é computável pelos outros)
```

```text
// Camadas de abstração em uma aplicação web
Camada de aplicação:  código do usuário (JS/Python)
Linguagem/compilador: tradução para código de máquina
Sistema operacional:  processos, memória, I/O
Hardware:             CPU, RAM, dispositivos
```

## Boas práticas
- Pensar em termos de modelos abstratos antes de implementar.
- Usar a abstração para dividir problemas complexos em camadas.
- Conhecer os limites teóricos para não tentar o impossível (indecidíveis).
- Relacionar cada conceito computacional à sua base teórica.

## Armadilhas comuns
- Confundir a Máquina de Turing com um computador físico real.
- Achar que todo problema pode ser resolvido com mais poder de hardware; problemas indecidíveis não dependem de máquina.
- Ignorar a camada de abstração e tratar problemas de hardware como se fossem de código ou vice-versa.
- Supor que representações de dados são universais, esquecendo codificação (bytes, encoding, endianness).

## Relacionadas
- [[Ciencia-da-Computacao]]
- [[Algoritmos]]
- [[Logica]]
- [[Sistemas]]
- [[Memoria]]
- [[Estudos-Complexidade]]