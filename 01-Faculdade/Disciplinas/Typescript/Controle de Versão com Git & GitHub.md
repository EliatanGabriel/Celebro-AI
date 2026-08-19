---
type: concept
area: faculdade
status: active
---

# Controle de Versão com Git & GitHub

#area/faculdade #conceito

**Resumo:** Controle de versão com Git e GitHub: conceitos, configuração, autenticação SSH, repositórios, as três árvores do Git, ciclo prático de comandos e fluxo completo do zero à nuvem.

## 1. O que é Controle de Versão?

Controle de versão é um sistema, também chamado de **VCS** (*Version Control System*) ou **SCM** (*Source Code Management*), que permite:

- Rastrear o histórico de alterações em arquivos
- Registrar cada modificação ao longo do tempo
- Coordenar o trabalho de várias pessoas
- Recuperar versões anteriores de um projeto

**Exemplo de histórico:**

```
Versão inicial
      ↓
Login criado
      ↓
Bug corrigido
      ↓
HEAD
```

Cada alteração fica registrada em uma linha do tempo.

## 2. Por que o Controle de Versão é essencial?

O controle de versão traz várias vantagens:

- **Trabalho em equipe** — permite que várias pessoas trabalhem simultaneamente sem sobrescrever o trabalho umas das outras.
- **Histórico completo** — permite voltar para versões anteriores do projeto.
- **Branches** — permitem experimentar novas funcionalidades de maneira segura, sem necessariamente alterar a versão principal.
- **Cópia completa** — cada máquina pode possuir uma cópia completa do repositório.
- **Qualidade e agilidade** — facilita a organização e a velocidade na entrega do software.

## 3. Git × GitHub

Git é a ferramenta. GitHub é a plataforma. Embora trabalhem juntos, Git e GitHub são coisas diferentes.

### 3.1. Git

O Git é uma ferramenta de controle de versão.

**Características:**

- Roda localmente no computador
- Possui uma cópia completa do repositório
- Funciona offline
- É operado principalmente pela linha de comando

**Papel:** cliente.

```
COMPUTADOR
    ↓
   GIT
```

### 3.2. GitHub

O GitHub é uma plataforma online que hospeda repositórios Git.

**Características:**

- Serviço online na nuvem
- Pull Requests
- Issues
- Automação com GitHub Actions
- Portfólio
- Colaboração

**Papel:** servidor.

```
GITHUB
  ☁
SERVIDOR
```

## 4. Git e GitHub trabalham juntos

A comunicação entre o Git local e o GitHub utiliza principalmente:

```
GIT LOCAL
   │
   │ push
   ↓
GITHUB
   │
   │ pull
   ↓
GIT LOCAL
```

- **push** — envia alterações do repositório local para o GitHub.
- **pull** — baixa alterações do GitHub para o repositório local.

Git e GitHub são ferramentas distintas e complementares.

## 5. Criando uma conta no GitHub

Para utilizar o GitHub:

1. Acessar github.com
2. Clicar em *Sign up*
3. Informar e-mail, senha e username
4. Resolver o CAPTCHA
5. Escolher o plano *Free*
6. Confirmar o e-mail

## 6. Configurando o Git

Depois de instalar o Git, é necessário configurar a identidade do usuário.

```bash
git config --global user.name "Seu Nome"
git config --global user.email "voce@ex.com"
```

O material recomenda utilizar o mesmo e-mail da conta GitHub.

## 7. Autenticação do GitHub

Para realizar operações como push, é necessário autenticar o Git com o GitHub. O material apresenta duas opções:

- **Token PAT** (*Personal Access Token*) — substitui a senha tradicional.
- **Chave SSH** — permite autenticar sem precisar digitar a senha sempre.

O GitHub não aceita mais senha tradicional no terminal para essas operações.

## 8. Autenticação SSH

A autenticação SSH utiliza um par de chaves:

- **Chave privada** — fica na sua máquina.
- **Chave pública** — cadastrada no GitHub.

