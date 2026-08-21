---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Ansible

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Ferramenta de automação de configuração e provisionamento agent-less baseada em YAML, que conecta-se aos hosts via SSH e executa tarefas idempotentes.

## Conceitos-chave
- **Agent-less:** não instala agente nos hosts gerenciados; usa SSH (Linux) ou WinRM (Windows).
- **Playbook:** arquivo YAML com uma sequência de plays; cada play mapeia hosts a tarefas.
- **Módulo:** unidade executável (package, copy, service, file). Módulos são idempotentes por padrão.
- **Inventário:** lista de hosts e grupos que o Ansible gerencia (arquivo INI/YAML ou dinâmico na nuvem).
- **Idempotência:** executar o playbook repetidamente produz o mesmo estado final sem efeitos colaterais.
- **Control node e managed nodes:** a máquina de controle roda o Ansible; os nós gerenciados são alvos.
- **Modo pull vs push:** o Ansible é push-based (control node inicia); pode operar pull com `ansible-pull` e cron.

## Exemplos

Playbook para instalar e iniciar Nginx:

```yaml
---
- name: Configurar servidor web
  hosts: webservers
  become: true
  tasks:
    - name: Instalar nginx
      ansible.builtin.apt:
        name: nginx
        state: present
        update_cache: true

    - name: Copiar site
      ansible.builtin.copy:
        src: ./site.html
        dest: /var/www/html/index.html
        owner: www-data
        group: www-data

    - name: Garantir nginx ativo
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true
```

Execução:

```bash
ansible-playbook -i hosts.ini site.yml
ansible all -i hosts.ini -m ping
```

## Boas práticas
- Usar roles para organizar tarefas reutilizáveis (defaults, handlers, vars, templates).
- Aplicar o princípio de menos privilégio: `become` apenas onde necessário.
- Versionar playbooks e inventário em git, integrando com CI/CD.
- Usar templates Jinja2 para configurações dinâmicas por host/grupo.
- Testar mudanças com `--check` (dry-run) e `--diff` antes de aplicar.

## Armadilhas comuns
- Confundir Ansible com IaC de provisionamento: ele configura máquinas existentes; para criar infra, usa-se Terraform.
- Playbooks não idempotentes (ex.: `command:` com efeito repetitivo) quebrando a premissa central.
- Esquecer de definir `hosts` corretamente e atingir o grupo errado.
- Guardar senhas/keys no inventário em texto puro — usar Ansible Vault.
- Módulo `shell`/`command` em excesso quando existe módulo específico.

## Relacionadas
- [[IaC]]
- [[Terraform]]
- [[DevOps]]
- [[Containers]]