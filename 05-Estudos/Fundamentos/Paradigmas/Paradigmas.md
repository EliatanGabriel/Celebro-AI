---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Paradigmas

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Estilos de programação que definem como estruturar o raciocínio e o código; os principais são imperativo, procedural, orientado a objetos, funcional e declarativo.

## Conceitos-chave
- **Imperativo:** foca em *como* fazer, com comandos que alteram o estado passo a passo.
- **Procedural:** extensão do imperativo que organiza o código em procedimentos/funções reutilizáveis.
- **Orientado a objetos:** organiza em objetos que combinam estado e comportamento; destaca encapsulamento, herança e polimorfismo.
- **Funcional:** trata a computação como avaliação de funções puras, evitando estado mutável e efeitos colaterais.
- **Declarativo:** foca em *o que* deve ser feito, deixando o *como* para a máquina (ex.: SQL, consultas, templates).
- **Misto:** a maioria das linguagens é multiparadigma; bons projetos combinam o que cada estilo oferece.
- **Escolha:** depende do problema, da equipe, do domínio e dos trade-offs de manutenção e performance.

## Exemplos
```javascript
// Imperativo: somar números de um array
let total = 0;
for (let i = 0; i < numeros.length; i++) {
  total += numeros[i];
}

// Funcional/declarativo: mesmo resultado, expressando o "o quê"
const total = numeros.reduce((acc, n) => acc + n, 0);
```

```sql
-- Declarativo: especifica o resultado, não os passos
SELECT nome FROM usuarios WHERE ativo = true ORDER BY nome;
```

```python
# Procedural: organizar em funções
def somar(a, b):
    return a + b

# Orientado a objetos: agrupar dados e comportamento
class Calculadora:
    def somar(self, a, b):
        return a + b
```

## Boas práticas
- Conhecer os trade-offs de cada paradigma para escolher com critério.
- Combinar paradigmas quando faz sentido (ex.: OO com funções puras internas).
- Priorizar legibilidade e manutenção, não apenas preferência pessoal.
- Usar o paradigma dominante da linguagem para aproveitar suas ferramentas (nada de "estilo Java" em JS puro, por exemplo).

## Armadilhas comuns
- Acreditar que um paradigma é universalmente superior; todos têm custos e benefícios.
- Misturar estilos sem consistência, gerando código difícil de entender.
- Forçar OO em problemas funcionais simples ou funções puras onde estado seria mais claro.
- Escrever código declarativo com efeitos colaterais escondidos.
- Ignorar que a maioria das linguagens suporta múltiplos paradigmas.

## Relacionadas
- [[Orientacao-a-Objetos]]
- [[Programacao-Funcional]]
- [[Programacao-Procedural]]
- [[Programacao]]
- [[Estudos-Funcoes]]
- [[Estudos-Variaveis]]