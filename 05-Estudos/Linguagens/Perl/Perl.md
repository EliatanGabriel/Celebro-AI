---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Perl

#area/estudos #estudos/linguagens #conceito

**Resumo:** Linguagem madura e multiparadigma conhecida pelo poderio em processamento de texto, expressões regulares e administração de sistemas, com o enorme repositório de módulos CPAN.

## Conceitos-chave
- Multiparadigma: procedural, orientada a objetos e funcional; lema "There's More Than One Way To Do It" (TMTOWTDI).
- Tipagem dinâmica: contextos (escalar, lista, vazio) determinam o comportamento das expressões.
- Interpretada: executada por interpretador/perl, sem compilação separada (bytecode opcional).
- Uso principal em processamento de texto (text processing), one-liners, scripts de sysadmin e sistemas legados de infraestrutura.
- Expressões regulares integradas à linguagem (`=~`, `m//`, `s///`, `g`).
- Três tipos principais de variáveis: `$` (escalar), `@` (array), `%` (hash).
- Particularidade: CPAN reúne dezenas de milhares de módulos reutilizáveis.

## Exemplos
```perl
#!/usr/bin/perl
use strict;
use warnings;

my %idade = ( Ana => 30, Bruno => 22 );

foreach my $nome (sort keys %idade) {
    print "$nome tem $idade{$nome} anos\n";
}

# Processamento de texto com regex
my $texto = "O IP é 192.168.0.1";
if ($texto =~ /(\d{1,3}(?:\.\d{1,3}){3})/) {
    print "IP encontrado: $1\n";
}
```

## Boas práticas
- Sempre inicie com `use strict;` e `use warnings;` para evitar erros silenciosos.
- Nomeie variáveis com significado e prefira hashes a arrays para buscas por chave.
- Use módulos do CPAN em vez de reinventar funcionalidades comuns.
- Comente one-liners complexos ou evite-os em scripts de produção.
- Teste regex com cuidado; use `qr//` para expressões reutilizáveis.

## Armadilhas comuns
- Esquecer `use strict`, permitindo variáveis globais acidentais e bugs difíceis.
- Confundir contexto: uma expressão muda de resultado em contexto de lista vs. escalar.
- Erros silenciosos ao ignorar `$!` e o código de saída de chamadas de sistema.
- Interpolar `@array` dentro de string ("...@array...") quando se deseja o escalar `@array[0]`.
- Regex greedy: `.*` captura mais do que o esperado; use `.*?` para lazy match.

## Relacionadas
- [[Python]]
- [[Bash]]
- [[Shell]]