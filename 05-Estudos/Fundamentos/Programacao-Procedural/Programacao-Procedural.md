---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Programacao-Procedural

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Paradigma de programação imperativo que organiza o código em procedimentos (funções), executados em sequência, com variáveis de estado modificadas passo a passo.

## Conceitos-chave
- **Procedimentos/funções:** blocos nomeados de instruções que podem receber parâmetros e retornar valores, promovendo reuso.
- **Sequência:** o programa é uma lista ordenada de instruções que modificam o estado.
- **Estado mutável:** variáveis são lidas e reatribuídas ao longo da execução.
- **Estruturas de controle:** condicionais (`if`) e loops (`for`, `while`) direcionam o fluxo.
- **Escopo:** variáveis locais aos procedimentos e globais ao programa; escopo define visibilidade.
- **Modularização:** dividir o problema em procedimentos com responsabilidades claras.
- **Exemplos de linguagem:** C, Pascal e a base de muitas outras; Python e Java suportam o estilo.

## Exemplos
```c
#include <stdio.h>

// Procedimento: reutilizável, com parâmetros e retorno
int soma_ate(int n) {
    int total = 0;
    for (int i = 1; i <= n; i++) {
        total += i;          // estado mutável
    }
    return total;
}

int main() {
    int n = 10;
    printf("Soma: %d\n", soma_ate(n));
    printf("Soma: %d\n", soma_ate(5));   // reuso
    return 0;
}
```

```python
# Estilo procedural em Python
def calcular_media(notas):
    total = 0
    for nota in notas:
        total += nota
    return total / len(notas)

def main():
    notas = [7, 8, 9]
    print(calcular_media(notas))

main()
```

## Boas práticas
- Dividir o programa em procedimentos com responsabilidade única e nomes claros.
- Limitar o uso de variáveis globais; preferir passar dados por parâmetros.
- Manter cada procedimento pequeno e compreensível.
- Estruturar a sequência principal de forma linear e legível.

## Armadilhas comuns
- Abusar de variáveis globais, tornando o fluxo imprevisível e difícil de testar.
- Criar procedimentos gigantescos que fazem tudo, perdendo o benefício da modularidade.
- Usar efeitos colaterais implícitos (modificar parâmetros ou globais) sem documentar.
- Ignorar o estado compartilhado, que dificulta depuração e paralelismo.
- Misturar estilos sem critério, combinando procedimentos com mudanças de estado confusas.

## Relacionadas
- [[Paradigmas]]
- [[Programacao-Funcional]]
- [[Orientacao-a-Objetos]]
- [[Estudos-Funcoes]]
- [[Estudos-Variaveis]]
- [[Logica-de-Programacao]]
- [[Programacao]]