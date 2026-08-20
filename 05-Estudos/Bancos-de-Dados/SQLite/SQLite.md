---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# SQLite

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Banco relacional embutido e sem servidor que armazena todo o banco em um único arquivo; amplamente usado em aplicações mobile, desktop, embarcados e no browser.

## Conceitos-chave
- **Embedded/serverless:** biblioteca embutida no processo da aplicação, sem servidor separado.
- **Arquivo único:** todo o banco vive em um `.db`/`.sqlite`, facilitando cópia e deploy.
- **SQL:** boa conformidade com o padrão, sem alguns recursos avançados de outros SGBDs.
- **ACID:** transações atômicas com locking de arquivo.
- **WAL mode:** journaling write-ahead log que melhora a concorrência de leitura e escrita.
- **Uso:** SQLite no navegador via sql.js/WASM, apps móveis e ferramentas CLI.

## Exemplos

```sql
CREATE TABLE tarefas (
  id        INTEGER PRIMARY KEY,
  titulo    TEXT NOT NULL,
  concluida INTEGER DEFAULT 0
);

INSERT INTO tarefas (titulo) VALUES ('Estudar SQLite');
SELECT * FROM tarefas WHERE concluida = 0;
```

## Boas práticas
- Usar WAL mode em apps com escrita e leitura concorrentes.
- Usar `INTEGER PRIMARY KEY` (alias de rowid) para autoincremento.
- Fazer backup com `.backup` em vez de copiar o arquivo em uso.
- Versionar o esquema com `PRAGMA user_version`.

## Armadilhas comuns
- Usar SQLite em serviços web com alta concorrência de escrita — o locking vira gargalo.
- Copiar o arquivo enquanto está aberto sem `.backup`, gerando corrupção.
- Achar que suporta todos os recursos de PostgreSQL/MySQL.
- Ignorar `PRAGMA foreign_keys = ON`, que é desabilitado por padrão.

## Relacionadas
- [[Bancos-de-Dados]]
- [[Transactions]]
- [[Estudos-SQL]]