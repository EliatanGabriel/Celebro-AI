---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Funcoes

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Blocos reutilizáveis de código que recebem parâmetros, executam instruções e retornam valores, permitindo organizar, abstrair e reutilizar a lógica.

## Conceitos-chave
- **Definição e chamada:** a função é declarada uma vez (`def`/`function`) e invocada quantas vezes forem necessárias.
- **Parâmetros e argumentos:** a função declara parâmetros; a chamada passa argumentos reais.
- **Retorno:** `return` devolve um valor e encerra a execução; sem `return`, a função retorna `None`/`undefined`.
- **Escopo:** variáveis locais pertencem à função; variáveis de escopo externo são acessíveis mas não devem ser modificadas sem declaração.
- **Assinatura:** nome + parâmetros (tipos e ordem); define como a função é usada.
- **Funções puras vs. com efeitos colaterais:** puras não alteram estado externo; efeitos colaterais dificultam testes e raciocínio.
- **Reuso e composição:** funções pequenas com responsabilidade única compõem comportamentos maiores.
- **Recursão:** uma função que chama a si mesma para resolver subproblemas.

## Exemplos
```python
def calcular_media(notas):          # parâmetro: notas
    if not notas:
        return 0                    # caso de borda
    total = sum(notas)
    return total / len(notas)       # retorno

print(calcular_media([7, 8, 9]))    # 8.0
print(calcular_media([]))           # 0
```

```javascript
// Função de alta ordem: recebe outra função como parâmetro
function aplicar(fn, valor) {
  return fn(valor);
}

const dobro = (x) => x * 2;
console.log(aplicar(dobro, 5));   // 10
```

```text
// Escopo: variável local existe apenas dentro da função
funcao exemplo():
    x = 10          // local a exemplo()
    retorne x
// fora de exemplo(), x não existe
```

## Boas práticas
- Dar nomes que descrevam a ação e manter uma responsabilidade por função.
- Retornar dados em vez de imprimir dentro da função; deixar a saída para o chamador.
- Validar entradas no início (casos de borda) e usar `return` cedo.
- Preferir funções puras: mais fáceis de testar e reutilizar.
- Limitar o número de parâmetros; agrupar em objetos/structs quando muitos.
- Usar recursão com caso base claro para problemas recursivos naturais.

## Armadilhas comuns
- Modificar parâmetros por referência e gerar efeitos colaterais inesperados.
- Esquecer o `return`, fazendo a função devolver `None`/`undefined`.
- Funções com muitas responsabilidades e parâmetros demais, difíceis de testar.
- Confundir escopo local com global e sobrescrever variáveis externas.
- Recursão sem caso base ou com profundidade excessiva (stack overflow).
- Não tratar caso de borda (lista vazia, divisão por zero).

## Relacionadas
- [[Estudos-Variaveis]]
- [[Estudos-Recursao]]
- [[Programacao-Funcional]]
- [[Programacao-Procedural]]
- [[Logica-de-Programacao]]
- [[Algoritmos]]
- [[Programacao]]