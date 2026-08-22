import json

from .config import caminho_dados


def _arquivo():
    return caminho_dados("tarefas.json")


def _carregar():
    try:
        with open(_arquivo(), encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def _salvar(tarefas):
    with open(_arquivo(), "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)


def adicionar(texto):
    tarefas = _carregar()
    tarefas.append({"texto": texto, "feita": False})
    _salvar(tarefas)
    return len(tarefas)


def listar():
    return _carregar()


def listar_ativas():
    return [t for t in _carregar() if not t["feita"]]


def concluir(indice):
    tarefas = _carregar()
    if indice < 0 or indice >= len(tarefas):
        return False
    if tarefas[indice]["feita"]:
        return "ja_feita"
    tarefas[indice]["feita"] = True
    _salvar(tarefas)
    return True


def limpar_concluidas():
    tarefas = _carregar()
    restantes = [t for t in tarefas if not t["feita"]]
    removidas = len(tarefas) - len(restantes)
    _salvar(restantes)
    return removidas


def limpar_tudo():
    _salvar([])
