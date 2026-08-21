import base64
import os
import pickle
from email.message import EmailMessage
from email.utils import formatdate, make_msgid

from .config import carregar_config, caminho_credenciais

ESCOPOS = ["https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/gmail.send"]

_servico = None


def _importar_google():
    global Request, Credentials, InstalledAppFlow, build
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build


def _autenticar():
    global _servico
    if _servico:
        return _servico
    _importar_google()
    config = carregar_config()
    cred_path = caminho_credenciais("credentials.json")
    token_path = caminho_credenciais("token.json")

    if not cred_path.exists():
        raise FileNotFoundError("credentials.json não encontrado em credenciais/")

    credenciais = None
    if token_path.exists():
        credenciais = Credentials.from_authorized_user_file(str(token_path), ESCOPOS)
    if not credenciais or not credenciais.valid:
        if credenciais and credenciais.expired and credenciais.refresh_token:
            credenciais.refresh(Request())
        else:
            fluxo = InstalledAppFlow.from_client_secrets_file(str(cred_path), ESCOPOS)
            credenciais = fluxo.run_local_server(port=0)
        with open(token_path, "w") as f:
            f.write(credenciais.to_json())

    _servico = build("gmail", "v1", credentials=credenciais)
    return _servico


def _pegar_contato(nome):
    config = carregar_config()
    contatos = config["gmail"]["contatos"]
    nome = nome.lower().strip()
    for chave, email in contatos.items():
        if chave in nome or nome in chave:
            return email
    return None


def ler_emails(qtd=None, nao_lidos=True):
    servico = _autenticar()
    config = carregar_config()
    if qtd is None:
        qtd = config["gmail"]["qtd_emails_padrao"]
    consulta = "is:unread" if nao_lidos else ""
    resultado = servico.users().messages().list(
        userId="me", q=consulta, maxResults=qtd
    ).execute()
    mensagens = resultado.get("messages", [])
    emails = []
    for item in mensagens:
        dados = servico.users().messages().get(userId="me", id=item["id"], format="full").execute()
        cabecalho = {}
        for cab in dados.get("payload", {}).get("headers", []):
            nome = cab["name"].lower()
            if nome in ("from", "subject", "date"):
                cabecalho[nome] = cab["value"]
        snippet = dados.get("snippet", "")
        emails.append(
            {
                "id": item["id"],
                "de": cabecalho.get("from", "desconhecido"),
                "assunto": cabecalho.get("subject", "(sem assunto)"),
                "data": cabecalho.get("date", ""),
                "trecho": snippet,
            }
        )
    return emails


def buscar_emails(termo, qtd=None):
    servico = _autenticar()
    config = carregar_config()
    if qtd is None:
        qtd = config["gmail"]["qtd_emails_padrao"]
    resultado = servico.users().messages().list(
        userId="me", q=termo, maxResults=qtd
    ).execute()
    mensagens = resultado.get("messages", [])
    emails = []
    for item in mensagens:
        dados = servico.users().messages().get(
            userId="me", id=item["id"], format="metadata",
            metadataHeaders=["From", "Subject", "Date"]
        ).execute()
        cabecalho = {}
        for cab in dados.get("payload", {}).get("headers", []):
            nome = cab["name"].lower()
            if nome in ("from", "subject", "date"):
                cabecalho[nome] = cab["value"]
        emails.append(
            {
                "de": cabecalho.get("from", "desconhecido"),
                "assunto": cabecalho.get("subject", "(sem assunto)"),
                "data": cabecalho.get("date", ""),
            }
        )
    return emails


def enviar_email(destinatario, assunto, mensagem):
    servico = _autenticar()
    email = EmailMessage()
    email["To"] = destinatario
    email["Subject"] = assunto
    email["From"] = "me"
    email["Date"] = formatdate(localtime=True)
    email["Message-ID"] = make_msgid()
    email.set_content(mensagem)
    codificado = base64.urlsafe_b64encode(email.as_bytes()).decode()
    corpo = {"raw": codificado}
    enviado = servico.users().messages().send(userId="me", body=corpo).execute()
    return enviado.get("id")


def resolver_destinatario(nome_ou_email):
    if "@" in nome_ou_email:
        return nome_ou_email.strip()
    return _pegar_contato(nome_ou_email)