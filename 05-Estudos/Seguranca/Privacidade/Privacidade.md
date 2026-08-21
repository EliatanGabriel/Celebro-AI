---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Privacidade

#area/estudos #estudos/seguranca #conceito

**Resumo:** Direito do indivíduo de controlar seus dados pessoais — como são coletados, usados, compartilhados e protegidos contra exposição não autorizada.

## Conceitos-chave
- **Dados pessoais vs. anônimos:** dado que identifica ou identifica uma pessoa está em escopo; anonimização bem-feita sai do escopo.
- **Consentimento e finalidade:** coletar com transparência, para finalidade declarada e pelo tempo necessário.
- **Minimização:** coletar apenas o indispensável à finalidade.
- **Anonimato e pseudonimização:** pseudonimização reduz risco mas continua sendo dado pessoal.
- **Rastreamento:** cookies, fingerprinting e trackers exigem consentimento explícito (GDPR/ePrivacy).
- **Privacy by design:** a proteção é embutida na arquitetura, não adicionada depois.

## Exemplos
```text
# Princípios práticos de privacidade
- Coletar o mínimo necessário.
- Criptografar dados pessoais em repouso e em trânsito.
- Definir retenção e descarte seguro.
- Fornecer acesso, correção e exclusão ao titular.
- Auditar quem acessou e por quê.
```

## Boas práticas
- Documentar o mapeamento de dados e as bases legais de cada processamento (ver [[GDPR]]).
- Usar pseudonimização/anonimização em análises e testes.
- Configurar privacidade máxima por padrão em produtos.
- Aplicar controle de acesso e logs a dados pessoais.
- Revisar fornecedores e transferências internacionais de dados.

## Armadilhas comuns
- Confundir privacidade com segurança: segurança protege dados; privacidade regula seu uso.
- Achar que dado anonimizado por "remoção de nome" está fora do escopo — reidentificação é possível.
- Pedir consentimento genérico demais ou impor "aceite ou saia" sem opção real.
- Reter dados indefinidamente "por segurança", violando minimização e retenção.

## Relacionadas
- [[GDPR]]
- [[Firewall]]
- [[Dados]]
- [[Biometria]]
- [[Zero-Trust]]