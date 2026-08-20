---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Django

#area/estudos #estudos/backend #conceito

**Resumo:** Framework web full-stack do Python, "batteries included": traz ORM, admin automático, autenticação, formulários e proteção contra ataques comuns embutidos.

## Conceitos-chave
- **O que é:** framework opinativo que já entrega quase tudo que uma aplicação web precisa, reduzindo decisões de arquitetura.
- **Quando usar:** CRUDs administrativos, sites com painel interno, projetos com prazo curto e times que querem convenções prontas.
- **Estrutura (MTV):** Model (banco), Template (apresentação) e View (lógica) — análogo ao MVC.
- **ORM:** mapeia classes Python para tabelas e gera migrations automaticamente.
- **Admin automático:** painel de gerenciamento gerado a partir dos models, sem código adicional.
- **Diferenças-chave:** mais pesado que Flask/FastAPI, porém traz autenticação, segurança e admin nativos; focado em apps web síncronas (DRF para APIs).
- **Django REST Framework (DRF):** biblioteca padrão para construir APIs REST sobre Django.

## Exemplos
```python
# models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=120)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
```

```python
# views.py com DRF
from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
```

```bash
django-admin startproject loja .
python manage.py startapp produtos
python manage.py makemigrations && python manage.py migrate
python manage.py runserver
```

## Boas práticas
- Manter a lógica de negócio em services/ou nos models, não em views gordas.
- Usar as proteções embutidas (CSRF, XSS, SQL injection) em vez de desativá-las.
- Aproveitar o admin para operações internas, mas restringir com permissões.
- Escrever migrations versionadas e usar `F()` para atualizações atômicas.
- Configurar DEBUG=False em produção e variáveis de ambiente para segredos.

## Armadilhas comuns
- "Fat views": colocar lógica de negócio dentro das views dificulta teste e reuso.
- Fazer N+1 queries ao percorrer relacionamentos sem `select_related`/`prefetch_related`.
- Usar `objects.all()` seguido de `.filter()` em loop, gerando consultas repetidas.
- Confiar no admin em produção sem controle de acesso adequado.
- Comparar com Flask/FastAPI sem considerar que Django entrega mais pronto, mas é menos leve.

## Relacionadas
- [[Python]]
- [[Backend]]
- [[REST]]
- [[Flask]]
- [[FastAPI]]
- [[ORM]]