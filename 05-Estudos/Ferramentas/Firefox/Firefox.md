---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Firefox

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Navegador open-source da Mozilla focado em privacidade e padrões web; traz DevTools próprios, proteção contra rastreamento e extensões baseadas em WebExtensions.

## Conceitos-chave
- **Gecko + SpiderMonkey**: engine de renderização (Gecko) e motor de JavaScript (SpiderMonkey, com JIT Ion).
- **Enhanced Tracking Protection**: bloqueio de rastreadores de terceiros, cookies cross-site e fingerprinting por padrão.
- **DevTools**: suite integrada com Firebug histórico; painéis para CSS, layout (Flexbox/Grid), network, performance e memory.
- **WebExtensions**: API de extensões compatível com Chrome (Manifest), com diferenças menores de permissões e APIs.
- **Firefox Developer Edition**: build com DevTools avançadas e perfis separados para desenvolvimento.
- **Privacidade**: ferramentas como Containers e gerenciamento rígido de cookies; bloqueadores integrados.

## Exemplos
Rodar testes automatizados com Selenium WebDriver:

```js
const { Builder } = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');

(async () => {
  const driver = await new Builder().forBrowser('firefox').build();
  await driver.get('https://exemplo.com');
  console.log(await driver.getTitle());
  await driver.quit();
})();
```

Inspecionar layout com DevTools via linha de comando:

```bash
# Headless mode do Firefox
firefox --headless --screenshot /tmp/page.png https://exemplo.com
```

## Boas práticas
- Use Containers para isolar sessões (ex.: múltiplas contas) sem logins conflitantes.
- Teste a compatibilidade com Chrome também, mas aproveite os relatórios de privacidade do Firefox.
- Aproveite o painel de Flexbox/Grid inspector para depurar layouts CSS complexos.
- Mantenha extensões mínimas e de fontes confiáveis; permissões amplas são um risco.
- Use perfis separados para dev e uso pessoal.

## Armadilhas comuns
- Diferenças de comportamento entre Gecko e Blink exigem testes em ambos os navegadores.
- Extensões V3 podem ter comportamentos distintos do Chrome; valide as permissões declaradas.
- Enhanced Tracking Protection pode quebrar logins de terceiros (ex.: SSO) — use o modo de exceção do site.
- Esquecer que o cache de DevTools é separado do cache normal da página ao medir performance.
- Headless do Firefox tem flags e capacidades diferentes do Chrome; leia a documentação ao automatizar.

## Relacionadas
- [[Chrome]]
- [[Browsers-DevTools]]