A chave privada deve permanecer na máquina do usuário. A chave pública é cadastrada no GitHub. Depois disso, o push pode ser autenticado sem digitar senha.

## 9. Gerando uma chave SSH

O comando apresentado para gerar a chave é:

```bash
ssh-keygen -t ed25519 -C "voce@email.com"
```

O e-mail utilizado deve ser o mesmo associado à conta GitHub.

## 10. Copiando a chave pública no Windows

No PowerShell:

```powershell
Get-Content ~\.ssh\id_ed25519.pub | clip
```

Esse comando copia a chave pública para a área de transferência.

## 11. Cadastrando a chave no GitHub

No GitHub:

```
Settings
   ↓
SSH and GPG keys
   ↓
New SSH key
```

Depois de cadastrar a chave, é possível testar a autenticação:

```bash
ssh -T git@github.com
```

Uma autenticação bem-sucedida apresenta uma mensagem semelhante a:

```
Hi voce! You've successfully authenticated
```

## 12. Onde fica a chave SSH no Windows?

O material indica:

```
C:\Users\SeuUsuario\.ssh\
```

É nessa pasta que ficam os arquivos relacionados à chave SSH.

## 13. Erro Permission denied (publickey)

Se aparecer `Permission denied (publickey)`, isso significa que a chave não está cadastrada ou configurada corretamente.

**Solução indicada:** refazer o cadastro da chave pública no GitHub.

## 14. O que é um Repositório?

Um repositório é uma pasta especial que contém:

- Arquivos do projeto
- Histórico completo das alterações

Dentro dela existe uma pasta oculta: `.git`. A pasta `.git` é o "cérebro" que monitora tudo. Ela armazena as informações necessárias para o Git controlar as versões do projeto.

## 15. Criando um Repositório do Zero

Primeiro, entre na pasta do projeto:

```bash
cd caminho/da/pasta
```

Depois execute:

```bash
git init
```

O Git retornará algo semelhante a `Initialized empty Git repo`.

O comando `git init`:

- Cria a pasta `.git`
- Inicializa o repositório
- Começa a monitorar o projeto

## 16. Clonando um Repositório

Outra maneira de obter um repositório é utilizar:

```bash
git clone https://github.com/user/proj.git
```

O `git clone` baixa os arquivos e todo o histórico do projeto.

```
GITHUB
  ↓
git clone
  ↓
COMPUTADOR LOCAL
```

## 17. git init × git clone

| Comando | Utilização |
| --- | --- |
| `git init` | Criar um repositório Git em uma pasta existente |
| `git clone` | Baixar um repositório existente |

**Memorize:**

- `git init` → começar
- `git clone` → copiar

## 18. As Três Árvores do Git

O Git trabalha com três áreas principais:

```
WORKING DIRECTORY
       ↓
STAGING AREA
       ↓
      HEAD
```

### 18.1. Working Directory

É o local onde você edita arquivos, cria arquivos, remove arquivos e trabalha no projeto. Onde você edita.

### 18.2. Staging Area

É a área onde você prepara as alterações que farão parte do próximo commit. Onde você prepara o commit. O comando utilizado é `git add`.

### 18.3. HEAD

Representa o histórico oficial do repositório. Depois de realizar um commit, a alteração passa a fazer parte do histórico. Histórico oficial.

## 19. O ciclo prático do Git

O fluxo básico apresentado é:

```bash
git status
git add .
git commit -m "..."
git log
```

- **Passo 1 — `git status`:** mostra o estado atual do repositório. Permite verificar quais arquivos foram modificados, criados, removidos ou adicionados ao staging.
- **Passo 2 — `git add .`:** adiciona as alterações à Staging Area. O `.` indica que as alterações da pasta atual serão adicionadas.
- **Passo 3 — `git commit`:** cria um registro das alterações no histórico. Exemplo: `git commit -m "aula concluída"`.
- **Passo 4 — `git log`:** exibe o histórico de commits.

**Resumo:**

```
git status
    ↓
verificar

git add .
    ↓
preparar

git commit
    ↓
consolidar

git log
    ↓
consultar histórico
```

