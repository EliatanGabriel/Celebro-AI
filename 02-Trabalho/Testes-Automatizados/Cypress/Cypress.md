---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Cypress

#area/trabalho #trabalho/testes-automatizados #conceito

**Resumo:** Framework de testes E2E moderno para aplicações web.

## Conceitos-chave
- Framework de testes E2E para web, em JavaScript/TypeScript, que executa no navegador real.
- Comandos encadeáveis: cy.visit, cy.get, cy.click, cy.type, com auto-retry até o elemento estar pronto.
- Asserções (expect/should) com retry automático, reduzindo flakiness.
- Interceptação de rede com cy.intercept para simular e validar requisições.
- Runner interativo com time travel, fixtures via cy.fixture e gravação de vídeo/screenshot.

## Exemplos
```
describe('Login', () => {
  beforeEach(() => {
    cy.visit('/login');
  });

  it('realiza login com credenciais válidas', () => {
    cy.get('[data-testid="email"]').type('qa@exemplo.com');
    cy.get('[data-testid="senha"]').type('123456');
    cy.get('[data-testid="entrar"]').click();
    cy.url().should('include', '/dashboard');
    cy.get('[data-testid="boas-vindas"]').should('contain', 'Olá');
  });
});
```

## Boas práticas
- Usar data-testid estável em vez de seletores CSS frágeis.
- Testar fluxos reais do usuário, sem pular etapas desnecessariamente com cy.request.
- Isolar dados com cy.intercept e cy.fixture.
- Manter um cenário por teste (it), independente e repetível.
- Rodar a suíte em ambiente controlado (staging) e integrar ao pipeline de CI.

## Armadilhas comuns
- Encadear comandos como promessas e usar then de forma síncrona.
- Testes flaky por seletor instável ou dependência da ordem de execução.
- cy.intercept com padrão de URL que não casa com a rota real.
- Depender de dados externos vivos (bancos de produção).
- Executar em produção e gerar dados de teste poluentes.

## Relacionadas
- [[Playwright]]
- [[E2E]]
- [[Test-frameworks]]
- [[Testes-Automatizados]]