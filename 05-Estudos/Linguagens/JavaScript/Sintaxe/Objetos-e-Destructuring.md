---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# Objetos e Destructuring em JavaScript

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** Objetos em JavaScript guardam pares chave-valor, e recursos como destructuring, spread e optional chaining deixam seu manuseio muito mais limpo.

## Referência rápida

| Sintaxe | O que faz | Exemplo |
|---|---|---|
| `{ chave: valor }` | Objeto literal | `const user = { nome: "Ana" };` |
| `obj.chave` / `obj["chave"]` | Acesso por ponto / colchetes (chave dinâmica) | `user.nome; user["idade"];` |
| `Object.keys(obj)` | Array com as chaves | `Object.keys(user);` |
| `Object.values(obj)` | Array com os valores | `Object.values(user);` |
| `Object.entries(obj)` | Array de pares `[chave, valor]` | `Object.entries(user);` |
| `{ a, b } = obj` | Destructuring extrai propriedades | `const { nome } = user;` |
| `[x, y] = arr` | Destructuring de array por posição | `const [primeiro] = lista;` |
| `{ ...obj }` | Spread copia/expande o objeto | `const copia = { ...user };` |
| `{ nome }` | Shorthand quando variável tem o mesmo nome | `const user2 = { nome, idade };` |
| `obj?.a?.b` | Optional chaining para caminhos nulos | `user?.endereco?.cidade;` |

## Exemplos

```js
// Objeto literal, shorthand e destructuring
const nome = "Ana";
const usuario = {
  nome,                          // shorthand
  idade: 25,
  endereco: { cidade: "Recife" }
};

const { nome: quem, idade, endereco: { cidade } } = usuario;
console.log(quem, idade, cidade);   // Ana 25 Recife
```

```js
// Iteração com entries, cópia com spread e merge
const estoque = { teclado: 12, mouse: 8 };

for (const [produto, qtd] of Object.entries(estoque)) {
  console.log(`${produto}: ${qtd} un.`);
}

const padrao = { tema: "claro", idioma: "pt" };
const config = { ...padrao, tema: "escuro" };   // merge + override
```

## Boas práticas

- Use destructuring nos parâmetros de função para APIs mais legíveis.
- Prefira spread a mutar objetos diretamente ao atualizar estado.
- Extraia chaves dinâmicas com colchetes: `obj[campoDigitado]`.
- Use shorthand para objetos curtos e limpos.
- Renomeie no destructuring (`{ id: codigo }`) para evitar conflitos.

## Armadilhas comuns

- Spread copia raso: objetos aninhados continuam compartilhando referência.
- Desestruturar `null` ou `undefined` lança erro imediatamente.
- Chaves numéricas viram strings no `for...in` e em `Object.keys`.
- Sobrescrever uma constante existente via destructuring dá erro.
- `delete obj.chave` é lento; prefira criar novo objeto sem a propriedade.

## Relacionadas

- [[Arrays-e-Metodos]]
- [[Classes-e-POO]]
- [[JavaScript]]
