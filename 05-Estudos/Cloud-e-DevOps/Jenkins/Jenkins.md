---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Jenkins

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Servidor de automação/CI/CD open-source e extensível, com pipelines declarativas (Jenkinsfile), ecossistema de plugins e agendamento de jobs.

## Conceitos-chave
- **Job/pipeline:** unidade de automação; moderna definida em Jenkinsfile (Declarative ou Scripted/Groovy).
- **Jenkinsfile:** pipeline-as-code versionado no repositório, com stages e steps.
- **Agente (agent):** nó onde o job roda (built-in ou escravos/agents separados).
- **Plugins:** ecossistema enorme (Git, Docker, Kubernetes, Slack) que estende o Jenkins.
- **Estágios (stages):** fases do pipeline (build, test, deploy) com visualização no Blue Ocean.
- **Triggers:** gatilhos por webhook (GitHub/GitLab), poll SCM, cron, upstream, manual.
- **Master/controller e agents:** o controller gerencia; agents executam workloads (padrão controller-agent).
- **Credentials:** gerenciamento de segredos com ciphertext e escopo por credencial.

## Exemplos

Jenkinsfile declarativo:

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'npm ci'
                sh 'npm run build'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        stage('Deploy') {
            when { branch 'main' }
            steps {
                withCredentials([string(credentialsId: 'deploy-token', variable: 'TOKEN')]) {
                    sh './deploy.sh'
                }
            }
        }
    }
}
```

## Boas práticas
- Usar Jenkinsfile versionado (pipeline-as-code) em vez de jobs configurados só na UI.
- Separar controller de agents e rodar agents via containers (Kubernetes/Docker).
- Guardar segredos em Credentials, nunca no código ou log.
- Monitorar o controller (disco, fila) e usar plugins de segurança/atualizações.
- Versionar a configuração do Jenkins com JCasC (Configuration as Code).

## Armadilhas comuns
- Manter pipeline inteiro em um único `sh` gigante e sem estágios.
- Deixar o controller executando jobs pesados, saturado o nó.
- Credenciais embutidas no Jenkinsfile que aparecem nos logs.
- Atualização manual de plugins que quebram o ambiente — testar upgrades.
- Jenkins legado sem declarative pipeline, difícil de versionar e reproduzir.

## Relacionadas
- [[CI-CD-Conceito]]
- [[Pipeline]]
- [[GitHub-Actions]]
- [[DevOps]]