## 20. Conectando o repositório local ao GitHub

Depois de criar o repositório local, é necessário conectá-lo ao repositório remoto.

1. **Adicionar o origin:**

```bash
git remote add origin https://github.com/voce/proj.git
```

O `origin` representa o repositório remoto principal.

## 21. Definindo a branch principal

O comando apresentado é:

```bash
git branch -M main
```

Ele define/renomeia a branch principal para `main`.

## 22. Enviando o projeto para o GitHub

Depois de configurar o repositório remoto:

```bash
git push -u origin main
```

Esse comando envia os commits locais para o GitHub.

**Fluxo:**

```
REPOSITÓRIO LOCAL
       ↓
   git push
       ↓
     GITHUB
```

## 23. Passo a passo: do zero à nuvem

O processo completo apresentado é:

1. **Criar o repositório remoto** — no GitHub: *New*.
2. **Copiar a URL** — copiar a URL do repositório criado.
3. **Vincular o repositório:**

```bash
git remote add origin https://github.com/voce/proj.git
```

4. **Definir a branch principal:**

```bash
git branch -M main
```

5. **Enviar:**

```bash
git push -u origin main
```

## 24. Fluxo completo do Git

O caminho completo apresentado na aula:

```
git init
   ↓
git add .
   ↓
git commit
   ↓
git push
   ↓
☁ GitHub
```

Ou seja: **criar → preparar → registrar → publicar**.

## 25. Comandos essenciais

| Comando | Função |
| --- | --- |
| `git init` | Inicializa um repositório |
| `git clone` | Clona um repositório existente |
| `git status` | Mostra o estado do repositório |
| `git add .` | Adiciona alterações ao staging |
| `git commit -m "..."` | Registra as alterações |
| `git log` | Mostra o histórico |
| `git remote add origin` | Conecta o repositório local ao remoto |
| `git branch -M main` | Define a branch principal como `main` |
| `git push` | Envia alterações para o remoto |
| `git pull` | Baixa alterações do remoto |

## 26. Mapa mental

```
                      GIT + GITHUB
                            │
          ┌─────────────────┴─────────────────┐
          ↓                                   ↓
         GIT                                GITHUB
     ferramenta                            plataforma
       local                                  online
          │                                   │
          └──────────────┬────────────────────┘
                         │
                       PUSH
                         ↓
                     ☁ NUVEM
                         │
                       PULL
                         ↓
                      LOCAL
```

## 27. O que decorar para a prova

- **Git × GitHub** — Git = ferramenta local de controle de versão. GitHub = plataforma online para hospedagem e colaboração.
- **Repositório** — pasta contendo os arquivos do projeto e seu histórico, controlado pela pasta `.git`.
- **`git init`** — cria um novo repositório Git.
- **`git clone`** — copia um repositório existente, incluindo seu histórico.
- **Staging Area** — área que prepara as alterações para o próximo commit.
- **Commit** — registra/consolida alterações no histórico.
- **Push** — envia alterações locais para o repositório remoto.
- **Pull** — traz alterações do repositório remoto para o ambiente local.
- **SSH** — método de autenticação baseado em um par de chaves pública e privada.

## 28. Fluxo para memorizar

```
┌──────────────────┐
│  WORKING DIRECTORY│
│  Onde eu edito   │
└────────┬─────────┘
         │
      git add
         ↓
┌──────────────────┐
│  STAGING AREA     │
│  Onde preparo     │
└────────┬─────────┘
         │
    git commit
         ↓
┌──────────────────┐
│       HEAD        │
│ Histórico oficial │
└────────┬─────────┘
         │
      git push
         ↓
┌──────────────────┐
│     GITHUB ☁      │
│ Repositório remoto│
└──────────────────┘
```

**Frase para decorar:** eu edito → adiciono → commito → faço push. Working Directory → Staging Area → HEAD → GitHub.

## Relacionadas

- [[Typescript]]
- [[Faculdade]]

[[Faculdade]]
