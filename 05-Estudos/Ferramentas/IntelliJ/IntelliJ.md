---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# IntelliJ

#area/estudos #estudos/ferramentas #conceito

**Resumo:** IDE da JetBrains, referência para JVM (Java, Kotlin, Scala), com análise de código profunda, refatorações seguras, debug integrado e plugins; a IntelliJ IDEA é a base de produtos como PyCharm, WebStorm e Android Studio.

## Conceitos-chave
- **IntelliJ IDEA**: edições Community (free, open-source) e Ultimate (paga, com Spring, JavaScript, bases de dados etc.).
- **Análise estática**: índice de símbolos e compilação incremental permitem go-to-definition, find-usages e detecção de erros em tempo real.
- **Refactoring**: renomear, extrair método/variável, mudar assinatura — atualiza todas as referências com preview.
- **Run/Debug**: configurações de execução com breakpoints, watches, evaluate expression e hot reload.
- **VCS integrado**: Git com UI de staging, diffs, resolve de conflitos, history e suporte a GitHub/GitLab.
- **Plugins e settings**: Marketplace, inspeções customizadas, live templates, keymaps e configuração via `settings.jar`/sync.
- **Gradle/Maven**: integração nativa para builds JVM com sincronização automática de dependências.

## Exemplos
Atalhos essenciais (keymap default):

```text
Shift+Shift     # busca geral (arquivos, ações, classes)
Alt+Enter       # intenções/sugestões e quick fixes
Ctrl+Shift+R    # renomear com preview de todas as referências
Ctrl+Shift+F10  # rodar a configuração atual
F8 / F9         # step over / resume no debugger
```

Configuração de checkstyle via CLI:

```bash
# validação de estilo em CI
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

## Boas práticas
- Compartilhe configurações (`.idea` com file templates, run configurations, inspections) de forma seletiva com o time.
- Use "Extract" e "Rename" do refactoring em vez de substituições manuais.
- Configure formatters e inspections no nível do projeto para padronizar o estilo.
- Aproveite o integrador com Gradle/Maven e valide problemas de build pelo próprio IDE.
- Ative "Show intention actions" e os quick fixes para aprender boas práticas da linguagem.

## Armadilhas comuns
- Índice/cache corrompido: `File > Invalidate Caches / Restart` resolve falsos erros.
- Keymaps diferentes do padrão confundem quem muda de IDE; use o keymap do VS Code/Eclipse se preferir.
- Projetos grandes com muitos plugins ficam lentos; ajuste heap (`-Xmx`) e desative plugins não usados.
- Edições Community não cobrem Spring/Jakarta EE e JS avançado — não confunda com a Ultimate.
- Esquecer de sincronizar dependências após alterar `build.gradle`/`pom.xml` causa erros de classe não encontrada.

## Relacionadas
- [[Eclipse]]
- [[Ferramentas]]
- [[Editor]]