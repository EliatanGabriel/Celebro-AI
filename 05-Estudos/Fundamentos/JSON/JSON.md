---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# JSON

#area/estudos #estudos/fundamentos #conceito

**Resumo:** Formato leve de troca de dados baseado em texto, derivado da notação de objetos JavaScript, padrão em APIs, arquivos de configuração e persistência.

## Conceitos-chave
- **Estruturas básicas:** objetos (`{"chave": valor}`), arrays (`[a, b, c]`), strings, números, booleanos e `null`.
- **Chave-valor:** pares organizados em objetos; as chaves sempre são strings entre aspas duplas.
- **Serialização:** converter estruturas de dados de uma linguagem para JSON (`JSON.stringify`, `json.dumps`).
- **Deserialização (parse):** converter JSON de volta para a estrutura nativa (`JSON.parse`, `json.loads`).
- **Interoperabilidade:** por ser texto simples, é legível e suportado por praticamente todas as linguagens.
- **Usos:** corpo de requisições HTTP, arquivos de configuração (`package.json`, `tsconfig.json`), comunicação entre serviços e bancos de dados.

## Exemplos
```json
{
  "usuario": {
    "nome": "Ana",
    "idade": 27,
    "ativo": true,
    "endereco": null,
    "hobbies": ["leitura", "corrida"]
  },
  "score": 95.5
}
```

```javascript
// Serializar e desserializar
const dados = { nome: "Ana", idade: 27 };
const json = JSON.stringify(dados);   // '{"nome":"Ana","idade":27}'
const obj  = JSON.parse(json);        // { nome: 'Ana', idade: 27 }
```

```python
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)          # JSON → dict

payload = json.dumps({"erro": None}, ensure_ascii=False)  # dict → JSON
```

## Boas práticas
- Validar JSON recebido de fontes externas antes de usar os campos.
- Não usar vírgulas finais nem comentários: o formato não os permite.
- Manter a codificação UTF-8 para acentuação.
- Para dados aninhados profundos, considerar o custo de parse repetido (cache do resultado quando possível).
- Usar `JSON.parse`/`json.loads` dentro de tratamento de erro, pois input malformado lança exceção.

## Armadilhas comuns
- Usar aspas simples ou sem aspas nas chaves — JSON exige aspas duplas.
- Deixar vírgula final, que quebra o parse.
- Tratar números como strings e perder precisão (ex.: ids grandes > 2^53 em JS).
- Esquecer de escapar strings com aspas dentro do conteúdo.
- Assumir que a ordem das chaves é preservada entre todas as linguagens.

## Relacionadas
- [[Hash]]
- [[Tipos-de-Dados]]
- [[Arrays]]
- [[Logica-de-Programacao]]
- [[Programacao]]