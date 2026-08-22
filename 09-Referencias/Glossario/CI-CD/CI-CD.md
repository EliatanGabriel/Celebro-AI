---
type: verbete
area: referencias
status: active
created: "2026-08-22"
updated: "2026-08-22"
---

# CI-CD

#area/referencias #referencias/glossario

**Definição:** prática de automatizar o caminho do código até produção. **CI** (integração contínua): todo push roda build + testes automaticamente, impedindo código quebrado de avançar. **CD** (entrega/deploy contínuo): o pipeline publica sozinho em staging/produção após os testes passarem — entrega a cada merge, ou deploy direto.

**Exemplo:** GitHub Actions que em todo PR instala dependências, roda lint e testes E2E no Playwright; se verde, gera imagem Docker e faz deploy no staging.

**Ver também:** [[Container]] · [[Playwright-locators]] · [[Git-comandos-dia-a-dia]]
