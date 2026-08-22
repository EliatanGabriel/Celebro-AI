import datetime
import platform
import random
import re
import threading
import webbrowser
from zoneinfo import ZoneInfo

import requests

from . import gmail_service, obsidian, tasks, weather
from .config import carregar_config
from .ui import exibir_jarvis

RESPOSTA_SAIR = "__SAIR__"

PITADAS = [
    "Por que o livro de matemática ficou triste? Porque tinha muitos problemas.",
    "O que o zero disse para o oito? Que cinto bonito você está usando!",
    "Por que o programador foi demitido? Porque só sabia dar 'nós' no código.",
    "O que o café disse para o computador? Vai com calma, não precisa me processar.",
    "Por que o fio foi preso? Porque estava conduzindo eletricidade.",
    "O que um chinês disse ao outro no elevador? Bing, bong... todos descem.",
    "Por que a plantinha não foi à festa? Porque estava com folga.",
    "O que o Wi-Fi disse para o outro Wi-Fi? Já te dei meu ponto de acesso, para com isso.",
]

_TIMERS = []


def _config():
    return carregar_config()


def _fuso():
    return ZoneInfo("America/Sao_Paulo")


def _numero_extenso(n):
    numeros = {
        0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco",
        6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez", 11: "onze",
        12: "doze", 13: "treze", 14: "quatorze", 15: "quinze", 16: "dezesseis",
        17: "dezessete", 18: "dezoito", 19: "dezenove", 20: "vinte",
        30: "trinta", 40: "quarenta", 50: "cinquenta", 60: "sessenta",
        70: "setenta", 80: "oitenta", 90: "noventa", 100: "cem",
    }
    if n in numeros:
        return numeros[n]
    if n < 100:
        dezena = (n // 10) * 10
        unidade = n % 10
        return f"{numeros[dezena]} e {numeros[unidade]}"
    if n < 1000:
        centena = n // 100
        resto = n % 100
        base = "cem" if centena == 1 else f"{_numero_extenso(centena)}centos"
        if resto == 0:
            return base
        return f"{base} e {_numero_extenso(resto)}"
    return str(n)


def _qtd_extenso(n):
    if n == 1:
        return "uma"
    if n == 2:
        return "duas"
    if n == 0:
        return "nenhuma"
    return _numero_extenso(n)


def _meses():
    return ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]


def _dias_semana():
    return ["segunda-feira", "terça-feira", "quarta-feira",
            "quinta-feira", "sexta-feira", "sábado", "domingo"]


def _agora():
    return datetime.datetime.now(_fuso())


def _hora_resposta():
    agora = _agora()
    hora = agora.hour
    minutos = agora.minute
    if hora == 1:
        texto_hora = "uma hora"
    elif hora == 0:
        texto_hora = "meia noite"
    else:
        texto_hora = f"{hora} horas"
    if minutos == 0:
        if hora == 0:
            return "São exatamente meia noite."
        if hora == 1:
            return "É uma hora em ponto."
        return f"São {_numero_extenso(hora)} horas em ponto."
    if minutos < 10:
        minutos_txt = f"0{minutos}"
    else:
        minutos_txt = str(minutos)
    return f"Agora são {_numero_extenso(hora)} horas e {minutos_txt} minutos."


def _data_resposta():
    agora = _agora()
    return f"Hoje é {_numero_extenso(agora.day)} de {_meses()[agora.month - 1]} de {agora.year}."


def _dia_semana_resposta():
    return f"Hoje é {_dias_semana()[_agora().weekday()]}."


def _saudacao_resposta():
    config = _config()
    hora = _agora().hour
    if hora < 12:
        return config["saudacoes"]["manha"]
    if hora < 18:
        return config["saudacoes"]["tarde"]
    return config["saudacoes"]["noite"]


def _clima_resposta(cidade=None):
    try:
        dados = weather.clima_agora(cidade)
    except Exception:
        return "Não consegui buscar o clima agora. Verifique sua conexão com a internet."
    temp = round(dados["temperatura"])
    maxi = round(dados["maxima"])
    mini = round(dados["minima"])
    sens = round(dados["sensacao"])
    if sens != temp:
        return (f"Agora em {dados['cidade']} está {dados['descricao']}, com "
                f"{temp} graus, sensação de {sens}. Máxima de {maxi} e mínima de {mini} hoje.")
    return (f"Agora em {dados['cidade']} está {dados['descricao']}, com {temp} graus. "
            f"Máxima de {maxi} e mínima de {mini} hoje.")


