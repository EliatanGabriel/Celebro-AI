---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Performance-review

#area/trabalho #trabalho/code-review #conceito

**Resumo:** Revisão focada em eficiência e uso de recursos do código.

## Conceitos-chave
- Avalia complexidade de algoritmos e impacto em escala.
- Identifica consultas N+1 e loops desnecessários.
- Verifica uso de cache para operações repetidas.
- Examina consumo de memória, I/O e concorrência.
- Usa benchmarks e métricas para comparar alternativas.

## Exemplos
```
// N+1: consulta por item dentro de um loop
const pedidos = await Pedido.find();
for (const p of pedidos) {
  await p.cliente; // dispara 1 query por pedido
}

// Correto: busca única com join/aggregate
const pedidos = await Pedido.find().populate('cliente');
```

## Boas práticas
- Medir antes de otimizar: usar profiler e métricas reais.
- Focar em gargalos reais, não em micro-otimizações.
- Verificar índice de banco e queries em review de integração.
- Aplicar cache em operações caras e estáveis.
- Testar o cenário sob carga antes de aprovar mudanças críticas.

## Armadilhas comuns
- Otimizar sem evidência, complicando o código à toa.
- Ignorar N+1 em camadas de acesso a dados.
- Cache com chave ou invalidação incorreta, servindo dados velhos.
- Preocupação só com CPU, esquecendo memória e I/O.
- Aprovar mudanças de performance sem benchmark.

## Relacionadas
- [[Refatoracao]]
- [[Monitoramento]]