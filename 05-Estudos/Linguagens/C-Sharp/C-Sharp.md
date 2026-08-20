---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# C-Sharp

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem orientada a objetos da Microsoft, principal do ecossistema .NET, usada em aplicações web, desktop, jogos (Unity) e serviços na nuvem.

## Conceitos-chave
- Paradigma orientado a objetos com suporte a programação funcional (LINQ, lambdas) e assíncrona (async/await).
- Tipagem estática e forte, com inferência de tipos via `var`.
- Compilada para IL (Intermediate Language) e executada pela CLR (Common Language Runtime) com JIT e garbage collector.
- Uso principal em ASP.NET (web/API), Unity (jogos), aplicações Windows e Azure.
- Propriedades, indexadores, delegates, eventos e records (C# 9+) enriquecem o modelo de objetos.
- Particularidade: plataforma multiplataforma via .NET Core/.NET 5+, com runtime unificado.

## Exemplos
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Pessoa
{
    public string Nome { get; set; }
    public int Idade { get; set; }
}

class Programa
{
    static async Task<int> Main()
    {
        var pessoas = new List<Pessoa>
        {
            new Pessoa { Nome = "Ana", Idade = 30 },
            new Pessoa { Nome = "Bruno", Idade = 22 }
        };

        var maiores = pessoas.Where(p => p.Idade > 25).Select(p => p.Nome);
        Console.WriteLine(string.Join(", ", maiores));  // Ana
        return 0;
    }
}
```

## Boas práticas
- Use `var` apenas quando o tipo for óbvio; mantenha nomes claros e expressivos.
- Prefira propriedades a campos públicos e classes imutáveis com `record`.
- Aproveite `async`/`await` para I/O sem bloquear threads.
- Use LINQ para composição declarativa de coleções.
- Padronize convenções de nomes (PascalCase para métodos, camelCase para parâmetros).

## Armadilhas comuns
- Confundir valor vs. referência: `class` é referência, `struct` é valor.
- Ignorar nullability: variáveis anuláveis (`string?`) exigem tratamento consciente para evitar NullReferenceException.
- Bloquear com `.Result`/`.Wait()` em código assíncrono, causando deadlocks no contexto de sincronização.
- Supor que o GC libera memória imediatamente — ele age quando o processo precisa.
- Uso excessivo de `dynamic`, que elimina a segurança de tipos em runtime.

## Relacionadas
- [[Java]]
- [[Backend]]
- [[Componentes]]