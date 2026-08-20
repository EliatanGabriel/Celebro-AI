---
type: concept
area: estudos
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Complexidade Computacional

#area/estudos #teoria-da-computacao #conceito #teoria #computacao #complexidade

**Resumo:** Estudo de quanto tempo e memória um algoritmo precisa para resolver um problema, classificando problemas por dificuldade intrínseca.

## Conceitos-chave
- **Notação Big-O:** descreve o crescimento assintótico do tempo e da memória em função do tamanho da entrada.
- **Classe P:** problemas solúveis em tempo polinomial por algoritmo determinístico.
- **Classe NP:** problemas cuja solução pode ser verificada em tempo polinomial.
- **NP-completo:** problemas em NP aos quais todo problema em NP pode ser reduzido; resolver um deles em tempo polinomial implicaria P = NP.
- **Redutibilidade:** converter um problema em outro para provar equivalência de dificuldade.
- **Indecidibilidade:** problemas que nenhum algoritmo pode resolver, como o problema da parada.

## Exemplos
```text
Exemplos de classes por problemas conhecidos:
- P: ordenação, busca, caminho mínimo em grafo
- NP: problema do caixeiro viajante, SAT (satisfatibilidade)
- NP-completo: SAT, clique, cobertura de vértices
- Indecidível: problema da parada
```

```python
# Verificação em tempo polinomial (NP): conferir se um vértice cobre as arestas
def verifica_cover(grafo, candidato):
    cobertas = set()
    for u, v in grafo:
        if u in candidato or v in candidato:
            cobertas.add((u, v))
    return cobertas == set(grafo)
```

## Boas práticas
- Distinguir a complexidade do algoritmo (como o problema é resolvido) da complexidade do problema (limite intrínseco).
- Usar reduções para provar NP-dureza de forma estruturada.
- Reconhecer problemas intratáveis e partir para heurísticas ou aproximações.

## Armadilhas comuns
- Confundir o problema P vs NP com "pode ser resolvido na prática": nem todo problema P tem algoritmo rápido.
- Achar que NP significa "não polinomial": a definição é sobre verificação.
- Tratar um caso particular como prova geral de complexidade.
- Confundir crescimento assintótico com desempenho para entradas pequenas.

## Relacionadas
- [[Automatos]]
- [[Linguagens]]
- [[Big-O]]
- [[Estudos-Complexidade]]