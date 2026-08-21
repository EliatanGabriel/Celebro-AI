---
type: concept
area: trabalho
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Jenkins

#area/trabalho #trabalho/ci-cd #conceito

**Resumo:** Servidor de automação open source para CI/CD com pipelines declarativas.

## Conceitos-chave
- Jenkins orquestra jobs: build, testes, análise de qualidade e deploy.
- Pipelines declarativas (Jenkinsfile) versionadas com o código.
- Agentes (agents) executam os jobs; mestre distribui as cargas de trabalho.
- Plugins estendem integrações (Git, Docker, Slack, JUnit, artefatos).

## Exemplos
```groovy
// Jenkinsfile (pipeline declarativa)
pipeline {
  agent any
  stages {
    stage('Build') { steps { sh 'npm ci && npm run build' } }
    stage('Test')  { steps { sh 'npm test' } }
    stage('Deploy') { steps { sh './deploy.sh staging' } }
  }
  post {
    failure { notifyBuildFailed() }
  }
}
```

## Boas práticas
- Manter o Jenkinsfile no repositório (pipeline as code).
- Definir tempos de timeout e política de falha explícita por etapa.
- Guardar credenciais no cofre do Jenkins, nunca no script.
- Monitorar os agentes e o volume de jobs para dimensionar corretamente.

## Armadilhas comuns
- Configurar pipelines na interface e perder versionamento/backup.
- Scripts Groovy complexos e frágeis sem revisão.
- Agentes sem recursos ou com ambientes divergentes entre si.
- Plugins desatualizados ou conflitantes quebrando o build.

## Relacionadas
- [[Build]]
- [[Deploy]]
- [[Pipeline]]