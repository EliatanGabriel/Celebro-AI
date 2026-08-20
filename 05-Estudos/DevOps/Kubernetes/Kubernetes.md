---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-20"
updated: "2026-08-20"
---

# Kubernetes

#area/estudos #estudos/devops #conceito #orquestracao #containers #estudos/devops

**Resumo:** Plataforma de orquestração de contêineres que automatiza deploy, escala e operação de aplicações em clusters de nós.

## Conceitos-chave
- **Pods:** unidade mínima de execução; encapsulam um ou mais contêineres que compartilham rede e armazenamento.
- **Deployments:** declaram o estado desejado (replicas, imagem) e garantem rollouts e rollbacks.
- **Services:** abstração de rede que expõe pods de forma estável, com balanceamento de carga.
- **Ingress:** ponto de entrada HTTP/HTTPS externo com roteamento por host ou caminho.
- **Nodes:** máquinas (físicas ou VMs) que compõem o cluster, controladas pelo control plane.
- **Escala automática (HPA):** ajusta o número de réplicas com base em métricas como CPU e memória.

## Exemplos
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: minha-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: minha-app
  template:
    metadata:
      labels:
        app: minha-app
    spec:
      containers:
        - name: app
          image: minha-app:1.0
          ports:
            - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: minha-app-svc
spec:
  selector:
    app: minha-app
  ports:
    - port: 80
      targetPort: 8000
```

```bash
kubectl apply -f deployment.yaml
kubectl get pods
kubectl rollout status deployment/minha-app
```

## Boas práticas
- Declarar recursos em manifestos versionados e usar GitOps quando possível.
- Definir requests e limits de CPU/memória para cada contêiner.
- Usar probes de saúde (liveness/readiness) para o controle de tráfego.
- Organizar recursos em namespaces e aplicar RBAC.

## Armadilhas comuns
- Subdimensionar requests/limits, causando evicções e instabilidade.
- Confundir Service com Ingress: o Service expõe internamente; o Ingress roteia o tráfego externo.
- Fazer deploy sem estratégia de rollout (recreate), gerando downtime.
- Assumir que pods são permanentes: eles são descartáveis e podem ser recriados a qualquer momento.

## Relacionadas
- [[Docker]]
- [[CI-CD]]
- [[Containers]]