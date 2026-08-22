import asyncio
import re
import threading

from .config import carregar_config, caminho_dados

EDGE_DISPONIVEL = False
PYGAME_DISPONIVEL = False
PYTTSX3_DISPONIVEL = False
STT_DISPONIVEL = False

try:
    import edge_tts

    EDGE_DISPONIVEL = True
except Exception:
    pass

try:
    import pygame

    PYGAME_DISPONIVEL = True
except Exception:
    pass

try:
    import pyttsx3

    PYTTSX3_DISPONIVEL = True
except Exception:
    pass

try:
    import speech_recognition as sr

    STT_DISPONIVEL = True
except Exception:
    pass

_MARCADORES_MASCULINOS = ("daniel", "davos", "antonio", "fabio", "thales", "ricardo", "eduardo", "goncalves")
_MARCADORES_PT = ("portugu", "brazil", "pt-br", "pt_br")

_travamento_fala = threading.Lock()
_mix_iniciado = False
_engine_pyttsx3 = None
_voz_masculina_id = None
_voz_masculina_checada = False


def _eh_voz_masculina(identificador):
    if re.search(r"\bfemale\b", identificador):
        return False
    if re.search(r"\bmale\b", identificador):
        return True
    return any(m in identificador for m in _MARCADORES_MASCULINOS)


def _buscar_voz_masculina():
    try:
        motor = pyttsx3.init()
        vozes = motor.getProperty("voices")
        melhor = None
        melhor_pontos = -1
        for v in vozes:
            identificador = (v.id + " " + v.name).lower()
            if not _eh_voz_masculina(identificador):
                continue
            pontos = 1
            if any(m in identificador for m in _MARCADORES_PT):
                pontos += 2
            if pontos > melhor_pontos:
                melhor_pontos = pontos
                melhor = v.id
        return melhor
    except Exception:
        return None


def _voz_masculina():
    global _voz_masculina_id, _voz_masculina_checada
    if not _voz_masculina_checada:
        _voz_masculina_checada = True
        _voz_masculina_id = _buscar_voz_masculina()
    return _voz_masculina_id


def _iniciar_mix():
    global _mix_iniciado
    if not _mix_iniciado:
        try:
            pygame.mixer.init()
            _mix_iniciado = True
        except Exception:
            pass


def _tocar_arquivo(arquivo):
    if not PYGAME_DISPONIVEL:
        return False
    try:
        _iniciar_mix()
        pygame.mixer.music.load(str(arquivo))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(40)
        pygame.mixer.music.unload()
        return True
    except Exception:
        try:
            _mix_iniciado = False
            pygame.mixer.quit()
            pygame.mixer.init()
            pygame.mixer.music.load(str(arquivo))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.wait(40)
            pygame.mixer.music.unload()
            return True
        except Exception:
            return False


async def _gerar_edge(texto, voz, arquivo):
    comunicador = edge_tts.Communicate(texto, voz)
    await comunicador.save(str(arquivo))


async def _gerar_edge_com_timeout(texto, voz, arquivo):
    await asyncio.wait_for(_gerar_edge(texto, voz, arquivo), timeout=20)


def _falar_edge(texto):
    voz = carregar_config()["voz"]["voz_edge"]
    arquivo = caminho_dados("_fala_tmp.mp3")
    try:
        loop = asyncio.new_event_loop()
        loop.run_until_complete(_gerar_edge_com_timeout(texto, voz, arquivo))
        loop.close()
    except Exception:
        return False
    return _tocar_arquivo(arquivo)


def _obter_engine():
    global _engine_pyttsx3
    if _engine_pyttsx3 is None:
        _engine_pyttsx3 = pyttsx3.init()
        config = carregar_config()
        _engine_pyttsx3.setProperty("rate", config["voz"]["velocidade_pyttsx3"])
        _engine_pyttsx3.setProperty("volume", config["voz"]["volume"])
        voz_id = _voz_masculina()
        if voz_id:
            try:
                _engine_pyttsx3.setProperty("voice", voz_id)
            except Exception:
                pass
    return _engine_pyttsx3


def _falar_pyttsx3(texto):
    try:
        _obter_engine().say(texto)
        _obter_engine().runAndWait()
        return True
    except Exception:
        return False


def falar(texto):
    if not texto:
        return False
    with _travamento_fala:
        config = carregar_config()
        preferencia = config["voz"]["engine"]
        ordem = ["pyttsx3", "edge"] if preferencia == "pyttsx3" else ["edge", "pyttsx3"]
        for motor in ordem:
            if motor == "edge" and EDGE_DISPONIVEL:
                if _falar_edge(texto):
                    return True
            elif motor == "pyttsx3" and PYTTSX3_DISPONIVEL and _voz_masculina() is not None:
                if _falar_pyttsx3(texto):
                    return True
        return False


def testar_voz():
    from .ui import aviso, exibir, habilitar_cores, linha_separador, mostrar_logo
    habilitar_cores()
    mostrar_logo()
    exibir("== TESTE DE VOZ ==")
    linha_separador()
    exibir("Edge-TTS (Antônio - masculino, internet): " + ("[OK]" if EDGE_DISPONIVEL else "[FALTANDO]"))
    exibir("Pyttsx3 (vozes do Windows): " + ("[OK]" if PYTTSX3_DISPONIVEL else "[FALTANDO]"))
    exibir("Pygame (reprodução): " + ("[OK]" if PYGAME_DISPONIVEL else "[FALTANDO]"))
    if PYTTSX3_DISPONIVEL:
        masculina = _voz_masculina()
        if masculina:
            exibir("Voz masculina encontrada: " + masculina)
        else:
            aviso("Nenhuma voz masculina no Windows. Vou usar a voz masculina online (Antônio).")
            try:
                motor = pyttsx3.init()
                for v in motor.getProperty("voices"):
                    exibir("  voz encontrada: " + v.name + " | " + v.id)
            except Exception:
                pass
    resultado = falar("Olá senhor Isaque, esta é a minha voz masculina.")
    linha_separador()
    exibir("Resultado da fala: " + ("[OK] VOZ MASCULINA ATIVA" if resultado else "[FALHOU]"))
    return resultado


def tem_microfone():
    return STT_DISPONIVEL


def ouvir_comando():
    if not STT_DISPONIVEL:
        return None
    config = carregar_config()
    mic = config["microfone"]
    try:
        reconhecedor = sr.Recognizer()
        reconhecedor.energy_threshold = mic["energia_minima"]
        with sr.Microphone() as fonte:
            reconhecedor.adjust_for_ambient_noise(fonte, duration=0.6)
            audio = reconhecedor.listen(
                fonte,
                timeout=mic["timeout_ouvinte"],
                phrase_time_limit=mic["timeout_frase"],
            )
        texto = reconhecedor.recognize_google(audio, language=mic["idioma"])
        return texto.lower()
    except sr.WaitTimeoutError:
        return None
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None
    except Exception:
        return None


def voz_preparada():
    if EDGE_DISPONIVEL:
        return True
    if PYTTSX3_DISPONIVEL and _voz_masculina() is not None:
        return True
    return False