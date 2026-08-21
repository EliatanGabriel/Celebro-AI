---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Kubernetes

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Orquestrador de containers open-source que automatiza deploy, escala e operação de aplicações em clusters, com abstrações como Pods, Deployments e Services.

## Conceitos-chave
- **Pod:** menor unidade executável; encapsula um ou mais containers com rede e storage compartilhados.
- **Deployment:** recurso declarativo que garante o estado desejado de réplicas e gerencia rolling updates.
- **Service:** abstração estável de rede que expõe um conjunto de Pods por label (ClusterIP, NodePort, LoadBalancer).
- **Ingress:** roteamento HTTP(S) externo para os Services (host/path rules).
- **ConfigMap e Secret:** configuração e dados sensíveis injetados nos Pods.
- **kube-apiserver, kubelet, scheduler:** componentes do control plane e do node.
- **Autoscaling:** HPA escala réplicas por métricas (CPU/memória/custom); VPA ajusta recursos.
- **Desired state e reconcilição:** o controlador observa o cluster e age até o estado real igualar o desejado.
- **Namespaces:** isolamento lógico de recursos por equipe/ambiente.

## Exemplos

Deployment + Service:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: minha-app:1.0
          ports:
            - containerPort: 3000
          resources:
            requests: { cpu: "100m", memory: "128Mi" }
            limits: { cpu: "500m", memory: "256Mi" }
---
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 3000
```

Comandos básicos:

```bash
kubectl apply -f deployment.yaml
kubectl get pods -w
kubectl scale deployment web --replicas=5
kubectl rollout status deployment/web
```

## Boas práticas
- Definir resource requests/limits para todos os containers.
- Usar readiness/liveness probes para tráfego e saúde dos Pods.
- Versionar imagens por tag/digest e fazer rolling update com reversão.
- Separar ambientes por cluster ou namespace e aplicar RBAC.
- Segregar segredos em Secrets e cifrar com encryption at rest.

## Armadilhas comuns
- Confundir Pod com Deployment: Pod é efêmero; Deployment gerencia réplicas.
- Trabalhar com containers sem requests/limits, causando throttling ou eviction.
- Fazer `kubectl edit`/alterações manuais que divergem do GitOps.
- Expor Pods sem Service, perdendo a descoberta e estabilidade de IP.
- Desconsiderar a curva de aprendizado e a complexidade operacional do cluster.

## Relacionadas
- [[Docker]]
- [[Containers]]
- [[Microservicos]]
- [[GCP]]