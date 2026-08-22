import datetime
import re
from pathlib import Path

from .config import carregar_config


def _vault():
    import re
    config = carregar_config()
    texto = str(Path(config["obsidian"]["vault"]))
    resultado = re.match(r"^([A-Za-z]):[/\\](.*)$", texto)
    if resultado:
        alternativo = Path("/mnt") / resultado.group(1).lower() / resultado.group(2)
        if alternativo.exists():
            return alternativo
    return Path(texto)


def _limpar_nome(nome):
    nome = re.sub(r'[\\/:*?"<>|]', "-", nome.strip())
    palavras = nome.split()
    menores = {"de", "da", "do", "das", "dos", "e", "a", "o", "em", "com", "para", "por", "no", "na", "nos", "nas", "um", "uma"}
    capitalizadas = [
        w if w.lower() in menores and i > 0 else w.capitalize()
        for i, w in enumerate(palavras)
    ]
    nome = " ".join(capitalizadas) if capitalizadas else "Nota"
    return nome


def caminho_diario(data=None):
    data = data or datetime.date.today()
    nome = f"Daily-{data.isoformat()}"
    pasta = _vault() / carregar_config()["obsidian"]["pasta_diario"] / nome
    return pasta / f"{nome}.md"


def diario_existe(data=None):
    return caminho_diario(data).exists()


def anotar_no_diario(texto, data=None):
    caminho = caminho_diario(data)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    bloco = f"- {datetime.datetime.now().strftime('%H:%M')} {texto}"
    if caminho.exists():
        with open(caminho, encoding="utf-8") as f:
            conteudo = f.read()
        novo = conteudo.rstrip() + "\n" + bloco + "\n"
    else:
        novo = f"# {caminho.stem}\n\n## Anotações\n{bloco}\n"
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(novo)
    return caminho


def adicionar_tarefa_obsidian(texto, data=None):
    caminho = caminho_diario(data)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    bloco = f"- [ ] {texto}"
    if caminho.exists():
        with open(caminho, encoding="utf-8") as f:
            conteudo = f.read()
        novo = conteudo.rstrip() + "\n" + bloco + "\n"
    else:
        novo = f"# {caminho.stem}\n\n## Tarefas\n{bloco}\n"
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(novo)
    return caminho


def criar_nota(titulo, pasta=None, conteudo=""):
    config = carregar_config()
    pasta = pasta or config["obsidian"]["pasta_notas_padrao"]
    nome = _limpar_nome(titulo)
    caminho = _vault() / pasta / f"{nome}.md"
    if not caminho.exists():
        caminho.write_text(conteudo, encoding="utf-8")
    return caminho


def ler_nota(nome, pasta=None):
    config = carregar_config()
    pasta = pasta or config["obsidian"]["pasta_notas_padrao"]
    caminho = _vault() / pasta / f"{_limpar_nome(nome)}.md"
    if not caminho.exists():
        return None
    return caminho.read_text(encoding="utf-8")


def formatar_resumo_diario(data=None):
    caminho = caminho_diario(data)
    if not caminho.exists():
        return None
    return caminho.read_text(encoding="utf-8")