def _formatar_email(email, indice=None):
    prefixo = f"{indice}. " if indice else ""
    assunto = email.get("assunto", "(sem assunto)")
    trecho = email.get("trecho", "")[:140]
    if trecho:
        return f"{prefixo}De {email.get('de', 'desconhecido')}, assunto {assunto}. {trecho}."
    return f"{prefixo}De {email.get('de', 'desconhecido')}, assunto {assunto}."


def _ler_emails_resposta():
    try:
        emails = gmail_service.ler_emails()
    except FileNotFoundError:
        return ("O Gmail ainda não está configurado. Leia o passo a passo no arquivo "
                "README, na pasta do Jarvis, para conectar sua conta.")
    except Exception:
        return "Não consegui acessar o Gmail. Verifique sua conexão e as credenciais."
    if not emails:
        return "Você não tem e-mails não lidos."
    partes = [f"Você tem {_numero_extenso(len(emails))} e-mail" +
              ("s" if len(emails) > 1 else "") + " não lido" +
              ("s" if len(emails) > 1 else "") + "."]
    for i, email in enumerate(emails, 1):
        partes.append(_formatar_email(email, i))
    return " ".join(partes)


def _buscar_emails_resposta(termo):
    try:
        emails = gmail_service.buscar_emails(termo)
    except Exception:
        return "Não consegui procurar e-mails agora."
    if not emails:
        return f"Não encontrei nenhum e-mail sobre {termo}."
    partes = [f"Encontrei {_numero_extenso(len(emails))} e-mail" +
              ("s" if len(emails) > 1 else "") + f" sobre {termo}."]
    for i, email in enumerate(emails, 1):
        partes.append(f"{i}. De {email.get('de', 'desconhecido')}, assunto {email.get('assunto', '(sem assunto)')}.")
    return " ".join(partes)


def _enviar_email_fluxo(destino, perguntar):
    config = _config()
    destinatario = gmail_service.resolver_destinatario(destino)
    if not destinatario:
        resp = perguntar("Para qual endereço de e-mail devo enviar?")
        if not resp:
            return "Não consegui entender o destinatário."
        destinatario = gmail_service.resolver_destinatario(resp)
        if not destinatario:
            destinatario = resp.strip()
    assunto = perguntar("Qual é o assunto do e-mail?")
    if not assunto:
        return "Cancelando o envio, não entendi o assunto."
    mensagem = perguntar("Qual é a mensagem?")
    if not mensagem:
        return "Cancelando o envio, não entendi a mensagem."
    confirmar = perguntar(f"Confirmo o envio do e-mail para {destinatario}, com assunto: {assunto}?")
    if not confirmar or not any(p in confirmar for p in ["sim", "pode", "manda", "enviar", "ok", "confirma"]):
        return "Envio cancelado."
    try:
        gmail_service.enviar_email(destinatario, assunto, mensagem)
        return "E-mail enviado com sucesso."
    except Exception:
        return "Não consegui enviar o e-mail. Verifique sua conexão e as credenciais."


def _tarefas_resposta():
    ativas = tasks.listar_ativas()
    if not ativas:
        return "Você não tem tarefas pendentes. Tudo em dia."
    total = len(ativas)
    if total == 1:
        introducao = "Você tem uma tarefa pendente."
    else:
        introducao = f"Você tem {_qtd_extenso(total)} tarefas pendentes."
    partes = [introducao]
    for i, tarefa in enumerate(ativas, 1):
        partes.append(f"Tarefa {_numero_extenso(i)}: {tarefa['texto']}.")
    return " ".join(partes)


def _adicionar_tarefa_resposta(texto):
    total = tasks.adicionar(texto)
    obsidian.adicionar_tarefa_obsidian(texto)
    pendentes = len(tasks.listar_ativas())
    if pendentes == 1:
        final = "Você tem agora uma tarefa pendente."
    else:
        final = f"Você tem agora {_qtd_extenso(pendentes)} tarefas pendentes."
    return f"Tarefa adicionada: {texto}. {final}"


