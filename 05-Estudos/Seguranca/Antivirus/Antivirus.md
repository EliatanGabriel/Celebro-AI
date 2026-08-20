---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Antivirus

#area/estudos #estudos/seguranca #conceito

**Resumo:** Software de segurança que detecta, bloqueia e remove malware, usando assinaturas, heurística e comportamento.

## Conceitos-chave
- **Assinaturas (signatures):** padrões conhecidos de malware; banco de dados atualizado continuamente.
- **Heurística:** análise de código suspeito sem assinatura conhecida para detectar variantes novas.
- **Análise comportamental:** monitora ações em tempo real (criptografia em massa, acesso a processos) para flagrar ransomware e trojans.
- **Scan on-access vs. on-demand:** verificação contínua ao acessar arquivos vs. varreduras agendadas.
- **Quarentena:** isola arquivos suspeitos sem deletá-los, permitindo análise posterior.
- **EDR/AV moderno:** evoluiu para Endpoint Detection and Response com resposta automática.

## Exemplos
```bash
# Varredura sob demanda (ClamAV, Linux)
clamscan -r /home/usuario --move=/tmp/quarentena

# Atualização das assinaturas
freshclam
```

## Boas práticas
- Manter assinaturas e engine sempre atualizados.
- Rodar com proteção em tempo real ativa, não apenas scans manuais.
- Usar múltiplas camadas: AV, firewall, patch e EDR.
- Tratar alertas de forma investigativa, não apenas desativando a detecção.

## Armadilhas comuns
- Confiar em falso negativo: nenhum antivírus detecta 100% dos malwares.
- Assumir que o AV protege contra engenharia social ou phishing de credenciais.
- Instalar dois AVs ativos simultaneamente, que podem conflitar e abrir brechas.
- Ignorar arquivos em quarentena, que podem ser legítimos (falsos positivos).

## Relacionadas
- [[Ransomware]]
- [[Patch]]
- [[Ataques]]
- [[Vulnerabilidades]]