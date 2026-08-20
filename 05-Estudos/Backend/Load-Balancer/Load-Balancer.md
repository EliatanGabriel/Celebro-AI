---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Load-Balancer

#area/estudos #estudos/backend #conceito

**Resumo:** Dispositivo ou serviço que distribui o tráfego recebido entre múltiplos servidores, garantindo disponibilidade, escalabilidade e uso eficiente da capacidade.

## Conceitos-chave
- **Função:** recebe requisições e encaminha para servidores de um pool, escolhendo o destino por um algoritmo.
- **Algoritmos:** round-robin (rotativo), least connections (menos conexões ativas), IP hash (mesmo cliente, mesmo servidor) e weighted (pesos).
- **Health checks:** sondas periódicas removem servidores com falha do pool automaticamente.
- **Failover:** se um servidor cai, o tráfego é redirecionado aos saudáveis, mantendo o serviço no ar.
- **Níveis:** L4 (TCP/UDP, IP e porta) e L7 (HTTP, com rotas, headers e SSL termination).
- **Sticky sessions:** em apps com sessões em memória, fixa o cliente a um servidor; melhor é usar estado externo (Redis).
- **Diferenças-chave:** um proxy também encaminha tráfego; o load balancer se especializa em distribuir e manter alta disponibilidade.

## Exemplos
```nginx
# Nginx como load balancer L7 (round-robin)
http {
  upstream app_servers {
    server 10.0.0.1:3000;
    server 10.0.0.2:3000;
    server 10.0.0.3:3000 backup;
  }

  server {
    listen 80;
    location / {
      proxy_pass http://app_servers;
    }
  }
}
```

```bash
# Kubernetes: Service do tipo LoadBalancer
kubectl expose deployment app --type=LoadBalancer --port=80 --target-port=3000
```

## Boas práticas
- Configurar health checks além de checks TCP (verificar endpoint real da aplicação).
- Usar stateful storage externo (Redis/banco) para não depender de sticky sessions.
- Dimensionar com base em métricas e testes de carga, não em suposição.
- Monitorar o pool e o próprio load balancer (ponto único de falha → usar HA/replicas).
- Terminar TLS no load balancer e encaminhar tráfego interno em rede privada.

## Armadilhas comuns
- Depender de sticky sessions para escalar: ao perder servidor, usuário perde a sessão.
- Não checar health de verdade, distribuindo para servidores mortos.
- Subdimensionar o próprio LB, criando novo gargalo/ponto único de falha.
- Confundir failover automático com recuperação de dados (estado externo é responsabilidade da aplicação).
- Ignorar o custo de conexões longas (WebSocket) que prendem workers de um servidor.

## Relacionadas
- [[Proxy]]
- [[Nginx]]
- [[Caching]]
- [[Kubernetes]]
- [[Microservicos]]