def _concluir_tarefa_resposta(texto):
    texto = re.sub(r"\b(conclu|fazer|marcar como feita|marcar)\b", "", texto).strip()
    numeros = re.findall(r"\d+", texto)
    if numeros:
        indice = int(numeros[0]) - 1
        resultado = tasks.concluir(indice)
        if resultado is True:
            return "Tarefa concluída. Bom trabalho."
        if resultado == "ja_feita":
            return "Essa tarefa já estava concluída."
        return "Tarefa concluída."
    return "Qual tarefa devo concluir? Fale o número dela."


def _anotar_resposta(texto):
    obsidian.anotar_no_diario(texto)
    return "Anotado no seu diário do dia."


def _criar_nota_resposta(titulo):
    try:
        caminho = obsidian.criar_nota(titulo)
    except Exception:
        return "Não consegui criar a nota."
    return f"Nota criada: {caminho.name}."


def _ler_nota_resposta(titulo):
    conteudo = obsidian.ler_nota(titulo)
    if conteudo is None:
        return f"Não encontrei a nota {titulo}."
    trecho = conteudo.replace("\n", " ").strip()[:400]
    return f"Conteúdo da nota {titulo}: {trecho}."


def _abrir_resposta(alvo):
    config = _config()
    apps = config["aplicativos"]
    alvo = alvo.lower().strip()
    for chave, url in apps.items():
        if chave in alvo:
            webbrowser.open(url)
            return f"Abrindo {chave}."
    if any(p in alvo for p in ["google", "pesquisa", "pesquisar"]):
        return None
    tentativas = {
        "chrome": "chrome", "navegador": "chrome", "firefox": "firefox",
        "edge": "msedge", "explorer": "explorer",
        "calculadora": "calc", "bloco de notas": "notepad", "notas": "notepad",
        "painel": "control", "configurações": "ms-settings:",
        "explorador": "explorer", "arquivos": "explorer",
    }
    for chave, cmd in tentativas.items():
        if chave in alvo:
            import os
            os.startfile(cmd) if platform.system() == "Windows" else None
            return f"Abrindo {chave}."
    return f"Não conheço o aplicativo {alvo}. Posso abrir YouTube, WhatsApp, Google, Gmail, Spotify e outros."


def _pesquisar_resposta(termo):
    url = "https://www.google.com/search?q=" + termo.replace(" ", "+")
    webbrowser.open(url)
    return f"Abrindo a pesquisa por {termo} no Google."


def _wikipedia_resposta(termo):
    try:
        resposta = requests.get(
            "https://pt.wikipedia.org/w/api.php",
            headers={"User-Agent": "Jarvis-Assistente-Pessoal/1.0 (isaquedeveloper@gmail.com)"},
            params={
                "action": "query",
                "format": "json",
                "prop": "extracts",
                "exintro": True,
                "explaintext": True,
                "redirects": 1,
                "titles": termo,
            },
            timeout=15,
        )
        paginas = resposta.json()["query"]["pages"]
        texto = ""
        for pagina in paginas.values():
            texto = pagina.get("extract", "")
        if not texto:
            return f"Não encontrei informações sobre {termo}."
        return f"{termo}. {texto[:350].strip()}."
    except Exception:
        return "Não consegui buscar na Wikipédia agora."


def _calcular_resposta(expressao):
    expressao = expressao.replace("x", "*").replace("×", "*").replace(",", ".")
    expressao = expressao.replace("dividido por", "/").replace("divido por", "/")
    expressao = expressao.replace("mais", "+").replace("menos", "-")
    expressao = expressao.replace(" vezes", "*").replace("vezes", "*")
    expressao = re.sub(r"[^0-9+\-*/(). ]", "", expressao)
    if not expressao.strip():
        return "Não entendi a expressão para calcular."
    try:
        resultado = eval(expressao, {"__builtins__": {}}, {})
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)
        return f"O resultado é {resultado}."
    except Exception:
        return "Não consegui calcular essa expressão."


def _piada_resposta():
    return random.choice(PITADAS)


