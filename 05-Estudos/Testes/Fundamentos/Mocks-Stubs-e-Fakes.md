---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# Mocks, Stubs e Fakes

#area/estudos #estudos/testes #conceito

**Resumo:** Test doubles substituem dependências reais em testes; cada tipo tem um propósito diferente, de fornecer dados a verificar interações.

## Referência rápida

| Double | O que faz | Exemplo |
|---|---|---|
| Dummy | Só preenche parâmetro; nunca é usado | Passar `null`/objeto vazio |
| Stub | Retorna respostas fixas ao chamador | `stubRandom()` sempre devolve 0.5 |
| Spy | Registra chamadas para inspecionar depois | Contar quantas vezes `enviarEmail` rodou |
| Mock | Verifica interações esperadas (falha se não ocorrerem) | `expect(enviar).toHaveBeenCalledWith(...)` |
| Fake | Implementação simples que funciona de verdade | Banco em memória, repositório em array |

## Exemplos

```js
// STUB: resposta fixa para isolar a rede
jest.spyOn(api, "buscarUsuario").mockResolvedValue({ id: 1, nome: "Ana" });

// SPY: registra interação sem mudar comportamento
const spy = jest.spyOn(logger, "info");

// MOCK: define expectativa de interacao
const enviar = jest.fn();
processarPedido(pedido, enviar);
expect(enviar).toHaveBeenCalledTimes(1);

// FAKE: repositorio em memoria que realmente funciona
class RepoFake {
  constructor() { this.itens = []; }
  salvar(item) { this.itens.push(item); return item; }
}
```

## Quando usar cada um

- **Stub**: quando o teste depende do retorno (dados de API, relógio, aleatoriedade).
- **Spy**: quando quer observar efeito colateral sem alterá-lo.
- **Mock**: quando a interação em si é o contrato (ex.: "o e-mail deve ser disparado").
- **Fake**: quando precisa de comportamento real barato, como DB em memória.
- **Dummy**: apenas para satisfazer assinaturas.

## A regra de ouro

- Mocke as **fronteiras** do sistema: rede, relógio, filesystem, DB externo.
- Não mocke o próprio código (classes/módulos internos): isso testa a implementação.

## Boas práticas

- Prefira fakes a mocks quando possível: testes mais realistas.
- Restaura spies/stubs após cada teste (`mockRestore`, `unstub`).
- Dê nomes claros ao double deixando óbvio o que está simulado.

## Armadilhas comuns

- Over-mocking: mockar tudo torna o teste acoplado à implementação.
- Teste verde com mock errado: valida a fantasia, não o sistema.
- Mockar funções puras e lógica própria "por conveniência".
- Esquecer de resetar mocks entre testes e gerar vazamentos.

## Relacionadas

- [[Testes]]
- [[TDD]]
- [[Boas-Praticas-de-Testes]]
- [[Tipos-de-Teste]]
- [[Jest]]
- [[Unittest-Python]]
