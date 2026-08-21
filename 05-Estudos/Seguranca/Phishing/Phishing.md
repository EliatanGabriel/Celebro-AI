---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Phishing

#area/estudos #estudos/seguranca #conceito

**Resumo:** Golpe de engenharia social que engana usuários por e-mail, SMS ou sites falsos para roubar credenciais, dados ou instalar malware.

## Conceitos-chave
- **Mecanismo:** mensagem que imita fonte legítima (banco, empresa, gov) com urgência para gerar ação.
- **Links e anexos falsos:** redirecionam para páginas clone ou instalam malware.
- **Variações:** spear phishing (alvo específico), whaling (executivos), smishing (SMS) e vishing (telefone).
- **Página clone:** site idêntico ao original para capturar login em tempo real (evilginx, reverse proxy).
- **Porta de entrada:** phishing costuma ser o primeiro passo de ransomware e Business Email Compromise.
- **Indicadores:** remetente parecido, URLs ofuscadas, anexos inesperados, pressão de tempo, erros de grafia.

## Exemplos
```
# E-mail típico de phishing
De: suporte@banco-seguro.info
Assunto: Acesso suspeito detectado — aja agora
Corpo: "Sua conta será bloqueada. Confirme em https://banco-seguro.info/verificar
        com seu usuário e senha em 24h."

# URL ofuscada
http://www.banco.com.br.seguranca-verificar.info/login
```

## Boas práticas
- Verificar remetente, domínio real e URL antes de clicar (passar o mouse sobre o link).
- Nunca informar credenciais por link de e-mail; acessar o site digitando o endereço.
- Habilitar [[MFA]] para mitigar o impacto de credenciais roubadas.
- Treinar com simulações regulares e reportar suspeitas sem punição.
- Usar filtros antispam, DMARC/SPF/DKIM e sandbox de anexos.

## Armadilhas comuns
- Confiar na aparência: logos e e-mails são fáceis de falsificar.
- Julgar phishing só por grafia — campanhas profissionais são quase perfeitas.
- Achar que "eu nunca cairia": sob urgência, qualquer pessoa pode cair.
- Tratar phishing como problema só de e-mail, ignorando SMS, redes sociais e telefone.

## Relacionadas
- [[Ataques]]
- [[Ransomware]]
- [[Engenharia-Social]]
- [[Credenciais]]
- [[MFA]]