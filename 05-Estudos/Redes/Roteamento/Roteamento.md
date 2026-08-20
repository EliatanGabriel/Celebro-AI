---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Roteamento

#area/estudos #estudos/redes #conceito

**Resumo:** Processo de selecionar caminhos para encaminhar pacotes entre redes, executado por roteadores com base em tabelas de rotas e protocolos de roteamento.

## Conceitos-chave
- **Tabela de rotas:** mapa de prefixos de rede → próxima interface / next hop.
- **Estático vs dinâmico:** manual (redes pequenas) vs protocolos (redes grandes e mutáveis).
- **Protocolos:** OSPF (link-state, intra-AS), BGP (path-vector, entre ASs), RIP (distância-vetor).
- **Métricas:** custo, hop count, banda e latência determinam o melhor caminho.
- **Longest prefix match:** a rota mais específica tem prioridade na escolha.
- **TTL:** decrementado a cada hop para evitar loops infinitos.

## Exemplos
```bash
# Exibir a tabela de rotas
ip route show
# Exemplo de saída
default via 192.168.1.1 dev eth0
10.0.0.0/24 via 192.168.1.254 dev eth0
```

```text
Decisão de roteamento
Pacote para 10.0.0.5
10.0.0.0/24 é mais específica que 0.0.0.0/0 (default)
=> encaminha via 192.168.1.254
```

## Boas práticas
- Usar roteamento dinâmico com redundância em redes que mudam com frequência.
- Documentar e revisar rotas estáticas para evitar divergências.
- Agregar prefixos (summarization) para reduzir o tamanho das tabelas.
- Planejar a convergência: o protocolo precisa recalcular rotas rápido após falha.

## Armadilhas comuns
- Rotas default apontando para o destino errado derruba a conectividade inteira.
- Loop de roteamento causado por rotas inconsistentes entre vizinhos.
- Conflito entre rota estática e dinâmica com métricas confusas.
- Esquecer que o longest prefix match vence, mesmo sobre uma rota "menor custo".

## Relacionadas
- [[IP]]
- [[Switching]]
- [[OSI]]
- [[TCP-IP]]
- [[Dispositivos]]