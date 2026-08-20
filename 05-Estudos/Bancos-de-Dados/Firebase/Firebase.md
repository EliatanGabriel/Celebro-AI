---
type: concept
area: estudos
status: active
progresso: "estudando"
created: "2026-08-15"
updated: "2026-08-20"
---

# Firebase

#area/estudos #estudos/bancos-de-dados #conceito

**Resumo:** Plataforma Backend-as-a-Service (BaaS) da Google que oferece bancos NoSQL com sincronização em tempo real (Firestore e Realtime Database), autenticação, storage e hosting.

## Conceitos-chave
- **Cloud Firestore:** banco document-based NoSQL com sincronização em tempo real e escala automática.
- **Realtime Database:** banco JSON em tempo real, mais simples e de baixa latência, porém menos escalável.
- **Listeners em tempo real:** clientes se inscrevem em documentos/coleções e recebem atualizações via websocket.
- **Firebase Auth:** autenticação por e-mail/senha, OAuth (Google, GitHub, etc.) e providers anônimos.
- **Security Rules:** regras avaliadas no servidor que controlam quem lê/escreve cada dado.
- **Offline persistence:** o SDK mantém dados locais e sincroniza quando a conexão volta.
- **Extensions/Functions:** integrações serverless para validação, envio de e-mail, etc.

## Exemplos

```js
import { doc, getDoc, onSnapshot } from "firebase/firestore";

const ref = doc(db, "users", "u1");
const snap = await getDoc(ref);
console.log(snap.data());

// Ouvinte em tempo real
onSnapshot(ref, (doc) => console.log("novo valor:", doc.data()));
```

```js
// Security Rules — somente o dono acessa seus próprios dados
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

## Boas práticas
- Modelar os dados para os padrões de leitura (denormalizar); não existem JOINs.
- Tratar Security Rules como a principal camada de segurança.
- Limitar o número de listeners para controlar custo e latência.
- Estruturar documentos para evitar leituras múltiplas por tela.

## Armadilhas comuns
- Confundir Firestore com banco relacional (consultas com OR em múltiplos campos são limitadas).
- Regras de segurança ausentes ou permissivas — dados expostos publicamente.
- Custo por leitura/escrita imprevisível em escala.
- Vendor lock-in com a nuvem da Google.

## Relacionadas
- [[NoSQL]]
- [[Auth]]
- [[Frontend]]
- [[Supabase]]