def _programar_lembrete(texto, perguntar):
    padrao = re.search(r"em\s+(\d+)\s*(min|minutos|minuto|seg|segundos|segundo|hora|horas)?", texto)
    if not padrao:
        return "Diga assim: lembre me de beber água em 10 minutos."
    quantidade = int(padrao.group(1))
    unidade = (padrao.group(2) or "min").lower()
    if unidade.startswith("seg"):
        segundos = quantidade
        unidade_texto = f"{quantidade} segundo" + ("s" if quantidade > 1 else "")
    elif unidade.startswith("hora"):
        segundos = quantidade * 3600
        unidade_texto = f"{quantidade} hora" + ("s" if quantidade > 1 else "")
    else:
        segundos = quantidade * 60
        unidade_texto = f"{quantidade} minuto" + ("s" if quantidade > 1 else "")
    mensagem = re.sub(r"^(lembre[-\s]?me|me lembre)\s+", "", texto)
    mensagem = re.sub(r"\s+em\s+\d+\s*(min|minutos|minuto|seg|segundos|segundo|hora|horas)?\s*$", "", mensagem).strip()
    mensagem = re.sub(r"^de\s+", "", mensagem).strip()
    if not mensagem:
        return "O que devo te lembrar?"

    def disparar():
        exibir_jarvis(f"Lembrete: {mensagem}.")
        exibir_jarvis("Atenção senhor, isso era importante.")
    timer = threading.Timer(segundos, disparar)
    timer.daemon = True
    timer.start()
    _TIMERS.append(timer)
    return f"Combinado. Vou te lembrar de {mensagem} em {unidade_texto}."


def _ajuda_resposta():
    return ("Posso fazer várias coisas: dizer a hora e a data, buscar o clima, "
            "ler e enviar e-mails, gerenciar suas tarefas, anotar no seu diário do Obsidian, "
            "abrir aplicativos, pesquisar na web, consultar a Wikipédia, contar piadas, "
            "calcular contas e criar lembretes. Diga Jarvis para me chamar e fale o comando.")


def _desligar_resposta(reiniciar=False):
    if platform.system() != "Windows":
        return "Não posso desligar este sistema."
    comando = "shutdown /r /t 30" if reiniciar else "shutdown /s /t 30"
    import os
    os.system(comando)
    return "Vou desligar o computador em trinta segundos. Digite shutdown /a para cancelar."


REGISTRO = [
    (r"(que horas|hora agora|horas são|hora certa|que hora)", "hora"),
    (r"(que dia é hoje|que dia hoje|data de hoje|qual a data)", "data"),
    (r"(dia da semana|que dia da semana)", "dia_semana"),
    (r"(bom dia|boa tarde|boa noite|boa madrugada)", "saudacao"),
    (r"^(olá|ola|oi|e aí|eai|opa|tudo bem|como você está|quem é você|quem e voce|o que você é|o que voce e)", "apresentar"),
    (r"(clima|tempo)\s+em\s+(.+)", "clima_cidade"),
    (r"(clima|tempo|previsão|previsao|chovendo|tá quente|ta quente)", "clima"),
    (r"(ler e-mails|ler emails|e-mails não lidos|emails nao lidos|meus e-mails|meus emails|caixa de entrada|e-mail novo|email novo|li meus e-mails)", "ler_emails"),
    (r"(procurar e-mail|procurar email|buscar e-mail|buscar email|achar e-mail|achar email)\s+(.+)", "buscar_email"),
    (r"(enviar e-mail|enviar email|mandar e-mail|mandar email)\s+(para\s+)?(.+)", "enviar_email"),
    (r"(adicionar tarefa|criar tarefa|nova tarefa|preciso fazer|lembre de fazer)\s+(.+)", "adicionar_tarefa"),
    (r"(listar tarefas|minhas tarefas|tarefas pendentes|quais são minhas tarefas|quais sao minhas tarefas)", "listar_tarefas"),
    (r"(concluir tarefa|tarefa concluída|tarefa concluida|marcar tarefa|marcar como feita|feita a tarefa|feita tarefa)\s*(.*)", "concluir_tarefa"),
    (r"(limpar tarefas concluídas|limpar tarefas concluidas|apagar tarefas feitas|remover tarefas)", "limpar_tarefas"),
    (r"(anotar|anota|anote|escrever no diário|escrever no diario|registra|registrar)\s+(.+)", "anotar"),
    (r"(criar nota|nova nota)\s+(.+)", "criar_nota"),
    (r"(ler nota|abrir nota)\s+(.+)", "ler_nota"),
    (r"(resumo do dia|como foi meu dia|resumo diário|resumo diario)", "resumo_dia"),
    (r"abrir\s+(.+)", "abrir"),
    (r"(pesquisar|pesquisa|procura na web|pesquisar sobre)\s+(.+)", "pesquisar"),
    (r"(quem é|quem e|o que é|o que e|quem foi|quem era)\s+(.+)", "wikipedia"),
    (r"(conta piada|piada|fazer rir|me faz rir)", "piada"),
    (r"(calcular|calcula|quanto é|quanto e|quanto dá|quanto da)\s+(.+)", "calcular"),
    (r"(lembre[-\s]?me|me lembre|lembrete)\s+(.+)", "lembrete"),
    (r"(desligar computador|desligar o pc|desligar o computador|desligar)", "desligar"),
    (r"(reiniciar computador|reiniciar o pc|reiniciar)", "reiniciar"),
    (r"(ajuda|comandos|o que você sabe|o que voce sabe|o que você pode fazer|o que voce pode fazer|listar comandos)", "ajuda"),
    (r"(encerrar|sair|tchau|boa noite, jarvis|dormir|hibernar|parar)", "sair"),
]

