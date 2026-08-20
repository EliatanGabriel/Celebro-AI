---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Performance

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Capacidade de um sistema executar tarefas com uso eficiente de recursos — principalmente tempo e memória — mantendo resposta aceitável sob carga.

## Conceitos-chave
- **Latência:** tempo entre a requisição e a resposta; importa para percepção do usuário.
- **Vazão (throughput):** quantidade de operações por unidade de tempo; importa para capacidade de processamento.
- **Otimização:** melhoria do uso de recursos; deve ser guiada por medição, não por suposição.
- **Benchmark e profiling:** medir e identificar gargalos (CPU, I/O, memória, rede) antes de alterar código.
- **Complexidade:** escolher algoritmos e estruturas adequados afeta o crescimento do custo com a entrada.
- **Escalabilidade:** capacidade de manter a performance conforme crescem a carga e os dados.
- **Trade-offs:** trocar memória por velocidade (cache, índices) é um padrão comum.

## Exemplos
```text
// Abordagem para otimizar
1. Medir (profiling/benchmark) — identificar o gargalo real
2. Priorizar (impacto × custo de implementação)
3. Alterar um ponto por vez e re-medir
4. Repetir até atingir a meta
```

```python
import time

# Perfil simples: medir antes de otimizar
inicio = time.perf_counter()
resultado = processar_dados(entrada)
print("tempo:", time.perf_counter() - inicio)
```

```text
// Estratégias comuns
- Cache de resultados repetidos (espaço por tempo)
- Índices em banco de dados
- Reduzir trabalho em loops (hoisting de operações invariantes)
- Evitar N+1 queries e chamadas de rede desnecessárias
- Compactar/streaming em vez de carregar tudo em memória
```

## Boas práticas
- Medir sempre: otimizar sem dados leva a esforço desperdiçado e código complexo.
- Otimizar os hot paths (caminhos executados com mais frequência).
- Estabelecer metas de latência e vazão por funcionalidade crítica.
- Revisar a escolha de algoritmos e estruturas antes de micro-otimizações.
- Fazer benchmark próximo do ambiente de produção.

## Armadilhas comuns
- Otimizar prematuramente (Knuth): complexidade desnecessária antes de existir problema real.
- Micro-otimizar código legível sem medir onde está o gargalo.
- Confundir baixa latência com alta vazão; otimizar um pode piorar o outro.
- Benchmarks artificiais que não refletem o uso real (dados pequenos, sem carga).
- Achar que "mais máquinas" resolve problema de algoritmo ineficiente; custo e complexidade aumentam.

## Relacionadas
- [[Memoria]]
- [[Estudos-Complexidade]]
- [[Big-O]]
- [[Algoritmos]]
- [[Hash]]
- [[Games]]
- [[Debug]]
- [[Sistemas]]