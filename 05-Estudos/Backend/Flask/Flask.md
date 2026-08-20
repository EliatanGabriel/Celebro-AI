---
type: concept
area: estudos
status: active
created: "2026-08-15"
updated: "2026-08-20"
---

# Flask

#area/estudos #estudos/backend #conceito

**Resumo:** Micro-framework do Python, leve e flexível, ideal para APIs e aplicações pequenas; delega escolhas como banco e ORM ao desenvolvedor.

## Conceitos-chave
- **O que é:** framework minimalista que fornece o núcleo (rotas, WSGI, templates) sem impor estrutura.
- **Quando usar:** protótipos, APIs simples, microsserviços pequenos e projetos com estrutura customizada.
- **Estrutura básica:** instância `Flask(__name__)` + decorator `@app.route` + retorno de dados (dict/string).
- **Jinja2:** template engine embutida para renderizar HTML no servidor.
- **Extensível:** Flask-SQLAlchemy, Flask-Login, Flask-Migrate expandem o núcleo conforme a necessidade.
- **Diferenças-chave:** mais leve que Django e FastAPI; não traz ORM, validação tipada nem docs automáticas por padrão.

## Exemplos
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/")
def raiz():
    return jsonify({"mensagem": "Olá"})

@app.get("/usuarios/<int:usuario_id>")
def get_usuario(usuario_id):
    return jsonify({"id": usuario_id})

@app.post("/usuarios")
def criar():
    dados = request.get_json()
    return jsonify(dados), 201

if __name__ == "__main__":
    app.run(debug=True)
```

```python
# Com Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
```

## Boas práticas
- Usar factory pattern (`create_app`) para montar a aplicação de forma testável.
- Separar rotas, models e serviços em módulos à medida que o projeto cresce.
- Escolher extensões oficiais e mantidas (SQLAlchemy, Migrate, Login).
- Configurar `SECRET_KEY` via variável de ambiente e nunca em código.
- Em produção, servir com WSGI (Gunicorn) em vez do servidor de desenvolvimento.

## Armadilhas comuns
- Achar que Flask escala mal: ele escala bem se bem estruturado, mas exige disciplina.
- Usar `debug=True` em produção.
- Crescer a aplicação em um único arquivo até ficar incontrolável.
- Assumir que há validação automática de dados (não há, como em FastAPI).
- Confundir o comportamento de `request.args` (query string) com `request.json`.

## Relacionadas
- [[Python]]
- [[Backend]]
- [[REST]]
- [[FastAPI]]
- [[Django]]