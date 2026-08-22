import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config.json"

_config_cache = None


def carregar_config():
    global _config_cache
    if _config_cache is None:
        with open(CONFIG_PATH, encoding="utf-8") as f:
            _config_cache = json.load(f)
    return _config_cache


def caminho_dados(*nomes):
    pasta = BASE_DIR / "jarvis" / "dados"
    pasta.mkdir(parents=True, exist_ok=True)
    return pasta.joinpath(*nomes)


def caminho_credenciais(*nomes):
    pasta = BASE_DIR / "credenciais"
    pasta.mkdir(parents=True, exist_ok=True)
    return pasta.joinpath(*nomes)
