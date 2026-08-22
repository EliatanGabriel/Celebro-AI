---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-21"
updated: "2026-08-21"
---

# TypeScript no Dia a Dia

#area/estudos #estudos/linguagens #sintaxe

**Resumo:** No cotidiano, o TypeScript brilha ao validar respostas de API, eventos do DOM e dados dinâmicos, com o strict mode como rede de segurança contra bugs silenciosos.

## Referência rápida

| Situação | Ferramenta | Exemplo |
|---|---|---|
| Resposta de API | interface + generics | `fetch<Usuario>()` |
| Promise tipada | `Promise<T>` | `Promise<Usuario[]>` |
| Evento de clique | `MouseEvent` | `(e: MouseEvent) => ...` |
| Input do DOM | `HTMLInputElement` | `el.value` |
| JSON.parse | cast + validação | `JSON.parse(t) as unknown` |
| Checagem global | `strict: true` | tsconfig.json |

## Exemplos

```ts
interface Usuario {
  id: number;
  nome: string;
}

async function listarUsuarios(): Promise<Usuario[]> {
  const resposta = await fetch("/api/usuarios");
  if (!resposta.ok) throw new Error(`HTTP ${resposta.status}`);
  const dados = (await resposta.json()) as Usuario[];
  return dados;
}

listarUsuarios().then((usuarios) =>
  usuarios.forEach((u) => console.log(u.nome)),
);
```

```ts
// Eventos do DOM já chegam tipados quando o alvo é conhecido
const campo = document.querySelector<HTMLInputElement>("#email");

campo?.addEventListener("input", (e) => {
  const alvo = e.target as HTMLInputElement;
  console.log(alvo.value.trim().length);
});

// JSON.parse retorna any: trate como unknown e valide antes
function lerJson(texto: string): unknown {
  return JSON.parse(texto);
}

const obj = lerJson('{"id":1}');
if (typeof obj === "object" && obj !== null && "id" in obj) {
  console.log((obj as { id: number }).id);
}
```

## Boas práticas

- Ative `strict` no projeto todo; desligar por arquivo vira dívida técnica.
- Modele contratos de API com interfaces versionadas junto ao backend.
- Use `unknown` + validação para qualquer dado que vem de fora.
- Aproveite a inferência do `addEventListener` com seletores específicos.
- Centralize tipos compartilhados (API, formulários) em arquivos próprios.

## Armadilhas comuns

- Fazer `as Usuario` direto no `json()`: a assertion não valida nada em runtime.
- Usar `(e.target as any).value` em vez de tipar o elemento corretamente.
- Esquecer que `querySelector` pode retornar null mesmo com tipo anotado.
- Confiar em `JSON.parse` sem checar estrutura: dados malformados vazam adiante.
- Tipar `Promise<any>` por pressa e perder erros na cadeia async.

## Relacionadas

- [[TypeScript]]
- [[JavaScript]]
- [[Modulos-e-Tipos-Externos]]
- [[Utility-Types]]
