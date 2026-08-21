---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Monolitos

#area/estudos #estudos/cloud-e-devops #conceito

**Resumo:** Arquitetura onde toda a aplicação é empacotada e executada como um único processo/deploy, com código, banco e UI integrados.

## Conceitos-chave
- **Deploy único:** uma build gera um artefato que contém todas as funcionalidades.
- **Banco de dados único:** um schema central compartilhado entre módulos da aplicação.
- **Simplicidade inicial:** desenvolvimento, testes e debug mais diretos no começo.
- **Escala vertical (scale up):** para crescer, aumenta-se recurso da máquina ou replica-se o app inteiro.
- **Acoplamento:** mudanças em um módulo afetam o sistema todo (build, teste, deploy).
- **Monólito modular:** boa evolução — módulos bem delimitados dentro de um único deploy.
- **Estratégias de migração:** Strangler Fig pattern, separação incremental por domínio.

## Exemplos

Estrutura típica:

```text
monolito/
├── app/           # código da aplicação
├── models/        # acesso ao banco (schema único)
├── controllers/   # endpoints da API
├── templates/     # frontend/servidor
└── tests/         # testes da aplicação
```

Deploy único:

```bash
docker build -t app-monolitica:1.0 .
docker run -d -p 8080:8080 app-monolitica:1.0
```

## Boas práticas
- Começar como monólito modular: limites de módulo claros e API interna estável.
- Manter testes automatizados para permitir deploys frequentes mesmo em um artefato.
- Modularizar por domínio (pasta/package) para facilitar futura extração.
- Monitorar o monólito com métricas por módulo para identificar gargalos.
- Só migrar para microserviços quando houver dor real (escala, times, deploy).

## Armadilhas comuns
- Deploy lento e arriscado: qualquer mudança requer revalidar tudo.
- Escala ineficiente: replica o sistema inteiro para atender um módulo.
- Acoplamento que trava times grandes no mesmo release.
- Migrar para microserviços "por moda" sem necessidade (complexidade não paga).
- Confundir "monólito ruim" (código bagunçado) com "monólito" (arquitetura) — o problema é código, não o formato.

## Relacionadas
- [[Microservicos]]
- [[Containers]]