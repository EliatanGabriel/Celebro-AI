---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# Tipos de Teste

#area/estudos #estudos/testes #conceito

**Resumo:** Cada tipo de teste cobre um nível diferente do sistema, variando em escopo, velocidade e custo de manutenção.

## Referência rápida

| Tipo | Escopo | Velocidade | Custo |
|---|---|---|---|
| Unitário | Função/classe isolada (mockando dependências) | Muito rápido (ms) | Baixo |
| Integração | Módulos juntos, com DB/API real ou fake | Médio | Médio |
| E2E | Fluxo completo no browser, como o usuário | Lento (s) | Alto |
| Aceitação | Valida requisito de negócio ponta a ponta | Lento | Alto |
| Regressão | Suíte que garante que nada quebrou | Variável | Variável |
| Fumaça | Camada mínima de sanidade após cada deploy | Muito rápido | Baixo |
| Carga/Performance | Comportamento sob volume/concorrência | Muito lento | Alto |

## Exemplos

```js
// Unitário: valida uma função pura de desconto
function aplicarDesconto(valor, percentual) {
  return valor - valor * (percentual / 100);
}
expect(aplicarDesconto(100, 10)).toBe(90);

// Integração: serviço + repositório com banco de teste real
const salvo = await repo.salvar({ nome: "Ana" });
const encontrado = await repo.buscarPorId(salvo.id);
expect(encontrado.nome).toBe("Ana");
```

```js
// E2E: fluxo completo no browser
await page.goto("/login");
await page.getByLabel("E-mail").fill("ana@test.com");
await page.getByRole("button", { name: "Entrar" }).click();
await expect(page.getByText("Bem-vinda")).toBeVisible();
```

## Boas práticas

- Combine níveis seguindo a [[Piramide-de-Testes]]: muitos unitários, poucos E2E.
- Use testes de fumaça como gate rápido antes de testar mais a fundo.
- Rode regressão completa em CI; fumaça a cada deploy.
- Prefira integração para lógica com DB/API: pega bugs que unitários não veem.
- Trate carga/performance como etapa separada, não em todo commit.

## Armadilhas comuns

- Apostar tudo em E2E: lentos, frágeis e caros de manter.
- Chamar de "unitário" um teste que toca banco ou rede de verdade.
- Ignorar testes de regressão até o primeiro bug em produção.
- Confundir aceitação (requisito de negócio) com E2E técnico.
- Medir cobertura só com unitários e ignorar caminhos de integração.

## Relacionadas

- [[Testes]]
- [[Piramide-de-Testes]]
- [[Boas-Praticas-de-Testes]]
- [[Mocks-Stubs-e-Fakes]]
- [[Cobertura-de-Codigo]]
