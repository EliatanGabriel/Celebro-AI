---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Erros e Exceções em Python

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** O bloco `try/except/else/finally` trata falhas previsíveis; capturar exceções específicas, lançar com `raise` e criar exceções próprias mantém o código robusto.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `try:` | Vigia o bloco contra exceções | `try:` |
| `except Tipo as e:` | Captura tipo específico com detalhes | `except ValueError as e:` |
| `except (A, B):` | Captura vários tipos no mesmo bloco | `except (KeyError, IndexError):` |
| `else:` (do try) | Roda somente se nenhuma exceção ocorreu | `else:` |
| `finally:` | Roda sempre; ideal para limpeza | `finally:` |
| `raise Erro("msg")` | Lança uma exceção explicitamente | `raise ValueError("nota inválida")` |
| `class MinhaErro(Exception)` | Cria exceção própria do domínio | `class SaldoInsuficiente(Exception):` |

Exceções comuns: `ValueError` (valor inadequado), `TypeError` (tipo errado), `KeyError` (chave ausente), `IndexError` (índice fora do intervalo), `FileNotFoundError` (arquivo inexistente).

## Exemplos

```python
# Tratamento completo com else e finally
try:
    a = float(input("Numerador: "))
    b = float(input("Denominador: "))
    resultado = a / b
except ValueError as e:
    print(f"Entrada inválida: {e}")
except ZeroDivisionError:
    print("Não é possível dividir por zero")
else:
    print(f"Resultado: {resultado:.2f}")
finally:
    print("Fim da operação")
```

```python
# Exceção própria para regra de negócio
class SaldoInsuficienteError(Exception):
    """Lançada quando o saque excede o saldo disponível."""

def sacar(saldo: float, valor: float) -> float:
    if valor > saldo:
        raise SaldoInsuficienteError(
            f"saldo {saldo:.2f} menor que o saque {valor:.2f}"
        )
    return saldo - valor

try:
    sacar(50.0, 100.0)
except SaldoInsuficienteError as e:
    print("Falhou:", e)
```

## Boas práticas

- Capture a exceção mais específica possível, nunca um `except` nu genérico.
- Mensagens de `raise` devem descrever o problema e o valor esperado.
- Use `with open(...)` ou `finally` para garantir fechamento de recursos.
- Crie exceções próprias quando o domínio tiver erros específicos.
- Registre (`logging`) em vez de engolir silenciosamente a falha.

## Armadilhas comuns

- `except:` sem tipo captura tudo, inclusive `KeyboardInterrupt`.
- Blocos `try` gigantes escondem qual linha realmente falhou.
- `else` deve vir depois de todos os `except` e antes do `finally`.
- Capturar a exceção e continuar como se nada tivesse acontecido propaga estado inválido.
- Confundir `raise MinhaErro("msg")` (lança) com `raise MinhaErro` dentro de `except` (relança).

## Relacionadas

- [[Controle-de-Fluxo]]
- [[Funcoes]]
- [[POO]]
- [[Python]]
