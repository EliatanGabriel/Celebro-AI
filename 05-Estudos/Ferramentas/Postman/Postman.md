---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Postman

#area/estudos #estudos/ferramentas #conceito

**Resumo:** Ferramenta gráfica para testar, depurar, documentar e automatizar APIs; organiza requisições em collections, usa environments com variáveis e gera testes de integração e coleções executáveis via Newman (CLI).

## Conceitos-chave
- **Collections**: grupos de requisições organizadas com pastas, exemplos e documentação embutida.
- **Environments**: conjuntos de variáveis (base URL, tokens) trocáveis entre dev/staging/produção.
- **Variáveis e scripts**: pré-request scripts e tests escritos em JavaScript; `pm.environment`, `pm.collectionVariables`.
- **Testes**: asserções com a biblioteca `pm.test` e Chai (status code, JSON schema, tempo de resposta).
- **Mock Server**: simula respostas a partir de exemplos salvos para desenvolvimento paralelo.
- **Newman**: runner CLI do Postman para rodar collections em CI sem interface.
- **Auth**: suporte a Basic, Bearer, OAuth 2.0, AWS SigV4 etc., com geração de token automática.

## Exemplos
Teste de resposta em um request:

```js
pm.test("Status 200", () => pm.response.to.have.status(200));
pm.test("Contém dados", () => {
  const body = pm.response.json();
  pm.expect(body.usuarios.length).to.be.greaterThan(0);
});
```

Pré-request script que injeta token:

```js
const token = pm.environment.get("access_token");
pm.request.headers.add({ key: "Authorization", value: `Bearer ${token}` });
```

Rodar coleção em CI:

```bash
npx newman run colecao.json -e ambiente.prod.json --reporters cli,junit \
  --reporters-junit-export results.xml
```

## Boas práticas
- Organize collections por domínio/fluxo e versionize-as com Git (export/import).
- Use environments e variáveis, nunca hardcode URLs ou tokens nas requisições.
- Escreva testes reutilizáveis (status, schema, contrato) para validar regressões de API.
- Extraia a base URL e segredos para variáveis de environment protegidas.
- Integre Newman no CI para executar testes de API a cada deploy.

## Armadilhas comuns
- Testes que dependem de ordem de execução dentro da collection (estado compartilhado).
- Tokens expirados em environments causam falhas intermitentes; gere token via script.
- Variáveis com escopo errado (global vs. environment) sobrescrevendo valores esperados.
- Esquecer de limpar/desativar proxy ou certificados corporativos ao testar APIs locais.
- Confiar em respostas de exemplo (mock) como verdade do contrato real da API.

## Relacionadas
- [[Ferramentas]]
- [[Curl]]
- [[Ferramentas-CLI]]