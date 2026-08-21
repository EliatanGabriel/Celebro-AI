---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Scala

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem para a JVM que combina orientação a objetos com programação funcional, usada em big data (Apache Spark), backend funcional e sistemas concorrentes (Akka).

## Conceitos-chave
- Multiparadigma: orientada a objetos (traits, classes) e funcional (imutabilidade, funções de alta ordem).
- Tipagem estática e forte, com inferência de tipos e typesystem expressivo.
- Compilada para bytecode JVM (também compila para JavaScript e Native).
- Uso principal em processamento de big data (Spark), microserviços e sistemas reativos (Akka).
- Case classes geram automaticamente `equals`, `hashCode`, `toString` e pattern matching.
- Imutabilidade por padrão (`val` em vez de `var`) e coleções imutáveis.
- Particularidade: interoperabilidade com bibliotecas Java e "Object-Oriented Meets Functional".

## Exemplos
```scala
// Case class + pattern matching
case class Pessoa(nome: String, idade: Int)

val pessoas = List(Pessoa("Ana", 30), Pessoa("Bruno", 16))

val adultos = pessoas
  .filter(_.idade >= 18)
  .map(_.nome)

println(adultos)  // List(Ana)

def descrever(p: Pessoa): String = p match {
  case Pessoa(nome, idade) if idade >= 18 => s"$nome é adulto"
  case Pessoa(nome, _)                    => s"$nome é menor de idade"
}

pessoas.foreach(p => println(descrever(p)))
```

## Boas práticas
- Prefira `val` (imutável) e coleções imutáveis para código mais seguro e testável.
- Use case classes para dados de valor e pattern matching para desconstrução.
- Aproveite a inferência de tipos, mas declare assinaturas públicas em APIs.
- Modele concorrência com futures/Akka em vez de threads cruas.
- Foque em funções puras para facilitar teste e previsibilidade.

## Armadilhas comuns
- `Option` tratado como valor: usar `.get` em vez de pattern matching/`fold` pode falhar.
- Confundir `val` (avaliado imediatamente) com `lazy val` (sob demanda) e `def` (reavaliado).
- Inferência de tipos para métodos recursivos falha; declare o tipo de retorno explicitamente.
- Sobrecarga e conversões implícitas (implicit) obsoletas, que dificultam a leitura.
- Ignorar null em interop com Java, quebrando a segurança de tipos do Scala.

## Relacionadas
- [[Java]]
- [[Kotlin]]