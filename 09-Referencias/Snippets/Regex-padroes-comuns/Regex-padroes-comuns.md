---
type: snippet
area: referencias
status: active
created: "2026-08-22"
updated: "2026-08-22"
---

# Regex-padroes-comuns

#area/referencias #referencias/snippets

Padrões regex prontos para validação e extração. Quando usar: validar campos de formulário, extrair dados de textos/logs, montar massa de teste.

## Validação (formato brasileiro)

```regex
^\d{5}-?\d{3}$                              # CEP (com ou sem hífen)
^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$              # CPF (aceitando pontuação)
^\(?\d{2}\)?\s?9?\d{4}-?\d{4}$              # celular com DDD
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$   # email (básico, não exaustivo)
```

## Extração com grupos

```regex
(\d{2})\/(\d{2})\/(\d{4})                   # data dd/mm/aaaa → grupos 1,2,3
Bearer\s+([A-Za-z0-9\-_\.]+)                # token de header Authorization
\[ERROR\]\s+(.+?)\s+-\s+(.+)$               # "[ERROR] mensagem - detalhe" do log
```

## Úteis no dia a dia

```regex
^\s*$                                       # linha em branco (limpar arquivos)
\d+\.\d+(\.\d+)?                            # versão tipo 1.2 ou 1.2.3
https?:\/\/[^\s"]+                          # URLs em texto livre
```

## Teste antes de usar

- [regex101.com](https://regex101.com) — explica cada token e testa ao vivo.
- Pegadinha clássica: `*` = zero ou mais, `+` = um ou mais. `colou*r` casa "color"; `colou+r` exige o "u".

> Email perfeito não existe em regex — valide também enviando confirmação real.
