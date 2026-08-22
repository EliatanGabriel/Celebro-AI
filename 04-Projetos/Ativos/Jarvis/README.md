# Jarvis — Assistente Pessoal (estilo FRIDAY)

Assistente de voz com interface HUD colorida inspirada no FRIDAY do Tony Stark: logo animado na abertura, cores ciano, e voz **masculina** ("Olá senhor Isaque").

## Funcionalidades

| Comando | Exemplo |
|---|---|
| Saudação de início | ao abrir: *"Olá senhor Isaque"* |
| Hora e data | "que horas são?", "que dia é hoje?" |
| Clima | "como está o tempo?", "clima em Florianópolis" |
| Gmail | "ler e-mails", "enviar e-mail para isaque", "procurar e-mail sobre faculdade" |
| Tarefas | "adicionar tarefa estudar", "listar tarefas", "concluir tarefa 2" |
| Obsidian | "anotar tive uma reunião hoje", "criar nota Projeto X", "resumo do dia" |
| Aplicativos | "abrir YouTube", "abrir WhatsApp", "abrir Google", "abrir Gmail", "abrir Spotify" |
| Pesquisa | "pesquisar notícias de hoje" |
| Wikipédia | "quem é Nikola Tesla" |
| Cálculos | "quanto é 15 vezes 4" |
| Piadas | "conta uma piada" |
| Lembretes | "me lembre de beber água em 10 minutos" |
| Sistema | "desligar computador", "reiniciar computador" |
| Ajuda | "ajuda" |
| Sair | "encerrar" |

## Como usar

1. Diga **"Jarvis"** para chamar o assistente (ou digite o comando direto no modo teclado).
2. Ele responde "Sim, senhor?" e você fala o comando.
3. Para encerrar, diga **"encerrar"** ou feche a janela.

## Instalação (uma vez só)

### 1. Instalar Python
Baixe e instale o Python 3 no site oficial: https://www.python.org/downloads/
Marque a opção **"Add Python to PATH"** durante a instalação.

### 2. Instalar as dependências
Abra o **Prompt de Comando (cmd)** e rode:

```bat
cd "C:\Users\isaqu\OneDrive\Documentos\Celebro AI\Celebro-AI\Jarvis"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

> Se o `PyAudio` falhar na instalação, rode:
> `python -m pip install pipwin` e depois `python -m pipwin install pyaudio`

### 3. Testar
Rode o diagnóstico para conferir se tudo foi instalado:

```bat
python main.py --teste
```

Tudo que mostrar `True` está pronto. Depois rode:

```bat
python main.py
```

Para testar sem microfone:

```bat
python main.py --teclado
```

Para conferir se tudo instalou certo:

```bat
python main.py --teste
```

Para testar a **voz** (ele fala uma frase e lista as vozes disponíveis):

```bat
python main.py --voz
```

> **Dica:** dá pra iniciar sempre com dois cliques no arquivo **`iniciar-jarvis.bat`**.

## Configurando o Gmail (5 minutos)

O Jarvis lê e envia e-mails pela sua conta do Google. É gratuito.

1. Acesse o **Google Cloud Console**: https://console.cloud.google.com/
2. Crie um novo projeto (botão no topo → "Novo projeto" → nome: `Jarvis`).
3. No menu lateral: **APIs e serviços** → **Biblioteca** → pesquise **"Gmail API"** → **Ativar**.
4. Menu lateral: **APIs e serviços** → **Tela de consentimento do OAuth**:
   - Tipo de usuário: **Externo** → Criar.
   - Preencha nome do app (`Jarvis`) e o e-mail de suporte.
   - Em "Escopos", clique em **Adicionar ou remover escopos** e marque os do **Gmail API** (`.../auth/gmail.readonly` e `.../auth/gmail.send`).
   - Em "Test users", adicione o **seu** e-mail (o seu Gmail).
   - Conclua o cadastro.
5. Menu lateral: **APIs e serviços** → **Credenciais** → **Criar credenciais** → **ID do cliente OAuth**:
   - Tipo de aplicativo: **Aplicativo para computador**.
   - Clique em **Criar** → baixe o JSON baixado.
6. Copie o arquivo baixado para a pasta **`credenciais/`** do Jarvis e renomeie para **`credentials.json`**.

Pronto! Na primeira vez que você disser "ler e-mails", o navegador abre para você autorizar o Jarvis (só uma vez). Depois disso funciona sozinho.

### Contatos de e-mail
Para "enviar e-mail para isaque" funcionar, edite o arquivo `config.json`:

```json
"contatos": {
  "isaque": "isaquedeveloper@gmail.com"
}
```

Adicione quantos contatos quiser, sempre em letras minúsculas.

## Configurações principais (`config.json`)

- **`cidade`** — usada no comando de clima. Troque para a sua cidade.
- **`nome_usuario`** / **`saudacao_inicial`** — quem ele cumprimenta e o que fala ao iniciar.
- **`voz.voz_edge`** — a voz masculina (padrão: `pt-BR-AntonioNeural`).
- **`obsidian.vault`** — caminho do seu vault. Se mudar de lugar, atualize aqui.
- **`aplicativos`** — sites que ele abre nos comandos "abrir ...".

### Trocar a voz (sempre masculina)
O Jarvis **só usa voz masculina** (nunca feminina). Ele procura na ordem:
1. **Daniel** (Windows 10) ou **Davos** (Windows 11) — masculina, funciona offline.
2. **Antônio** (internet) — masculina, qualidade superior.

Se quiser forçar a voz da internet (Antônio), mude no `config.json`:
```json
"voz": { "engine": "edge", "voz_edge": "pt-BR-AntonioNeural" }
```
Para o offline, deixe `"engine": "pyttsx3"` e `"voz_pyttsx3": "auto"` (ele acha a masculina sozinho).

> Se ao abrir ele **não falar nada**, rode `python main.py --voz` para ver o diagnóstico da voz e as vozes instaladas.

## Estrutura

```
Jarvis/
├── main.py                  # entrada (python main.py)
├── iniciar-jarvis.bat       # atalho de duplo clique
├── config.json              # suas configurações
├── requirements.txt         # dependências
├── credenciais/             # credentials.json (Gmail)
└── jarvis/
    ├── assistant.py         # loop principal
    ├── brain.py             # comandos
    ├── voice.py             # voz + microfone
    ├── ui.py                # HUD colorido estilo FRIDAY
    ├── gmail_service.py     # Gmail
    ├── tasks.py             # tarefas
    ├── obsidian.py          # notas no seu vault
    ├── weather.py           # clima
    ├── config.py            # leitura de config.json
    └── dados/               # tarefas.json, áudio temporário
```

> As tarefas também são gravadas no seu diário do Obsidian (como checkboxes), então aparecem em qualquer dispositivo com o vault sincronizado.
