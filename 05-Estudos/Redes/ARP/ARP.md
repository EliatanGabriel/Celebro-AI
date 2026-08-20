---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# ARP

#area/estudos #estudos/redes #conceito

**Resumo:** Protocolo da camada de enlace que resolve endereço IP (camada 3) para endereço MAC (camada 2) dentro de uma mesma rede local.

## Conceitos-chave
- **Request (broadcast):** envia "quem tem o IP X?" para toda a LAN.
- **Reply (unicast):** o dono do IP responde diretamente com seu endereço MAC.
- **Cache ARP:** tabela que guarda mapeamentos IP→MAC por alguns minutos para evitar requisições repetidas.
- **Gratuitous ARP:** anúncio espontâneo do próprio MAC, usado em failover e detecção de conflito de IP.
- **Proxy ARP:** um roteador responde em nome de hosts de outra rede, mascarando o encaminhamento.
- **Limitação:** opera apenas dentro de um domínio de broadcast (L2); não atravessa roteadores.

## Exemplos
```text
Host A (10.0.0.1) quer falar com 10.0.0.2
1. A consulta o cache ARP -> não encontrou
2. A envia ARP request broadcast: "Quem tem 10.0.0.2?"
3. B responde unicast com seu MAC (AA:BB:CC:00:00:02)
4. A grava no cache e monta o frame Ethernet
```

```bash
# Consultar a tabela ARP do host
arp -a
ip neigh show
# Remover uma entrada para forçar nova resolução
ip neigh del 10.0.0.2 dev eth0
```

## Boas práticas
- Manter o cache ARP saudável para reduzir broadcasts na LAN.
- Usar gratuitous ARP em configurações de failover (IP flutuante).
- Utilizar entradas ARP estáticas apenas em segmentos críticos e pequenos.
- Em redes de acesso, considere ARP inspection no switch para mitigar spoofing.

## Armadilhas comuns
- ARP é stateless e sem autenticação: vulnerável a ARP spoofing/poisoning (mitm).
- Confundir ARP com DNS: ARP resolve L3→L2, DNS resolve nomes→IP.
- Esquecer que ARP não atravessa roteadores — cada enlace resolve seu próprio mapeamento.
- Assumir que resposta ARP rápida significa host ativo; o host pode estar fora, mas com cache válido.

## Relacionadas
- [[IP]]
- [[Switching]]
- [[OSI]]
- [[Ethernet]]