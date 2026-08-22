---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# Pytest

#area/estudos #estudos/testes #ferramenta

**Resumo:** Framework de testes para Python com assert nativo, fixtures poderosas, parametrização e enorme ecossistema de plugins.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `test_*.py` | Convenção de arquivo descoberto | `test_carrinho.py` |
| `def test_*` | Função de teste | `def test_soma():` |
| `assert` | Verificação nativa com diff rico | `assert soma(1, 2) == 3` |
| `@pytest.fixture` | Injeção de dependência para testes | `def db(tmp_path): ...` |
| `scope=` | Escopo do fixture (function/class/module/session) | `@pytest.fixture(scope="session")` |
| `@pytest.mark.parametrize` | Mesmo teste com vários dados | `parametrize("n,r", [(2,4),(3,9)])` |
| `@pytest.mark.skip` | Pula o teste | Motivo documentado |
| `@pytest.mark.xfail` | Espera falha conhecida | Bug em aberto |
| `conftest.py` | Fixtures compartilhadas sem import | Por diretório da suíte |
| `-k` | Filtra testes por nome | `pytest -k "frete"` |
| `--maxfail=1` | Para na primeira falha | Loop rápido de correção |

## Exemplos

```python
import pytest
from app.carrinho import Carrinho

@pytest.fixture
def carrinho():
    return Carrinho()

@pytest.fixture(scope="session")
def conexao_db():
    conn = criar_conexao_teste()
    yield conn
    conn.fechar()

@pytest.mark.parametrize("subtotal,frete", [
    (250, 0),
    (100, 25),
])
def test_calculo_frete(carrinho, subtotal, frete):
    carrinho.adicionar(subtotal)
    assert carrinho.frete == frete

@pytest.mark.skip(reason="agora migracao de schema")
def test_import_legado():
    ...
```

```bash
pytest -v                 # verboso, mostra cada teste
pytest -k "frete and not cupom"  # filtra por nome
pytest --maxfail=1 -x     # para na primeira falha
pytest --cov=app          # cobertura via pytest-cov
```

## Boas práticas

- Prefira fixtures a setup manual repetido; use `yield` para cleanup.
- Coloque fixtures comuns no `conftest.py`, não em imports cruzados.
- Escolha escopos pequenos (`function`) por padrão; `session` só p/ caro e imutável.
- Use `parametrize` em vez de loops dentro do teste.

## Armadilhas comuns

- Fixture com escopo session mutando estado entre testes.
- Nomear arquivo sem prefixo `test_`: pytest não descobre.
- `assert` dentro de loop: para na primeira iteração; use parametrize.
- Marcar `xfail` e esquecer de promover quando o bug é corrigido.

## Relacionadas

- [[Testes]]
- [[Unittest-Python]]
- [[BDD]]
- [[Boas-Praticas-de-Testes]]
- [[Cobertura-de-Codigo]]
- [[Mocks-Stubs-e-Fakes]]
