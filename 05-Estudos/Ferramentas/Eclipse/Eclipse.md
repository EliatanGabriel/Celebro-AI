---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Eclipse

#area/estudos #estudos/ferramentas #conceito

**Resumo:** IDE open-source clássica baseada em plugins (arquitetura Equinox/OSGi), historicamente referência para Java e ainda usada em C/C++, PHP e modelagem; gerencia projetos em workspaces.

## Conceitos-chave
- **Eclipse IDE**: suíte construída sobre o Eclipse Platform; versões "packages" pré-configuradas para cada linguagem.
- **Workspace**: diretório que guarda preferências e metadados; projetos podem viver fora dele via importação.
- **Perspectives**: conjuntos de views (Java, Debug, Git) organizados para cada tarefa.
- **JDT (Java Development Tools)**: compilação incremental, autocompletar, refatorações e debug via JDB.
- **Plugins/PDE**: o próprio Eclipse é extensível; há mercado de plugins (Eclipse Marketplace) e suporte a OSGi/RCP.
- **Builds**: o builder incremental compila automaticamente conforme alterações; o Maven é integrado via m2e.

## Exemplos
Importar e compilar um projeto Maven:

```bash
# Cli opcional (eclipsec)
eclipsec -nosplash -application org.eclipse.jdt.core.javabuilder \
  -data /tmp/workspace -import /caminho/do/projeto
```

Configuração de formato/formatador via `.settings/org.eclipse.jdt.core.prefs`:

```properties
org.eclipse.jdt.core.compiler.problem.unusedLocal=warning
org.eclipse.jdt.core.compiler.problem.fallthroughCase=error
```

Rodar testes JUnit com atalhos:

```text
Alt+Shift+X, T   # executar teste JUnit selecionado
F11              # iniciar debug no arquivo ativo
```

## Boas práticas
- Use workspaces diferentes por projeto/versão para evitar conflitos de preferências.
- Aproveite o "Refactor > Rename" que atualiza referências em todo o workspace de forma segura.
- Prefira o gerenciamento de dependências via Maven/Gradle (m2e) em vez de classpath manual.
- Configure save actions (formatação e organização de imports ao salvar) para padronizar o código.
- Em projetos legados, use o Debug com breakpoints e Hot Code Replace para iterar sem restart.

## Armadilhas comuns
- Workspace corrompido após crash: as pastas `.metadata` são sensíveis; faça backup antes de grandes migrações.
- Confundir perspective com aba: alterar perspective não fecha o projeto, apenas muda as views.
- Build incremental não recompila tudo em projetos com plugins customizados mal declarados.
- Eclipse é mais pesado que editores modernos; projetos com muitos plugins ficam lentos e consomem memória.
- Ícones e plugins do Marketplace podem vir de fontes não oficiais; instale apenas de repositórios confiáveis.

## Relacionadas
- [[IntelliJ]]
- [[Ferramentas]]
- [[VS-Code]]