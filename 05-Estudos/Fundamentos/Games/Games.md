---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Games

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Desenvolvimento de jogos digitais, combinando lógica de programação, gráficos, física, som e interação em tempo real.

## Conceitos-chave
- **Game loop:** o ciclo contínuo que atualiza a lógica (update) e desenha a cena (render) dezenas de vezes por segundo.
- **Game engine:** conjunto de ferramentas (Unity, Unreal, Godot) que abstrai renderização, física, áudio e entrada.
- **Sprites e assets:** imagens, sons e modelos que compõem o conteúdo visual do jogo.
- **Física:** simulação de movimento, colisão e gravidade; engines usam motores de física (ex.: Box2D, PhysX).
- **IA de jogo:** comportamentos de personagens não controlados, como pathfinding (A*, BFS) e máquinas de estado.
- **Delta time:** intervalo entre frames, usado para manter o movimento consistente independentemente da taxa de frames.
- **Multijogador:** sincronização de estado entre clientes via rede, com preocupações de latência e autoridade do servidor.

## Exemplos
```text
// Game loop simples (pseudocódigo)
enquanto jogo_rodando:
    delta = tempo_desde_ultimo_frame()   // tempo em segundos
    processar_input()
    atualizar(delta)                     // mover personagem: posicao += velocidade * delta
    renderizar()
```

```javascript
// Movimento independente da taxa de frames
function update(delta) {
    jogador.x += jogador.velocidadeX * delta;  // mesmo deslocamento em qualquer FPS
    jogador.y += jogador.velocidadeY * delta;
}

// Verificação simples de colisão entre retângulos (AABB)
function colide(a, b) {
    return a.x < b.x + b.largura &&
           a.x + a.largura > b.x &&
           a.y < b.y + b.altura &&
           a.y + a.altura > b.y;
}
```

## Boas práticas
- Começar com protótipos pequenos antes de investir em mecânicas complexas.
- Separar lógica de negócio da renderização para facilitar testes e manutenção.
- Usar delta time em todo movimento baseado em tempo.
- Criar um estado de jogo centralizado (menu, jogando, pausado, game over) em vez de condições espalhadas.
- Otimizar o loop de renderização: desenhar apenas o que está visível.

## Armadilhas comuns
- Ignorar delta time e ter movimento mais rápido em monitores de alta taxa de frames.
- Verificar colisões por pixel em vez de usar colisores simples, custando performance.
- Acoplar lógica ao frame em vez do tempo (simulações não determinísticas).
- Confundir coordenadas de tela com coordenadas do mundo do jogo.
- Otimizar prematuramente sem medir onde está o gargalo (profile antes).

## Relacionadas
- [[Performance]]
- [[Algoritmos]]
- [[Logica]]
- [[Programacao]]
- [[Grafos]]
- [[Estruturas-de-Dados]]