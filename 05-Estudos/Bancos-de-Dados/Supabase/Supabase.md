---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Supabase

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Plataforma open-source, alternativa ao Firebase, construída sobre PostgreSQL — oferece banco relacional com auth, realtime, storage e edge functions.

## Conceitos-chave
- **PostgreSQL como base:** SQL completo, foreign keys, extensões e Row Level Security (RLS).
- **Realtime:** streaming de mudanças no banco via websockets, usando o WAL do Postgres.
- **Auth:** usuários, provedores OAuth e tokens JWT integrados ao banco (`auth.users`).
- **Storage:** buckets para armazenar arquivos com políticas de acesso.
- **Edge Functions:** funções serverless executadas em Deno.
- **RLS/Policies:** segurança no nível do banco, com políticas por linha.

## Exemplos

```sql
CREATE TABLE notas (
  id         BIGSERIAL PRIMARY KEY,
  usuario_id UUID REFERENCES auth.users(id),
  texto      TEXT
);

ALTER TABLE notas ENABLE ROW LEVEL SECURITY;

CREATE POLICY "user_notes" ON notas
  FOR ALL
  USING (usuario_id = auth.uid());
```

```js
import { createClient } from "@supabase/supabase-js";
const sb = createClient(url, anonKey);

const { data } = await sb
  .from("notas")
  .select("*")
  .order("id", { ascending: false });

// Assinatura em tempo real
sb.channel("notas")
  .on("postgres_changes", { event: "INSERT", schema: "public", table: "notas" },
    (payload) => console.log(payload.new))
  .subscribe();
```

## Boas práticas
- Habilitar RLS em todas as tabelas expostas ao client.
- Colocar a segurança nas policies do banco, não apenas no client.
- Modelar normalmente como PostgreSQL relacional.
- Versionar o esquema com migrations (SQL ou Prisma).

## Armadilhas comuns
- Expor tabelas sem RLS — dados ficam acessíveis pela API anônima.
- Tratar Supabase como "NoSQL mágico" esquecendo que é relacional.
- Depender do hosted e ignorar a complexidade do self-host.
- Esquecer que o auth (`auth.users`) exige configuração prévia.

## Relacionadas
- [[PostgreSQL]]
- [[Firebase]]
- [[Backend]]
- [[Migrations]]