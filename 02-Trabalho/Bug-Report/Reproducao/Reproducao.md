---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Reproducao

#area/trabalho #trabalho/bug-report #conceito

**Resumo:** Conjunto de passos capazes de gerar o bug de forma consistente.

## Conceitos-chave
- Reprodução é a capacidade de refazer o bug de forma previsível em um dado ambiente.
- É o pré-requisito para investigação, correção e verificação do bug.
- Pode ser determinística (sempre ocorre) ou intermitente (ocorre em algumas tentativas).

## Estrutura de um bom bug report
- Passos numerados e objetivos, com dados de entrada específicos (usuário, valores, ações).
- Condições iniciais do sistema: sessão, estado de dados, permissões.
- Indicação da frequência: sempre, às vezes, raramente.
- Resultado observado em cada passo, para localizar onde o fluxo quebra.

## Boas práticas
- Reduzir ao caso mínimo antes de reportar (menos passos, menos dados).
- Testar a reprodução mais de uma vez para confirmar a consistência.
- Registrar o caminho exato, inclusive ações intermediárias (cliques, scroll, refresh).
- Quando intermitente, anotar padrões (horário, volume de dados, rede).

## Armadilhas comuns
- Passos vagos ("faça algo e dê erro") que não permitem reproduzir.
- Depender de dados que o dev não tem acesso sem informar.
- Confundir "bug não reproduzido" com "bug inexistente".
- Descartar detalhes "irrelevantes" que são justamente a causa do bug.

## Relacionadas
- [[Steps-to-reproduce]]
- [[Ambiente]]
- [[Evidencias]]