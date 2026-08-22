import sys
import time

from .config import carregar_config
from .voice import falar

class Cores:
    RESET = "\033[0m"
    NEGRITO = "\033[1m"
    ESCURO = "\033[2m"
    CIANO = "\033[96m"
    CIANO_ESCURO = "\033[36m"
    MAGENTA = "\033[95m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    VERMELHO = "\033[91m"
    AZUL = "\033[94m"
    BRANCO = "\033[97m"

BARRA = "\u2500"
BOLAS = "\u25cf"

LOGO = [
    "    \u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2557   \u2588\u2588\u2557\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2557",
    "    \u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d",
    "    \u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255d\u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2557",
    "    \u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\u255a\u2588\u2588\u2557 \u2588\u2588\u2554\u255d\u2588\u2588\u2551\u255a\u2550\u2550\u2550\u2550\u2588\u2588\u2557",
    "    \u2588\u2588\u2588\u2588\u2588\u2588\u2551\u2588\u2588\u2551  \u2588\u2588\u2551\u2588\u2588\u2551  \u2588\u2588\u2551 \u255a\u2588\u2588\u2588\u2588\u2554\u255d \u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255d",
    "    \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u255d\u255a\u2550\u255d  \u255a\u2550\u255d\u255a\u2550\u255d  \u255a\u2550\u255d  \u255a\u2550\u2550\u2550\u2550\u255d  \u255a\u2550\u255d\u255a\u2550\u2550\u2550\u2550\u2550\u255d",
]

LINHAS_BOOT = [
    ("inicializando núcleo neural", Cores.CIANO),
    ("carregando protocolos de segurança", Cores.CIANO_ESCURO),
    ("sincronizando com os servidores Stark", Cores.CIANO),
    ("acoplando módulos de voz e escuta", Cores.CIANO_ESCURO),
    ("conectando ao Obsidian", Cores.CIANO),
    ("sistema operacional online", Cores.VERDE),
]


def habilitar_cores():
    if sys.platform == "win32":
        try:
            import os
            os.system("")
        except Exception:
            pass


def colorir(texto, cor=Cores.CIANO, negrito=False):
    prefixo = Cores.NEGRITO if negrito else ""
    return prefixo + cor + texto + Cores.RESET


def linha_separador(comprimento=60):
    print(colorir(BARRA * comprimento, Cores.CIANO_ESCURO))


def mostrar_logo():
    print()
    for linha in LOGO:
        print(colorir(linha, Cores.CIANO, negrito=True))
    print()


def barra_progresso(total=24, pausa=0.06):
    print(colorir("[", Cores.CIANO_ESCURO), end="")
    for i in range(total):
        print(colorir("\u2588", Cores.CIANO, negrito=True), end="", flush=True)
        time.sleep(pausa)
    print(colorir("] 100%", Cores.VERDE, negrito=True))


def boot_animado():
    for texto, cor in LINHAS_BOOT:
        print(colorir("  " + BOLAS + " " + texto, cor))
        time.sleep(0.35)
    print()
    print(colorir("  inicializando sistema", Cores.CIANO_ESCURO), end=" ")
    barra_progresso()
    print()
    linha_separador()


def exibir(texto, cor=Cores.CIANO, negrito=False):
    print(colorir(texto, cor, negrito))


def aviso(texto):
    exibir("[!] " + texto, Cores.AMARELO, negrito=True)


def erro(texto):
    exibir("[X] " + texto, Cores.VERMELHO, negrito=True)


def sucesso(texto):
    exibir("[OK] " + texto, Cores.VERDE, negrito=True)


def exibir_jarvis(texto):
    if texto:
        exibir("JARVIS \u25b8 " + texto, Cores.CIANO)
        falar(texto)


def mostrar_escuta(rotulo="fale JARVIS"):
    print("\r" + colorir(f"\u25b8 ouvindo... {rotulo}", Cores.CIANO_ESCURO), end="", flush=True)


def limpar_linha():
    print("\r" + " " * 60 + "\r", end="")


def entrada_usuario(rotulo="VOC\u00ca"):
    return input(colorir(f"{rotulo} \u25b8 ", Cores.AMARELO, negrito=True)).strip().lower() or None