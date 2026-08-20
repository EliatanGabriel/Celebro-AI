---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Docker

#area/trabalho #trabalho/ferramentas #conceito

**Resumo:** Como o QA usa Docker para criar ambientes de teste isolados, subir dependências e rodar testes de forma reproduzível.

## Conceitos-chave
- **Container:** processo isolado que roda uma aplicação e suas dependências, sem precisar instalar nada no host.
- **Imagem:** modelo imutável que gera containers; o QA normalmente consome imagens prontas, não cria as suas.
- **Dockerfile:** receita que define a imagem; útil para ler e entender o que a aplicação precisa (versão do PHP/Node, extensões, comandos).
- **docker-compose.yml:** define o conjunto de serviços (app, banco, redis, mailpit) com um comando só.
- **Volume:** diretório compartilhado entre host e container, usado para logs, evidências e dados de banco.
- **Bind mount / hot reload:** código montado do host no container, permitindo testar mudanças sem rebuild.

## Exemplos
- Subir o ambiente de testes do projeto:
  `docker compose up -d` e verificar os serviços com `docker compose ps`.
- Rodar um comando dentro do container da aplicação:
  `docker compose exec app php artisan test` ou `docker compose exec app npm run test`.
- Rodar um teste específico do Playwright/Cypress dentro de um container:
  `docker compose run --rm e2e npx playwright test --grep "login"`.
- Limpar ambiente após os testes:
  `docker compose down -v` (remove volumes, resetando bancos de dados).

## Boas práticas
- Sempre conferir as variáveis de ambiente no `.env` e no `docker-compose.yml` antes de começar a testar.
- Usar volumes para persistir evidências e relatórios de teste gerados dentro do container.
- Anotar no relatório a versão da imagem/serviço usada para reproduzir o mesmo ambiente depois.
- Quando houver mismatch de versão de dependência, comparar a imagem local com a de CI/CD.
- Testar o fluxo completo de boot (up, migração, seed) antes de iniciar o ciclo de testes, porque quebra de ambiente confunde o resultado.

## Armadilhas comuns
- Esquecer o `-v` no `docker compose down`: dados de banco persistem e geram falsos resultados.
- Portas conflitantes com outros projetos locais (verificar `ports` no compose).
- Alterar código sem bind mount ativo: o container continua com a versão antiga.
- Confundir `exec` (dentro do container em execução) com `run` (cria um container novo).
- Performance de testes em container no macOS/Windows via Docker Desktop costuma ser mais lenta que no host.

## Relacionadas
- [[Trabalho]]
- [[Deploy]]
- [[Staging]]
- [[Ambiente-Local-Laravel-Vite]]