CONTADORES = {"apresentou": False}


def processar(texto, perguntar):
    texto = texto.lower().strip()
    texto = texto.replace("quanto é que", "quanto é")

    if any(p in texto for p in ["pare tudo", "cancela tudo"]):
        return "Entendido, interrompendo tudo."

    for padrao, acao in REGISTRO:
        combinacao = re.search(padrao, texto)
        if not combinacao:
            continue
        grupos = combinacao.groups()
        if acao == "hora":
            return _hora_resposta()
        if acao == "data":
            return _data_resposta()
        if acao == "dia_semana":
            return _dia_semana_resposta()
        if acao == "saudacao":
            return _saudacao_resposta()
        if acao == "apresentar":
            return ("Eu sou o Jarvis, seu assistente pessoal. Estou aqui para facilitar "
                    "sua vida, cuidar de seus e-mails, tarefas, notas e lembretes.")
        if acao == "clima_cidade":
            return _clima_resposta(grupos[-1].strip())
        if acao == "clima":
            return _clima_resposta()
        if acao == "ler_emails":
            return _ler_emails_resposta()
        if acao == "buscar_email":
            return _buscar_emails_resposta(grupos[-1].strip())
        if acao == "enviar_email":
            return _enviar_email_fluxo(grupos[-1].strip(), perguntar)
        if acao == "adicionar_tarefa":
            return _adicionar_tarefa_resposta(grupos[-1].strip())
        if acao == "listar_tarefas":
            return _tarefas_resposta()
        if acao == "concluir_tarefa":
            return _concluir_tarefa_resposta(grupos[-1] or "")
        if acao == "limpar_tarefas":
            removidas = tasks.limpar_concluidas()
            if removidas == 0:
                return "Não havia tarefas concluídas para limpar."
            if removidas == 1:
                return "Removi uma tarefa concluída."
            return f"Removi {_qtd_extenso(removidas)} tarefas concluídas."
        if acao == "anotar":
            return _anotar_resposta(grupos[-1].strip())
        if acao == "criar_nota":
            return _criar_nota_resposta(grupos[-1].strip())
        if acao == "ler_nota":
            return _ler_nota_resposta(grupos[-1].strip())
        if acao == "resumo_dia":
            conteudo = obsidian.formatar_resumo_diario()
            if not conteudo:
                return "Você ainda não fez anotações hoje."
            trecho = conteudo.replace("\n", " ").strip()[:350]
            return f"Seu diário de hoje: {trecho}."
        if acao == "abrir":
            resp = _abrir_resposta(grupos[-1].strip())
            return resp or _pesquisar_resposta(grupos[-1].strip())
        if acao == "pesquisar":
            return _pesquisar_resposta(grupos[-1].strip())
        if acao == "wikipedia":
            return _wikipedia_resposta(grupos[-1].strip())
        if acao == "piada":
            return _piada_resposta()
        if acao == "calcular":
            return _calcular_resposta(grupos[-1].strip())
        if acao == "lembrete":
            return _programar_lembrete(texto, perguntar)
        if acao == "desligar":
            return _desligar_resposta()
        if acao == "reiniciar":
            return _desligar_resposta(reiniciar=True)
        if acao == "ajuda":
            return _ajuda_resposta()
        if acao == "sair":
            for timer in _TIMERS:
                timer.cancel()
            return RESPOSTA_SAIR

    return None
