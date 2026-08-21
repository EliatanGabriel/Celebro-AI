---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Dart

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem otimizada para UI criada pelo Google, base do framework Flutter para aplicações móveis, web e desktop multiplataforma.

## Conceitos-chave
- Paradigma orientado a objetos (tudo é objeto, inclusive funções) com suporte a programação funcional.
- Tipagem estática e forte, com inferência de tipos (`var`, `final`, `const`).
- Compilação dupla: JIT (just-in-time) com hot reload durante o desenvolvimento e AOT (ahead-of-time) para código nativo em produção.
- Uso principal em Flutter (UI multiplataforma: Android, iOS, web, desktop), além de backend e CLI.
- Null safety: tipos não anuláveis por padrão, evitando NullPointerException em tempo de compilação.
- Particularidade: garbage collector e isolates (threads isoladas que se comunicam por mensagens, sem memória compartilhada).

## Exemplos
```dart
void main() {
  var nomes = ['Ana', 'Bruno'];
  nomes.add('Carlos');

  final numeros = [1, 2, 3, 4, 5];
  final pares = numeros.where((n) => n.isEven).toList();

  imprimirSaudacao(nome: 'Mundo');
  print(pares);  // [2, 4]
}

void imprimirSaudacao({required String nome}) {
  print('Olá, $nome!');
}

class Usuario {
  Usuario(this.nome, {this.idade});  // construtor com parâmetro opcional nomeado
  final String nome;
  final int? idade;  // tipo anulável
}
```

## Boas práticas
- Prefira `final`/`const` para imutabilidade e melhor desempenho do AOT.
- Use null safety de forma explícita: `!` (bang) apenas quando o valor é garantidamente não nulo.
- Em Flutter, mantenha widgets pequenos e estados gerenciados com padrões consolidados (Provider, Riverpod).
- Use `async`/`await` com Futures e Streams para I/O e eventos.
- Evite objetos grandes e profundos no layout; use construtos de renderização eficientes.

## Armadilhas comuns
- Aplicar `!` em valor possivelmente nulo, gerando erro em runtime.
- Ignorar `const` em widgets Flutter, causando rebuilds desnecessários.
- Confundir `==` (identidade de referência) com igualdade estrutural em classes sem `==`/`hashCode`.
- Usar `print()` em produção em vez de logging estruturado.
- Assumir que isolates compartilham memória como threads em outras linguagens.

## Relacionadas
- [[Swift]]
- [[Kotlin]]
- [[Frontend]]
- [[Componentes]]