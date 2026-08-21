---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Ambiente

#area/trabalho #trabalho/bug-report #conceito

**Resumo:** Contexto de hardware, sistema e configuração onde o bug foi reproduzido.

## Conceitos-chave
- O ambiente é o conjunto de condições em que o bug ocorre: SO, navegador, dispositivo, versão e configuração.
- Bugs dependentes de ambiente só reproduzem sob condições específicas.
- A informação de ambiente permite ao dev reproduzir com a mesma stack e filtrar causas.

## Estrutura de um bom bug report
- **Sistema:** SO e versão (Windows 11, macOS 14, Ubuntu 22.04).
- **Navegador:** Chrome/Safari/Firefox e versão (incluir mobile quando aplicável).
- **Dispositivo:** desktop, notebook, tablet ou modelo de celular.
- **Versão do sistema/testado:** build, branch ou tag do deploy.
- **Configuração:** variáveis, feature flags, idioma, zona horária, dados de rede.

## Boas práticas
- Preencher todos os campos de ambiente mesmo que o bug pareça universal.
- Testar em mais de um navegador/dispositivo antes de reportar, se possível.
- Reproduzir em staging quando o bug também ocorre em produção.
- Descrever configurações não padrão usadas durante o teste.

## Armadilhas comuns
- Omitir a versão do navegador quando o bug é específico de uma versão.
- Reportar bug de produção sem informar o ambiente (produção vs staging).
- Assumir que o ambiente do dev é igual ao do QA.
- Ignorar diferenças de dados entre ambientes que alteram o comportamento.

## Relacionadas
- [[Steps-to-reproduce]]
- [[Evidencias]]
- [[Reproducao]]