---
type: concept
area: faculdade
status: active
created: "2026-08-20"
updated: "2026-08-20"
---

# Segurança da Informação

#area/faculdade #faculdade/disciplinas #conceito

**Resumo:** Segurança da informação: pilares CIA, ameaças e vulnerabilidades, ataques comuns, princípios de proteção e boas práticas.

## 1. O que é segurança da informação

É a proteção de informações contra acesso, uso, divulgação, alteração ou destruição não autorizados.

## 2. Pilares da segurança (CIA)

- **Confidencialidade** — só quem tem permissão acessa.
- **Integridade** — a informação não é alterada indevidamente.
- **Disponibilidade** — o sistema está acessível quando necessário.

```
CONFIDENCIALIDADE
        ↓
    SEGURANÇA
        ↓
  INTEGRIDADE ←→ DISPONIBILIDADE
```

Complementos: **autenticidade** (quem é você) e **não repúdio** (não negar o que fez).

## 3. Ameaça × Vulnerabilidade × Risco

- **Ameaça** — agente que pode causar dano (hacker, malware).
- **Vulnerabilidade** — fraqueza explorável (senha fraca, software desatualizado).
- **Risco** — probabilidade e impacto de a ameaça explorar a vulnerabilidade.

```
Risco = Ameaça × Vulnerabilidade × Impacto
```

## 4. Ataques comuns

- **Phishing** — engana o usuário para roubar dados (e-mails falsos).
- **Malware** — software malicioso (vírus, trojan, ransomware).
- **Ransomware** — sequestra dados e exige resgate.
- **Engenharia social** — manipulação psicológica.
- **SQL Injection** — injeção de comandos maliciosos em bancos de dados.
- **DDoS** — sobrecarga de serviços para tirá-los do ar.
- **Man-in-the-middle** — interceptação da comunicação.
- **Brute force** — tentativa de senha por força bruta.

## 5. Como se proteger

- **Senhas fortes e únicas** + gerenciador de senhas.
- **Autenticação em dois fatores (2FA/MFA)**.
- **Atualizações** regulares de sistema e softwares.
- **Backups** periódicos (regra 3-2-1: 3 cópias, 2 mídias, 1 fora do local).
- **Antivírus/EDR** atualizado.
- **Firewall** e segmentação de rede.
- **Conscientização** — desconfiar de links e anexos.

## 6. Criptografia

- **Simétrica** — mesma chave para cifrar e decifrar (AES).
- **Assimétrica** — par de chaves pública/privada (RSA, ECC).
- **Hash** — função unidirecional para integridade e senhas (SHA-256, bcrypt).

```
Mensagem → [criptografia] → Cifra → [criptografia] → Mensagem
                    chave                 chave
```

## 7. Segurança no desenvolvimento (DevSecOps)

- Validar **entradas** (evitar SQL Injection/XSS).
- Não armazenar senhas em texto puro (use hash + salt).
- Gerenciar **segredos** (chaves de API) fora do código.
- Revisar dependências (análise de vulnerabilidades).
- Testes de segurança no pipeline (SAST, DAST).

## 8. Conceitos de governança

- **LGPD** — Lei Geral de Proteção de Dados (Brasil).
- **PCI-DSS** — segurança de dados de cartões.
- **ISO 27001** — padrão de gestão de segurança da informação.
- **IAM** — gestão de identidades e acessos (princípio do menor privilégio).

## 9. Boas práticas no dia a dia

- Bloquear a tela ao sair da máquina.
- Não usar Wi-Fi público sem VPN.
- Verificar a URL antes de digitar credenciais.
- Separar contas pessoais e profissionais.
- Reportar incidentes rapidamente.

## Tópicos
- 

## Relacionadas

- [[TI]]
- [[Fundamentos de TI]]
- [[Faculdade]]