---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Selenium

#area/trabalho #trabalho/testes-automatizados #conceito

**Resumo:** Framework clássico de automação de navegador via WebDriver.

## Conceitos-chave
- Framework clássico de automação de navegador via protocolo WebDriver.
- Suporta múltiplas linguagens: Java, Python, JavaScript, C#, Ruby.
- Selenium Grid distribui testes em vários navegadores/máquinas.
- WebDriver controla o navegador real em modo headed ou headless.
- Base para E2E legados e integração com ferramentas de CI.

## Exemplos
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://exemplo.com")
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "resultado"))
)
driver.quit()
```

## Boas práticas
- Usar esperas explícitas (WebDriverWait) em vez de sleeps fixos.
- Selecionar elementos por atributos estáveis (data-testid, name).
- Gerenciar drivers com WebDriverManager para evitar erros de versão.
- Rodar headless em CI e de forma paralela com Grid.
- Organizar com Page Objects para reduzir duplicação de seletores.

## Armadilhas comuns
- Flakiness por waits fixos ou sincronização com a página.
- Seletores frágeis que quebram com qualquer mudança de layout.
- Necessidade de manter servidor/processo WebDriver compatível.
- Execução lenta em comparação com frameworks modernos.
- Manter suítes legadas sem refatorar para padrões atuais.

## Relacionadas
- [[Playwright]]
- [[Cypress]]
- [[E2E]]
- [[Test-frameworks]]