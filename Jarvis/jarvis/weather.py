import requests

from .config import carregar_config

BASE_GEO = "https://geocoding-api.open-meteo.com/v1/search"
BASE_TEMPO = "https://api.open-meteo.com/v1/forecast"


def _coordenadas(cidade):
    resposta = requests.get(
        BASE_GEO,
        params={"name": cidade, "count": 1, "language": "pt", "format": "json"},
        timeout=15,
    )
    dados = resposta.json().get("results")
    if not dados:
        return None
    item = dados[0]
    return {
        "lat": item["latitude"],
        "lon": item["longitude"],
        "nome": item.get("name", cidade),
        "pais": item.get("country", ""),
    }


def _descricao(codigo):
    tabela = {
        0: "céu limpo",
        1: "predominantemente limpo",
        2: "parcialmente nublado",
        3: "encoberto",
        45: "nevoeiro",
        48: "neblina com gelo",
        51: "garoa leve",
        53: "garoa moderada",
        55: "garoa intensa",
        61: "chuva leve",
        63: "chuva moderada",
        65: "chuva forte",
        66: "chuva congelante leve",
        67: "chuva congelante forte",
        71: "neve leve",
        73: "neve moderada",
        75: "neve forte",
        80: "pancadas de chuva leves",
        81: "pancadas de chuva moderadas",
        82: "pancadas de chuva violentas",
        95: "trovoada",
        96: "trovoada com granizo leve",
        99: "trovoada com granizo forte",
    }
    return tabela.get(codigo, "condições variadas")


def clima_agora(cidade=None):
    config = carregar_config()
    cidade = cidade or config["cidade"]
    local = _coordenadas(cidade)
    if not local:
        raise ValueError(f"Não encontrei a cidade {cidade}")
    resposta = requests.get(
        BASE_TEMPO,
        params={
            "latitude": local["lat"],
            "longitude": local["lon"],
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m",
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "America/Sao_Paulo",
        },
        timeout=15,
    )
    dados = resposta.json()
    atual = dados["current"]
    diario = dados["daily"]
    return {
        "cidade": local["nome"],
        "descricao": _descricao(atual["weather_code"]),
        "temperatura": atual["temperature_2m"],
        "sensacao": atual["apparent_temperature"],
        "umidade": atual["relative_humidity_2m"],
        "vento": atual["wind_speed_10m"],
        "maxima": diario["temperature_2m_max"][0],
        "minima": diario["temperature_2m_min"][0],
    }
