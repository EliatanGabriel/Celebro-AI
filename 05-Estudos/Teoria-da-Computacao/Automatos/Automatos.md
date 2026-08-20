---
type: concept
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Autômatos

#area/estudos #teoria-da-computacao #conceito #teoria #computacao #automatos

**Resumo:** Modelos matemáticos abstratos de máquinas que reconhecem linguagens, ordenados pela hierarquia de Chomsky conforme o poder computacional.

## Conceitos-chave
- **Autômatos finitos (AFD/AFN):** máquinas com estado finito e leitura única; reconhecem linguagens regulares.
- **Autômatos com pilha (AP):** acrescentam memória do tipo pilha; reconhecem linguagens livres de contexto.
- **Máquinas de Turing:** modelo mais poderoso, com fita ilimitada; formalizam o conceito de algoritmo e decidibilidade.
- **Componentes formais:** estado, alfabeto, função de transição, estado inicial e estados finais.
- **Equivalências:** AFN e AFD são equivalentes; autômatos finitos equivalem a expressões regulares.

## Exemplos
```python
# AFD que aceita cadeias binárias terminadas em "1"
class AFD:
    def __init__(self):
        self.estado = "q0"
        self.finais = {"q1"}

    def transicoes(self, simbolo):
        if self.estado == "q0":
            self.estado = "q1" if simbolo == "1" else "q0"
        elif self.estado == "q1":
            self.estado = "q1" if simbolo == "1" else "q0"

    def aceita(self, cadeia):
        self.estado = "q0"
        for s in cadeia:
            self.transicoes(s)
        return self.estado in self.finais

afd = AFD()
print(afd.aceita("101"))   # True
print(afd.aceita("100"))   # False
```

## Boas práticas
- Desenhar o diagrama de estados antes de formalizar a função de transição.
- Usar AFN primeiro quando a linguagem for complexa e converter para AFD se necessário.
- Verificar a minimização do autômato para simplificar implementações.

## Armadilhas comuns
- Confundir linguagens regulares (AF) com livres de contexto (AP) no reconhecimento.
- Esquecer estados de erro/sink em autômatos finitos.
- Assumir que toda linguagem é decidível: a máquina de Turing também demonstra problemas indecidíveis.

## Relacionadas
- [[Complexidade]]
- [[Linguagens]]
- [[Logica]]
- [[Computacao]]