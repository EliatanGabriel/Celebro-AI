---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Portas

#area/estudos #estudos/redes #conceito

**Resumo:** Identificadores numéricos (0-65535) que multiplexam conexões dentro de um host, direcionando o tráfego ao processo ou aplicação correta sobre TCP ou UDP.

## Conceitos-chave
- **Faixas:** 0-1023 well-known (exigem privilégio), 1024-49151 registradas, 49152-65535 efêmeras/dinâmicas.
- **Socket:** combinação de endereço IP + porta (ex.: 192.168.1.10:443).
- **Multiplexação:** permite que vários serviços coexistam no mesmo host.
- **Portas comuns:** 22 SSH, 53 DNS, 80 HTTP, 443 HTTPS, 3306 MySQL, 5432 PostgreSQL, 6379 Redis.
- **ICMP não usa portas:** identifica mensagens por type/code.
- **Escuta vs efêmera:** a porta de escuta recebe conexões; as portas efêmeras são usadas pelo cliente nas conexões de saída.

## Exemplos
```text
Portas well-known
20/21 FTP   22 SSH   25 SMTP   53 DNS   80 HTTP
443 HTTPS   3306 MySQL  5432 PostgreSQL  6379 Redis  8080 HTTP alternativo
```

```bash
# Portas em escuta e processos associados
ss -tulnp
# Testar abertura de porta em um host remoto
nmap -p 80,443 8.8.8.8
```

## Boas práticas
- Fechar portas não utilizadas e liberar apenas o necessário no firewall.
- Monitorar portas em escuta e novos serviços não autorizados.
- Preferir nomes/serviços a portas na documentação para facilitar auditoria.
- Ao expor serviços, usar TLS e autenticação mesmo em portas não padrão.

## Armadilhas comuns
- Achar que mudar a porta padrão (ex.: SSH 2222) é segurança de verdade: scanners cobrem toda a faixa.
- Esquecer que a mesma porta pode existir separadamente em TCP e UDP.
- Confundir a porta de escuta do servidor com a porta efêmera do cliente.
- Bloquear a porta errada no firewall e deixar o serviço aparentemente "fora do ar".

## Relacionadas
- [[TCP]]
- [[UDP]]
- [[Protocolos]]
- [[Firewall]]
- [[Sockets]]