---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Tipos-de-Dados

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Categorias de valores que definem o conjunto de operações permitidas e o espaço de memória usado; incluem tipos primitivos, compostos e estruturas de dados.

## Conceitos-chave
- **Primitivos:** inteiros (`int`), ponto flutuante (`float`/`double`), caractere (`char`), booleano (`bool`) e valores sem valor (`null`/`undefined`).
- **Compostos:** agrupam primitivos — strings (sequência de caracteres), arrays, tuplas, structs e objetos.
- **Tipagem estática:** o tipo é definido em tempo de compilação (Java, C, TypeScript), detectando erros cedo.
- **Tipagem dinâmica:** o tipo é verificado em tempo de execução (Python, JavaScript), mais flexível, com risco de erros em runtime.
- **Tipagem forte vs. fraca:** forte evita conversões implícitas entre tipos; fraca realiza coerções automáticas (ex.: `"1" + 1`).
- **Conversão de tipos:** implícita (coerção) ou explícita (casting); pode perder precisão (float → int) ou falhar (string inválida → número).
- **Tamanho em memória:** `int` ocupa tamanho fixo conforme a linguagem; tipos maiores armazenam intervalos maiores.

## Exemplos
```javascript
// Dinâmico e fracamente tipado
let valor = 10;            // number
valor = "texto";           // reatribuído para string (dinâmico)
console.log("1" + 2);      // "12" — coerção implícita (fraco)

// Conversão explícita
let n = Number("42");      // 42
let falha = Number("abc"); // NaN — conversão inválida
```

```python
# Tipos primitivos e compostos
idade = 27          # int
altura = 1.75       # float
nome = "Ana"        # str
ativo = True        # bool
notas = [8, 9, 7]   # list (composto)
pessoa = {"nome": nome, "idade": idade}  # dict
```

```c
// Tipagem estática: tipo fixo em tempo de compilação
int x = 5;                 // int ocupa 4 bytes (típico)
double y = 3.14;           // ponto flutuante
char letra = 'A';
int z = (int) y;           // cast: 3 (perde a parte decimal)
```

## Boas práticas
- Escolher o tipo com o menor intervalo que atenda à necessidade (memória e clareza).
- Evitar conversões implícitas; usar conversão explícita e validar resultados.
- Preferir tipagem estática em projetos grandes para capturar erros cedo.
- Documentar o tipo esperado de parâmetros e retornos quando a linguagem é dinâmica.

## Armadilhas comuns
- Confiar em coerções implícitas de linguagens fracamente tipadas (`"1" + 1`).
- Comparar tipos diferentes com `==` e obter surpresas (`0 == false` em JS).
- Perder precisão em conversões (float para int, ou floats muito grandes).
- Ignorar o intervalo do tipo: overflow de inteiros ou precisão de ponto flutuante.
- Assumir que "tudo é objeto" ou que "todos os tipos têm o mesmo tamanho" entre linguagens.

## Relacionadas
- [[Memoria]]
- [[Estudos-Variaveis]]
- [[Arrays]]
- [[JSON]]
- [[Logica]]
- [[Orientacao-a-Objetos]]
- [[Hash]]