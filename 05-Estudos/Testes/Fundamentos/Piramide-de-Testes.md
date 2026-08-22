---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-22"
updated: "2026-08-22"
---

# Pirâmide de Testes

#area/estudos #estudos/testes #conceito

**Resumo:** Modelo que distribui testes em camadas: muitos unitários na base, integração no meio e poucos E2E lentos no topo.

## Referência rápida

| Camada | Quantidade | Feedback | Realismo |
|---|---|---|---|
| Unitários (base) | Muitos | Instantâneo (ms) | Baixo |
| Integração/serviço (meio) | Moderados | Rápido (s) | Médio |
| E2E (topo) | Poucos | Lento (min) | Alto |

## Exemplos

```text
      /  E2E  \        poucos, lentos, realistas
     /---------\
    / Integracao \     moderados, equilibrio
   /--------------\
  /  Unitarios     \  muitos, rapidos, baratos
 /------------------\
```

```js
// Base: centenas de unitários rápidos
expect(calcularFrete(peso)).toBe(25);

// Meio: dezenas de testes de integração com DB em memória ou container
const pedido = await criarPedido(dados);
expect(pedido.status).toBe("confirmado");

// Topo: meia dúzia de E2E cobrindo os fluxos críticos
await page.goto("/checkout");
await expect(page.getByText("Pedido confirmado")).toBeVisible();
```

## Por quê a pirâmide

- Unitários dão feedback rápido: falham em segundos e apontam a linha exata.
- E2E dão realismo, mas são lentos, caros e instáveis; use só para fluxos críticos.
- O meio (integração) é o melhor custo-benefício entre rapidez e realismo.

## Anti-padrão: casquinha de sorvete

- Suíte invertida: quase tudo E2E, quase nada unitário.
- Sintomas: CI lento, flakes frequentes, medo de refatorar.
- Causa típica: equipe sem hábito de testar unidades isoladamente.

## Testing Trophy (Kent C. Dodds)

- Variação moderna: peso maior em testes de integração do que a pirâmide clássica.
- Ideia: mockar pouco e testar módulos reais juntos pega mais bugs úteis.
- Unitários continuam valendo para lógica pura e casos extremos.

## Boas práticas

- Comece pela base; adicione E2E apenas para jornadas essenciais.
- Revise a distribuição da suíte periodicamente no CI.
- Prefira integração quando o valor está na colaboração entre módulos.

## Armadilhas comuns

- Achar que "mais testes" significa sempre "mais E2E".
- Copiar a forma da pirâmide sem entender o trade-off velocidade x realismo.
- Deixar o meio vazio: nem puro unitário, nem E2E, sem integração.
- Ignorar flakes: um E2E instável mina a confiança em toda a suíte.

## Relacionadas

- [[Testes]]
- [[Tipos-de-Teste]]
- [[Boas-Praticas-de-Testes]]
- [[Mocks-Stubs-e-Fakes]]
- [[Testing-Library]]
