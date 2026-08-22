---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# Unittest (Python)

#area/estudos #estudos/testes #ferramenta

**Resumo:** Framework de testes da biblioteca padrão do Python, no estilo xUnit, com classes TestCase, fixtures de ciclo de vida e módulo mock embutido.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `class TestX(TestCase)` | Classe que agrupa testes | Métodos começando com `test_` |
| `setUp` | Roda antes de cada teste | Criar objeto sob teste |
| `setUpClass` | Uma vez por classe (`@classmethod`) | Conexão compartilhada |
| `tearDown` | Limpeza após cada teste | Fechar arquivo |
| `assertEqual` | Igualdade | `self.assertEqual(soma, 3)` |
| `assertTrue` / `assertFalse` | Booleanos | `self.assertTrue(valido)` |
| `assertRaises` | Contexto de exceção | `with self.assertRaises(ValueError):` |
| `MagicMock` | Mock com atributos/métodos automáticos | `mock = MagicMock()` |
| `patch` | Substitui alvo durante o teste | Decorator ou context manager |
| `python -m unittest` | Runner via stdlib | `python -m unittest discover` |

## Exemplos

```python
import unittest
from unittest.mock import MagicMock, patch

from app.servico import ServicoEmail

class TestServicoEmail(unittest.TestCase):
    def setUp(self):
        self.cliente = MagicMock()
        self.servico = ServicoEmail(self.cliente)

    def test_envia_com_destinatario(self):
        self.servico.enviar("ana@test.com", "Olá")
        self.cliente.send.assert_called_once()

    @patch("app.servico.agora")
    def test_nao_envia_fora_do_horario(self, mock_agora):
        mock_agora.return_value = hora_madrugada()
        with self.assertRaises(HorarioInvalido):
            self.servico.enviar("ana@test.com", "Oi")
```

```bash
python -m unittest                    # roda a suite atual
python -m unittest discover           # descobre tests/ automaticamente
python -m unittest -v app.test_servico  # verboso e especifico
```

## Boas práticas

- Use `patch` como decorator para alvos fixos e context manager para pontuais.
- Prefira `assert_called_once` a checagens manuais em `call_count`.
- Mantenha um TestCase por unidade testada; nomes claros nos métodos.
- Em projetos novos, avalie [[Pytest]]: roda testes unittest e adiciona fixtures.

## Armadilhas comuns

- Patchear onde o nome é usado, não onde é definido.
- Esquecer `if __name__ == "__main__": unittest.main()` ao rodar direto.
- Depender de ordem alfabética dos métodos `test_a`, `test_b`.
- Não resetar mocks entre testes quando reutilizados em nível de classe.

## Relacionadas

- [[Testes]]
- [[Pytest]]
- [[JUnit]]
- [[Mocks-Stubs-e-Fakes]]
- [[Boas-Praticas-de-Testes]]
