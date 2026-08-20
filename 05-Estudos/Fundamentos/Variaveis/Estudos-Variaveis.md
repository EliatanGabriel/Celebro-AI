---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Variaveis

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Espaços nomeados na memória que armazenam valores que podem mudar durante a execução; a declaração, a atribuição e o escopo definem como acessá-los.

## Conceitos-chave
- **Declaração:** criar a variável, reservando espaço e (em linguagens estáticas) definindo o tipo.
- **Atribuição:** guardar um valor na variável (`=`, `:=`, `let`); substitui o valor anterior.
- **Escopo:** região do código onde a variável é visível — local (dentro da função/bloco) ou global.
- **Constantes:** valores que não mudam após definição (`const`, `final`), evitando alterações acidentais.
- **Nomes:** devem ser descritivos e seguir convenções da linguagem (camelCase, snake_case).
- **Mutabilidade vs. imutabilidade:** variáveis podem ser reatribuídas; objetos referenciados podem ou não ser mutáveis.
- **Valor vs. referência:** tipos primitivos geralmente copiam valor; objetos são passados por referência.

## Exemplos
```javascript
let contador = 0;          // declaração + atribuição (mutável)
const LIMITE = 10;         // constante: não pode ser reatribuída
contador = contador + 1;   // reatribuição

function exemplo() {
  let local = "dentro";    // escopo local à função
  console.log(local);
}
// local não existe fora de exemplo()
```

```python
total = 0

def incrementar():
    global total           # declara que usará a variável global
    total += 1

# Mutabilidade de objetos
lista = [1, 2, 3]
lista.append(4)            # o objeto muda; a referência é a mesma
```

```c
// Tipagem estática: tipo fixo na declaração
int idade = 30;            // int
float altura = 1.75;       // float
const double PI = 3.14159; // constante
```

## Boas práticas
- Declarar variáveis no menor escopo necessário.
- Usar constantes para valores que não mudam, comunicando a intenção.
- Escolher nomes claros que descrevam o conteúdo, não o tipo.
- Inicializar variáveis no momento da declaração.
- Evitar variáveis globais mutáveis; preferir parâmetros e retornos.

## Armadilhas comuns
- Usar variável sem declarar/inicializar, gerando erro ou valor inesperado.
- Sombra (shadowing): declarar uma variável com o mesmo nome de outra externa, ocultando-a.
- Reatribuir constante ou modificar objeto "constante" por referência.
- Confundir valor com referência ao copiar objetos (cópia rasa).
- Escopo de bloco vs. função: comportamento varia entre linguagens (var vs. let em JS).

## Relacionadas
- [[Tipos-de-Dados]]
- [[Estudos-Funcoes]]
- [[Memoria]]
- [[Logica-de-Programacao]]
- [[Ponteiros]]
- [[Programacao-Procedural]]
- [[Programacao-Funcional]]