---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Firewall-Seg

#area/estudos #estudos/seguranca #conceito

**Resumo:** Dispositivo ou software que filtra o tráfego de rede com base em regras, definindo o que entra e o que sai entre redes ou hosts.

## Conceitos-chave
- **Filtragem por pacote (stateless):** decide por IP, porta e protocolo, pacote a pacote.
- **Stateful firewall:** mantém estado das conexões (conexões estabelecidas passam; novas são avaliadas).
- **Next-Generation Firewall (NGFW):** inspeção profunda (DPI), controle de aplicação e prevenção de intrusão.
- **Regras deny by default:** política de bloquear tudo e liberar explicitamente.
- **Zonas/segmentação:** separa rede interna, DMZ e internet com políticas distintas.
- **Defesa em profundidade:** firewall é uma camada; complementa IDS/IPS, antivírus e [[Zero-Trust]].

## Exemplos
```bash
# iptables: bloquear tudo e liberar SSH e HTTP
iptables -P INPUT DROP
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

```yaml
# Regra conceitual de NGFW
- nome: permitir-https-entrada
  origem: internet
  destino: web-server
  protocolo: tcp/443
  acao: permitir
```

## Boas práticas
- Configurar por padrão negar e liberar apenas o necessário.
- Revisar e remover regras obsoletas periodicamente.
- Logar tráfego bloqueado para auditoria e detecção de varredura.
- Manter os próprios serviços do firewall atualizados e patchados.
- Segmentar a rede para conter a propagação de ataques laterais.

## Armadilhas comuns
- Regras "allow all" para simplificar — anula a função do firewall.
- Confiar apenas no perímetro e tratar a rede interna como confiável.
- Regras com ordens erradas: firewalls aplicam a primeira regra que casa.
- Negligenciar o tráfego de saída, usado por malware para exfiltração e C2.

## Relacionadas
- [[Firewall]]
- [[Zero-Trust]]
- [[Ataques]]