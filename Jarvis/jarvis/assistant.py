import sys

from . import brain, ui
from .config import carregar_config
from .voice import ouvir_comando, tem_microfone, voz_preparada


def _escutar(usar_mic, rotulo="fale JARVIS"):
    if usar_mic:
        ui.mostrar_escuta(rotulo)
        texto = ouvir_comando()
        ui.limpar_linha()
        return texto
    return ui.entrada_usuario()


def _perguntar(usar_mic):
    def pergunta(frase):
        ui.exibir_jarvis(frase)
        return _escutar(usar_mic, rotulo="responda")
    return pergunta


def _boas_vindas():
    config = carregar_config()
    ui.mostrar_logo()
    ui.linha_separador()
    ui.boot_animado()

    if not voz_preparada():
        ui.aviso("Nenhum motor de voz instalado. Rode: python -m pip install -r requirements.txt")
    if not tem_microfone():
        ui.aviso("Microfone não detectado (PyAudio não instalado). Rodando em modo de teclado.")
        ui.exibir("  Digite 'ajuda' para ver os comandos.", ui.Cores.CIANO_ESCURO)
    else:
        ui.sucesso("Microfone online. Fale 'Jarvis' para me chamar.")

    ui.linha_separador()
    ui.exibir_jarvis(config["saudacao_inicial"])


def executar(usar_mic=None, teste=False):
    ui.habilitar_cores()

    if teste:
        from . import voice
        ui.mostrar_logo()
        ui.exibir("== DIAGNÓSTICO DO SISTEMA ==", ui.Cores.CIANO, negrito=True)
        ui.exibir("Edge-TTS (voz masculina online):", ui.Cores.BRANCO)
        ui.exibir("  " + ("OK" if voice.EDGE_DISPONIVEL else "FALTANDO"), ui.Cores.VERDE if voice.EDGE_DISPONIVEL else ui.Cores.VERMELHO)
        ui.exibir("Pyttsx3 (voz offline do Windows):", ui.Cores.BRANCO)
        ui.exibir("  " + ("OK" if voice.PYTTSX3_DISPONIVEL else "FALTANDO"), ui.Cores.VERDE if voice.PYTTSX3_DISPONIVEL else ui.Cores.VERMELHO)
        ui.exibir("Pygame (reprodução de áudio):", ui.Cores.BRANCO)
        ui.exibir("  " + ("OK" if voice.PYGAME_DISPONIVEL else "FALTANDO"), ui.Cores.VERDE if voice.PYGAME_DISPONIVEL else ui.Cores.VERMELHO)
        ui.exibir("PyAudio (microfone):", ui.Cores.BRANCO)
        ui.exibir("  " + ("OK" if voice.STT_DISPONIVEL else "FALTANDO"), ui.Cores.VERDE if voice.STT_DISPONIVEL else ui.Cores.VERMELHO)
        return

    if usar_mic is None:
        usar_mic = tem_microfone()

    _boas_vindas()

    while True:
        texto = _escutar(usar_mic)

        if not texto:
            continue

        if usar_mic:
            if "jarvis" not in texto and "jabes" not in texto and "jadis" not in texto:
                continue
            ui.exibir_jarvis("Sim, senhor?")
            comando = _escutar(usar_mic, rotulo="fale o comando")
            if not comando:
                ui.exibir_jarvis("Não entendi. Pode repetir?")
                continue
        else:
            comando = texto

        resposta = brain.processar(comando, _perguntar(usar_mic))

        if resposta == brain.RESPOSTA_SAIR:
            ui.exibir_jarvis("Sistemas em repouso, senhor. Estarei aqui quando precisar.")
            break

        if resposta:
            ui.exibir_jarvis(resposta)
        else:
            ui.exibir_jarvis("Comando não reconhecido. Diga 'ajuda' para ver o que eu sei fazer.")