---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Debug

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Processo sistemático de localizar e corrigir bugs — falhas que fazem o programa se comportar de forma inesperada — usando ferramentas e técnicas de investigação.

## Conceitos-chave
- **Bug:** diferença entre o comportamento esperado e o observado; pode ser erro de lógica, de tipagem ou de ambiente.
- **Reproduzir:** o primeiro passo é obter uma entrada mínima e consistente que reexiba o erro.
- **Breakpoints:** pontos de parada que pausam a execução para inspecionar variáveis e o fluxo em um instante exato.
- **Step over / step into / step out:** navegação linha a linha pela execução, entrando ou saindo de chamadas de função.
- **Logging:** registrar valores e eventos ao longo do código, útil em produção onde debuggers não estão disponíveis.
- **Leitura de stack trace:** a pilha de chamadas mostra a sequência de funções até o erro, apontando a origem do problema.
- **Binary search / bisect:** dividir o problema ao meio para isolar rapidamente a região do código culpada.

## Exemplos
```text
// Stack trace típico
Uncaught TypeError: Cannot read properties of undefined (reading 'name')
  at renderUser (app.js:12)
  at renderList (app.js:20)
  at main (app.js:30)

// Leitura: o erro acontece em renderUser, chamada por renderList,
// chamada por main. O problema provavelmente está em app.js:12.
```

```text
// Depuração por logging
funcao calcular_total(itens):
    total = 0
    para cada item em itens:
        log("item:", item)            // confere o que está chegando
        total = total + item.preco    // se item.preco for undefined, o erro aparece aqui
        log("total parcial:", total)
    retorne total
```

## Boas práticas
- Reproduzir o bug com o menor caso possível antes de corrigir.
- Ler a mensagem de erro e o stack trace por inteiro antes de alterar código.
- Usar o debugger em vez de adivinhar: breakpoints e inspeção de variáveis são mais confiáveis que `print` aleatórios.
- Fazer uma correção por vez e re-testar; mudanças múltiplas simultâneas confundem o diagnóstico.
- Escrever testes que cobram o caso que causou o bug, prevenindo regressões.
- Isolar o problema usando bisect quando o código é extenso.

## Armadilhas comuns
- Corrigir o sintoma em vez da causa (ex.: suprimir a exceção com `try/catch` vazio).
- Usar `print`/`log` excessivos e remover depois, sem entender o erro.
- Assumir que a variável tem um valor sem verificar; muitas vezes o bug está na entrada.
- Ignorar o stack trace e procurar o erro no lugar errado.
- Alterar várias coisas ao mesmo tempo e não conseguir identificar qual mudança corrigiu ou quebrou o código.
- Ficar preso no mesmo trecho em vez de buscar o ponto exato com breakpoints.

## Relacionadas
- [[Logica]]
- [[Logica-de-Programacao]]
- [[Algoritmos]]
- [[Estudos-Funcoes]]
- [[Sistemas]]
- [[Performance]]