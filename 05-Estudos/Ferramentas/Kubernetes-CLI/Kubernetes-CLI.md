---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Kubernetes-CLI

#area/estudos #estudos/ferramentas #conceito

**Resumo:** kubectl, a CLI oficial do Kubernetes, usada para declarar, inspecionar e depurar recursos (pods, deployments, services) contra um cluster; também cobre ferramentas complementares como k9s e helm.

## Conceitos-chave
- **kubeconfig**: arquivo (padrão `~/.kube/config`) com contextos, clusters e credenciais; `kubectl config use-context` troca de cluster.
- **Recursos declarativos**: `kubectl apply -f arquivo.yaml` aplica o estado desejado; `delete` remove; `get` consulta.
- **Pods**: menor unidade executável; containers dentro de um pod compartilham rede e volume.
- **Workloads**: Deployments (desejo de réplicas), StatefulSets, DaemonSets, Jobs/CronJobs.
- **Networking**: Services (ClusterIP, NodePort, LoadBalancer) expõem pods; Ingress faz roteamento HTTP.
- **Logs e debug**: `kubectl logs`, `exec` interativo, `port-forward` para acesso local a serviços.
- **Escala e rollout**: `scale`, `rollout status/undo`, `describe` e `events` para diagnóstico.

## Exemplos
Operações comuns:

```bash
kubectl get pods -n producao
kubectl describe pod meu-app-5dff7f6bf6-abcde
kubectl logs -f deploy/meu-app --tail=100
kubectl exec -it deploy/meu-app -- sh
kubectl port-forward svc/meu-app 8080:80
```

Aplicar manifesto e acompanhar rollout:

```bash
kubectl apply -f deployment.yaml
kubectl rollout status deploy/meu-app
kubectl scale deploy/meu-app --replicas=3
kubectl rollout undo deploy/meu-app
```

## Boas práticas
- Aplique mudanças via manifestos versionados, nunca com comandos imperativos ad-hoc.
- Separe namespaces por ambiente (dev, staging, producao) e use labels para seleção.
- Configure contextos com clusters/namespaces corretos e evite operar em produção sem cuidado.
- Use `kubectl get events` e `describe` antes de abrir issue no cluster.
- Combine com Helm para empacotar/reutilizar charts e com k9s para navegação rápida.

## Armadilhas comuns
- `kubectl apply` não reverte mudanças removidas do manifesto; use `kubectl delete` ou tooling (Kustomize/Helm) para remoções.
- Esquecer `-n` e operar no namespace errado (ou no default).
- Contar com DNS estável: endpoints mudam conforme rollout; use Services, não IPs de pods.
- Port-forward exposto localmente sem autenticação pode ser acessado por terceiros na rede.
- Confundir `restart` (pod recreado) com reload de configuração — configmaps montados nem sempre são recarregados.

## Relacionadas
- [[Terminal]]
- [[Ferramentas]]
- [[Docker-Desktop]]
- [[GitLab]]